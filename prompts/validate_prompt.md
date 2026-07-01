# Validate Prompt

Use this prompt to check whether an Entry Window Radar output stays inside the scaffold-approved boundary.

```text
Review the Entry Window Radar output below.

Check whether it:

1. Produces exactly one entry label from:
   FAST ENTRY, NICHE WEDGE, WAIT, SHORT CYCLE, AVOID

2. Includes all required fields:
   Entry Label
   Market Line
   Competition Line
   Operator Edge Line
   Missing Evidence
   Risk
   Recommended Next Action
   Recheck Condition

3. Uses as-of language instead of future certainty.

4. Avoids telling the operator "you should build this."

5. Avoids Delivery Scope Radar, V14 Resource Justice deep scoring, score history, drift tracking, external posting, and automated web research.

6. Keeps the next action bounded to one practical move.

Return:

- PASS or FAIL
- Boundary issues
- Missing required fields
- Suggested minimal correction

Output to validate:

```
