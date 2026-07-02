# Codex Interpretation Note / Evidence Basis v0.1

## Purpose

Codex Interpretation Note explains why a Quest Map position or Industry Slope Timeline classification was chosen.

It should help:

- the user understand the basis of the chart
- future Codex/AI continue without re-asking for context
- reviewers see which claims are grounded, estimated, or unknown
- prevent broad market hype from replacing reference-chart reasoning
- prevent weak apps/tools from ignoring commoditization or absorption risk

Core principle:

```text
Figures show position. Interpretation notes carry the evidence.
```

## Relationship To Existing Artifacts

### Quest Position Map

Quest Position Map shows where each quest sits by reward distance, habitat/reward potential, enemy pressure, and survival/relationship risk.

### Industry Slope Timeline

Industry Slope Timeline shows where the selected reference niche sits in its lifecycle.

### Quest Snapshot / TimeTube Archive

Quest Snapshot / TimeTube Archive saves both the visuals and the interpretation note as an As-of artifact.

### Codex Interpretation Note

Codex Interpretation Note explains why the visuals were placed or classified that way.

## Required Sections

### A. Reference Chart Used

Explain what reference chart is being used and why the parent market alone is insufficient.

Example:

Do not judge a specific AI app by the whole AI market. Use the relevant app category, buyer willingness, workflow urgency, distribution channel, and monetization behavior.

### B. Position Reasoning

Explain why the quest is placed where it is.

Include:

- why proof/reward distance is close or far
- why habitat/reward potential is low, medium, or high
- why enemy/competition pressure is low, medium, or high
- why survival/relationship risk is low, medium, or high
- why the recommended action is LAUNCH / PROOF / SHORT CYCLE / INCUBATE / HOLD / AVOID / SALVAGE

### C. Industry Lifecycle Reasoning

Explain why the niche is classified as:

- PRE-WAVE
- EARLY ENTRY
- STEEPENING
- CROWDED GROWTH
- ABSORPTION RISK
- MATURE / LOCAL HABITAT
- POST-FOMO / SALVAGE
- DECLINING / AVOID

Also explain the Concern Level:

- LOW
- WATCH
- PREPARE
- URGENT
- AVOID

### D. Evidence Basis

List the evidence basis using these labels:

- SOURCE-BACKED: backed by a cited source, dataset, report, direct measurement, or explicit project evidence
- OBSERVED: observed from repo, user workflow, buyer behavior, paid repeat, project history, or local facts
- ESTIMATED: inferred from available evidence, but not directly measured
- UNKNOWN: not known yet; should not be treated as true
- ASSUMPTION: explicitly assumed for a bounded evaluation

### E. Market / Capital / Size Claims

Rules:

- Do not invent market-size numbers.
- If market size, investment amount, funding flow, growth rate, or "2030 range" is mentioned, it must be source-backed or marked UNKNOWN.
- If a range is used, label it as As-of reference range, not prediction.
- If no source is available, write:

```text
Market-size evidence: UNKNOWN / source required.
```

### F. Commoditization / Absorption Risk

Explain why weak apps, generic tools, or thin wrappers may be commoditized.

Potential reasons:

- LLM-native feature absorption
- OS/platform absorption
- SaaS/incumbent absorption
- easy replication
- weak payment willingness
- no distribution edge
- no workflow lock-in
- no paid repeat
- no domain proof
- no trust or relationship moat
- generic UX with no buyer urgency

Important:

Do not claim every app will fail. Explain which apps/tools are vulnerable and what evidence would reduce the risk.

### G. Why This Niche May Still Be Valid

Explain why the selected niche may still have a proof window.

Potential reasons:

- local/workflow-specific friction
- repeated manual work
- current cost pressure
- output equivalence can be tested
- buyer already pays for the workflow
- paid repeat can be measured
- relationship or implementation friction slows generic absorption
- domain knowledge or operational fit matters

### H. Counterarguments

List at least 3 counterarguments.

Examples:

- The market may be real, but this operator may lack distribution.
- The workflow may repeat, but buyers may self-serve with free tools.
- Output may be cheaper, but not trusted enough.
- AI tools may absorb the niche before paid repeat appears.
- Relationship damage may exceed cost savings.
- Market size may be large, but reference chart quality may still be weak.

### I. Missing Evidence

List what is missing before stronger action.

Examples:

- source-backed market range
- buyer willingness to pay
- output equivalence
- paid repeat
- repeat retention reason
- direct local/reference chart
- exposure ratio
- relationship value coverage
- competitive comparison
- distribution path

### J. Do-Not-Do Boundary

Restate the boundary in plain language.

Example:

```text
Do not broaden into a generic AI automation product until one paid repeat and output equivalence are shown.
```

### K. Recheck Condition

State when the note should be updated.

Examples:

- after paid repeat appears
- after buyer refuses with a reason
- after source-backed market data is added
- after competitor/LLM/SaaS absorption appears
- after reference chart quality improves
- after survival exposure changes

## Output Style

The note should be readable by both humans and Codex.

It should be:

- concise but evidence-aware
- clear about unknowns
- explicit about assumptions
- useful for future handoff
- not promotional
- not overconfident

## Future Placement

A future Quest Snapshot may include:

- Quest Position Map image
- Industry Slope Timeline image
- Codex Interpretation Note
- Quest Card
- Completion Line
- Recheck Condition

This specification does not implement snapshot output, PDF generation, screenshot automation, or archive generation.

## Governance Rules

- Do not let visuals stand alone if the decision is non-trivial.
- Do not let source-free market claims appear as facts.
- Do not convert assumptions into certainty.
- Do not treat the note as prediction.
- Do not remove the human Seat.
- Do not allow Codex to implement beyond the current Gate.
- If evidence is missing, mark it as missing.
- If a claim is only estimated, mark it as estimated.
- If the selected reference chart is weak, lower confidence.
- If the note is stale, mark it stale before reuse.

## Example Mini Note

### Quest

AI-low-adoption recurring workflow compression

### Recommended Action

PROOF

### Reference Chart

AI-low-adoption recurring workflow compression, not the whole AI market

### Evidence Basis

- OBSERVED: current workflow cost compression scenario
- ESTIMATED: buyer switching pressure
- UNKNOWN: source-backed market size
- UNKNOWN: paid repeat
- UNKNOWN: output equivalence

### Commoditization Risk

Generic AI apps may be absorbed by LLMs/SaaS, but workflow-specific adoption may remain valid if paid repeat and output equivalence are proven.

### Counterarguments

- buyer may self-serve
- output may not be trusted
- competitor may copy
- relationship damage may matter

### Do-Not-Do

Do not build a generic automation platform before proof.

## Completion Line

Codex Interpretation Note / Evidence Basis v0.1 defines the written evidence layer that explains why Quest Map visuals are placed/classified as they are, while keeping charts visually simple and preventing unsourced market claims, commoditization blind spots, and broad hype from driving decisions.
