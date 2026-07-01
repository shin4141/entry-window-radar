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

## Planned Entry Window Map

Entry Window Map v0.1 is a spec-defined future view for showing the current As-of position at a glance. The specification lives in `docs/entry_window_map_v0_1.md`; chart rendering is not implemented yet.

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
- output files for an Entry Window report and decision card
- structured `outputs/chart_data.json` for future Entry Window Map use
- an Entry Window Chart schema for the MVP output shape
- validation and Operator Edge extraction prompts
- one worked example

## Local Usage

Run from the repo root:

```bash
python3 -B tools/entry_window_radar.py
```

For a minimal worked example, see `examples/example_001.md`.

AI-assisted route: paste `prompts/ai_assisted_entry_window_prompt.md` into Codex / GPT / Claude Code to generate an Entry Window Card before or instead of running the CLI.

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
```

`outputs/chart_data.json` contains display-stage levels for future Entry Window Map use. It is not chart rendering and it is not a probability, VC score, prediction, or investment signal.

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
- Entry Window Map rendering
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
prompts/validate_prompt.md
prompts/operator_edge_extraction_prompt_v0_2.md
prompts/ai_assisted_entry_window_prompt.md
docs/entry_window_map_v0_1.md
examples/example_001.md
```
