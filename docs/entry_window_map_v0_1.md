# Entry Window Map v0.1

## Purpose

Entry Window Map shows the current As-of position of a repo, README, idea, or small project inside an entry window.

It is a map of current evidence, not a prediction of future success.

## Core Axes

### X-Axis: Market Readiness

Meaning: how much current evidence suggests demand, pain strength, user urgency, market movement, or usable timing.

### Y-Axis: Operator Edge

Meaning: how much current evidence suggests this operator has a specific edge in this market, repo, workflow, distribution path, or proof loop.

### Pressure Layer: Competition Pressure

Meaning: how much current evidence suggests saturation, incumbent strength, major-player absorption risk, fast substitutes, price pressure, or LLM commoditization.

## Labels

The map can display one Entry Label:

- FAST ENTRY
- NICHE WEDGE
- WAIT
- SHORT CYCLE
- AVOID

## Interpretation Rules

- High Market Readiness + high Operator Edge + manageable Competition Pressure can support FAST ENTRY.
- Medium Market Readiness + high Operator Edge + crowded space can support NICHE WEDGE.
- Low Market Readiness or thin evidence can support WAIT.
- Usable but time-limited opportunity can support SHORT CYCLE.
- High competition pressure with weak operator edge or weak evidence can support AVOID.

## Non-Goals

The map is not:

- a future prediction engine
- investment advice
- VC scoring
- founder/personality judgment
- market oracle
- automated launch permission
- external research automation

## Important Boundary

The map should not say:

- "This will succeed."
- "You should build this."
- "This founder is weak."
- "This market is guaranteed."

It may say:

- "The current evidence places this around NICHE WEDGE."
- "The bottleneck is independent user proof."
- "The next action is one bounded proof point."

## Data Model Direction

Phase 8.2 adds data-only structured output:

- `outputs/chart_data.json`

Phase 8.3 adds local-only static SVG rendering:

- `outputs/entry_window_map.svg`

Phase 8.5 renders Competition Pressure as a simple visual pressure layer in the SVG:

- a calm scaled ring around the plotted point
- the numeric Competition Pressure value remains a display-stage level

Future implementation may add:

- `outputs/entry_window_map.html`

PNG, HTML, interactive rendering, history, and drift remain out of scope.

Potential future data shape:

```text
{
  "as_of": "...",
  "target": "...",
  "market_readiness": 0-5,
  "operator_edge": 0-5,
  "competition_pressure": 0-5,
  "entry_label": "...",
  "maximum_bottleneck": "...",
  "next_action": "...",
  "confidence": "...",
  "missing_evidence": [],
  "interpretation_note": "Display-stage levels, not probabilities or predictions."
}
```

These values are display-stage levels, not precise probabilities.

## Current Design Decision

Entry Window Radar should evolve from terminal-first CLI toward AI-first Entry Window Card + Entry Window Map workflow.

Terminal route remains available, but star-ready value depends on making the current position visible at a glance.

## Completion Line

Entry Window Map v0.1 has documented meaning, axes, labels, non-goals, structured data, static SVG output, and a simple Competition Pressure layer, without expanding into prediction, history, drift, PNG, HTML, or external scope.
