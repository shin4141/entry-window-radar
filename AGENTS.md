# AGENTS.md

## Project Boundary

Entry Window Radar is a local-only MVP for evaluating the current entry window of a GitHub repo, README, idea, or small project.

Keep the MVP bounded to:

- local markdown inputs
- local markdown outputs
- one Entry Window Chart shape
- Market Line
- Competition Line
- Operator Edge Line
- five entry labels: FAST ENTRY, NICHE WEDGE, WAIT, SHORT CYCLE, AVOID
- one maximum bottleneck
- one bounded next action
- one recheck condition

Entry Window Radar is an as-of diagnosis tool. It is not a future prediction tool and must not judge the operator or founder.

## Current Gate

Read `STATUS.md` before making changes. Do not infer permission from prior commits or prior chat context.

```text
Phase 0 Repo basis: PASS
Phase 1 Local-only CLI v0.1: PASS
Phase 2 Worked Example v0.1: PASS
Phase 2.5 Governance audit: PASS / Patch Required now being closed
Phase 3 Schema / Output stabilization: PASS
Phase 3.5 Governance Re-entry Patch: PASS
Phase 4 README minimal usage/readiness: PASS
Phase 5 Acceptance Audit v0.2: PASS WITH MINOR NOTES
Phase 5.1 Governance State Reconciliation: PASS
Phase 6 Public Readiness Audit: PUBLIC READY WITH MINOR NOTES
GitHub publishing: PASS
Phase 7.1 AI-assisted Usage Prompt: PASS
Phase 7.2 AI-assisted Route Dogfood: PASS
Phase 8.1 Entry Window Map Spec: PASS
Phase 8.2 Structured Output v0.2: PASS
Phase 8.3 Entry Window Map SVG Rendering: PASS
Phase 8.4 V13 LoopKit Map Dogfood: PASS
Phase 8.5 Competition Pressure Layer: PASS
Phase 9.0 Portfolio Entry Horizon Spec: PASS
Phase 9.1 Portfolio Input Templates: PASS
Phase 9.2 Portfolio Dogfood Inputs: PASS
Phase 9.3 Market Slope & Operator Position: PASS
External API: HOLD
External posting: HOLD
Delivery Scope Radar: BLOCK
V14 deep scoring: BLOCK
```

## V12 Completion Integrity

- Completion means restartable by a future self or next AI/Codex, not merely "the command ran."
- False completion is prohibited.
- Before claiming PASS, make sure Current Gate, Completion Line, Missing Closure, and next action owner are visible in repo-carried files.
- Handoff/re-entry must preserve enough context for another AI/Codex to continue without asking the maintainer routine cleanup questions.
- If repo state and chat state conflict, stop and reconcile before implementation.

## V13 Loop Governance

- Next loop decisions use GO / HOLD / CAP / BLOCK.
- CAP is not vague permission. CAP must include boundary, stop condition, recheck condition, expected residue, rollback/closure path, and maximum Carrier impact when applicable.
- One loop should improve one main variable.
- Generated outputs must keep next action exactly one.
- Re-entry Capacity must be preserved: next AI/Codex should be able to restart from repo files without hidden chat context.
- Implementation, external posting, Delivery Scope Radar, and V14 deep scoring remain gated.
- GitHub publishing is PASS for the current public repo; external posting remains HOLD until explicit maintainer GO.
- AI-assisted usage through `prompts/ai_assisted_entry_window_prompt.md` is allowed, but it must not be treated as permission for external APIs, automated web research, or external posting.
- Structured `outputs/chart_data.json` is allowed as data-only output. Its 0-5 levels are display-stage levels, not probabilities, predictions, VC scores, or investment advice.
- Static `outputs/entry_window_map.svg` is allowed as local-only As-of display, including a simple Competition Pressure layer. It does not authorize PNG, HTML, interactive rendering, Score History, Entry Window Drift, or advanced scoring.
- Portfolio Entry Horizon is allowed as a specification plus manual dogfood templates in `inputs/projects.md` and `inputs/markets.md`. It does not authorize portfolio scoring, portfolio JSON output, portfolio SVG output, launch-order automation, ranking, or external research.
- Market Slope inputs do not authorize web research or invented market estimates. Market data must be source-backed or marked unknown. Operator Position is a strategic posture, not investment advice.

## Allowed In Current MVP

- maintain the local-only CLI
- maintain input/output markdown templates
- maintain `schema/chart.json`
- maintain the worked example
- maintain the AI-assisted usage prompt
- maintain the Entry Window Map specification
- maintain the Portfolio Entry Horizon specification
- maintain manual Portfolio Entry Horizon input templates
- maintain manual Portfolio Entry Horizon dogfood inputs
- maintain Market Slope and Operator Position fields as manual inputs
- maintain data-only `outputs/chart_data.json`
- maintain static `outputs/entry_window_map.svg`, including the simple Competition Pressure layer
- update governance/re-entry files when phase state changes

## Not Allowed Without Explicit GO Or CAP

- do not add external API integrations
- do not add Grok, X, or automated web research
- do not add PNG output
- do not add HTML or interactive Entry Window Map rendering
- do not implement portfolio scoring, ranking, portfolio outputs, portfolio SVG, or launch-order automation
- do not implement Delivery Scope Radar
- do not implement V14 Resource Justice deep scoring
- do not add Pro/Advanced scoring
- do not add Score History
- do not add Entry Window Drift
- do not make external posts or posting materials
- do not turn the repo into a generic startup advisor
- do not present the tool as a future prediction engine

## Output Language

Use entry-window language, not certainty language.

Prefer:

```text
As of the available evidence, this looks like NICHE WEDGE.
```

Avoid:

```text
You should build this.
This will win.
```

## Completion Line

The local-only MVP is complete for its current gate only when the repo is committed, the working tree is clean, generated outputs still run locally, and `STATUS.md` preserves Current Gate, Completion Line, Missing Closure, next action owner, and re-entry notes.
