# Quest Snapshot Storage Modes / User Flow v0.1

## Purpose

Quest Snapshot Storage Modes / User Flow v0.1 defines where Quest Snapshots should live and how users should use them across Codex/AI sessions.

It exists to reduce user burden before any runtime implementation. Quest Snapshot should help future AI/Codex sessions resume, not force users into repo commits, fork setup, or public/private disclosure decisions before they trust the tool.

## Core Principle

Quest Snapshot is not primarily a repo artifact.

It is a re-entry capsule for the next AI/Codex session.

Default storage should minimize user burden.

## Storage Modes

### A. Default: Codex Memory / Project Context

Use when:

- user is working with Codex / AI coding agent
- user wants low-friction continuation
- user does not want to modify their repo
- user is still testing the idea

Description:
The Quest Snapshot is stored in the AI/Codex project context or working memory so the next session can resume from:

- current Gate
- next action
- do-not-do boundary
- recheck condition
- Completion Line

Pros:

- lowest friction
- no repo pollution
- no public/private concern
- best for first-time users
- works before the user commits to adoption

Cons:

- may be harder to migrate across tools
- may be less durable than a file
- depends on Codex/project memory behavior

### B. Optional: Markdown / Local File

Use when:

- user wants portable re-entry
- user wants to move between AI tools
- user wants backup outside Codex memory
- user wants to archive a specific As-of state

Suggested paths:

- local project folder
- exported Markdown
- cloud drive
- project notes

Pros:

- portable
- human-readable
- easy to attach to another AI
- does not require repo commit

Cons:

- user must manage the file
- may become stale if not updated

### C. Advanced: Target Repo Storage

Use when:

- user is comfortable modifying the repo
- project is serious or long-running
- multiple contributors / agents need shared state
- the repo is private or intended to carry decision history

Suggested paths:

- `docs/quest_snapshots/`
- `.decision-os/quest_snapshots/`
- `.ai/quest_snapshots/`

Pros:

- durable
- version-controlled
- close to the work
- future Codex can read it directly from the repo

Cons:

- public/private risk
- repo hygiene burden
- user may not want project-state notes in source control
- too heavy for first-time use

### D. Entry Window Radar Repo Storage

Use when:

- creating dogfood examples
- preserving public-safe examples
- improving templates
- showing how the tool works

This is not intended as default storage for normal users.

## Recommended User Flow

Basic flow:

1. User gives Codex/AI access to their repo, README, idea, or project description.
2. User provides Quest Snapshot Generator Prompt.
3. Codex/AI creates a Quest Snapshot draft.
4. User reviews the snapshot.
5. Snapshot is saved first into Codex memory / project context.
6. User optionally exports Markdown or stores it in their repo.

## First-Time User Flow

Do not ask first-time users to fork Entry Window Radar.

Do not ask first-time users to commit to their own repo.

Do not ask first-time users to understand every Decision-OS layer.

First-time instruction should be:

```text
Paste this prompt into your AI/Codex session. It will create a Quest Snapshot for your project. Save it in your project context. Export it only if you want portability.
```

## Developer / OSS User Flow

For users with repos:

- Start with Codex memory / project context.
- If useful after one or two sessions, save Markdown to target repo.
- If the project becomes long-running, store snapshots in a dedicated folder.

## Fork-Based Advanced Flow

Entry Window Radar may be forked by advanced users who want:

- local templates
- examples
- visual prototypes
- future runtime outputs
- repeated internal dogfood

Fork is not required for basic use.

## Where The Snapshot Should Be Read From

Future Codex should read sources in this order:

1. Current Codex project memory / project context
2. Latest user-provided Quest Snapshot Markdown
3. Target repo snapshot folder, if present
4. Entry Window Radar template/example, only as reference

Codex should not assume Entry Window Radar repo contains the user's live project state.

## Staleness Rule

A Quest Snapshot in memory or file should be marked stale if:

- Gate changed
- next action completed or abandoned
- recheck condition passed
- do-not-do boundary changed
- evidence changed
- risk changed
- Seat owner changed
- user moved to a different target project

## Privacy / Public Safety Rule

Do not recommend repo storage by default when:

- the repo is public
- the snapshot contains private strategy
- the snapshot contains business plans
- the snapshot contains relationship/cashflow/survival notes
- the snapshot contains unreleased product strategy
- the user is not sure about disclosure

Default to Codex memory or local/private Markdown.

## Relationship To Quest Snapshot Generator Prompt

Storage Modes answer:

```text
Where does the snapshot live?
```

Generator Prompt answers:

```text
How does an AI create the snapshot?
```

Therefore:
Phase 10.41 defines storage and user flow.

A later phase should define Quest Snapshot Generator Prompt with UNKNOWN handling.

## Governance Rules

- Do not force repo storage.
- Do not require fork for first use.
- Do not treat Codex memory as permanent truth.
- Do not treat old snapshots as current without recheck.
- Do not hide UNKNOWN fields.
- Do not let Codex upgrade Gate from memory alone.
- Human keeps the Seat.
- If future Codex resumes from a snapshot, it must state what it now owns.

## Completion Line

Quest Snapshot Storage Modes / User Flow v0.1 defines Codex memory / project context as the default low-friction storage mode, Markdown/local file as optional portable storage, and target repo storage as an advanced route, so users can benefit from Quest Snapshot without being forced into repo commits or public/private disclosure decisions.
