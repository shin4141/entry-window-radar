# Local Markdown Task Tracker — Quest Snapshot Example v0.1

## Sample Project Brief

Local Markdown Task Tracker is a fictional small solo-developer repo idea for managing tasks, next actions, and work notes in local Markdown files.
It is not a full app yet.
It currently has only a README concept, a sample `tasks.md` idea, and a possible CLI later.
The owner is considering cloud sync, notifications, AI categorization, calendar integration, mobile app support, and team features, but wants to avoid broadening before proof.

## Why This Example Exists

This example demonstrates Entry Window Radar on an ordinary small project.
It is not Decision-OS, V13 LoopKit, or Entry Window Radar evaluating itself.
The goal is to show a public-safe Quest Snapshot flow that a first-time user can understand without Decision-OS context.

## Quest Snapshot Draft

- Snapshot ID: local-markdown-task-tracker-2026-07-03-v0-1
- As-of Date: 2026-07-03 JST
- Project / Quest Name: Local Markdown Task Tracker
- Current Gate: PROOF / CAP
- Recommended Action: PROOF
- Seat Owner: Human / project owner

### One-line Judgment

As of the available evidence, this looks suitable for a bounded proof: test whether one local Markdown task file can preserve restart context before adding app-like features.

### One Next Action

Test whether one local Markdown task file can preserve next action, status, and restart context across one work session.

### Do-Not-Do Boundary

Do not add cloud sync, notifications, AI categorization, calendar integration, mobile app, team features, external posting, or paid product framing before proof.

### Recheck Condition

Recheck after one or two real work sessions using only local Markdown files and a session checkpoint.

### Completion Line

A future Codex/AI or human can understand the current task state, next action, and boundaries from the Markdown file and/or session checkpoint without re-explaining the project.

## UNKNOWN Fields

| Field | Impact | Why It Matters | Optional Question |
| --- | --- | --- | --- |
| Independent user proof | IMPORTANT UNKNOWN | The idea may solve only the owner's personal workflow until another user can understand and use the file pattern. | What would count as one outside-user proof? |
| Repeat usage | BLOCKING UNKNOWN | A task tracker has value only if it survives repeated sessions, not one enthusiastic setup pass. | What proof window is enough: one session, seven days, or another person trying it? |
| Existing todo app differentiation | IMPORTANT UNKNOWN | The project must show why local Markdown restart context is meaningfully different from common todo apps, notes apps, or issue trackers. | Which existing tool is the closest substitute? |
| Paid value | OPTIONAL UNKNOWN | Paid value is not required for a local proof, but it matters before product framing or launch claims. | Is this intended as a product, utility, or personal workflow pattern? |
| Whether automation is needed | IMPORTANT UNKNOWN | The proof may show that a simple Markdown convention is enough, which would reduce the need for CLI or AI features. | Which feature is most tempting to add too early? |

## Optional Decision Owner Questions

1. What counts as proof: one user session, seven days of use, or another person trying it?
2. What must remain local-only before proof?
3. Which feature is most tempting to add too early?

## Recommended Storage

Default storage:
Codex memory / project context.

Optional storage:
A local Markdown note in the target project if the owner wants portable handoff state.

Advanced storage:
Version-controlled target repo storage only if the project owner wants durable project-state history.

## save_session_snapshot Checkpoint

The user can close a work session with:

```bash
python3 -B tools/save_session_snapshot.py --note "Tested local Markdown task tracker example"
```

This creates `outputs/session_snapshot.md` as a restartable checkpoint.
It is not a completion claim.
It does not generate Quest Snapshot automatically.

## Boundary Note

This example does not authorize:

- full Quest Snapshot auto-generation
- `outputs/quest_snapshot.md`
- AI/API calls
- PNG/PDF export
- snapshot comparison
- scoring/drift scoring
- external posting
