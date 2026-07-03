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
Phase 8.7 Single Target Screenshot-Ready Map: PASS
Phase 9.0 Portfolio Entry Horizon Spec: PASS
Phase 9.1 Portfolio Input Templates: PASS
Phase 9.2 Portfolio Dogfood Inputs: PASS
Phase 9.3 Market Slope & Operator Position: PASS
Phase 9.4 Quest Map Layer v0.1 Spec: PASS
Phase 10.1 Reference Chart Quality Spec Patch: PASS
Phase 10.3 Minimum Viable Edge & Starting Advantage Spec Patch: PASS
Phase 10.5 Repeat Frequency / Order Volume Spec Patch: PASS
Phase 10.7 Paid Repeat Signal Spec Patch: PASS
Phase 10.9 Repeat Retention Reason Spec Patch: PASS
Phase 10.10 Survival Cost Drag & Regret Cost Spec Patch: PASS
Phase 10.12 Actual Cashflow Sensitivity Spec Patch: PASS
Phase 10.14 Quantified Runway / Payroll Exposure Spec Patch: PASS
Phase 10.16 Exposure Ratio Spec Patch: PASS
Phase 10.18 Relationship Value Coverage Spec Patch: PASS
Phase 10.20 Relationship Damage Severity Spec Patch: PASS
Phase 10.21 Dependency Asymmetry Spec Patch: PASS
Phase 10.22 Seat-Owned Regret Guard Spec Patch: PASS
Phase 10.23 Quest Snapshot / TimeTube Archive Spec: PASS
Phase 10.24 Quest Position Map Prototype: PASS
Phase 10.25 Quest Position Map Visual Cleanup: PASS
Phase 10.26 Japanese Quest Position Map Visual: PASS
Phase 10.27 Japanese Quest Position Map Clarity: PASS
Phase 10.28 Industry Slope Timeline Prototype: PASS
Phase 10.29 Industry Slope Timeline Niche Meaning: PASS
Phase 10.30 Industry Lifecycle Classification: PASS
Phase 10.31 Codex Interpretation Note / Evidence Basis Spec: PASS
Phase 10.32 Snapshot Trajectory / Drift Delta Spec: PASS
Phase 10.33 Snapshot Trajectory / Drift Delta Visual Prototype: PASS
Phase 10.34 Quest Snapshot Visual Design System Spec: PASS
Phase 10.35 Snapshot Trajectory Visual Cleanup: PASS
Phase 10.36 Quest Map Current Architecture Summary: PASS
Phase 10.37 Architecture Acceptance Audit: PASS
Phase 10.38 Minimal Runtime Cutline / Output Path Decision: PASS
Phase 10.39 Quest Snapshot Markdown Template: PASS
Phase 10.40 V13 LoopKit Manual Quest Snapshot Example: PASS
Phase 10.41 Quest Snapshot Storage Modes / User Flow: PASS
Phase 10.42 Quest Snapshot Generator Prompt: PASS
Phase 10.43 Quest Snapshot Generator Prompt Dogfood: PASS
Phase 10.44 README First-Screen / Use Path Rewrite: PASS
Phase 10.45 README First-Screen Acceptance Audit: PASS
Phase 10.46 V13 Actual Repo Re-entry Dogfood: BLOCKED / local repo unavailable
Phase 10.46b V13 Remote-source Re-entry Dogfood: PASS
Phase 10.47 Remote Dogfood Governance Closeout: PASS
Phase 10.48 Use-ready / Star-ready Gate Audit: USE-READY PASS / STAR-READY HOLD / EXTERNAL POSTING HOLD
Phase 10.49 Cold-user Prompt-only Trial: PASS
Phase 10.50 Cold-user Trial Governance Closeout: PASS
Phase 10.51 V13 Integration Validation Receipt: PASS
Phase 10.52 Community Standards Uplift: PASS
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
- Static `outputs/entry_window_map.svg` is allowed as local-only As-of display and screenshot-ready shared human/AI context, including a simple Competition Pressure layer. It does not authorize posting, PNG, HTML, interactive rendering, portfolio automation, Score History, Entry Window Drift, or advanced scoring.
- Portfolio Entry Horizon is allowed as a specification plus manual dogfood templates in `inputs/projects.md` and `inputs/markets.md`. It does not authorize portfolio scoring, portfolio JSON output, portfolio SVG output, launch-order automation, ranking, or external research.
- Market Slope inputs do not authorize web research or invented market estimates. Market data must be source-backed or marked unknown. Operator Position is a strategic posture, not investment advice. Portfolio Entry Horizon supports launch-order reasoning, not automated permission.
- Quest Map Layer is allowed as a specification in `docs/quest_map_layer_v0_1.md`, including Reference Chart Quality, Minimum Viable Edge, Switching Pressure, Cost Compression Trigger, Survival Cost Drag, Actual Cashflow Sensitivity, Survival Threshold, Quantified Runway / Payroll Exposure, Exposure Anchor, Exposure Severity, Exposure Amount, Exposure Ratio, Reciprocal Value Coverage Ratio, Relationship Value Coverage Band, Relationship Damage Severity, Relationship Damage Quality, Relationship Damage Channels, Damage Mitigation Option, Damage Mitigation Note, Dependency Asymmetry, Counterparty Viability, Shared Sink Risk, Exit Timing Pressure, Relationship Optionality, Inherited / Local Relationship Inertia, Historical Rescue Credit, Legacy Trust Decay, Local Reputation Constraint, Seat-Owned Regret Guard, Protected Priority Stack, Counterfactual Integrity, Future Self-Blame Risk, As-of Reality Shown, Human Override / Commitment, Regret Guard Note, Dependency / Viability Note, Regret Cost of Inaction, Reciprocal Relationship Value, Net Switching Delta, Switching Damage Risk, Split Routing Option, Repeat Frequency / Order Volume, Paid Repeat Signal, Repeat Retention Reason, Output Equivalence, Trial Friction, As-of Starting Advantage, and AI Expansion Potential. It does not authorize Quest Map rendering, Quest Map JSON/SVG outputs, quest scoring automation, external research, posting, or automated launch permission.
- Quest Snapshot / TimeTube Archive is allowed only as a specification in `docs/quest_snapshot_timetube_archive_v0_1.md`. It does not authorize snapshot output files, PDF generation, screenshot automation, Quest Map rendering, CLI behavior changes, Score History, Entry Window Drift, or implementation beyond the current Gate.
- Codex Interpretation Note / Evidence Basis is allowed only as a specification in `docs/codex_interpretation_note_v0_1.md`. It defines a future written evidence layer for Quest Snapshot, but does not authorize market research, source invention, new charts, scoring automation, snapshot output, CLI behavior changes, PDF generation, screenshot automation, or external posting.
- Snapshot Trajectory / Drift Delta is allowed as a specification in `docs/snapshot_trajectory_drift_delta_v0_1.md` and as a cleaned-up static/manual Japanese visual prototype in `outputs/snapshot_trajectory_drift_delta_ja.svg`, with example note in `examples/snapshot_trajectory_drift_delta_v0_1_ja.md`. It does not authorize runtime comparison, automatic drift scoring, live snapshot reading, Quest Snapshot runtime, CLI behavior changes, PDF generation, screenshot automation, or external posting.
- Quest Snapshot Visual Design System is allowed only as a specification in `docs/quest_snapshot_visual_design_system_v0_1.md`. It defines future visual consistency rules, but does not authorize redesigning existing SVGs, new chart logic, renderer implementation, PDF generation, screenshot automation, scoring, market research, CLI behavior changes, or external posting.
- Quest Map Current Architecture is allowed only as a documentation summary in `docs/quest_map_current_architecture_v0_1.md`. It records current artifact roles, PASS/HOLD/BLOCK state, and the next recommended architecture acceptance audit; it does not authorize new analysis fields, runtime outputs, snapshot comparison, automatic drift scoring, renderer implementation, PDF generation, screenshot automation, market research, CLI behavior changes, full Quest Map implementation, or external posting.
- Minimal Runtime Cutline is allowed only as a decision/spec in `docs/minimal_runtime_cutline_v0_1.md`. It selects Markdown `outputs/quest_snapshot.md` as the first safe future runtime path, but does not authorize generating that output yet. Future runtime must assemble manually provided fields only; it must not infer Gate, recommended action, lifecycle classification, risk level, evidence quality, relationship risk, market size, or paid repeat signal.
- Quest Snapshot Markdown Template is allowed only as a reusable manual template in `templates/quest_snapshot_template_v0_1.md`, with usage notes in `docs/quest_snapshot_template_usage_v0_1.md`. It does not authorize runtime generation, `outputs/quest_snapshot.md`, CLI behavior changes, PDF/PNG/screenshot automation, snapshot comparison, automatic scoring, drift scoring, market research, external APIs, full Quest Map implementation, or external posting.
- Quest Snapshot Storage Modes / User Flow is allowed only as a specification in `docs/quest_snapshot_storage_modes_user_flow_v0_1.md`. It defines Codex memory/project context as the default, Markdown/local export as optional, and target repo storage as advanced; it does not authorize a generator prompt, runtime generation, `outputs/quest_snapshot.md`, CLI behavior changes, PDF/PNG/screenshot automation, snapshot comparison, automatic scoring, drift scoring, market research, external APIs, full Quest Map implementation, or external posting.
- Quest Snapshot Generator Prompt is allowed only as a pasteable prompt in `prompts/quest_snapshot_generator_prompt_v0_1.md`, with usage notes in `docs/quest_snapshot_generator_prompt_usage_v0_1.md`. It does not authorize runtime generation, `outputs/quest_snapshot.md`, CLI behavior changes, PDF/PNG/screenshot automation, snapshot comparison, automatic scoring, drift scoring, market research, external APIs, full Quest Map implementation, or external posting.
- README First-Screen / Use Path Rewrite is allowed only as navigation and public-readiness cleanup. It does not authorize runtime generation, `outputs/quest_snapshot.md`, CLI behavior changes, PDF/PNG/screenshot automation, snapshot comparison, automatic scoring, drift scoring, market research, external APIs, full Quest Map implementation, or external posting.
- When referencing the cold-user prompt-only trial, describe it only as prompt-first Use-ready evidence. Do not describe it as runtime validation, do not claim `outputs/quest_snapshot.md` generation exists, and do not use it to authorize automation, scoring, snapshot comparison, PDF/PNG export, Star-ready promotion, or external posting.
- When referencing V13 integration validation, describe it as a read-only receipt from V13 evidence at `field_notes/110_quest_snapshot_as_v13_reconnection_surface.md` and commit `2e12fec`. It supports Quest Snapshot as a V13 reconnection surface and Quest Snapshot + Quest Position Map as the minimum useful configuration. It does not authorize runtime, `outputs/quest_snapshot.md`, automation, visual export, snapshot comparison, scoring or drift scoring, hooks/MCP/pluginization/execution engine work, implementation expansion, or external posting.
- Community standards files are governance/documentation hygiene only. Issue templates and the pull request template must not be interpreted as a feature roadmap. They do not authorize runtime, `outputs/quest_snapshot.md`, automation, visual export, snapshot comparison, scoring or drift scoring, hooks/MCP/pluginization/execution engine work, implementation expansion, or external posting.
- When referencing V13 LoopKit dogfood, do not claim the local V13 repo was inspected. It was unavailable locally. The verified actual repo evidence is the remote-source GitHub clone at commit `2f52572`, recorded in `examples/v13_remote_source_reentry_dogfood_v0_1.md`. Prior notes may support context but must not be treated as actual repo evidence. Remote-source dogfood PASS does not authorize implementation expansion, runtime generation, scoring, snapshot comparison, automation, or external posting.
- Quest Position Map v0.1 is allowed only as a static/manual prototype in `outputs/quest_position_map.svg` and simplified Japanese visual variant in `outputs/quest_position_map_ja.svg`, with its spec in `docs/quest_position_map_v0_1.md`, example in `examples/quest_position_map_v0_1.md`, and Japanese interpretation note in `examples/quest_position_map_v0_1_ja.md`. Future Codex/AI should read the selected card and interpretation note before modifying scope. This does not authorize full Quest Map implementation, automatic scoring, market research, runtime rendering, Quest Snapshot output, PDF generation, screenshot automation, CLI behavior changes, or external posting.
- Industry Slope Timeline v0.1 is allowed only as a static/manual Japanese visual prototype in `outputs/industry_slope_timeline_ja.svg`, with its spec in `docs/industry_slope_timeline_v0_1.md` and example in `examples/industry_slope_timeline_v0_1_ja.md`. Its curve represents a specific niche's entry-window lifecycle, not the whole AI industry peaking or declining. Future Codex/AI should read the lifecycle classification and concern level before assuming a project is late, early, safe, crowded, or risky. It does not authorize automatic market analysis, market research, web research, forecasting logic, scoring automation, full Quest Map implementation, PDF generation, screenshot automation, CLI behavior changes, or external posting.
- Quest Map recommendations must not use broad parent-market charts as strong evidence. Parent-market-only or unknown reference charts should lower confidence and avoid LAUNCH or broad build recommendations.
- Quest Map recommendations must not move from HOLD to PROOF unless Minimum Viable Edge is named. High AI Expansion Potential alone is not permission to launch.
- Quest Map recommendations must not recommend LAUNCH when Repeat Frequency / Order Volume is unknown, or when cost compression is one-off without a repeatable proof path.
- Quest Map recommendations must not recommend LAUNCH without at least PARTIAL Paid Repeat Signal. Free trial satisfaction is not the same as paid repeat.
- Quest Map recommendations must not treat relationship/favor repeats or discount-only repeats as durable habitat evidence.
- Quest Map recommendations must not recommend full replacement only because a cheaper provider exists. Relationship value, survival cost drag, switching damage risk, and split routing options must be named before recommending displacement.
- Quest Map recommendations must not treat cost drag as harmless when Actual Cashflow Sensitivity is unknown. If cashflow sensitivity is high, critical, or unknown, name the survival threshold or require a bounded proof, offset plan, negotiation, or split routing.
- Quest Map recommendations must not treat unknown exposure as safety or as permission for cold replacement. Unknown exposure should trigger measurement, exposure-anchor naming, bounded proof, negotiation, or split routing.
- Quest Map recommendations must not treat unknown Exposure Ratio as safety or use Exposure Ratio alone to recommend cold replacement. Use the ratio to judge urgency, offset planning, and proof priority alongside relationship value, switching damage risk, Carrier Fit, and Reference Chart Quality.
- Quest Map recommendations must not treat relationship value as zero because it is hard to measure or infinite because it is emotionally important. Relationship Value Coverage should guide offset planning and split routing, not cold replacement by itself.
- Quest Map recommendations must not treat split routing as automatically safe. Relationship Damage Severity and damage mitigation must be named when relationship value, exposure ratio, or survival drag make routing changes consequential.
- Quest Map recommendations must not assume relationship value is durable when Counterparty Viability is DECLINING or STRANDED. Dependency Asymmetry, Shared Sink Risk, Exit Timing Pressure, and Relationship Optionality must be named before accepting passive loyalty under meaningful cost drag.
- Quest Map recommendations must not condemn past loyalty under current AI-era conditions. Historical Rescue Credit, Legacy Trust Decay, and Local Reputation Constraint should distinguish gratitude for past help from current survival viability.
- Quest Map recommendations must preserve human Seat ownership. The AI surfaces As-of reality and counterfactual risk, but the human decision owner chooses PRESERVE, SPLIT ROUTE, NEGOTIATE, EXIT, or HOLD.

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
- maintain the Quest Map Layer specification
- maintain the Quest Snapshot / TimeTube Archive specification
- maintain the Codex Interpretation Note / Evidence Basis specification
- maintain the Snapshot Trajectory / Drift Delta specification
- maintain the static/manual Snapshot Trajectory / Drift Delta visual prototype
- maintain the Quest Snapshot Visual Design System specification
- maintain the Quest Map Current Architecture summary
- maintain the Minimal Runtime Cutline decision/spec
- maintain the Quest Snapshot Markdown Template
- maintain the Quest Snapshot Storage Modes / User Flow specification
- maintain the Quest Snapshot Generator Prompt
- maintain README first-screen navigation for Quest Snapshot use
- maintain the static/manual Quest Position Map prototype
- maintain the Japanese static/manual Quest Position Map visual variant
- maintain the static/manual Industry Slope Timeline visual prototype
- maintain data-only `outputs/chart_data.json`
- maintain static `outputs/entry_window_map.svg`, including the simple Competition Pressure layer and screenshot-ready context card layout
- update governance/re-entry files when phase state changes

## Not Allowed Without Explicit GO Or CAP

- do not add external API integrations
- do not add Grok, X, or automated web research
- do not add PNG output
- do not add HTML or interactive Entry Window Map rendering
- do not implement portfolio scoring, ranking, portfolio outputs, portfolio SVG, or launch-order automation
- do not implement full Quest Map rendering, runtime Quest Map outputs, quest scoring automation, or automated launch permission
- do not implement Quest Snapshot outputs, including `outputs/quest_snapshot.md`, PDF export, screenshot automation, or archive generation
- do not implement Snapshot Trajectory / Drift Delta runtime comparison, automatic drift scoring, additional runtime visual output, or trajectory automation
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
