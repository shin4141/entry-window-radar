# Entry Window Radar

A save point for long AI/Codex work.

AI-built projects drift when every AI session starts from scratch.

Quest Snapshot preserves the current Gate, next action, and do-not-do boundary.

AIで作った作品を伸ばしたいなら、
現在地を可視化し、判断を残し、次のAIに引き継げ。

If you want your AI-built project to survive and improve,
visualize where it is, save the decision, and hand it to the next AI.

Entry Window Radar is a Quest Snapshot system for AI-built apps, OSS, and long-running projects.

It helps Codex/AI remember:

- where the project is
- what the next action is
- what not to build yet
- what evidence is still missing
- when the project should be rechecked

This is not a market predictor, startup scorer, launch permission system, or automatic decision-maker.

The human keeps the Seat.

## In One Minute

Entry Window Radar helps you save a restart point so future Codex/AI can understand where the work is, what changed, and what not to do next.

For a quick session checkpoint:

```bash
python3 -B tools/save_session_snapshot.py --note "End of session checkpoint"
```

This writes `outputs/session_snapshot.md`. It is a restart checkpoint, not a completion claim, full handoff, or Quest Snapshot generator.

For a project-level Quest Snapshot, use `prompts/quest_snapshot_generator_prompt_v0_1.md` in Codex/AI and save the result in project context or local notes.

Long-context AI can keep a chat going longer, but it can also hide context debt. Entry Window Radar is a restart-boundary tool, not an execution engine.

Not implemented: Quest Snapshot runtime generation, `outputs/quest_snapshot.md`, image/visual/diff automation, scoring, snapshot comparison, AI/API calls, and external posting.

## What It Does

Entry Window Radar helps you create a Quest Snapshot for a repo, app, OSS project, product idea, or workflow.

A Quest Snapshot records:

- Current Gate
- Recommended Action
- One Next Action
- Do-Not-Do Boundary
- Recheck Condition
- UNKNOWN fields
- Optional questions for the Decision Owner
- Completion Line for the next Codex/AI session

## Start Here

1. Open:
   `prompts/quest_snapshot_generator_prompt_v0_1.md`

2. Paste it into Codex / Claude Code / Cursor / ChatGPT.

3. Give the AI your repo, README, product idea, or current project question.

4. Ask it to create a Quest Snapshot.

5. Save the result in Codex memory / project context.

Optional:
Export it as Markdown if you want portability.

Advanced:
Save it into your target repo only if you want version-controlled project-state history.

Example:
`examples/local_markdown_task_tracker_quest_snapshot_example_v0_1.md` shows a public-safe non-Decision-OS Quest Snapshot flow.

## Default Storage

Default:
Codex memory / project context

Optional:
Markdown / local file

Advanced:
Target repo storage

Important:
The Entry Window Radar repo is the rule/template source.
Your live project state usually belongs in Codex memory, local notes, or your target repo, not here.

## Why UNKNOWN Matters

The generator should not fake certainty.

If a field cannot be filled, it marks it UNKNOWN and explains why it matters.

This helps the Decision Owner notice:

- unpaid proof is missing
- the reference chart is too broad
- the next action is vague
- Codex may broaden too early
- the Gate should remain HOLD / PROOF / CAP

UNKNOWN is not failure.

UNKNOWN is where the next decision becomes sharper.

## Core Artifacts

- Quest Position Map:
  first-position chart

- Industry Slope Timeline:
  niche lifecycle chart

- Codex Interpretation Note:
  evidence, counterarguments, source state, unknowns

- Quest Snapshot:
  As-of handoff artifact

- Snapshot Trajectory / Drift Delta:
  recurring TimeTube layer

## Current State

- Generator Prompt: available
- Markdown Template: available
- Visual prototypes: available
- GitHub metadata: prompt-first Quest Snapshot workflow plus local V12-style checkpoint command.
- Non-Decision-OS example: Local Markdown Task Tracker Quest Snapshot example available.
- Dogfood status: Quest Snapshot Generator Prompt PASS; V13 LoopKit remote-source re-entry dogfood PASS using actual GitHub repo evidence at commit `2f52572`; local V13 repo dogfood was blocked only because the local repo path was unavailable.
- Cold-user prompt-only trial: PASS; the README first screen plus Generator Prompt produced a useful Quest Snapshot draft without extra Decision-OS explanation.
- V13 integration validation receipt: Quest Snapshot PASS; Quest Position Map PASS as the first supporting figure; minimum recommended configuration is Quest Snapshot + 1 figure.
- Star-ready: FULL GO. This means the public repo surface is durable enough for organic discovery, stars, casual reading, and cold-reader inspection. It is not external posting permission, active promotion permission, runtime expansion, productization, or automatic launch permission.
- Runtime generation: HOLD
- PDF / PNG / screenshot automation: HOLD
- Snapshot comparison: HOLD
- External posting: HOLD

## Future Command Direction

Minimal `save_session_snapshot` command is available:

```bash
python3 -B tools/save_session_snapshot.py --note "End of session checkpoint"
```

It creates `outputs/session_snapshot.md` as a V12-style restart checkpoint. It does not generate Quest Snapshot automatically and does not call AI or external APIs.
`save_session_snapshot.py` creates a restartable checkpoint, not a full handoff. For project-level handoff, pair it with a Quest Snapshot or a short Handoff Header that states what the receiving AI now owns.

For the short distinction between Session Snapshot, Quest Snapshot, and Full Handoff / Handoff Header, see `docs/quest_snapshot_vs_session_snapshot_explainer_v0_1.md`.

## Community / Contributions

- Contributing: `CONTRIBUTING.md`
- Code of conduct: `CODE_OF_CONDUCT.md`
- Security: `SECURITY.md`
- Support: `SUPPORT.md`
- Issue templates: `.github/ISSUE_TEMPLATE/`

## What This Is Not

This is not:

- a market prediction tool
- investment advice
- an automatic launch permission system
- a VC score
- a full project manager
- an execution engine
- a replacement for the human Decision Owner

## For Codex / AI Agents

When resuming from a Quest Snapshot, Codex/AI must state:

- what it now owns
- current Gate
- next action
- do-not-do boundary
- recheck condition
- Completion Line

Handoff is not complete until the receiving AI knows what it now owns.

Codex/AI must not broaden runtime, posting, scoring, rendering, PDF/PNG/screenshot automation, snapshot comparison, market research, or external API scope without a new Gate.

## Deeper Docs

### Spec Shelf Boundary

Unless this README explicitly says a local command or output is available, Deeper Docs entries are parked documentation / field-note material only.

For every planned/spec-defined future layer referenced below:

- it is not implemented as runtime capability
- it does not grant runtime permission
- it does not change the current Gate
- it remains documentation / field-note material only
- it requires a future explicit Gate before implementation

The audit receipt lives in `docs/spec_shelf_boundary_audit_v0_1.md`.

Entry Window Card is the original single-target diagnosis shape:

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

Entry Window Map is a static local SVG view for showing the current As-of position at a glance. It is screenshot-ready as a shared human/AI Entry Window Card and includes a simple visual Competition Pressure layer; the specification lives in `docs/entry_window_map_v0_1.md`; PNG, HTML, and interactive rendering are not implemented.

Portfolio Entry Horizon is a planned/spec-defined future layer for comparing multiple projects and launch order. Its specification lives in `docs/portfolio_entry_horizon_v0_1.md`; manual templates live in `inputs/projects.md` and `inputs/markets.md`, including Market Slope and Operator Position fields, but automated portfolio scoring is not implemented.

Quest Map Layer is a planned/spec-defined future layer for choosing the right opportunity as a game-like quest under current constraints. Its specification lives in `docs/quest_map_layer_v0_1.md`; Quest Map rendering, scoring automation, and launch permission are not implemented.

Quest Position Map v0.1 is a static/manual SVG prototype for showing quest candidates by proof distance, habitat/reward potential, enemy pressure, and survival/relationship risk. Its specification lives in `docs/quest_position_map_v0_1.md`; the English prototype SVG lives at `outputs/quest_position_map.svg`, with a simplified Japanese visual variant at `outputs/quest_position_map_ja.svg` and interpretation note at `examples/quest_position_map_v0_1_ja.md`; full Quest Map scoring and automated rendering are not implemented.

Industry Slope Timeline v0.1 is a static/manual Japanese SVG prototype for showing where a project or workflow sits inside a reference-market lifecycle. Its specification lives in `docs/industry_slope_timeline_v0_1.md`; the prototype SVG lives at `outputs/industry_slope_timeline_ja.svg`; automatic market analysis, forecasting, and market research are not implemented.

Quest Snapshot / TimeTube Archive is a planned/spec-defined archive layer for saving Quest Map outputs as As-of handoff artifacts. Its specification lives in `docs/quest_snapshot_timetube_archive_v0_1.md`; snapshot export, PDF generation, screenshot automation, and archive generation are not implemented.

Codex Interpretation Note is a planned/spec-defined evidence layer for Quest Snapshot. Its specification lives in `docs/codex_interpretation_note_v0_1.md`; it explains why visuals were placed or classified, but does not add market research, scoring automation, or snapshot generation.

Snapshot Trajectory / Drift Delta is a planned/spec-defined recurring value layer for comparing saved Quest Snapshots over time. Its specification lives in `docs/snapshot_trajectory_drift_delta_v0_1.md`; a static/manual Japanese visual prototype lives at `outputs/snapshot_trajectory_drift_delta_ja.svg`, with an example note at `examples/snapshot_trajectory_drift_delta_v0_1_ja.md`; runtime comparison and automatic drift scoring are not implemented.

Quest Snapshot Visual Design System is a planned/spec-defined design layer for making future Quest Map and Snapshot visuals more consistent, readable, Japanese-friendly, and screenshot-ready. Its specification lives in `docs/quest_snapshot_visual_design_system_v0_1.md`; existing SVGs are not redesigned by this spec.

Quest Map Current Architecture is a documentation summary of the current Quest Map / Quest Snapshot layers, PASS/HOLD/BLOCK state, and next recommended audit phase. It lives in `docs/quest_map_current_architecture_v0_1.md`; it is not an implementation plan or runtime output.

Minimal Runtime Cutline defines Markdown Quest Snapshot output as the first safe future runtime path. It lives in `docs/minimal_runtime_cutline_v0_1.md`; `outputs/quest_snapshot.md` is not implemented yet.

Quest Snapshot Markdown Template is a reusable manual template for future As-of Quest Snapshot artifacts. It lives at `templates/quest_snapshot_template_v0_1.md`; usage notes live in `docs/quest_snapshot_template_usage_v0_1.md`; runtime generation remains HOLD.

Quest Snapshot Storage Modes / User Flow defines Codex memory / project context as the default low-friction storage mode, Markdown/local file as optional portable storage, and target repo storage as an advanced route. It lives in `docs/quest_snapshot_storage_modes_user_flow_v0_1.md`; runtime generation remains HOLD.

Quest Snapshot Generator Prompt is a pasteable prompt for normal users to draft Quest Snapshots in Codex / Claude Code / Cursor / ChatGPT while preserving UNKNOWN fields and human Seat. It lives at `prompts/quest_snapshot_generator_prompt_v0_1.md`; usage notes live in `docs/quest_snapshot_generator_prompt_usage_v0_1.md`; runtime generation remains HOLD.

Handoff Horizon Recession Field Note records the structural observation that long-context AI makes handoff failure less visible, not less important. It lives at `docs/handoff_horizon_recession_field_note_v0_1.md`; it is documentation-only and does not authorize external posting, runtime expansion, Quest Snapshot auto-generation, scoring, snapshot comparison, visual export, hooks/MCP/plugins, or execution-engine work.

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
- an Industry Slope Timeline v0.1 static/manual Japanese SVG prototype
- a Quest Snapshot / TimeTube Archive v0.1 specification for future As-of handoff artifacts
- a Codex Interpretation Note v0.1 specification for future evidence-basis handoff
- a Snapshot Trajectory / Drift Delta v0.1 specification and static/manual Japanese visual prototype for future multi-snapshot comparison
- a Quest Snapshot Visual Design System v0.1 specification for future visual consistency
- a Quest Map Current Architecture v0.1 summary for future Codex/AI re-entry
- a Minimal Runtime Cutline v0.1 decision for future Markdown Quest Snapshot output
- a Quest Snapshot Markdown Template v0.1 for manual As-of snapshot drafting
- a Quest Snapshot Storage Modes / User Flow v0.1 specification for low-friction re-entry
- a Quest Snapshot Generator Prompt v0.1 for pasteable AI-assisted snapshot drafting
- a Spec Shelf Boundary Audit v0.1 for keeping planned/spec-defined future layers non-runtime
- a Handoff Horizon Recession Field Note v0.1 for documenting long-context handoff risk and context debt
- manual Portfolio Entry Horizon input templates in `inputs/projects.md` and `inputs/markets.md`
- output files for an Entry Window report and decision card
- structured `outputs/chart_data.json` and static `outputs/entry_window_map.svg`
- an Entry Window Chart schema for the MVP output shape
- validation and Operator Edge extraction prompts
- one worked example

## Local Usage

Quest Snapshot route: paste `prompts/quest_snapshot_generator_prompt_v0_1.md` into Codex / Claude Code / Cursor / ChatGPT to draft a Quest Snapshot.

Entry Window Card route: paste `prompts/ai_assisted_entry_window_prompt.md` into Codex / GPT / Claude Code to generate an Entry Window Card before or instead of running the CLI.

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
- `outputs/quest_snapshot.md` runtime generation
- Snapshot Trajectory / Drift Delta runtime comparison or automatic drift scoring
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
outputs/industry_slope_timeline_ja.svg
outputs/snapshot_trajectory_drift_delta_ja.svg
prompts/validate_prompt.md
prompts/operator_edge_extraction_prompt_v0_2.md
prompts/ai_assisted_entry_window_prompt.md
prompts/quest_snapshot_generator_prompt_v0_1.md
docs/entry_window_map_v0_1.md
docs/quest_map_layer_v0_1.md
docs/quest_position_map_v0_1.md
docs/industry_slope_timeline_v0_1.md
docs/quest_snapshot_timetube_archive_v0_1.md
docs/codex_interpretation_note_v0_1.md
docs/snapshot_trajectory_drift_delta_v0_1.md
docs/quest_snapshot_visual_design_system_v0_1.md
docs/quest_map_current_architecture_v0_1.md
docs/minimal_runtime_cutline_v0_1.md
docs/quest_snapshot_template_usage_v0_1.md
docs/quest_snapshot_storage_modes_user_flow_v0_1.md
docs/quest_snapshot_generator_prompt_usage_v0_1.md
templates/quest_snapshot_template_v0_1.md
examples/example_001.md
examples/quest_position_map_v0_1.md
examples/quest_position_map_v0_1_ja.md
examples/industry_slope_timeline_v0_1_ja.md
examples/snapshot_trajectory_drift_delta_v0_1_ja.md
examples/v13_loopkit_manual_quest_snapshot_v0_1.md
examples/quest_snapshot_generator_dogfood_v13_loopkit_v0_1.md
```
