# Quest Map Layer v0.1

## Purpose

Quest Map Layer helps the operator choose the right opportunity under current constraints.

It treats a market or project opportunity like an RPG/game quest: the question is not only whether the world is growing, but whether this operator can enter this area now with the current level, gear, capital, distribution, proof, and time.

Core principle:

```text
The purpose is not to predict the winning market.
The purpose is to raise the operator's starting certainty before entering a quest.
Cost compression becomes strategically meaningful when it repeats.
```

## Core Metaphor

- Market / industry chart = world map
- Relevant segment chart = local map
- Project / idea = quest candidate
- Operator Edge = character build / skill modifier
- Capital / API access / distribution / credibility = gear
- Competition Pressure = enemy strength
- Proof Distance = distance to first clear proof or reward
- Reward Potential = quest reward
- Window Lifespan = how long the quest remains available
- Absorption Risk = whether the quest will be swallowed by LLMs, incumbents, or large platforms
- Carrier Fit = whether the operator can keep playing without burning out
- Recommended Action = quest selection

## Required Dimensions

### Reference Chart

Reference Chart is the chart that actually controls the opportunity.

The parent market may be too broad. A useful quest judgment should identify the narrower map that controls timing, proof, payment, access, or competition.

Examples:

- A Solana meme coin bot should not be judged by the whole crypto market alone. It may depend on Solana liquidity, DEX volume, meme trading activity, bot competition, API depth, capital, and top-bot concentration.
- A ramen shop in Yokohama should not be judged by the national ramen market alone. It should be judged through Kanagawa, Yokohama, or local area proxies when direct local data is missing.
- An AI app should not be judged by the whole AI market alone. It should be judged by the relevant app category, buyer willingness, distribution channel, and payment behavior.

If the direct local or segment chart is unavailable, use the closest proxy and lower confidence.

### Reference Chart Quality

Reference Chart Quality indicates how close the selected chart is to the actual factor that controls the quest's win/loss condition.

The point is to prevent a broad parent-market chart from creating false confidence when the real opportunity depends on a narrower segment, proxy, local chart, payment behavior, or execution layer.

Allowed levels:

#### DIRECT

The chart directly measures the relevant segment or local market.

Examples:

- A Yokohama ramen shop judged by Yokohama or local-area ramen demand, rent, competition, foot traffic, and price behavior.
- A Solana meme BOT judged by Solana DEX/meme volume, bot competition, API depth, latency, capital requirements, and top-bot concentration.

#### CLOSE PROXY

Direct chart is unavailable, but a close proxy exists.

Examples:

- Kanagawa ramen data used to infer Yokohama when Yokohama-specific data is unavailable.
- Solana DEX volume and wallet activity used as a proxy for meme BOT opportunity.

#### SEGMENT PROXY

The chart measures the right category but not the exact local/workflow layer.

Examples:

- AI developer tools used as a proxy for AI handoff audit tools.
- Consumer productivity apps used as a proxy for a specific habit app.

#### PARENT MARKET ONLY

Only broad market data exists.

Examples:

- AI market growth used to judge a specific AI app.
- Crypto market growth used to judge a Solana meme BOT.

This is allowed only as a weak starting point and must lower confidence.

#### UNKNOWN / UNGROUNDED

No usable chart or proxy is available.

The system must mark confidence low and recommend HOLD or PROOF before stronger action.

### Minimum Viable Edge

Minimum Viable Edge is the smallest concrete advantage required before the operator can move from HOLD to PROOF, or from PROOF to SHORT CYCLE / LAUNCH.

It answers:

```text
What must be true before this quest is worth entering?
```

Examples:

- For a Solana meme BOT, Minimum Viable Edge may require BOT-layer visibility, capital boundary, RPC/API access, latency route, risk controls, and a paper/simulated proof condition.
- For an AI-not-yet-adopted industry automation quest, Minimum Viable Edge may require one repeated manual workflow, clear current cost, output equivalence, buyer access, and a low-friction trial path.
- For an app/tool, Minimum Viable Edge may require a named buyer/workflow, measurable pain, willingness to pay, and one proof outcome.

### Market Slope

Market Slope describes whether the relevant market/map is flat, slowly rising, steepening, hype-spiking, rolling over, post-FOMO, or unclear.

The slope must be based on available evidence, not invented market data.

### Reward Distance

Reward Distance describes how far the operator is from first meaningful reward or proof.

Reward may mean paid use, a credible user proof point, distribution proof, trust, a reusable artifact, strategic positioning, or future option value.

### Reward Potential

Reward Potential describes what can realistically be gained if the quest succeeds.

The reward may be money, paid proof, distribution proof, trust, reusable artifact, strategic positioning, or future option value.

Reward Potential is not a guarantee of outcome.

### Switching Pressure

Switching Pressure is the pressure that makes a customer consider replacing an existing provider, workflow, tool, or habit.

It may come from:

- cost pressure
- slow delivery
- labor shortage
- economic deterioration
- repeated operational pain
- poor existing UX
- compliance or reporting burden
- inability to justify old pricing

Example:

A customer has long used Company A:

- human work
- 10,000 yen per job
- normal delivery speed
- trusted relationship

Company B offers:

- same perceived output
- faster delivery
- 3,000 yen per job
- first trial free

The customer may switch not because they love AI, but because the old cost becomes harder to justify.

### Cost Compression Trigger

Cost Compression Trigger is the moment when AI, automation, or process redesign can compress an existing paid workflow enough to create a realistic entry window.

Important factors:

- current price is high
- output is standardized enough
- delivery speed matters
- buyer is under cost pressure
- trial is low-friction
- failure cost is acceptable
- relationship lock-in is not too strong

The system should distinguish:

```text
AI is interesting
```

from:

```text
the buyer can no longer justify paying the old cost
```

### Repeat Frequency / Order Volume

Repeat Frequency / Order Volume indicates how often the target workflow repeats and whether enough orders exist to create revenue, learning, trust, distribution proof, or a durable habitat.

It answers:

```text
Is this a one-off compression, or a repeatable quest worth building around?
```

Why it matters:

A 10,000 yen -> 3,000 yen compression is not equally valuable in every workflow.

If the workflow happens once per year, the entry window may be weak.

If it repeats weekly, monthly, or across many similar buyers, it may become a real proof path or habitat.

Allowed levels:

#### ONE-OFF

The workflow occurs rarely or only once.

Usually not enough for LAUNCH.

May support a small proof, case study, or salvage action.

#### LOW REPEAT

The workflow repeats occasionally.

PROOF may be valid, but long-term habitat is uncertain.

#### MEDIUM REPEAT

The workflow repeats enough to test paid recurrence, improve delivery, and build trust.

PROOF or SHORT CYCLE may be valid depending on window lifespan and enemy strength.

#### HIGH REPEAT

The workflow repeats often or exists across many similar buyers.

If output equivalence, switching pressure, and revenue capture are also strong, this can support LAUNCH or habitat-building.

#### UNKNOWN

Repeat frequency is not known.

Do not recommend LAUNCH.

Recommend PROOF or HOLD until repeat behavior is observed.

### Output Equivalence

Output Equivalence means the buyer perceives the new output as good enough compared with the existing paid output.

This is not the same as perfect quality.

It means:

- good enough for the use case
- same apparent business value
- lower price or faster delivery
- low enough risk to try

If Output Equivalence is missing, low price alone may not create a real entry window.

### Trial Friction

Trial Friction is how hard it is for the buyer to compare the new option against the old one.

Low Trial Friction:

- first trial free
- one small task
- no migration
- no contract lock-in
- no sensitive data
- no operational disruption

High Trial Friction:

- migration required
- legal risk
- trust-heavy output
- high failure cost
- stakeholder approval required

### Window Lifespan

Window Lifespan describes how long the opportunity may remain available.

A short-lived opportunity may be valid as SHORT CYCLE.

A long-lived but currently low-reward opportunity may be valid as INCUBATE.

### Enemy Strength

Enemy Strength describes competition pressure, incumbent strength, LLM absorption risk, platform capture, capital requirements, API depth, or distribution difficulty.

Enemy Strength should not become a fear label. It is a current constraint layer.

### Required Gear

Required Gear describes what the operator would need to compete or prove the quest.

Required gear may include capital, API access, algorithmic edge, domain proof, distribution path, credibility, legal capacity, technical ability, time, or operational stamina.

### Operator Fit

Operator Fit describes whether this operator has the level, gear, edge, and Carrier capacity to enter this quest now.

Operator Fit is not a founder/personality judgment. It is an as-of fit between current opportunity requirements and current operator assets.

### As-of Starting Advantage

As-of Starting Advantage means the operator can begin from a better-informed and better-positioned starting point than someone who only knows the broad hype.

This is the core purpose of Quest Map Layer.

It does not mean:

- predicting the future
- guaranteeing success
- knowing the market will grow

It means:

- the operator knows the relevant reference chart
- the operator knows the minimum edge required
- the operator knows the switching pressure
- the operator knows the proof distance
- the operator knows what not to build
- the operator can take an early position before the opportunity becomes obvious

### AI Expansion Potential

AI Expansion Potential is the degree to which AI can compound the operator's early position after entry.

Examples:

- research expansion
- workflow mapping
- prototype generation
- sales material generation
- comparison trial preparation
- customer interview analysis
- proof documentation
- delivery compression
- operating procedure generation

Important rule:

AI Expansion Potential is not enough by itself.

It must be connected to:

- Reference Chart Quality
- Minimum Viable Edge
- Switching Pressure
- Operator Fit
- Carrier Fit

## Quest Action Labels

### LAUNCH

The operator has enough edge, readiness, payment/reward path, and the window is open now.

### PROOF

Do not broadly launch yet. Collect one bounded proof point.

### SHORT CYCLE

The opportunity may pay soon but has short lifespan or high absorption risk. Harvest carefully; do not overbuild.

### INCUBATE

The opportunity may have long-term habitat value, but current reward/proof is too far or the market is not ready yet.

### HOLD

Wait for a specific recheck condition.

### AVOID

The reward is too far, enemy strength is too high, payment path is weak, or Carrier cost is not justified.

### SALVAGE

The main hype/entry window may be gone, but there may be remaining value in tools, infrastructure, distressed assets, content, or niche repair.

## Strategic Interpretation

A 100m quest with 300,000 yen reward may be good if the window is short and the operator should not overbuild.

A 2km quest with 40,000 yen reward may still be worth incubating if the habitat may last 10 years and compounds with operator edge.

The correct question is not only "which reward is bigger?"

The correct question is:

- reward distance
- reward size
- window lifespan
- enemy strength
- required gear
- operator fit
- carrier cost

Large reward does not automatically mean LAUNCH.

Small reward does not automatically mean AVOID.

A quest with strong operator fit, short proof distance, and low Carrier cost may be chosen before a larger but less enterable quest.

## Examples

### Example A: AI App

- Parent market: AI market
- Relevant chart: payment willingness by app category and workflow urgency
- Reference Chart Quality: SEGMENT PROXY or CLOSE PROXY depending on evidence
- Minimum Viable Edge: named buyer/workflow, measurable pain, willingness to pay, and one proof outcome
- Recommended Action: PROOF

The broad AI market is not enough to support LAUNCH. The quest should first prove a narrower workflow, buyer, and payment behavior.

### Example B: Solana Meme BOT

- Parent market: crypto market
- Relevant chart: Solana meme trading + BOT competition layer
- Reference Chart Quality: PARENT MARKET ONLY if only BTC/SOL price is used
- Minimum Viable Edge: BOT-layer visibility, capital boundary, RPC/API route, risk controls, and simulated proof
- Switching Pressure: not buyer switching; this is edge capture competition
- Recommended Action: HOLD / PROOF / AVOID until deeper BOT-layer evidence exists

Crypto market growth does not prove a specific bot opportunity. The controlling chart is closer to liquidity, DEX volume, latency, API depth, capital requirements, bot concentration, and substitute pressure.

### Example C: Yokohama Ramen Shop

- Parent market: national ramen market
- Relevant chart: Yokohama/local area ramen demand, rent, competition, foot traffic, and price behavior
- Reference Chart Quality: CLOSE PROXY if only Kanagawa data is available
- Recommended Action: depends on local proxy quality, not national market size

National ramen demand may be useful background, but the quest is controlled by local foot traffic, rent, competition, pricing, and operator fit.

### Example D: AI-Not-Yet-Adopted Industry Automation

- Parent market: AI / automation
- Relevant quest: replace or compress one expensive manual workflow
- Minimum Viable Edge: known repeated workflow + current price + buyer access + output equivalence + low-friction trial
- Repeat Frequency / Order Volume: HIGH REPEAT if the buyer orders weekly/monthly or many similar buyers have the same workflow
- Switching Pressure: high if the buyer is under cost pressure and the current provider is expensive or slow
- Current price: 10,000 yen per job
- Compressed price: 3,000 yen per job
- Recommended Action: PROOF first; LAUNCH only after output equivalence and paid repeat are proven

This is not an "AI is growing" quest. It becomes real only when an existing paid workflow can be compressed while preserving perceived output value.

### Example E: Generic AI App

- Parent market: AI app market
- Relevant quest: one paid workflow
- Minimum Viable Edge: named buyer + measurable pain + payment willingness + one proof outcome
- Recommended Action: PROOF, not broad LAUNCH

The operator should avoid building a generic app from hype. The first quest is to prove that one buyer/workflow has enough pain and payment willingness.

### Example F: One-Time Document Cleanup

- Relevant quest: compress one document cleanup task
- Cost Compression Trigger: may be real
- Repeat Frequency / Order Volume: ONE-OFF
- Recommended Action: PROOF / SALVAGE, not broad build

A one-time compression can create a useful case study or small salvage action, but it does not by itself justify a durable quest.

### Example G: Monthly Reporting Workflow

- Relevant quest: compress a recurring monthly report
- Repeat Frequency / Order Volume: MEDIUM REPEAT or HIGH REPEAT
- Recommended Action: PROOF first; durable habitat may be possible if buyer cost pressure and output equivalence are strong

Monthly reporting can become a real habitat when recurrence, output equivalence, switching pressure, and low trial friction are all visible.

## Non-Goals

Quest Map Layer is not:

- a market prediction engine
- investment advice
- a guarantee of reward
- VC scoring
- founder ranking
- automated launch permission
- an excuse to enter every rising market
- external research automation

## Governance

- If market size or capital flow is used, it must be source-backed or marked unknown.
- If direct local/reference chart is unavailable, use the closest proxy and lower confidence.
- Do not judge by the parent market alone when the opportunity depends on a narrower segment.
- Do not recommend LAUNCH from PARENT MARKET ONLY.
- Do not recommend broad build from UNKNOWN / UNGROUNDED.
- If Reference Chart Quality is PARENT MARKET ONLY, allowed actions are usually PROOF, HOLD, INCUBATE, or AVOID.
- If Reference Chart Quality is DIRECT or CLOSE PROXY, stronger action may be considered only if Operator Fit, Payment Willingness, Reward Distance, and Carrier Fit also support it.
- If the chosen chart is too broad, the card must say: "Reference chart too broad."
- Prefer a lower but more relevant chart over a higher but generic chart.
- Do not move from HOLD to PROOF unless Minimum Viable Edge is named.
- Do not recommend SHORT CYCLE unless reward distance is close and window lifespan is short.
- Do not recommend LAUNCH unless Minimum Viable Edge, Payment/Revenue Capture, Operator Fit, and Carrier Fit are all strong.
- If Switching Pressure is high but Output Equivalence is weak, recommend PROOF, not LAUNCH.
- If Output Equivalence is high but Trial Friction is high, recommend PROOF or HOLD.
- If As-of Starting Advantage is weak, do not recommend broad build from hype alone.
- If AI Expansion Potential is high but Reference Chart Quality is weak, recommend research/proof, not launch.
- Prefer early small position + AI expansion over broad speculative build.
- Do not recommend LAUNCH if Repeat Frequency / Order Volume is UNKNOWN.
- If Cost Compression Trigger is strong but Repeat Frequency is ONE-OFF, prefer PROOF or SALVAGE, not broad build.
- If Repeat Frequency is HIGH but Output Equivalence is unproven, recommend PROOF.
- If Repeat Frequency is HIGH, Switching Pressure is high, Output Equivalence is proven, Trial Friction is low, and Carrier Fit is strong, stronger action may be considered.
- Repeat Frequency helps distinguish SHORT CYCLE from long-term habitat: high repeat but short lifespan may be SHORT CYCLE; medium/high repeat with long lifespan may be INCUBATE or LAUNCH depending on proof.
- Repeat Frequency must not override Reference Chart Quality. A high-repeat claim from a weak parent-market chart should lower confidence.
- Do not recommend broad build when the operator only has proof-level edge.
- Do not turn SHORT CYCLE into long-term habitat.
- Do not turn INCUBATE into immediate launch.
- Keep the human as Decision Owner.

## Future Input Direction

Future implementation may add or revise:

- `inputs/quest.md`
- `inputs/reference_chart.md`
- `inputs/operator_position.md`

Potential input fields:

- quest_name
- parent_market
- relevant_reference_chart
- reference_chart_quality
- reference_chart_warning
- proxy_chart_used
- minimum_viable_edge
- market_slope
- reward_distance
- reward_potential
- switching_pressure
- cost_compression_trigger
- repeat_frequency_order_volume
- repeat_frequency_note
- output_equivalence
- trial_friction
- window_lifespan
- enemy_strength
- required_gear
- operator_fit
- carrier_cost
- as_of_starting_advantage
- ai_expansion_potential
- absorption_risk
- payment_willingness
- proof_path
- recommended_action
- recheck_condition

This phase does not add those inputs.

## Future Output Direction

Future implementation may add:

- `outputs/quest_map.json`
- `outputs/quest_map.svg`

Potential output:

- Quest label
- Map / reference chart used
- Reference Chart Quality
- Reference Chart Warning
- Minimum Viable Edge
- Current operator position
- Reward distance
- Reward potential
- Switching Pressure
- Cost Compression Trigger
- Repeat Frequency / Order Volume
- Repeat Frequency Note
- Output Equivalence
- Trial Friction
- Window lifespan
- Required gear
- Enemy strength
- As-of Starting Advantage
- AI Expansion Potential
- Recommended action
- One next action
- Do-not-do boundary for Codex/AI

This phase does not add those outputs.

## Relationship To Existing Entry Window Radar

Quest Map Layer does not replace Entry Window Card.

It extends it.

Entry Window Card answers:

```text
Where is this project now?
```

Quest Map Layer answers:

```text
Given the market map, reward distance, required gear, and operator fit, which quest should be taken now?
```

Quest Map Layer should preserve Entry Window Radar's as-of language. It should not become prediction, investment advice, founder judgment, or automatic launch permission.

## Completion Line

Quest Map Layer now distinguishes one-time cost-compression opportunities from repeatable workflow habitats by adding Repeat Frequency / Order Volume.
