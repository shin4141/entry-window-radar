# Session Snapshot Command Placement v0.1

## Purpose

This specification explains why the first future save/checkpoint command should be a V12-style Session Snapshot command rather than a full Quest Snapshot generator.

The immediate need is restartability. The first command should preserve what happened in the current session, what remains unfinished, and what the next AI needs in order to resume without false completion.

It should not pretend to understand the full strategic position of a project, infer missing evidence, score viability, or generate a complete Quest Snapshot automatically.

## Layer Placement

### A. V12 Session Snapshot

Purpose:

- make the current work restartable
- preserve partial completion
- prevent false completion
- reduce re-explanation burden

Question it answers:

```text
What happened in this session, what remains unfinished, and how can the next AI restart?
```

Output candidate:

```text
outputs/session_snapshot.md
```

Status:

```text
Future command candidate / spec only.
```

### B. V13 Loop Gate

Purpose:

- decide whether the next loop should run
- protect Carrier, Seat, Returnability, and Do-Not-Do Boundary
- prevent uncontrolled next-loop expansion

Question it answers:

```text
Should the next loop GO, HOLD, CAP, or BLOCK?
```

Status:

```text
Governance layer, not the first command implementation.
```

### C. Entry Quest Snapshot

Purpose:

- preserve the project or quest's current position
- record Current Gate, Recommended Action, UNKNOWN fields, Recheck Condition, and Completion Line
- serve as a strategic re-entry capsule

Question it answers:

```text
Where is this project/quest now, and what should the next AI understand before continuing?
```

Status:

```text
Prompt-first workflow exists.
Auto-generation remains HOLD.
```

## Recommended First Command

Name candidates:

```text
tools/save_session_snapshot.py
tools/checkpoint_session.py
```

Recommended initial name:

```text
tools/save_session_snapshot.py
```

Reason:

The command should be understood as a V12 session checkpoint, not as a complete Quest Snapshot generator.

## Future Command Behavior

Spec only. No command is implemented in this phase.

A future `save_session_snapshot` command may:

- read current git status
- read latest commit hash
- read `STATUS.md` for current Gate
- read `AGENTS.md` for boundaries
- accept a user note via `--note`
- write a restartable session checkpoint to `outputs/session_snapshot.md`

It must include:

- As-of timestamp
- Current Gate
- What changed
- What remains unfinished
- Next Action
- Do-Not-Do Boundary
- Recheck Condition
- Completion Line
- UNKNOWN / Missing Closure
- Git status
- Latest commit
- Runtime / automation state
- External posting state

## Required Warning

Generated session snapshots must include this exact line:

```text
This is a restartable checkpoint, not a completion claim.
```

Japanese equivalent:

```text
これは再開可能な途中保存であり、完了宣言ではない。
```

## Explicit Non-Goals

The first command must NOT:

- generate a full Quest Snapshot automatically
- call an AI API
- perform market research
- score a project
- classify startup viability
- generate PNG/PDF/screenshot outputs
- compare snapshots
- modify target repos
- commit automatically
- authorize external posting
- upgrade any Gate

## Placement Rationale

Starting with a V12 Session Snapshot command is safer than immediate Quest Snapshot auto-generation because it has:

- smaller scope
- less prompt-injection risk
- less secret-mixing risk
- lower chance of hallucinated UNKNOWN filling
- easier validation
- direct usefulness at the end of each work session
- clear alignment with V12 Completion Integrity

The command records current work state. It does not judge the project's strategic position.

## Relationship To Quest Snapshot

Session Snapshot and Quest Snapshot are complementary.

Session Snapshot:

- session/day/work-unit level
- restartability
- what changed today
- next immediate action

Quest Snapshot:

- project/quest level
- strategic current position
- Gate and recommended action
- broader UNKNOWN and evidence state

## Relationship To Entry Window Radar

Entry Window Radar may eventually include both:

- prompt-first Quest Snapshot workflow
- local V12-style session checkpoint command

But the first command should not imply that full Quest Snapshot runtime exists.

## Completion Line

Entry Window Radar now distinguishes V12 Session Snapshot, V13 Loop Gate, and Entry Quest Snapshot, and records that the first future command should be a V12-style restart checkpoint rather than full Quest Snapshot auto-generation.
