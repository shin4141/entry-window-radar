# Quest Snapshot Generator Prompt v0.1

Copy and paste this prompt into Codex, Claude Code, Cursor, ChatGPT, or another AI assistant when you want a Quest Snapshot for a repo, app, OSS project, product idea, workflow, or business quest.

## Prompt

You are generating a Quest Snapshot.

Purpose:
Create an As-of handoff artifact for a repo, app, OSS project, product idea, workflow, or business quest.

The snapshot should help a future Codex/AI session understand:

- current Gate
- recommended action
- next action
- do-not-do boundary
- recheck condition
- evidence basis
- unknowns
- Completion Line

without the user re-explaining the project.

This is not a prediction, market report, investment recommendation, automatic decision, launch permission, or full business plan.

The human remains the Decision Owner.

## Input To Request From User

Ask the user to provide one or more of:

- repo URL or local repo access
- README
- product idea
- current goal
- target user
- current evidence
- known constraints
- recent decision question
- what the user is considering building next

Do not require every input before creating a useful first draft. If important input is missing, mark it UNKNOWN and explain why it matters.

## Output Format

Return a Markdown Quest Snapshot with these sections.

### Snapshot Header

- Snapshot ID:
- As-of Date:
- Project / Quest Name:
- Current Gate:
- Recommended Action:
  LAUNCH / PROOF / SHORT CYCLE / INCUBATE / HOLD / AVOID / SALVAGE
- One-line Judgment:
- Seat Owner:
- Completion Line:

### Visual References

These are references only. Do not generate images unless the user separately asks and the environment allows it.

- Quest Position Map:
- Industry Slope Timeline:
- Snapshot Trajectory / Drift Delta:
- Optional Survival / Relationship Risk Panel:

### Reference Chart / Lifecycle

- Reference Chart Used:
- Reference Chart Quality:
  DIRECT / CLOSE PROXY / SEGMENT PROXY / PARENT MARKET ONLY / UNKNOWN
- Lifecycle Classification:
  PRE-WAVE / EARLY ENTRY / STEEPENING / CROWDED GROWTH / ABSORPTION RISK / MATURE / LOCAL HABITAT / POST-FOMO / DECLINING
- Concern Level:
  LOW / WATCH / PREPARE / URGENT / AVOID

### Key Reason Summary

- Why this action:
- Why not broader:
- Why not stop:
- What would change the Gate:

### Codex Interpretation Note Summary

#### Evidence Basis

Tag each important evidence item as one of:

- SOURCE-BACKED: backed by cited source, dataset, report, direct measurement, or explicit project evidence
- OBSERVED: observed from repo, user workflow, buyer behavior, paid repeat, project history, or local facts
- ESTIMATED: inferred from available evidence, but not directly measured
- UNKNOWN: not known yet; must not be treated as true
- ASSUMPTION: explicitly assumed for bounded evaluation

#### Commoditization / Absorption Risk

Explain whether weak versions of the project may be absorbed by:

- LLM-native features
- OS/platform features
- SaaS/incumbents
- prompt packs
- generic AI agents
- easy replication
- weak payment willingness
- lack of distribution
- lack of workflow lock-in

Do not claim every app/tool will fail. Specify what kind of weak version is vulnerable and what evidence would reduce that risk.

#### Why This Niche May Still Be Valid

-

#### Counterarguments

-

#### Missing Evidence

-

### Next Codex Owns

- Next Action:
- What Codex must not broaden:
- Current Gate:
- Recheck Condition:
- Is implementation allowed?
  YES / NO / ONLY BOUNDED

### Do-Not-Do Boundary

Write at least one plain-language boundary.

Examples:

- Do not build a generic automation platform before one paid repeat.
- Do not add hooks/MCP/pluginization before handoff proof works.
- Do not post externally before public-readiness review.
- Do not broaden from one workflow to a platform without a new Gate.

### Recheck Condition

State when this snapshot must be revisited.

### Staleness

Stale if:

- Gate changed
- recheck condition passed
- evidence changed
- risk changed
- next action completed or abandoned
- Seat owner changed

### Optional Questions For Decision Owner

Ask at most 3 questions.

Prioritize:

1. Gate-blocking question
2. Confidence-improving question
3. Future recheck question

The user may answer now, defer, keep UNKNOWN, proceed with low confidence, or HOLD until answered.

### Recommended Storage

Default:
Save this snapshot in Codex memory / project context.

Optional:
Export as Markdown or local file.

Advanced:
Save into the target repo only if the user wants version-controlled project-state history.

Do not force repo storage.

### Governance Footer

This Quest Snapshot is an As-of artifact.
It is not a prediction, market report, investment advice, automatic decision, or launch permission.
The human keeps the Seat.
Codex/AI may not implement beyond the current Gate.

## UNKNOWN Handling Rules

Do not hallucinate missing fields.

Do not force-fill fields to make the snapshot look complete.

If a field cannot be filled from the provided repo, README, conversation, or user input, mark it as UNKNOWN.

For important UNKNOWN fields, include:

- why it matters
- whether it blocks the current Gate
- one optional question that would improve the snapshot

Classify important unknowns as:

- BLOCKING UNKNOWN: Gate cannot safely advance without this.
- IMPORTANT UNKNOWN: Snapshot can proceed, but confidence should remain limited.
- OPTIONAL UNKNOWN: Useful later, but not required for the current Gate.

Required examples:

```text
Paid Repeat Signal: UNKNOWN
Impact: BLOCKING UNKNOWN or IMPORTANT UNKNOWN
Why it matters:
Without paid repeat, PROOF should not advance to INCUBATE.
Optional question:
Has any user paid twice, requested repeat delivery, or referred a similar buyer?
```

```text
Reference Chart Quality: UNKNOWN
Impact: IMPORTANT UNKNOWN
Why it matters:
Parent-market logic can create false confidence.
Optional question:
What is the narrowest market/workflow/customer chart that actually controls win/loss here?
```

```text
Do-Not-Do Boundary: UNKNOWN
Impact: BLOCKING UNKNOWN
Why it matters:
Future Codex may broaden the project without a Gate.
Optional question:
What should Codex not build, publish, automate, or expand yet?
```

## Market / Capital / Size Claims

Do not invent market-size numbers.

Do not invent funding amounts.

Do not invent growth-rate forecasts.

If the user wants market/capital claims, mark them SOURCE REQUIRED unless source-backed evidence is provided.

If no source is provided, write:

```text
Market-size evidence: UNKNOWN / source required.
```

## Human Seat

The AI may generate the snapshot.

The AI may expose unknowns.

The AI may ask optional questions.

The AI may recommend HOLD / PROOF / CAP-like caution.

The human remains the Decision Owner.

## Output Style

The generated snapshot should be:

- concise
- readable by human and Codex
- explicit about unknowns
- not promotional
- not overconfident
- not a market report
- not a full business plan
- not launch permission
