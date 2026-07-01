#!/usr/bin/env python3
"""Local-only Entry Window Radar CLI v0.1."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUTS = {
    "idea": ROOT / "inputs" / "idea.md",
    "evidence": ROOT / "inputs" / "evidence.md",
    "operator": ROOT / "inputs" / "operator.md",
}
OUTPUT_REPORT = ROOT / "outputs" / "report.md"
OUTPUT_DECISION = ROOT / "outputs" / "decision.md"
SCHEMA = ROOT / "schema" / "chart.json"

LABELS = {"FAST ENTRY", "NICHE WEDGE", "WAIT", "SHORT CYCLE", "AVOID"}

@dataclass
class Line:
    summary: str
    signals: list[str]
    open_questions: list[str]


@dataclass
class Diagnosis:
    as_of: str
    entry_label: str
    market_line: Line
    competition_line: Line
    operator_edge_line: Line
    maximum_bottleneck: str
    next_action: str
    confidence: str
    missing_evidence: list[str]
    risk: list[str]
    recheck_condition: str


def read_inputs() -> dict[str, str]:
    return {name: path.read_text(encoding="utf-8") for name, path in INPUTS.items()}


def validate_schema_file() -> None:
    json.loads(SCHEMA.read_text(encoding="utf-8"))


def section(markdown: str, heading: str) -> str:
    pattern = rf"^## {re.escape(heading)}\s*$"
    match = re.search(pattern, markdown, flags=re.MULTILINE)
    if not match:
        return ""
    start = match.end()
    next_heading = re.search(r"^## ", markdown[start:], flags=re.MULTILINE)
    end = start + next_heading.start() if next_heading else len(markdown)
    return markdown[start:end]


def authored_text(text: str) -> str:
    blocks = re.findall(r"```(?:text)?\n(.*?)```", text, flags=re.DOTALL)
    if blocks:
        return "\n".join(blocks)
    return text


def clean_lines(text: str) -> list[str]:
    lines: list[str] = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("#") or line.startswith("```"):
            continue
        if line in {"-", "- ", "FAST ENTRY | NICHE WEDGE | WAIT | SHORT CYCLE | AVOID | Unknown"}:
            continue
        if re.fullmatch(r"[A-Za-z][A-Za-z /-]*:", line):
            continue
        if "|" in line:
            continue
        if re.fullmatch(r"-\s*", line):
            continue
        line = re.sub(r"^-+\s*", "", line).strip()
        if line:
            lines.append(line)
    return lines


def compact(items: list[str], limit: int = 5) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for item in items:
        normalized = re.sub(r"\s+", " ", item).strip()
        if not normalized or normalized.lower() in seen:
            continue
        seen.add(normalized.lower())
        result.append(normalized)
        if len(result) == limit:
            break
    return result


def evidence_lines(inputs: dict[str, str], key: str) -> list[str]:
    if key == "market":
        chunks = [
            section(inputs["idea"], "Pain Or Demand"),
            section(inputs["evidence"], "Market Evidence"),
        ]
    elif key == "competition":
        chunks = [section(inputs["evidence"], "Competition Evidence")]
    else:
        chunks = [
            section(inputs["idea"], "Current Artifact Evidence"),
            section(inputs["operator"], "Operator Context"),
            section(inputs["operator"], "What The Operator Knows Or Notices"),
            section(inputs["operator"], "Existing Assets"),
            section(inputs["operator"], "Proof Capacity"),
        ]
    return compact(clean_lines("\n".join(authored_text(chunk) for chunk in chunks)))


def explicit_missing(inputs: dict[str, str]) -> list[str]:
    return compact(clean_lines(authored_text(section(inputs["evidence"], "Missing Evidence"))))


def expected_label(inputs: dict[str, str]) -> str | None:
    for line in clean_lines(authored_text(section(inputs["idea"], "Expected Entry Label"))):
        value = line.strip().upper()
        if value in LABELS:
            return value
    return None


def as_of_date(inputs: dict[str, str]) -> str:
    for raw in authored_text(section(inputs["idea"], "Artifact")).splitlines():
        line = raw.strip()
        if not line.lower().startswith("as-of date:"):
            continue
        value = line.split(":", 1)[1].strip()
        if value:
            return value
    return date.today().isoformat()


def summarize_line(name: str, signals: list[str]) -> Line:
    if signals:
        summary = f"{name} has {len(signals)} usable as-of signal(s) in the current inputs."
        open_questions = [f"What primary evidence would strengthen the {name.lower()} judgment?"]
    else:
        summary = f"{name} is not yet supported by concrete as-of evidence in the current inputs."
        open_questions = [f"What concrete evidence describes the current {name.lower()}?"]
    return Line(summary=summary, signals=signals or ["No concrete signal provided."], open_questions=open_questions)


def choose_bottleneck(market: list[str], competition: list[str], operator: list[str]) -> str:
    counts = {
        "Market evidence": len(market),
        "Competition evidence": len(competition),
        "Operator edge evidence": len(operator),
    }
    return min(counts, key=lambda item: (counts[item], item))


def infer_label(
    market: list[str], competition: list[str], operator: list[str], wanted: str | None
) -> str:
    total = len(market) + len(competition) + len(operator)
    if total < 3:
        return "WAIT"
    if wanted in LABELS and wanted not in {"FAST ENTRY", "AVOID"}:
        return wanted
    if market and operator and not competition:
        return "NICHE WEDGE"
    if market and operator and competition:
        return "NICHE WEDGE"
    return "WAIT"


def confidence(total_signals: int) -> str:
    if total_signals >= 8:
        return "Medium"
    if total_signals >= 4:
        return "Low-medium"
    return "Low"


def missing_evidence(
    market: list[str], competition: list[str], operator: list[str], explicit: list[str]
) -> list[str]:
    missing = list(explicit)
    if not market:
        missing.append("Concrete market demand, pain, urgency, or usage evidence.")
    if not competition:
        missing.append("Named alternatives, incumbent behavior, saturation, or absorption-risk evidence.")
    if not operator:
        missing.append("Specific operator edge, artifact proof, distribution path, or proof-capacity evidence.")
    return compact(missing, limit=8)


def next_action(label: str, bottleneck: str) -> str:
    if label == "WAIT":
        return f"Collect one primary evidence item for the current {bottleneck.lower()} before changing the entry label."
    if label == "NICHE WEDGE":
        return "Define one narrow user/workflow wedge and gather one proof point that the operator can serve it better than a generic alternative."
    if label == "SHORT CYCLE":
        return "Run one bounded proof cycle with a clear stop condition."
    if label == "AVOID":
        return "Pause entry work until the bottleneck evidence materially changes."
    return "Run one small proof target with a bounded scope and recheck the entry window afterward."


def diagnose(inputs: dict[str, str]) -> Diagnosis:
    market = evidence_lines(inputs, "market")
    competition = evidence_lines(inputs, "competition")
    operator = evidence_lines(inputs, "operator")
    total = len(market) + len(competition) + len(operator)
    label = infer_label(market, competition, operator, expected_label(inputs))
    bottleneck = choose_bottleneck(market, competition, operator)
    missing = missing_evidence(market, competition, operator, explicit_missing(inputs))
    return Diagnosis(
        as_of=as_of_date(inputs),
        entry_label=label,
        market_line=summarize_line("Market Line", market),
        competition_line=summarize_line("Competition Line", competition),
        operator_edge_line=summarize_line("Operator Edge Line", operator),
        maximum_bottleneck=bottleneck,
        next_action=next_action(label, bottleneck),
        confidence=confidence(total),
        missing_evidence=missing or ["No major missing evidence listed."],
        risk=["The judgment may shift when concrete primary evidence is added."],
        recheck_condition="Re-run after adding market, competition, or operator-edge evidence that materially changes the as-of picture.",
    )


def bullet(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def render_report(diagnosis: Diagnosis) -> str:
    return f"""# Entry Window Report

## As-Of Judgment

As-of date: {diagnosis.as_of}
Entry Label: {diagnosis.entry_label}
Confidence: {diagnosis.confidence}

As of the available evidence, this is an entry-window diagnostic, not a prediction of future success and not a command to build.

## Market Line

Summary: {diagnosis.market_line.summary}

Signals:
{bullet(diagnosis.market_line.signals)}

Open questions:
{bullet(diagnosis.market_line.open_questions)}

## Competition Line

Summary: {diagnosis.competition_line.summary}

Signals:
{bullet(diagnosis.competition_line.signals)}

Open questions:
{bullet(diagnosis.competition_line.open_questions)}

## Operator Edge Line

Summary: {diagnosis.operator_edge_line.summary}

Signals:
{bullet(diagnosis.operator_edge_line.signals)}

Open questions:
{bullet(diagnosis.operator_edge_line.open_questions)}

## Maximum Bottleneck

{diagnosis.maximum_bottleneck}

## Missing Evidence

{bullet(diagnosis.missing_evidence)}

## Risk

{bullet(diagnosis.risk)}

## Next Action

{diagnosis.next_action}

## Recheck Condition

{diagnosis.recheck_condition}

## Boundary Note

This report describes the current entry posture from available evidence. It does not judge the operator or founder.
"""


def render_decision(diagnosis: Diagnosis) -> str:
    return f"""# Entry Window Decision Card

As of the available evidence, this looks like:

Entry Label: {diagnosis.entry_label}
Maximum Bottleneck: {diagnosis.maximum_bottleneck}
Next Action: {diagnosis.next_action}
Confidence: {diagnosis.confidence}

Market Line: {diagnosis.market_line.summary}
Competition Line: {diagnosis.competition_line.summary}
Operator Edge Line: {diagnosis.operator_edge_line.summary}

Missing Evidence:
{bullet(diagnosis.missing_evidence)}

Risk:
{bullet(diagnosis.risk)}

Recheck Condition: {diagnosis.recheck_condition}
"""


def main() -> int:
    validate_schema_file()
    diagnosis = diagnose(read_inputs())
    OUTPUT_REPORT.write_text(render_report(diagnosis), encoding="utf-8")
    OUTPUT_DECISION.write_text(render_decision(diagnosis), encoding="utf-8")
    print(f"Wrote {OUTPUT_REPORT.relative_to(ROOT)}")
    print(f"Wrote {OUTPUT_DECISION.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
