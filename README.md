# Entry Window Radar

Is this idea early, late, crowded, or still worth a narrow entry?

Entry Window Radar is a small local-only MVP for evaluating whether a GitHub repo, README, idea, or small project currently sits inside a usable entry window.

It does not predict future success. It produces an as-of entry posture based on visible evidence.

## Entry Window Card

```text
Entry Label: FAST ENTRY | NICHE WEDGE | WAIT | SHORT CYCLE | AVOID

Market Line:
Competition Line:
Operator Edge Line:

Missing Evidence:
Maximum Bottleneck:
Next Action:
Confidence:
Risk:
Recheck Condition:
```

## Entry Window Map

Entry Window Map is a static local SVG view for showing the current As-of position at a glance. It is screenshot-ready as a shared human/AI Entry Window Card and includes a simple visual Competition Pressure layer; the specification lives in `docs/entry_window_map_v0_1.md`; PNG, HTML, and interactive rendering are not implemented.

Portfolio Entry Horizon is a planned/spec-defined future layer for comparing multiple projects and launch order. Its specification lives in `docs/portfolio_entry_horizon_v0_1.md`; manual templates live in `inputs/projects.md` and `inputs/markets.md`, including Market Slope and Operator Position fields, but automated portfolio scoring is not implemented.

Quest Map Layer is a planned/spec-defined future layer for choosing the right opportunity as a game-like quest under current constraints. Its specification lives in `docs/quest_map_layer_v0_1.md`; Quest Map rendering, scoring automation, and launch permission are not implemented.

Quest Position Map v0.1 is a static/manual SVG prototype for showing quest candidates by proof distance, habitat/reward potential, enemy pressure, and survival/relationship risk. Its specification lives in `docs/quest_position_map_v0_1.md`; the English prototype SVG lives at `outputs/quest_position_map.svg`, with a simplified Japanese visual variant at `outputs/quest_position_map_ja.svg` and interpretation note at `examples/quest_position_map_v0_1_ja.md`; full Quest Map scoring and automated rendering are not implemented.

Quest Snapshot / TimeTube Archive is a planned/spec-defined archive layer for saving Quest Map outputs as As-of handoff artifacts. Its specification lives in `docs/quest_snapshot_timetube_archive_v0_1.md`; snapshot export, PDF generation, screenshot automation, and archive generation are not implemented.

## Three Lines

### Market Line

Signals about current demand, pain strength, market growth, capital movement, user urgency, and major-player attention.

### Competition Line

Signals about saturation, incumbent strength, major-player entry, LLM absorption risk, price pressure, and how quickly alternatives are improving.

### Operator Edge Line

Signals about what this operator knows, has, notices, can show, can distribute, or can prove faster than a generic competitor.

## Entry Labels

### FAST ENTRY

The entry window appears open. Enter small and fast, with a bounded proof target.

### NICHE WEDGE

The broad space may be crowded, but there may still be a narrow edge or neglected workflow to enter through.

### WAIT

The market may come later, but current evidence is too early, too thin, or too ambiguous.

### SHORT CYCLE

The opportunity may be usable for a short build-and-recover cycle, but long-term holding looks risky.

### AVOID

Given current market, competition, absorption, and operator evidence, now is not the time to enter.

## MVP Scope

This repo currently contains a local-only MVP.

Included:

- input templates for an idea, evidence, and operator context
- a local-only CLI that reads `inputs/*.md` and writes markdown outputs
- an AI-assisted usage prompt for chat-first diagnosis
- an Entry Window Map v0.1 specification for a future view
- a Portfolio Entry Horizon v0.1 specification for a future multi-project comparison layer
- a Quest Map Layer v0.1 specification for future quest-style opportunity selection
- a Quest Position Map v0.1 static/manual SVG prototype, including a Japanese visual variant
- a Quest Snapshot / TimeTube Archive v0.1 specification for future As-of handoff artifacts
- manual Portfolio Entry Horizon input templates in `inputs/projects.md` and `inputs/markets.md`
- output files for an Entry Window report and decision card
- structured `outputs/chart_data.json` and static `outputs/entry_window_map.svg`
- an Entry Window Chart schema for the MVP output shape
- validation and Operator Edge extraction prompts
- one worked example

## Local Usage

AI-assisted route: paste `prompts/ai_assisted_entry_window_prompt.md` into Codex / GPT / Claude Code to generate an Entry Window Card before or instead of running the CLI.

For terminal/local output generation, run from the repo root:

```bash
python3 -B tools/entry_window_radar.py
```

For a minimal worked example, see `examples/example_001.md`.

Reads:

```text
inputs/idea.md
inputs/evidence.md
inputs/operator.md
```

Writes:

```text
outputs/report.md
outputs/decision.md
outputs/chart_data.json
outputs/entry_window_map.svg
```

`outputs/chart_data.json` contains display-stage levels for Entry Window Map use. `outputs/entry_window_map.svg` is a static As-of display, not a probability, VC score, prediction, or investment signal.

## Current Limits

This is a local-only, rule/template-based MVP. It does not call external services, perform external research, or create posting materials.

Not included:

- external API integrations
- automated web research
- Grok, X, or API research
- Delivery Scope Radar
- V14 Resource Justice deep scoring
- Pro/Advanced scoring
- Score History
- Entry Window Drift
- external posting materials
- PNG, HTML, or interactive Entry Window Map rendering
- portfolio scoring, portfolio outputs, or launch-order automation
- full Quest Map rendering, runtime Quest Map outputs, or quest scoring automation
- Quest Snapshot outputs, PDF export, screenshot automation, or archive generation
- prediction of future success

## Boundary

Entry Window Radar describes current entry lines from available evidence.

V13 remains the GO / HOLD / CAP / BLOCK gate.

This tool may say:

```text
This looks like FAST ENTRY.
This looks like NICHE WEDGE.
This looks like WAIT.
```

It must not say:

```text
You should build this.
This will succeed.
The future is predictable from this score.
```

## Re-entry

Next AI/Codex should read `STATUS.md` and `AGENTS.md` first.

## File Map

```text
README.md
AGENTS.md
STATUS.md
inputs/idea.md
inputs/evidence.md
inputs/operator.md
schema/chart.json
outputs/report.md
outputs/decision.md
outputs/chart_data.json
outputs/entry_window_map.svg
outputs/quest_position_map.svg
outputs/quest_position_map_ja.svg
prompts/validate_prompt.md
prompts/operator_edge_extraction_prompt_v0_2.md
prompts/ai_assisted_entry_window_prompt.md
docs/entry_window_map_v0_1.md
docs/quest_map_layer_v0_1.md
docs/quest_position_map_v0_1.md
docs/quest_snapshot_timetube_archive_v0_1.md
examples/example_001.md
examples/quest_position_map_v0_1.md
examples/quest_position_map_v0_1_ja.md
```
