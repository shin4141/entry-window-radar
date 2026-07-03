#!/usr/bin/env python3
"""Write a local V12-style restart checkpoint for the current session."""

from __future__ import annotations

import argparse
import subprocess
from datetime import datetime
from pathlib import Path


ROOT = Path.cwd()
DEFAULT_OUTPUT = ROOT / "outputs" / "session_snapshot.md"
WARNING_EN = "This is a restartable checkpoint, not a completion claim."
WARNING_JA = "これは再開可能な途中保存であり、完了宣言ではない。"
HANDOFF_WARNING_EN = (
    "This is not a full handoff.\n"
    "A receiving AI must still state what it now owns before continuing.\n"
    "For project-level handoff, use a Quest Snapshot or add a Handoff Header."
)
HANDOFF_WARNING_JA = (
    "これは完全な引き継ぎではありません。\n"
    "受け側AIは、続行前に「自分が今なにを引き受けたか」を明示する必要があります。\n"
    "プロジェクト単位の引き継ぎには、Quest Snapshot または Handoff Header を併用してください。"
)


def run_git(args: list[str]) -> str:
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
            timeout=8,
        )
    except (OSError, subprocess.TimeoutExpired):
        return "UNKNOWN"
    if result.returncode != 0:
        return "UNKNOWN"
    return result.stdout.strip() or "UNKNOWN"


def read_text_if_present(path: Path) -> tuple[str, bool]:
    if not path.exists() or not path.is_file():
        return "", False
    try:
        return path.read_text(encoding="utf-8"), True
    except OSError:
        return "", False


def section(text: str, heading: str) -> str:
    marker = f"## {heading}"
    start = text.find(marker)
    if start == -1:
        return ""
    next_start = text.find("\n## ", start + len(marker))
    if next_start == -1:
        return text[start:].strip()
    return text[start:next_start].strip()


def code_block_after_heading(text: str, heading: str) -> str:
    block = section(text, heading)
    if "```text" not in block:
        return ""
    start = block.find("```text") + len("```text")
    end = block.find("```", start)
    if end == -1:
        return ""
    return block[start:end].strip()


def bounded_excerpt(text: str, terms: list[str], *, before: int = 2, after: int = 4) -> str:
    lines = text.splitlines()
    selected: list[str] = []
    seen: set[int] = set()
    lowered_terms = [term.lower() for term in terms]
    for index, line in enumerate(lines):
        lowered_line = line.lower()
        if not any(term in lowered_line for term in lowered_terms):
            continue
        start = max(0, index - before)
        end = min(len(lines), index + after + 1)
        for line_index in range(start, end):
            if line_index not in seen:
                selected.append(lines[line_index])
                seen.add(line_index)
        if len(selected) >= 60:
            break
    return "\n".join(selected).strip()


def limit_lines(text: str, limit: int = 80) -> str:
    lines = text.splitlines()
    if len(lines) <= limit:
        return text.strip()
    kept = lines[:limit]
    kept.append(f"... ({len(lines) - limit} line(s) omitted by local checkpoint command)")
    return "\n".join(kept).strip()


def first_matching_line(text: str, terms: list[str]) -> str:
    lowered_terms = [term.lower() for term in terms]
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or line.startswith("```"):
            continue
        lowered = line.lower()
        if any(term in lowered for term in lowered_terms):
            return line.lstrip("- ").strip()
    return "UNKNOWN"


def matching_lines(text: str, terms: list[str], limit: int = 6) -> list[str]:
    lowered_terms = [term.lower() for term in terms]
    matches: list[str] = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or line.startswith("```"):
            continue
        lowered = line.lower()
        if any(term in lowered for term in lowered_terms):
            matches.append(line.lstrip("- ").strip())
        if len(matches) >= limit:
            break
    return matches


def joined_matches(text: str, terms: list[str], fallback: str = "UNKNOWN", limit: int = 6) -> str:
    matches = matching_lines(text, terms, limit=limit)
    return "; ".join(matches) if matches else fallback


def bullet_block(text: str) -> str:
    if not text:
        return "- UNKNOWN"
    return "\n".join(f"- {line}" if line else "" for line in text.splitlines())


def git_state() -> dict[str, str]:
    return {
        "branch": run_git(["branch", "--show-current"]),
        "latest_hash": run_git(["log", "-1", "--format=%h"]),
        "latest_subject": run_git(["log", "-1", "--format=%s"]),
        "status": run_git(["status", "--short", "--branch"]),
    }


def display_repo_path() -> str:
    try:
        return f"~/{ROOT.relative_to(Path.home())}"
    except ValueError:
        return str(ROOT)


def build_snapshot(note: str | None) -> str:
    status_text, status_read = read_text_if_present(ROOT / "STATUS.md")
    agents_text, agents_read = read_text_if_present(ROOT / "AGENTS.md")
    git = git_state()

    current_gate = code_block_after_heading(status_text, "Current Gate") if status_read else ""
    completion_line = section(status_text, "Completion Line") if status_read else ""
    missing_closure = section(status_text, "Missing Closure") if status_read else ""
    missing_closure_excerpt = bounded_excerpt(
        missing_closure,
        [
            "external posting",
            "runtime",
            "session snapshot",
            "quest snapshot",
            "automation",
            "scoring",
            "api",
            "hold",
            "block",
        ],
        before=0,
        after=1,
    )
    status_excerpt_parts = [
        part
        for part in [
            limit_lines(section(status_text, "Current Gate"), 90),
            limit_lines(section(status_text, "Completion Line"), 12),
            limit_lines(missing_closure_excerpt, 40),
            limit_lines(section(status_text, "Next Action Owner"), 16),
        ]
        if part
    ]
    status_excerpt = "\n\n".join(status_excerpt_parts)
    agent_excerpt = (
        bounded_excerpt(
            agents_text,
            [
                "do-not-do",
                "not allowed",
                "human seat",
                "seat",
                "handoff",
                "completion line",
                "runtime",
                "external posting",
                "scoring",
                "automation",
            ],
        )
        if agents_read
        else ""
    )

    next_action = first_matching_line(status_text, ["next action owner", "after this patch"])
    do_not_do = first_matching_line(
        agents_text,
        ["must not", "not authorize", "not allowed", "do-not-do", "external posting"],
    )
    recheck_condition = "UNKNOWN"
    runtime_state = joined_matches(
        missing_closure,
        [
            "v12-style session snapshot command implementation",
            "session snapshot output",
            "quest snapshot markdown runtime output",
            "snapshot trajectory / drift delta runtime comparison",
            "full quest map rendering/output/scoring automation",
            "quest snapshot outputs/pdf/screenshot/archive generation",
            "entry window map png/html rendering",
        ],
    )
    external_posting = joined_matches(missing_closure, ["external posting"], limit=2)

    files_read: list[str] = []
    if status_read:
        files_read.append("STATUS.md")
    if agents_read:
        files_read.append("AGENTS.md")
    files_read.extend(["git metadata", "command note"])

    user_note = note if note else "No user note provided."
    as_of = datetime.now().astimezone().isoformat(timespec="seconds")
    repo_path = display_repo_path()

    return f"""# Session Snapshot

## Warning

{WARNING_EN}
{WARNING_JA}
{HANDOFF_WARNING_EN}
{HANDOFF_WARNING_JA}

## As-of Timestamp

{as_of}

## Repository State

- Repo path: {repo_path}
- Branch: {git["branch"]}
- Latest commit short hash: {git["latest_hash"]}
- Latest commit subject: {git["latest_subject"]}
- Git status summary:

~~~text
{git["status"]}
~~~

## Current Governance State

Source excerpt from `STATUS.md`:

~~~text
{status_excerpt if status_excerpt else "STATUS.md not found or no bounded governance excerpt available."}
~~~

## Agent Boundary

Bounded excerpt from `AGENTS.md`:

~~~text
{agent_excerpt if agent_excerpt else "AGENTS.md not found or no bounded boundary excerpt available."}
~~~

## Session Note

{user_note}

## Restart Card

- Current Gate:

~~~text
{current_gate if current_gate else "UNKNOWN"}
~~~

- What changed: Not inferred by local command.
- What remains unfinished: Not inferred by local command.
- Next Action: {next_action}
- Do-Not-Do Boundary: {do_not_do}
- Recheck Condition: {recheck_condition}
- Completion Line:

~~~text
{completion_line if completion_line else "UNKNOWN"}
~~~

- UNKNOWN / Missing Closure:

~~~text
{missing_closure_excerpt if missing_closure_excerpt else "UNKNOWN"}
~~~

- Runtime / automation state: {runtime_state}
- External posting state: {external_posting}

## Source Manifest

{bullet_block(chr(10).join(files_read))}

## Footer

Human keeps the Seat.
This checkpoint does not authorize runtime expansion, external posting, Quest Snapshot auto-generation, scoring, comparison, or automation.
"""


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Write a local V12-style restart checkpoint for the current session."
    )
    parser.add_argument("--note", help="Optional free text note to include in the checkpoint.")
    parser.add_argument(
        "--out",
        default=str(DEFAULT_OUTPUT),
        help="Output markdown path. Defaults to outputs/session_snapshot.md.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    output_path = Path(args.out)
    if not output_path.is_absolute():
        output_path = ROOT / output_path
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(build_snapshot(args.note), encoding="utf-8")
    print(f"Wrote {output_path.relative_to(ROOT) if output_path.is_relative_to(ROOT) else output_path}")


if __name__ == "__main__":
    main()
