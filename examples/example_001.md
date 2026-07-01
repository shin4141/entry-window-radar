# Worked Example 001: Local Newsletter Triage

This example shows the smallest useful Entry Window Radar flow:

1. write an idea
2. add current evidence
3. add operator edge context
4. run the local CLI
5. read the as-of report and decision card

It is local-only. The example is not market research, not a launch plan, and not a prediction of future success.

## Sample Idea

Copy this block into `inputs/idea.md` if you want to try the example.

````markdown
# Idea Input Template

## Artifact

```text
Name: Local Newsletter Triage
Type: idea
URL or local path:
As-of date: 2026-07-01
```

## One-Sentence Description

```text
A small tool that helps solo local-newsletter writers sort reader replies into leads, corrections, story tips, and follow-ups.
```

## Target User

```text
Solo newsletter writers covering a local community or niche industry.
```

## Pain Or Demand

```text
Writers receive useful replies, but the replies are scattered across email threads and are easy to lose.
The job is recurring, manual, and painful when the writer is also reporting, editing, and selling sponsorships.
```

## Current Artifact Evidence

```text
README:
Prototype: rough local script that tags pasted replies into four buckets.
Demo:
Examples: five anonymized reply examples from one newsletter workflow.
Usage evidence:
Other:
```

## Expected Entry Label

```text
NICHE WEDGE
```

## Constraints

```text
Time: one weekend for a proof pass.
Budget: no paid services.
Deadline:
Available distribution: direct access to two newsletter operators.
Known blockers: no broad market evidence yet.
```
````

## Sample Evidence

Copy this block into `inputs/evidence.md`.

````markdown
# Evidence Input Template

## Market Evidence

```text
- Two newsletter operators described reply triage as a weekly cleanup task.
- One operator already keeps a manual spreadsheet of story tips and sponsor leads.
```

## Competition Evidence

```text
- Generic inbox tools and CRM tools exist, but no named alternative has been compared for this exact workflow.
```

## Operator Edge Evidence

```text
- The operator has direct access to two newsletter workflows.
- The operator can test with anonymized replies without building a full SaaS product.
```

## Missing Evidence

```text
- More examples from newsletters outside the initial two operators.
- A named comparison against the closest existing inbox or CRM workflow.
```

## Notes On Evidence Quality

```text
Primary evidence: direct operator conversations and anonymized workflow examples.
Calibration material:
Speculation: broader market size is unknown.
```
````

## Sample Operator Context

Copy this block into `inputs/operator.md`.

````markdown
# Operator Input Template

## Operator Context

```text
Name or alias: example operator
Relevant domain: local newsletters and small editorial workflows.
Available time: one weekend.
Deadline:
Budget: no paid services.
Current artifact: rough local script.
Distribution paths: two direct operator relationships.
```

## What The Operator Knows Or Notices

```text
Newsletter replies often contain multiple jobs at once: correction, lead, story tip, and sponsor signal.
Small operators care more about not losing useful replies than about advanced automation.
```

## Existing Assets

```text
- Five anonymized reply examples.
- A simple local tagging script.
- Direct feedback access to two newsletter operators.
```

## Proof Capacity

```text
The operator can run a before/after test on one week of replies and ask whether the buckets saved cleanup time.
```

## Weak Spots

```text
Artifact: only a rough script.
Distribution: two direct relationships, not a repeatable channel.
Credibility:
Speed:
Market access: narrow.
Other:
```
````

## Run The CLI

From the repo root:

```bash
python3 -B tools/entry_window_radar.py
```

The CLI reads:

```text
inputs/idea.md
inputs/evidence.md
inputs/operator.md
```

It writes:

```text
outputs/report.md
outputs/decision.md
```

## Expected Decision Shape

The exact wording may change as the CLI evolves, but the decision should stay small:

```text
Entry Label: NICHE WEDGE
Maximum Bottleneck: Competition evidence
Next Action: Define one narrow user/workflow wedge and gather one proof point that the operator can serve it better than a generic alternative.
Confidence: Medium
Missing Evidence:
- More examples from newsletters outside the initial two operators.
- A named comparison against the closest existing inbox or CRM workflow.
```

The decision card should not include the full three-line rationale. That belongs in `outputs/report.md`.

## Why This Label Makes Sense

`NICHE WEDGE` fits because the sample has a narrow workflow, direct operator access, and a cheap proof path. The broad market is not proven, and the competition picture is still thin, so `FAST ENTRY` would be too strong.

The maximum bottleneck is exactly one: `Competition evidence`.

The next action is exactly one: define the narrow workflow wedge and gather one proof point for it.

The diagnosis remains an as-of view of the current evidence. It does not judge the operator and does not claim the idea will succeed.
