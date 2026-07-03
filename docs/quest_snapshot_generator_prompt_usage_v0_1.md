# Quest Snapshot Generator Prompt Usage v0.1

## Purpose

Quest Snapshot Generator Prompt Usage v0.1 explains how normal users should use `prompts/quest_snapshot_generator_prompt_v0_1.md`.

The prompt is for users who want an AI/Codex session to draft a Quest Snapshot without forking Entry Window Radar or running a local runtime.

## Who This Is For

Use this prompt when you want to create a Quest Snapshot for:

- a repo
- a README
- an app
- an OSS project
- a product idea
- a workflow
- a business quest

The user does not need to fork Entry Window Radar.

The user does not need to commit anything to their own repo.

## How To Use

1. Open Codex, Claude Code, Cursor, ChatGPT, or another AI assistant.
2. Paste `prompts/quest_snapshot_generator_prompt_v0_1.md`.
3. Provide the repo, README, idea, current goal, target user, evidence, constraints, or decision question.
4. Let the AI produce a Quest Snapshot draft.
5. Review the draft as the Decision Owner.
6. Save it in Codex memory / project context by default.
7. Export Markdown only if portability is useful.

## Default Storage

Default:
Save the snapshot in Codex memory / project context.

Optional:
Export as Markdown or local file.

Advanced:
Save into the target repo only if the user wants version-controlled project-state history.

Do not force repo storage.

## UNKNOWN Fields Are Useful

UNKNOWN fields are not failure.

They are the point.

The prompt should preserve what is unknown so the human Decision Owner can see:

- what is known
- what is not known
- why the unknown matters
- whether it blocks the current Gate
- what question would improve the next decision

The AI should not hide uncertainty by filling every field.

## Optional Questions

The prompt limits optional questions to at most 3.

They should help the Decision Owner notice missing definitions without creating question spam.

The user may:

- answer now
- defer
- keep UNKNOWN
- proceed with low confidence
- HOLD until answered

## Relationship To Runtime

This prompt does not implement runtime.

It does not generate `outputs/quest_snapshot.md`.

It does not change CLI behavior.

It does not create PDF, PNG, screenshot, snapshot comparison, or drift scoring output.

It does not perform market research or call external APIs.

It does not authorize external posting.

## Relationship To Storage Modes

Storage Modes answer:

```text
Where does the snapshot live?
```

Generator Prompt answers:

```text
How does an AI create the snapshot?
```

Use `docs/quest_snapshot_storage_modes_user_flow_v0_1.md` for storage guidance.

## Human Seat

The AI may draft the snapshot, expose unknowns, and ask optional questions.

The human remains the Decision Owner.

Codex/AI may not implement beyond the current Gate.

## Completion Line

Quest Snapshot Generator Prompt Usage v0.1 explains how normal users can paste the generator prompt into an AI/Codex session, provide repo/README/idea context, and get a Quest Snapshot draft with UNKNOWN fields preserved before any runtime implementation exists.
