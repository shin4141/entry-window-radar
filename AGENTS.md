# AGENTS.md

## Project Boundary

Entry Window Radar is a scaffold-stage OSS candidate for evaluating the current entry window of a GitHub repo, README, idea, or small project.

Keep the MVP bounded to:

- repo / README / idea input
- one Entry Window Chart
- Market Line
- Competition Line
- Operator Edge Line
- five entry labels: FAST ENTRY, NICHE WEDGE, WAIT, SHORT CYCLE, AVOID
- one biggest bottleneck
- one bounded next action
- one recheck condition

## Current Gate

```text
Launch Capsule: PASS
New repo scaffold: GO
Implementation: HOLD
External posting: HOLD
Delivery Scope Radar: BLOCK
V14 deep scoring: BLOCK
```

## Allowed At Scaffold Stage

- edit README and template wording
- refine schema placeholders without adding runtime logic
- add examples that remain placeholders or manually worked examples
- improve prompts for validation and Operator Edge extraction
- keep status / handoff notes current

## Not Allowed At Scaffold Stage

- do not implement full CLI logic
- do not add external API integrations
- do not add Grok, X, or automated web research
- do not implement Delivery Scope Radar
- do not implement V14 Resource Justice deep scoring
- do not make external posts
- do not turn the repo into a generic startup advisor
- do not present the tool as a future prediction engine

## Output Language

Use entry-window language, not certainty language.

Prefer:

```text
As of the available evidence, this looks like NICHE WEDGE.
```

Avoid:

```text
You should build this.
This will win.
```

## Completion Line For This Scaffold

The scaffold is complete when the repo contains the initial file structure, is committed, has a clean working tree, and contains no implementation beyond capsule-approved templates and placeholders.
