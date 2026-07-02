#!/usr/bin/env python3
"""Local-only Entry Window Radar CLI v0.1."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import date
from html import escape
from pathlib import Path
from textwrap import wrap


ROOT = Path(__file__).resolve().parents[1]
INPUTS = {
    "idea": ROOT / "inputs" / "idea.md",
    "evidence": ROOT / "inputs" / "evidence.md",
    "operator": ROOT / "inputs" / "operator.md",
}
OUTPUT_REPORT = ROOT / "outputs" / "report.md"
OUTPUT_DECISION = ROOT / "outputs" / "decision.md"
OUTPUT_CHART_DATA = ROOT / "outputs" / "chart_data.json"
OUTPUT_MAP_SVG = ROOT / "outputs" / "entry_window_map.svg"
SCHEMA = ROOT / "schema" / "chart.json"

LABELS = {"FAST ENTRY", "NICHE WEDGE", "WAIT", "SHORT CYCLE", "AVOID"}
REQUIRED_SCHEMA_FIELDS = {
    "as_of",
    "entry_label",
    "market_line",
    "competition_line",
    "operator_edge_line",
    "rationale",
    "maximum_bottleneck",
    "next_action",
    "confidence",
    "missing_evidence",
    "risk",
    "recheck_condition",
}


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
    rationale: str
    maximum_bottleneck: str
    next_action: str
    confidence: str
    missing_evidence: list[str]
    risk: list[str]
    recheck_condition: str


@dataclass
class ChartData:
    as_of: str
    target: str
    market_readiness: int
    operator_edge: int
    competition_pressure: int
    entry_label: str
    maximum_bottleneck: str
    next_action: str
    confidence: str
    missing_evidence: list[str]
    interpretation_note: str


def read_inputs() -> dict[str, str]:
    return {name: path.read_text(encoding="utf-8") for name, path in INPUTS.items()}


def validate_schema_file() -> None:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    schema_fields = set(schema.get("properties", {}))
    missing_fields = REQUIRED_SCHEMA_FIELDS - schema_fields
    if missing_fields:
        missing = ", ".join(sorted(missing_fields))
        raise ValueError(f"schema/chart.json is missing required MVP field(s): {missing}")


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


def target_name(inputs: dict[str, str]) -> str:
    for raw in authored_text(section(inputs["idea"], "Artifact")).splitlines():
        line = raw.strip()
        if not line.lower().startswith("name:"):
            continue
        value = line.split(":", 1)[1].strip()
        if value:
            return value
    return "Unspecified target"


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


def rationale(label: str) -> str:
    if label == "WAIT":
        return "The current inputs do not yet provide enough concrete as-of evidence to support a stronger entry label."
    if label == "NICHE WEDGE":
        return "The current inputs suggest a narrow workflow may exist, but the evidence does not support a broad or fast-entry posture yet."
    if label == "SHORT CYCLE":
        return "The current inputs suggest a bounded proof cycle may be more appropriate than a durable entry claim."
    if label == "AVOID":
        return "The current inputs show the entry posture is constrained enough that pausing is the clearest as-of diagnosis."
    return "The current inputs show market, competition, and operator-edge signals strong enough for a small bounded proof target."


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
        rationale=rationale(label),
        maximum_bottleneck=bottleneck,
        next_action=next_action(label, bottleneck),
        confidence=confidence(total),
        missing_evidence=missing or ["No major missing evidence listed."],
        risk=["The judgment may shift when concrete primary evidence is added."],
        recheck_condition="Re-run after adding market, competition, or operator-edge evidence that materially changes the as-of picture.",
    )


def validate_diagnosis(diagnosis: Diagnosis) -> None:
    if diagnosis.entry_label not in LABELS:
        raise ValueError(f"entry_label must be one of {sorted(LABELS)}")
    for field in ("maximum_bottleneck", "next_action", "confidence"):
        value = getattr(diagnosis, field)
        if not value or "\n" in value:
            raise ValueError(f"{field} must be exactly one non-empty line")
    if not diagnosis.missing_evidence:
        raise ValueError("missing_evidence must be present")
    if not diagnosis.operator_edge_line.summary:
        raise ValueError("operator_edge_line must remain present")


def display_levels(diagnosis: Diagnosis) -> tuple[int, int, int]:
    levels = {
        "FAST ENTRY": (4, 4, 2),
        "NICHE WEDGE": (3, 4, 4),
        "WAIT": (1, 1, 2),
        "SHORT CYCLE": (4, 3, 4),
        "AVOID": (1, 1, 5),
    }
    return levels[diagnosis.entry_label]


def chart_data(diagnosis: Diagnosis, inputs: dict[str, str]) -> ChartData:
    market_readiness, operator_edge, competition_pressure = display_levels(diagnosis)
    return ChartData(
        as_of=diagnosis.as_of,
        target=target_name(inputs),
        market_readiness=market_readiness,
        operator_edge=operator_edge,
        competition_pressure=competition_pressure,
        entry_label=diagnosis.entry_label,
        maximum_bottleneck=diagnosis.maximum_bottleneck,
        next_action=diagnosis.next_action,
        confidence=diagnosis.confidence,
        missing_evidence=diagnosis.missing_evidence,
        interpretation_note=(
            "Display-stage levels, not precise probabilities, future predictions, "
            "VC scores, or investment advice."
        ),
    )


def validate_chart_data(data: ChartData) -> None:
    for field in ("market_readiness", "operator_edge", "competition_pressure"):
        value = getattr(data, field)
        if not isinstance(value, int) or not 0 <= value <= 5:
            raise ValueError(f"{field} must be an integer from 0 to 5")
    if data.entry_label not in LABELS:
        raise ValueError(f"entry_label must be one of {sorted(LABELS)}")
    for field in ("maximum_bottleneck", "next_action", "confidence"):
        value = getattr(data, field)
        if not value or "\n" in value:
            raise ValueError(f"{field} must be exactly one non-empty line")
    if not isinstance(data.missing_evidence, list):
        raise ValueError("missing_evidence must be a list")
    if "not precise probabilities" not in data.interpretation_note:
        raise ValueError("interpretation_note must preserve the display-stage boundary")


def bullet(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def render_report(diagnosis: Diagnosis) -> str:
    return f"""# Entry Window Report

## As-Of Diagnosis

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

## Rationale

{diagnosis.rationale}

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

Entry Label: {diagnosis.entry_label}
Maximum Bottleneck: {diagnosis.maximum_bottleneck}
Next Action: {diagnosis.next_action}
Confidence: {diagnosis.confidence}

Missing Evidence:
{bullet(diagnosis.missing_evidence)}
"""


def render_chart_data(data: ChartData) -> str:
    payload = {
        "as_of": data.as_of,
        "target": data.target,
        "market_readiness": data.market_readiness,
        "operator_edge": data.operator_edge,
        "competition_pressure": data.competition_pressure,
        "entry_label": data.entry_label,
        "maximum_bottleneck": data.maximum_bottleneck,
        "next_action": data.next_action,
        "confidence": data.confidence,
        "missing_evidence": data.missing_evidence,
        "interpretation_note": data.interpretation_note,
    }
    return json.dumps(payload, indent=2, ensure_ascii=False) + "\n"


def read_chart_data_output() -> ChartData:
    payload = json.loads(OUTPUT_CHART_DATA.read_text(encoding="utf-8"))
    return ChartData(
        as_of=str(payload["as_of"]),
        target=str(payload["target"]),
        market_readiness=int(payload["market_readiness"]),
        operator_edge=int(payload["operator_edge"]),
        competition_pressure=int(payload["competition_pressure"]),
        entry_label=str(payload["entry_label"]),
        maximum_bottleneck=str(payload["maximum_bottleneck"]),
        next_action=str(payload["next_action"]),
        confidence=str(payload["confidence"]),
        missing_evidence=list(payload["missing_evidence"]),
        interpretation_note=str(payload["interpretation_note"]),
    )


def svg_text_block(text: str, x: int, y: int, width: int, line_height: int = 16) -> str:
    lines = wrap(text, width=width)
    return "\n".join(
        f'<text x="{x}" y="{y + index * line_height}" class="small">{escape(line)}</text>'
        for index, line in enumerate(lines)
    )


def render_entry_window_map_svg(data: ChartData) -> str:
    width = 760
    height = 560
    plot_left = 96
    plot_top = 92
    plot_size = 330
    plot_bottom = plot_top + plot_size
    plot_right = plot_left + plot_size
    market_x = plot_left + (data.market_readiness / 5) * plot_size
    operator_y = plot_bottom - (data.operator_edge / 5) * plot_size
    point_label_x = min(int(market_x) + 14, plot_right - 130)
    point_label_y = max(int(operator_y) - 10, plot_top + 18)
    pressure_radius = 14 + data.competition_pressure * 7
    pressure_label_x = plot_left + 18
    pressure_label_y = plot_top + 24

    grid_lines: list[str] = []
    tick_labels: list[str] = []
    for value in range(6):
        x = plot_left + value * plot_size / 5
        y = plot_bottom - value * plot_size / 5
        grid_lines.append(f'<line x1="{x:.1f}" y1="{plot_top}" x2="{x:.1f}" y2="{plot_bottom}" class="grid"/>')
        grid_lines.append(f'<line x1="{plot_left}" y1="{y:.1f}" x2="{plot_right}" y2="{y:.1f}" class="grid"/>')
        tick_labels.append(f'<text x="{x:.1f}" y="{plot_bottom + 22}" class="tick" text-anchor="middle">{value}</text>')
        tick_labels.append(f'<text x="{plot_left - 16}" y="{y + 4:.1f}" class="tick" text-anchor="end">{value}</text>')

    note_x = 510
    note_y = 122
    bottleneck = svg_text_block(f"Bottleneck: {data.maximum_bottleneck}", note_x, note_y + 116, 34)
    next_action = svg_text_block(f"Next action: {data.next_action}", note_x, note_y + 170, 34)

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
  <title id="title">Entry Window Map</title>
  <desc id="desc">A local-only As-of display of Market Readiness, Operator Edge, and Competition Pressure.</desc>
  <style>
    .bg {{ fill: #f8fafc; }}
    .panel {{ fill: #ffffff; stroke: #cbd5e1; stroke-width: 1; }}
    .grid {{ stroke: #e2e8f0; stroke-width: 1; }}
    .axis {{ stroke: #334155; stroke-width: 1.6; }}
    .title {{ fill: #0f172a; font-family: Arial, sans-serif; font-size: 24px; font-weight: 700; }}
    .label {{ fill: #334155; font-family: Arial, sans-serif; font-size: 14px; font-weight: 700; }}
    .small {{ fill: #334155; font-family: Arial, sans-serif; font-size: 13px; }}
    .tick {{ fill: #64748b; font-family: Arial, sans-serif; font-size: 12px; }}
    .pressure-ring {{ fill: #e0f2fe; fill-opacity: 0.18; stroke: #64748b; stroke-width: 2; stroke-dasharray: 5 5; stroke-opacity: 0.7; }}
    .pressure-label {{ fill: #475569; font-family: Arial, sans-serif; font-size: 12px; font-weight: 700; }}
    .point {{ fill: #2563eb; stroke: #ffffff; stroke-width: 3; }}
    .tag {{ fill: #dbeafe; stroke: #93c5fd; stroke-width: 1; }}
    .boundary {{ fill: #475569; font-family: Arial, sans-serif; font-size: 12px; }}
  </style>
  <rect class="bg" x="0" y="0" width="{width}" height="{height}"/>
  <text x="40" y="48" class="title">Entry Window Map</text>
  <text x="40" y="72" class="small">Target: {escape(data.target)} | As-of: {escape(data.as_of)}</text>
  <rect class="panel" x="32" y="82" width="430" height="400" rx="6"/>
  {chr(10).join(grid_lines)}
  <line x1="{plot_left}" y1="{plot_bottom}" x2="{plot_right}" y2="{plot_bottom}" class="axis"/>
  <line x1="{plot_left}" y1="{plot_top}" x2="{plot_left}" y2="{plot_bottom}" class="axis"/>
  {chr(10).join(tick_labels)}
  <text x="{(plot_left + plot_right) / 2:.1f}" y="{plot_bottom + 52}" class="label" text-anchor="middle">Market Readiness</text>
  <text transform="translate(48 {(plot_top + plot_bottom) / 2:.1f}) rotate(-90)" class="label" text-anchor="middle">Operator Edge</text>
  <circle cx="{market_x:.1f}" cy="{operator_y:.1f}" r="{pressure_radius}" class="pressure-ring"/>
  <text x="{pressure_label_x}" y="{pressure_label_y}" class="pressure-label">Competition pressure layer: {data.competition_pressure}/5</text>
  <circle cx="{market_x:.1f}" cy="{operator_y:.1f}" r="8" class="point"/>
  <rect x="{point_label_x - 6}" y="{point_label_y - 17}" width="124" height="24" rx="5" class="tag"/>
  <text x="{point_label_x}" y="{point_label_y}" class="label">{escape(data.entry_label)}</text>
  <rect class="panel" x="490" y="82" width="230" height="400" rx="6"/>
  <text x="{note_x}" y="{note_y}" class="label">As-of Position</text>
  <text x="{note_x}" y="{note_y + 28}" class="small">Market Readiness: {data.market_readiness}/5</text>
  <text x="{note_x}" y="{note_y + 50}" class="small">Operator Edge: {data.operator_edge}/5</text>
  <text x="{note_x}" y="{note_y + 72}" class="small">Competition Pressure: {data.competition_pressure}/5</text>
  <text x="{note_x}" y="{note_y + 94}" class="small">Confidence: {escape(data.confidence)}</text>
  {bottleneck}
  {next_action}
  <text x="40" y="518" class="boundary">As-of display levels, not probabilities or predictions.</text>
  <text x="40" y="538" class="boundary">This is not investment advice, VC scoring, or automated launch permission.</text>
</svg>
"""


def main() -> int:
    validate_schema_file()
    inputs = read_inputs()
    diagnosis = diagnose(inputs)
    validate_diagnosis(diagnosis)
    map_data = chart_data(diagnosis, inputs)
    validate_chart_data(map_data)
    OUTPUT_REPORT.write_text(render_report(diagnosis), encoding="utf-8")
    OUTPUT_DECISION.write_text(render_decision(diagnosis), encoding="utf-8")
    OUTPUT_CHART_DATA.write_text(render_chart_data(map_data), encoding="utf-8")
    svg_data = read_chart_data_output()
    validate_chart_data(svg_data)
    OUTPUT_MAP_SVG.write_text(render_entry_window_map_svg(svg_data), encoding="utf-8")
    print(f"Wrote {OUTPUT_REPORT.relative_to(ROOT)}")
    print(f"Wrote {OUTPUT_DECISION.relative_to(ROOT)}")
    print(f"Wrote {OUTPUT_CHART_DATA.relative_to(ROOT)}")
    print(f"Wrote {OUTPUT_MAP_SVG.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
