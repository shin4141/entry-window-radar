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
- output files for an Entry Window report and decision card
- an Entry Window Chart schema for the MVP output shape
- validation and Operator Edge extraction prompts
- one worked example

Not included:

- external API integrations
- automated web research
- Grok, X, or API research
- Delivery Scope Radar
- V14 Resource Justice deep scoring
- prediction of future success

## Boundary

Entry Window Radar discovers and compares possible future lines.

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
prompts/validate_prompt.md
prompts/operator_edge_extraction_prompt_v0_2.md
examples/example_001.md
```
