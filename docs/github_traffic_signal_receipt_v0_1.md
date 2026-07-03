# GitHub Traffic Signal Receipt v0.1

## As-of

2026-07-03 JST

## Observed Metrics

- Clones in last 14 days: 452
- Unique cloners in last 14 days: 169
- Total views in last 14 days: 12
- Unique visitors in last 14 days: 1

## Context

Entry Window Radar recently reached:

- Use-ready: PASS
- Command-ready: PASS
- Star-ready: SOFT GO
- External posting: HOLD

## Interpretation

This traffic is recorded as an early external signal.
It does not prove human adoption or usage.
The clone/view mismatch should be treated cautiously.

Clone count is much higher than view count, so automation, bots, indexing, GitHub tooling, or non-human clone activity may be involved.
Unique visitors remains very low.

Treat this as external residue / traffic anomaly worth tracking, not as validation of usage.

## Decision-OS Interpretation

Using V9 / V13 framing:

- Star or clone activity is not proof of correctness.
- It is external residue indicating the artifact entered some external retrieval or option set.
- The correct action is observation, not promotion escalation.

## Current Gate After Observation

- Use-ready: PASS
- Command-ready: PASS
- Star-ready: SOFT GO
- External posting: HOLD
- Runtime expansion: HOLD

## Recheck Condition

Recheck GitHub Traffic after one of:

- 7 days
- a new star
- repeated unique visitors
- issue/PR activity
- external mention
- manual user trial

## Do-Not-Do Boundary

Do not use this traffic signal to authorize:

- external posting
- runtime expansion
- Quest Snapshot auto-generation
- AI/API calls
- screenshot automation
- scoring/drift scoring
- market claims
- adoption claims

## Completion Line

Entry Window Radar records early GitHub Traffic as an external-contact signal while preserving Star-ready SOFT GO, External posting HOLD, and runtime expansion HOLD.
