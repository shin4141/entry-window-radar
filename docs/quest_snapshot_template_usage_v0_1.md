# Quest Snapshot Template Usage v0.1

## Purpose

Quest Snapshot Template Usage v0.1 explains how `templates/quest_snapshot_template_v0_1.md` should be used before any runtime generation exists.

This is a template, not runtime.

## What The Template Does

The template provides a reusable Markdown shape for a Quest Snapshot As-of artifact.

It is meant to preserve:

- current Gate
- recommended action
- one-line judgment
- visual references
- reference chart / lifecycle context
- Codex Interpretation Note summary
- missing evidence
- one next action
- do-not-do boundary
- recheck condition
- Seat owner
- Completion Line

## What The Template Does Not Do

The template does not:

- generate `outputs/quest_snapshot.md`
- change CLI behavior
- infer Gate
- infer recommended action
- infer lifecycle classification
- infer evidence quality
- infer risk level
- perform market research
- call external APIs
- generate PDF / PNG / screenshot output
- compare snapshots
- calculate drift
- authorize external posting

## How Future Codex Can Use It

Future Codex can fill the template manually when the user gives a target, evidence, Gate, next action, and boundary.

Codex should:

- keep the snapshot As-of
- preserve the human Seat
- include only one next action
- keep the do-not-do boundary visible
- state whether implementation is allowed
- mark unknown evidence as unknown
- avoid turning visual prototypes into scoring

Codex should not:

- create runtime output unless explicitly gated
- infer missing market data
- upgrade Gate automatically
- implement beyond the current Gate
- treat the template as launch permission

## Bridge To Future Runtime

This template is the bridge between Quest Map visuals and a future Markdown runtime.

The future runtime cutline is:

```text
outputs/quest_snapshot.md
```

That output remains HOLD until separately gated.

If the template proves useful manually, a later phase may implement a small local runtime that reads a filled template or sample data and writes `outputs/quest_snapshot.md` without scoring or inference.

## Dogfood Direction

A later phase may use this template manually on V13 LoopKit before runtime implementation.

That dogfood should test whether the snapshot format helps future Codex/AI understand:

- what it now owns
- the current Gate
- the one next action
- what must not be broadened
- when to recheck
- who owns the Seat

## Completion Line

Quest Snapshot Template Usage v0.1 explains how the Quest Snapshot Markdown template can be filled manually before runtime generation, preserving the bridge between Quest Map visuals and future Markdown snapshots without adding implementation scope.
