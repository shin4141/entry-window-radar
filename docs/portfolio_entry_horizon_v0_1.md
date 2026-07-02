# Portfolio Entry Horizon v0.1

## Purpose

Portfolio Entry Horizon compares multiple projects owned by the same operator and helps decide which project should be launched first, which should gather proof, which should be incubated, which should be held, and which should be avoided.

## Core Problem

AI makes it easy to create many projects.

The strategic problem is no longer only "Can this project be built?"

The problem is:

- Which project matches the current market horizon?
- Which project fits the operator's current edge?
- Which project can be launched or proven soon?
- Which project should be delayed because it is long-horizon, too heavy, or not yet winnable?
- Which project would consume the operator's Carrier if launched too early?

## Core Distinction

Single Entry Window Map:

- evaluates one repo / README / idea.

Portfolio Entry Horizon:

- compares several projects at once.
- helps decide launch order.

## Required Dimensions

### Market Horizon

How strongly the project connects to a source-backed future market or current timing signal.

This may include 2030 market estimates, market growth, buyer urgency, category momentum, or adjacent market pull.

It must be source-backed when used.

It must not invent market size.

### Operator Edge

How much the operator has specific proof, assets, knowledge, artifacts, distribution, or execution advantage.

### Launch Readiness

How close the project is to being shown, tested, or launched without major additional build cost.

### Competition Pressure

How strongly the project is exposed to incumbents, generic AI tools, prompt packs, automation frameworks, pricing pressure, or commoditization.

### Build Burden

How much time, cost, cognitive load, explanation load, or implementation complexity is required before a meaningful proof can be obtained.

### Proof Path

Whether there is one bounded proof point that can be collected soon.

### Carrier Fit

Whether launching or proving this project preserves the operator's time, attention, recovery capacity, credibility, and re-entry capacity.

## Future Action Labels

### LAUNCH

The project is timely, operator edge is strong, launch readiness is high, and proof path is clear.

### PROOF

The project should not be broadly launched yet, but one bounded proof point should be collected now.

### INCUBATE

The project connects to a meaningful future market, but it is too early, too heavy, or not yet sufficiently legible.

### HOLD

The project should remain paused until a recheck condition appears.

### AVOID

The project is too crowded, too weakly connected to operator edge, too costly, or too likely to consume the Carrier.

## Strategic Rule

When multiple projects exist, prefer:

- launchable proof over abstract potential
- high operator edge over large but generic markets
- bounded proof over broad launch
- Carrier-preserving projects over exciting but heavy projects
- source-backed market horizon over hype

## Key Interpretation

A huge 2030 market does not automatically mean launch first.

A smaller project with stronger operator edge and faster proof path may be strategically better.

Long-horizon projects may be incubated rather than abandoned.

## Non-Goals

Portfolio Entry Horizon is not:

- investment advice
- market prediction
- VC scoring
- founder ranking
- revenue guarantee
- automated launch permission
- external research automation
- portfolio management for financial assets

## Input Direction

Phase 9.1 adds manual input templates:

- `inputs/projects.md`
- `inputs/markets.md`

These templates make multi-project and source-backed market-horizon inputs visible, but they do not authorize portfolio scoring, JSON output, SVG output, or launch-order automation.

Potential `projects.md` shape:

- project_name
- project_summary
- current_artifact
- operator_edge
- launch_readiness
- build_burden
- proof_path
- carrier_fit
- missing_evidence

Potential `markets.md` shape:

- market_name
- horizon_year
- market_size_estimate
- source
- source_confidence
- adjacent_markets
- timing_signal
- notes

## Future Output Direction

Future implementation may add:

- `outputs/portfolio_radar.json`
- `outputs/portfolio_entry_map.svg`
- `outputs/launch_order.md`

Potential output fields:

- project_name
- market_horizon
- operator_edge
- launch_readiness
- competition_pressure
- build_burden
- proof_path
- carrier_fit
- recommended_action
- reason
- next_action
- recheck_condition

## Relationship To Existing Entry Window Radar

Portfolio Entry Horizon should reuse the existing Entry Window Card logic where possible.

Each project may first receive its own Entry Window Card.

Then the portfolio layer compares the cards and recommends launch order.

## Governance Boundary

This specification does not authorize implementation yet.

Phase 9.1 must be separately gated.

External posting remains HOLD.

Delivery Scope Radar remains BLOCK.

V14 deep scoring remains BLOCK.

Score History and Entry Window Drift remain BLOCK unless explicitly reopened later.

## Completion Line

Portfolio Entry Horizon v0.1 defines how Entry Window Radar can compare multiple projects and support launch-order decisions without becoming prediction, VC scoring, investment advice, or uncontrolled portfolio automation.
