# Snapshot Trajectory / Drift Delta v0.1

## Purpose

Snapshot Trajectory / Drift Delta compares multiple Quest Snapshots over time.

It turns isolated As-of judgments into a TimeTube-like project trajectory.

Core principle:

```text
One snapshot shows current position.
Multiple snapshots show trajectory.
```

## Relationship To Prior Artifacts

### Quest Position Map

Quest Position Map shows where a quest sits now.

### Industry Slope Timeline

Industry Slope Timeline shows where the reference niche sits in its lifecycle.

### Codex Interpretation Note

Codex Interpretation Note explains why the position or classification was chosen.

### Quest Snapshot

Quest Snapshot saves a single As-of decision state.

### Snapshot Trajectory / Drift Delta

Snapshot Trajectory / Drift Delta compares snapshots to reveal movement, drift, stagnation, or escalation.

## What This Layer Is

This layer is a comparison layer for saved Quest Snapshots.

It is not:

- prediction
- market forecasting
- automatic scoring
- performance guarantee
- investment advice
- AI-owned decision-making
- a replacement for human Seat
- proof that the project should continue

## Minimum Comparable Fields

Required comparison fields:

- Snapshot ID
- Date / As-of time
- Project / Quest name
- Current Gate
- Recommended Action
- One-line Judgment
- Reference Chart Used
- Reference Chart Quality
- Lifecycle Classification
- Concern Level
- Key Evidence Status
- Missing Evidence
- One Next Action
- Do-Not-Do Boundary
- Recheck Condition
- Seat Owner
- Completion Line

Optional comparison fields:

- Paid Repeat Signal
- Repeat Frequency / Order Volume
- Repeat Retention Reason
- Minimum Viable Edge
- Exposure Ratio
- Survival Cost Drag
- Relationship Value Coverage
- Relationship Damage Severity
- Counterparty Viability
- Future Self-Blame Risk
- Regret Guard Note

## Drift Delta Types

### A. Gate Delta

Examples:

- HOLD -> PROOF
- PROOF -> INCUBATE
- PROOF -> HOLD
- INCUBATE -> SHORT CYCLE
- PROOF -> AVOID

Meaning:

Shows whether the project is allowed to move, should remain bounded, or must stop.

### B. Evidence Delta

Examples:

- output equivalence: UNKNOWN -> OBSERVED
- paid repeat: NONE -> PARTIAL -> STRONG
- reference chart: PARENT MARKET ONLY -> CLOSE PROXY -> DIRECT
- market-size evidence: UNKNOWN -> SOURCE-BACKED
- buyer willingness: ASSUMPTION -> OBSERVED

Meaning:

Shows whether the project's confidence is improving or still hype-based.

### C. Risk Delta

Examples:

- enemy pressure: LOW -> MEDIUM -> HIGH
- survival exposure: LOW -> HIGH
- relationship damage: UNKNOWN -> HIGH
- absorption risk: MEDIUM -> HIGH
- cashflow sensitivity: UNKNOWN -> CRITICAL

Meaning:

Shows whether continued work is becoming safer or more dangerous.

### D. Scope Delta

Examples:

- Do-not-do boundary unchanged
- boundary loosened after evidence
- boundary violated
- Codex broadened beyond Gate
- scope expanded without recheck

Meaning:

Shows whether the project is staying on route or drifting.

### E. Action Delta

Examples:

- next action completed
- next action changed
- next action repeated because evidence did not improve
- next action became stale
- next action became too broad

Meaning:

Shows whether work is compounding or looping.

### F. Seat / Handoff Delta

Examples:

- Seat owner clear -> unclear
- Completion Line present -> missing
- Codex knows what it owns -> unclear
- recheck condition preserved -> lost

Meaning:

Shows whether handoff integrity is improving or degrading.

## Trajectory Labels

### COMPOUNDING

Evidence improves, Gate advances or remains intentionally bounded, and Do-Not-Do boundaries are respected.

### STALLED

Gate remains the same because required evidence has not changed.

### DRIFTING

Scope expands, assumptions increase, or Do-Not-Do boundaries weaken without evidence.

### RISK ESCALATING

Survival, relationship, enemy, absorption, or cashflow risks increase.

### READY TO ADVANCE

Required evidence appears and next Gate may be reconsidered by the human Seat.

### SHOULD HOLD

Evidence is missing, risk is high, or reference chart remains weak.

### SHOULD CAP

The project has useful direction but must not broaden further.

### SHOULD BLOCK

Continuation would violate Seat, Gate, survival, or evidence boundaries.

## Visual Direction

Future Figure 4:

Snapshot Trajectory / Drift Delta

Suggested layout:

- x-axis: snapshot time
- rows: Gate, Evidence, Risk, Scope, Next Action, Do-Not-Do, Seat/Handoff
- each column: one snapshot
- highlight changes between columns
- show trajectory label at the top
- show "what changed" and "what did not change"

Example visual table:

```text
Snapshot 1      Snapshot 2      Snapshot 3
PROOF           PROOF           INCUBATE
Paid Repeat: NO PARTIAL         STRONG
Risk: MEDIUM    MEDIUM          HIGH
Boundary: same  same            narrower
Trajectory: STALLED -> COMPOUNDING -> RISK ESCALATING
```

Important:

Do not implement this visual in Phase 10.32.

Only specify it.

## Drift Prevention

This layer prevents drift by preserving:

- previous Gate
- previous reason
- previous boundary
- previous missing evidence
- previous recheck condition

It asks:

- did we satisfy the recheck condition?
- did we move without evidence?
- did we broaden because we were anxious?
- did Codex implement beyond the Gate?
- did the project's risk increase silently?

## Codex Role

Future Codex should:

- read the latest snapshot
- compare it with the prior snapshot when available
- state what changed
- state what did not change
- identify whether the next action is still valid
- detect if the project is drifting
- preserve the current Gate
- avoid broadening without evidence
- ask for human Seat decision when Gate should change

Codex should not:

- silently continue from stale state
- treat old snapshots as permanent truth
- upgrade Gate automatically
- ignore missing evidence
- treat trajectory labels as final decision
- override human Seat

## User Value

Initial charts are useful once.

Trajectory becomes useful repeatedly.

Users get:

- less repeated explanation
- clearer project memory
- visible progress or stagnation
- early warning of drift
- stronger handoff to Codex/AI
- fewer uncontrolled feature additions
- evidence-based Gate changes
- a durable record of why the project changed direction

## Example

### Project

AI-low-adoption recurring workflow compression

### Snapshot 1

- Gate: PROOF
- Paid Repeat: NONE
- Output Equivalence: UNKNOWN
- Do-not-do: do not build generic automation product

### Snapshot 2

- Gate: PROOF
- Paid Repeat: PARTIAL
- Output Equivalence: OBSERVED
- Do-not-do: do not broaden beyond one workflow

### Snapshot 3

- Gate: INCUBATE candidate
- Paid Repeat: STRONG
- Risk: competitor pressure rising
- Do-not-do: do not build platform before repeat package stabilizes

### Trajectory

COMPOUNDING, but risk rising.

### Interpretation

The project is no longer only hype-based, but it should advance carefully rather than broaden.

## Governance Rules

- Do not compare snapshots without As-of dates.
- Do not upgrade Gate automatically.
- Do not treat missing prior snapshot as failure; mark trajectory as first snapshot.
- If the latest snapshot is stale, mark stale before reuse.
- If the Do-Not-Do boundary changed, explain why.
- If evidence did not improve, do not advance the Gate.
- If risk increased, do not hide it behind progress.
- If the human Seat is unclear, HOLD.
- If Codex does not know what it now owns, handoff is incomplete.
- A trajectory label is advisory, not permission.

## Completion Line

Snapshot Trajectory / Drift Delta v0.1 defines how multiple Quest Snapshots can be compared over time to reveal project trajectory, drift, evidence improvement, risk escalation, and handoff integrity without becoming automatic scoring, prediction, or launch permission.
