# Minimal Runtime Cutline / Output Path Decision v0.1

## Purpose

Minimal Runtime Cutline / Output Path Decision v0.1 defines the first safe runtime output path for Quest Map / Quest Snapshot after architecture audit.

The purpose is to identify the smallest runtime step that can preserve handoff value without accidentally turning visual prototypes into full automation, scoring, prediction, market research, or uncontrolled Quest Map implementation.

## Decision

The first runtime output should be:

```text
outputs/quest_snapshot.md
```

This should be a Markdown Quest Snapshot.

Reason:

- low risk
- human-readable
- Codex-readable
- easy to diff
- easy to archive
- works without PDF / PNG / screenshot automation
- preserves Gate, Next Action, Do-Not-Do Boundary, Recheck Condition, and Completion Line
- can later reference visual SVGs
- can become source for future PDF / PNG export

## Explicit HOLD

The cutline keeps these scopes on HOLD:

- PDF generation
- screenshot automation
- PNG conversion
- Quest Snapshot runtime image export
- snapshot comparison runtime
- automatic drift scoring
- full Quest Map implementation
- market research / external APIs
- HTML/CSS renderer
- external posting

## Source Of Truth

For the first runtime, the source of truth should be manually or AI-assisted Quest Snapshot fields, not automatic scoring.

The first runtime should not infer:

- recommended action
- market phase
- evidence quality
- risk level
- paid repeat signal
- relationship risk
- lifecycle classification

It should only assemble already-provided or manually filled fields into a stable Markdown artifact.

## Minimum Fields For `outputs/quest_snapshot.md`

Required:

- Snapshot ID
- As-of date
- Project / Quest name
- Current Gate
- Recommended Action
- One-line Judgment
- Quest Position Map reference
- Industry Slope Timeline reference
- Reference Chart Used
- Reference Chart Quality
- Lifecycle Classification
- Concern Level
- Key Reason Summary
- Codex Interpretation Note summary
- Missing Evidence
- One Next Action
- Do-Not-Do Boundary
- Recheck Condition
- Seat Owner
- Completion Line

Optional:

- Regret Guard Note
- Survival / Relationship Risk summary
- Source Notes
- Visual artifact links
- Prior Snapshot ID
- Trajectory note

## Visual References

The Markdown snapshot may reference existing SVG prototype paths:

- `outputs/quest_position_map_ja.svg`
- `outputs/industry_slope_timeline_ja.svg`
- `outputs/snapshot_trajectory_drift_delta_ja.svg`

The first runtime should not generate new images.

## Codex Handoff Requirement

The snapshot must include a visible section:

```text
Next Codex Owns
```

This section should state:

- what Codex should do next
- what Codex must not broaden
- current Gate
- recheck condition
- whether implementation is allowed

## Human Seat Requirement

The snapshot must state:

- Seat Owner
- whether the decision is human-owned
- whether AI/Codex is only preserving / assembling the As-of artifact

## Staleness

The snapshot should be marked stale when:

- recheck condition has passed
- Gate has changed
- evidence has changed
- risk has changed
- source-backed evidence has been updated
- human Seat has changed
- next action has been completed or abandoned

Do not implement staleness detection yet. This document only defines the rule.

## Future Path After Markdown Runtime

If `outputs/quest_snapshot.md` works, future phases may consider:

- Quest Snapshot template
- multiple snapshot archive folder
- PDF export
- PNG screenshot export
- Snapshot Trajectory comparison
- HTML/CSS renderer

All remain HOLD until the Markdown artifact proves useful.

## Non-Goals

The first runtime is not:

- a scoring engine
- a prediction system
- a market research system
- an automatic recommendation engine
- a project management platform
- a launch permission system
- a replacement for the human Seat

## Implementation Cutline

The future implementation should be allowed to:

- read a filled template or sample data
- write `outputs/quest_snapshot.md`
- preserve links to visual artifacts
- format sections consistently
- validate required fields are present

The future implementation should not:

- decide the action
- infer the Gate
- infer market size
- perform web research
- update visuals automatically
- create PDF / PNG
- compare snapshots
- post externally

## Recommended Next Phase

If this cutline passes, the next phase should be one of:

```text
Phase 10.39:
Quest Snapshot Markdown Template
```

Still not runtime if desired. Create a template or sample first.

Alternative:

```text
Phase 10.39:
V13 LoopKit Quest Snapshot Dogfood
```

Use the template manually on V13 LoopKit before runtime.

## Completion Line

Minimal Runtime Cutline v0.1 defines Markdown Quest Snapshot output as the first safe runtime path, while keeping image export, PDF generation, snapshot comparison, drift scoring, market research, and full Quest Map implementation on HOLD.
