# Validate Prompt

Use this prompt to check whether an Entry Window Radar output stays inside the scaffold-approved boundary.

```text
Review the Entry Window Radar output below.

Check whether it:

1. Produces exactly one entry label from:
   FAST ENTRY, NICHE WEDGE, WAIT, SHORT CYCLE, AVOID

2. Keeps output roles separated:

   report.md is the detailed as-of diagnosis and includes:
   Entry Label
   Market Line
   Competition Line
   Operator Edge Line
   Rationale
   Missing Evidence
   Maximum Bottleneck
   Next Action
   Confidence
   Risk
   Recheck Condition

   decision.md is the short decision card and includes only:
   Entry Label
   Maximum Bottleneck
   Next Action
   Confidence
   Missing Evidence

3. Keeps Operator Edge as a first-class line.

4. Uses as-of language instead of future certainty.

5. Avoids judging the operator or telling the operator "you should build this."

6. Avoids Delivery Scope Radar, V14 Resource Justice deep scoring, score history, drift tracking, external posting, and automated web research.

7. Keeps maximum bottleneck and next action bounded to exactly one each.

Return:

- PASS or FAIL
- Boundary issues
- Missing required fields
- Suggested minimal correction

Output to validate:

```
