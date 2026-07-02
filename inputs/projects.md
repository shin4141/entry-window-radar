# Portfolio Projects

Use this file to describe multiple projects owned by the same operator.

This is a manual dogfood snapshot for Portfolio Entry Horizon. It does not trigger portfolio scoring, ranking, rendering, or launch-order automation.

Definitions:

- Launch readiness means how close this project is to being shown, tested, or launched without major additional build cost.
- Build burden means time, cost, cognitive load, explanation load, or implementation complexity before meaningful proof.
- Proof path means one bounded proof point that can be collected soon.
- Carrier fit means whether pursuing this preserves operator time, attention, recovery capacity, credibility, and re-entry capacity.

## Project: Entry Window Radar

- Project summary: Local-only As-of diagnosis tool for deciding whether a repo, README, idea, or small project currently sits inside a usable entry window.
- Current artifact: Public GitHub repo with CLI, Entry Window Card, chart_data.json, Entry Window Map SVG, competition pressure ring, worked examples, dogfood notes, and Portfolio Entry Horizon templates.
- Target user / workflow: Builders or AI-assisted operators deciding whether one idea or repo should be entered, narrowed, held, or avoided before spending more build energy.
- Operator edge: Shin has created the tool through repeated Codex-assisted Launch Capsule loops, dogfood runs, and boundary-first governance around false completion, scope drift, and As-of diagnosis.
- Launch readiness: High for local/OSS usage; the repo already runs locally and has examples, but public messaging and user proof remain gated.
- Build burden: Low for continued OSS readiness; medium if the next step becomes clearer public explanation or user onboarding.
- Proof path: Ask one technically capable builder to run the AI-assisted prompt or CLI on one repo and report whether the Entry Window Card and Map changed their next action.
- Carrier fit: Strong if kept local-only and bounded; weaker if it turns into external posting, broad startup-advisor positioning, or support-heavy public launch.
- Competition pressure: Medium to high from generic GPT advice, startup scoring templates, market-analysis prompts, and AI project-planning tools.
- Missing evidence: Independent user runs, comprehension by first-time readers, examples outside Shin's own project set, and evidence that users do not misread it as prediction or investment advice.
- Recheck condition: Recheck after one independent user completes a diagnosis and can explain the label, bottleneck, and next action without extra Shin context.

## Project: Decision-OS V13 LoopKit

- Project summary: Boundary-first loop governance layer for deciding whether the next AI loop should GO, HOLD, CAP, or BLOCK after completion/handoff.
- Current artifact: Separate V13 LoopKit repo/context referenced by dogfood notes; includes README/AGENTS/docs/examples where available, Next Action Card, Context Risk, Route Fidelity, Returnability, Consult Mode, and GOAL Health Overlay.
- Target user / workflow: AI-assisted operators who need restartable handoffs, false-completion prevention, and next-action confidence across repeated Codex/AI loops.
- Operator edge: Shin has Decision-OS V9-V13 lineage, direct workflow failures, accepted loop-library residue, and repeated observations from real AI-loop operation.
- Launch readiness: Medium; artifact evidence exists and dogfood was strong, but the narrow user/workflow wedge and first external proof point are not yet collected.
- Build burden: Medium; the concept is coherent, but explanation load is non-trivial because it can look like a prompt kit unless the restartability workflow is made concrete.
- Proof path: Define one narrow restartability / handoff / next-action-confidence workflow and get one external user to complete it.
- Carrier fit: Strong if launched as a narrow governance kit; weaker if framed as generic agent automation or expanded into execution infrastructure too early.
- Competition pressure: High from generic agent automation, prompt packs, model-native memory/resume, workflow tools, and automation frameworks.
- Missing evidence: Independent users, comparison against generic alternatives, first-time reader completion, user-written handoffs or field notes, and repeated human-looking reuse signals.
- Recheck condition: Recheck after one external user writes a usable handoff or next-action confidence check from the LoopKit without Shin guiding the session.

## Project: Decision-OS V12 Completion Integrity

- Project summary: Governance layer defining completion as restartable by a future self or next AI, not merely that a command ran.
- Current artifact: Concept and governance invariant carried in this repo's STATUS/AGENTS lineage and prior Decision-OS context; standalone artifact status not confirmed here.
- Target user / workflow: AI-assisted operators who need to prevent false completion, stale handoffs, and context-loss after long coding or planning loops.
- Operator edge: Shin has direct false-completion recovery experience and has embedded the invariant across Entry Window Radar repo governance.
- Launch readiness: Medium-low; the invariant is crisp and proven internally, but it may need a standalone note, checklist, or repo slice before external use.
- Build burden: Low to medium; the core concept is already articulated, but packaging it without overlap with V13 LoopKit needs care.
- Proof path: Create one five-minute completion-integrity checklist and have a future AI/Codex use it to restart a task without chat context.
- Carrier fit: Strong if kept as a small reusable invariant; weaker if it becomes a broad methodology document.
- Competition pressure: Medium from generic project handoff checklists, AI task-management habits, and model-native summaries.
- Missing evidence: Standalone artifact, external reader comprehension, before/after example, and proof that it catches false completion better than ordinary checklists.
- Recheck condition: Recheck after the invariant successfully helps one separate repo or thread avoid a false PASS.

## Project: Decision-OS V10 Survival-Bounded Planning

- Project summary: Planning approach that treats human capacity, recovery, and survivability as hard boundaries rather than afterthoughts.
- Current artifact: Decision-OS V10 lineage referenced in context; standalone artifact status not confirmed in this repo.
- Target user / workflow: Operators deciding what to build, defer, or stop when time, health, attention, or recovery capacity are binding constraints.
- Operator edge: Shin's Decision-OS lineage centers Carrier preservation and practical operating boundaries rather than abstract productivity.
- Launch readiness: Low to medium; concept may be meaningful, but visible artifact, examples, and target workflow are not yet clear here.
- Build burden: Medium; explanation load is high because the project touches sensitive capacity and planning language.
- Proof path: Use one real planning decision to show how a survival-bounded plan changes scope, timing, or stop conditions.
- Carrier fit: Potentially strong because the concept protects capacity; risky if packaging it requires heavy writing or emotional explanation.
- Competition pressure: Medium from productivity frameworks, burnout-aware planning, coaching materials, and generic AI planning prompts.
- Missing evidence: Standalone example, target audience, proof that the method changes decisions, and safe wording that avoids becoming personal judgment.
- Recheck condition: Recheck after one concrete planning case shows a bounded plan that prevents overextension.

## Project: Decision-OS V9 Impact-Weighted Release

- Project summary: Release-governance approach that weighs release impact, risk, and timing rather than treating all outputs as equal.
- Current artifact: Decision-OS V9 lineage referenced in context; standalone artifact status not confirmed in this repo.
- Target user / workflow: Builders deciding what to release, hold, revise, or sequence when multiple artifacts compete for attention.
- Operator edge: Shin has a release-governance lineage that connects launch timing, completion integrity, and Carrier preservation.
- Launch readiness: Low to medium; the name is strong, but concrete artifact and proof path are less visible than Entry Window Radar or V13 LoopKit.
- Build burden: Medium; the idea needs one small release-decision example to become legible.
- Proof path: Apply the method to one already-finished artifact and show why release timing or scope changes.
- Carrier fit: Strong if used as an internal decision aid; weaker if launched before it has a concise example.
- Competition pressure: Medium from release checklists, product-management frameworks, and generic prioritization matrices.
- Missing evidence: Current artifact, example decision, target user, and proof that it improves release sequencing over simpler priority lists.
- Recheck condition: Recheck after one release decision is documented with impact-weighted reasoning and a clear next action.

## Project: Value Dynamics / Settlement Conditions

- Project summary: Conceptual framework for understanding value exchange, settlement conditions, and what must be true for a relationship, deal, or workflow to resolve cleanly.
- Current artifact: Known concept in Shin's project set; artifact status not confirmed in this repo.
- Target user / workflow: Operators negotiating scope, value, boundaries, or mutual expectations in projects, collaborations, or service relationships.
- Operator edge: Shin's Decision-OS work already emphasizes boundary conditions, closure, re-entry, and non-coercive decision framing.
- Launch readiness: Low; promising but not yet visibly packaged as a repo, checklist, or worked example.
- Build burden: Medium to high; the domain can become abstract, sensitive, or easily misunderstood without careful examples.
- Proof path: Write one concrete settlement-condition example showing what evidence or agreement closes a loop.
- Carrier fit: Medium; it may clarify valuable boundary work, but could consume explanation energy quickly.
- Competition pressure: Medium from negotiation frameworks, pricing strategy, coaching, and generic business advice.
- Missing evidence: Definitions, examples, target audience, artifact, and proof that the concept helps resolve a real decision without over-personalizing it.
- Recheck condition: Recheck after one bounded example distinguishes settlement conditions from generic negotiation or advice.

## Project: AI video creation workflow

- Project summary: Workflow for producing AI-assisted video assets or short-form creative output with repeatable steps, quality checks, and tool boundaries.
- Current artifact: Candidate project from Shin's portfolio context; current repo/artifact not confirmed here.
- Target user / workflow: Creator/operator making short videos, explainers, demos, or visual launch assets with AI-assisted production.
- Operator edge: Shin can combine AI workflow design, launch discipline, and taste checks from repo/dogfood practice, but video-specific proof is not visible in this repo.
- Launch readiness: Low to medium; likely practical and market-legible, but current artifact and repeatable workflow evidence are missing here.
- Build burden: Medium; requires tool selection, media quality iteration, examples, and possibly high attention cost.
- Proof path: Produce one complete short video from a documented workflow and record time, steps, quality gaps, and reuse potential.
- Carrier fit: Mixed; strong if it creates reusable launch assets, weak if it becomes tool-chasing or production-heavy.
- Competition pressure: High from AI video tools, creator workflows, template packs, agencies, and fast-changing model features.
- Missing evidence: Sample output, workflow doc, tool list, quality bar, target user, and proof that Shin's workflow beats generic AI video templates.
- Recheck condition: Recheck after one finished video demonstrates a repeatable quality threshold without excessive recovery cost.

## Project: Crypto / HQ operation notes

- Project summary: Operational notes around crypto, HQ, coordination, or decision routines; exact product boundary not yet clear.
- Current artifact: Candidate project from Shin's portfolio context; current repo/artifact not confirmed here.
- Target user / workflow: Unknown; could involve internal operations, community coordination, decision logs, or crypto-related execution notes.
- Operator edge: Shin may have operator-context insight, but the specific edge is not yet visible in this repo.
- Launch readiness: Low; project boundary, artifact, target user, and proof path are unclear.
- Build burden: Unknown to high; ambiguity, regulatory/compliance sensitivity, and explanation load may be significant.
- Proof path: Define one non-financial, non-advisory operational workflow and identify one safe proof point.
- Carrier fit: Unclear; could become heavy or risky if it drifts into financial advice, market calls, or public claims.
- Competition pressure: High from crypto tooling, analytics, community operations, trading content, and regulatory-sensitive advice spaces.
- Missing evidence: Scope boundary, non-advisory framing, current artifact, target workflow, operator edge, and safe proof point.
- Recheck condition: Recheck only after the project is narrowed to a clear operational note format that does not imply trading, investment, or market advice.
