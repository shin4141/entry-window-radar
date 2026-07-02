# Quest Snapshot Visual Design System v0.1

## Purpose

Quest Snapshot Visual Design System defines shared visual rules for Quest Map / Quest Snapshot artifacts.

This design system should help future visual outputs become:

- readable at a glance
- screenshot-ready
- Japanese-friendly
- consistent across figures
- useful for future Codex/AI handoff
- not overloaded with analysis text

Core principle:

```text
Figure shows position. Card explains judgment. Snapshot preserves context.
```

## Artifact Roles

### Figure

The figure shows position, trajectory, or risk visually.

It should stay lightweight.

### Card

The card explains selected state, next action, and do-not-do boundary.

### Codex Interpretation Note

The Codex Interpretation Note carries evidence, assumptions, counterarguments, source status, and missing proof.

### Snapshot

The snapshot stores the figure, card, interpretation note, Gate, and Completion Line as an As-of artifact.

## Standard Artifact Types

### Quest Position Map

Expected role:

- show quest candidates by proof/reward distance and habitat/reward potential
- show enemy pressure and survival/relationship warning as visual cues
- keep labels short
- move selected-quest explanation into a card

### Industry Slope Timeline

Expected role:

- show where the selected reference niche sits in lifecycle time
- keep the curve light and clearly scoped to the niche
- show current As-of point
- use lifecycle classification and concern level in the card

### Snapshot Trajectory / Drift Delta

Expected role:

- compare multiple snapshots over time
- show what changed and what did not change
- make Gate, evidence, risk, boundary, and Codex handoff visible
- avoid showing every snapshot field at once

### Survival / Relationship Risk Panel, Future

Expected role:

- show survival pressure, relationship damage, dependency asymmetry, and Seat-owned regret risk
- use simple stacked bars or cards only when explicitly gated
- avoid turning relationship risk into a blame chart

### Quest Snapshot Cover/Card, Future

Expected role:

- provide a compact front page for saved snapshot artifacts
- include current Gate, recommended action, one next action, do-not-do boundary, and Completion Line
- keep enough context for future Codex/AI to resume without re-asking routine questions

## Canvas / Viewport Rules

Recommended default sizes:

- Square snapshot: `1200 x 1200` for compact share/save
- Wide timeline: `1600 x 1000` or `1600 x 1200` for multi-column trajectory

Rules:

- Do not clip the right edge.
- Keep the footer fully visible.
- Leave an outer margin.
- Avoid putting key text near the canvas edge.
- Keep visual hierarchy stable across artifacts.

## Layout Rules

Use consistent vertical structure:

### Standard Visual

Top:

- title
- subtitle
- current Gate / trajectory label if needed

Middle:

- main chart or timeline

Lower:

- selected card / interpretation card

Bottom:

- legend / governance footer

### Trajectory Charts

Top:

- trajectory judgment

Middle:

- snapshot columns

Lower:

- drift delta panel

Bottom:

- Codex handoff / governance footer

## Typography Rules

Japanese-first.

Use this font fallback:

```text
font-family="Inter, -apple-system, BlinkMacSystemFont, 'Hiragino Sans', 'Yu Gothic', 'Noto Sans CJK JP', sans-serif"
```

Rules:

- Avoid English/Japanese mixed lines unless needed.
- Use Japanese for primary labels.
- Use English labels only for fixed action/status tokens when useful: PROOF / HOLD / INCUBATE / CAP / BLOCK / COMPOUNDING.
- Keep in-chart labels short.
- Move long explanations to cards or notes.
- Prefer 1-2 line labels.
- Avoid dense paragraphs inside chart area.

## Color / Status Rules

Use consistent semantic colors.

Suggested mapping:

- Blue: selected / current / PROOF / active position
- Green: next action / safe continuation / preserved boundary
- Amber: watch / caution / partial risk / HOLD / evidence missing
- Red: high risk / BLOCK / survival or relationship danger
- Gray: unknown / inactive / past / baseline
- Purple or teal: incubation / strategic build / future option, optional

Important:

Do not rely on color alone.

Use labels, icons, or text as backup.

## Symbol Rules

### Quest Position Map

- point = quest
- ring = enemy / competition pressure
- triangle = survival / relationship risk
- halo = selected quest

### Industry Slope Timeline

- vertical line = current As-of point
- shaded band = future range / recheck zone
- dashed line = uncertain path
- branch arrow = next niche / future branching

### Snapshot Trajectory

- columns = snapshots
- arrows = delta between snapshots
- badges = trajectory labels
- panels = changed / unchanged / risk increased

### Risk Panel

Stacked bars or cards may be used, but do not implement now.

## Information Density Rules

A visual should not explain everything.

In-chart:

- position
- label
- status
- major warning only

Card:

- one-line judgment
- reason
- next action
- do-not-do boundary
- recheck condition

Interpretation note:

- evidence basis
- counterarguments
- market/source status
- missing evidence

If text does not fit, move it down into card or interpretation note.

Do not shrink font below readable size to force text into chart.

## Japanese Wrapping / Spacing Rules

- Prefer shorter Japanese labels.
- Avoid long labels inside plot area.
- Use cards for longer Japanese text.
- Keep at least `12-16px` padding inside cards.
- Keep sufficient line height.
- Avoid text touching borders.
- Do not place long text over grid lines.

## Screenshot / Archive Rules

Each visual should work as a saved artifact.

Must include:

- title
- As-of or prototype status if relevant
- current Gate / recommended action if relevant
- selected state
- next action or Codex handoff note
- do-not-do boundary or governance footer
- footer that states it is not prediction / scoring / launch permission

## Codex Handoff Visibility

For artifacts meant to guide Codex, include a visible section:

```text
Codexが次に引き受けること
```

or:

```text
次のAIが引き受けること
```

It should state:

- next action
- what not to broaden
- current Gate
- recheck condition if applicable

## Anti-Patterns

Avoid:

- right edge clipping
- overlong labels in graph area
- mixed Japanese/English paragraphs
- too many badges
- every field shown at once
- tiny fonts
- treating chart as full report
- hiding Do-Not-Do boundary
- missing Gate
- no As-of / prototype status
- visuals that look like market prediction
- color-only meaning
- old snapshot shown as current truth

## Future Renderer Direction

Future options:

### A. SVG-Only Design Tokens

- safest
- no dependency
- good for repo artifacts

### B. HTML/CSS Snapshot Renderer

- better layout and wrapping
- easier screenshot/PDF later
- possible future phase

### C. Mermaid/Graphviz

- useful for flow/logic
- less suitable for polished snapshot cards

Current recommendation:

Stay SVG-only for now, but define the design system so a future HTML/CSS renderer can reuse the same layout rules.

## Relationship To Current Prototypes

Existing prototypes are valid as early artifacts and should not be edited in Phase 10.34:

- `outputs/quest_position_map.svg`
- `outputs/quest_position_map_ja.svg`
- `outputs/industry_slope_timeline_ja.svg`
- `outputs/snapshot_trajectory_drift_delta_ja.svg`

They may be refined later using this design system only after a separate GO or CAP.

## Completion Line

Quest Snapshot Visual Design System v0.1 defines the shared visual rules for future Quest Map and Quest Snapshot artifacts so charts remain readable, Japanese-friendly, screenshot-ready, and useful for Codex handoff without adding analysis complexity.
