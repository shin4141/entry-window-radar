# Quest Snapshot / TimeTube Archive v0.1

## Purpose

Quest Snapshot / TimeTube Archive preserves Quest Map outputs as As-of artifacts.

It allows:

- the user to avoid re-explaining current position
- Codex/AI to understand what it now owns
- project drift to be detected
- future regret to review the As-of record
- multiple snapshots to form a project trajectory over time

Core principle:

```text
Handoff is not complete until the receiving AI knows what it now owns.
```

Quest Snapshot operationalizes this principle by saving:

- current Gate
- recommended quest action
- one-line judgment
- next action
- do-not-do boundary
- recheck condition
- key reasons
- Seat / Regret Guard note when relevant

## Relationship To V8-V13

### V8 TimeTube

Multiple snapshots create a project trajectory over time.

### V9 As-of

Each snapshot preserves what was known at that decision point.

### V11 Reconnectable Forgetting

Even if context is compressed or forgotten, the snapshot allows reconnection.

### V12 Completion Integrity

The snapshot helps the next AI/person resume without false completion.

### V13 Loop Governance

The snapshot carries Gate state, Seat, next action, and stop conditions into the next loop.

## Primary Use Case

The primary use case is post-release apps, OSS projects, and repos being expanded with Codex or AI coding agents.

After release, projects drift through:

- feature creep
- stale context
- repeated explanation
- unclear next gates
- Codex continuing as a task executor without knowing the prior decision state

Quest Snapshot preserves the project's current Gate, next action, do-not-do boundary, and As-of reasoning so future Codex/AI sessions can continue without turning every request into uncontrolled expansion.

## What A Quest Snapshot Is

A Quest Snapshot is a saved As-of artifact generated after a Quest Map evaluation.

It is not:

- a prediction
- a market report
- investment advice
- an automatic decision
- a replacement for human Seat
- a complete project memory
- a new scoring system

## Minimum Saved Content

Required fields:

- Snapshot ID
- Date / As-of time
- Project / Quest name
- Current Gate
- Recommended Action: LAUNCH / PROOF / SHORT CYCLE / INCUBATE / HOLD / AVOID / SALVAGE
- One-line Judgment
- Reference Chart Used
- Reference Chart Quality
- Key Reason Summary
- One Next Action
- Do-Not-Do Boundary
- Recheck Condition
- Seat Owner
- Completion Line

Optional fields:

- Quest Position Map image
- Industry Slope Timeline image
- Survival / Relationship Risk Panel image
- detailed Quest Map Card
- Regret Guard Note
- source notes
- Codex handoff note

## Storage Formats

Allowed future formats:

- Markdown snapshot
- PDF export
- PNG / screenshot
- Codex project file
- local project archive folder

This phase does not implement any of those formats.

It defines intended use only.

## Suggested Future File Layout

Future implementation may use:

```text
snapshots/
  2026-07-xx__project-name__quest-snapshot.md
  2026-07-xx__project-name__quest-map.png
  2026-07-xx__project-name__quest-snapshot.pdf
```

or:

```text
outputs/
  quest_snapshot.md
  quest_snapshot.pdf
  quest_snapshot.png
```

This phase must not create runtime output files.

It only specifies future paths.

## Snapshot Lifecycle

### Create

Create a snapshot after Quest Map evaluation.

### Save

Save it as Markdown, PDF, screenshot, or project file when a future implementation is explicitly gated.

### Reopen

Future AI/Codex reads the snapshot before continuing.

### Compare

Compare the latest snapshot with earlier snapshots.

### Detect Drift

Identify changes in Gate, action, reference chart, risk, next action, or do-not-do boundary.

### Archive

Preserve completed or superseded snapshots as historical As-of records.

## Drift Prevention

Snapshot drift prevention comes from preserving:

- what the project was trying to do
- what it was not supposed to do
- why the action was chosen
- when to recheck
- what changed since the last snapshot
- who owns the Seat

This is not automatic drift scoring.

It is a saved As-of comparison anchor.

## Codex Role

Codex should be able to:

- read the latest Quest Snapshot
- know the current Gate
- know what not to broaden
- know the next action
- know what has already been decided
- avoid asking the user to restate the project state
- avoid continuing from stale assumptions

Codex should not:

- override the human Seat
- turn old snapshots into permanent truth
- ignore recheck conditions
- treat snapshots as predictions
- implement beyond current Gate

## User Value

Many users will not use GitHub history.

They still need a durable decision artifact.

Quest Snapshot lets users:

- save their current project position
- return later without re-explaining
- show another AI/person what the project currently owns
- reduce decision drift
- compare project trajectory over time
- remember why a difficult decision was reasonable As-of

## TimeTube Trajectory

Multiple snapshots form a TimeTube.

Example:

```text
Snapshot 1:
PROOF - output equivalence not proven

Snapshot 2:
PROOF - paid repeat appears

Snapshot 3:
INCUBATE - repeat habitat visible

Snapshot 4:
HOLD - survival exposure increased
```

This creates a project trajectory, not just isolated advice.

## Governance

- Do not create a snapshot without an As-of date.
- Do not omit Current Gate.
- Do not omit Do-Not-Do Boundary.
- Do not omit Recheck Condition.
- Do not let old snapshots override current reality.
- Do not treat snapshots as predictions.
- Do not use snapshots to remove the human Seat.
- If a snapshot is stale, mark it stale rather than silently using it.
- If the project resumes from a snapshot, the receiving AI must state what it now owns.
- Quest Snapshot must not authorize implementation beyond the current Gate.

## Completion Line

Quest Snapshot / TimeTube Archive v0.1 defines how Quest Map outputs should be saved as As-of artifacts so future users, Codex, or AI sessions can resume from the project's prior position without relying on memory, GitHub history, or repeated explanation.
