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
Phase 5 Acceptance Audit v0.2: FAIL / Reconciliation in progress
Phase 5.1 Governance State Reconciliation: PASS
Phase 6 Public readiness: HOLD
External API: HOLD
External posting: HOLD
Delivery Scope Radar: BLOCK
V14 deep scoring: BLOCK
```

## V12 Completion Integrity

- Completion means restartable by a future self or next AI/Codex, not merely "the command ran."
- False completion is prohibited.
- Before claiming PASS, make sure Current Gate, Completion Line, Missing Closure, and next action owner are visible in repo-carried files.
- Handoff/re-entry must preserve enough context for another AI/Codex to continue without asking Shin routine cleanup questions.
- If repo state and chat state conflict, stop and reconcile before implementation.

## V13 Loop Governance

- Next loop decisions use GO / HOLD / CAP / BLOCK.
- CAP is not vague permission. CAP must include boundary, stop condition, recheck condition, expected residue, rollback/closure path, and maximum Carrier impact when applicable.
- One loop should improve one main variable.
- Generated outputs must keep next action exactly one.
- Re-entry Capacity must be preserved: next AI/Codex should be able to restart from repo files without hidden chat context.
- Implementation, external posting, Delivery Scope Radar, and V14 deep scoring remain gated.
- Phase 5 Acceptance Audit v0.2 must be rerun after Phase 5.1 reconciliation; do not represent Phase 5 as PASS until that audit passes.

## Allowed In Current MVP

- maintain the local-only CLI
- maintain input/output markdown templates
- maintain `schema/chart.json`
- maintain the worked example
- update governance/re-entry files when phase state changes

## Not Allowed Without Explicit GO Or CAP

- do not add external API integrations
- do not add Grok, X, or automated web research
- do not add PNG output
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
