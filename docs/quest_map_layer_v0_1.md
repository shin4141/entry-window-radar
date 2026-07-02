# Quest Map Layer v0.1

## Purpose

Quest Map Layer helps the operator choose the right opportunity under current constraints.

It treats a market or project opportunity like an RPG/game quest: the question is not only whether the world is growing, but whether this operator can enter this area now with the current level, gear, capital, distribution, proof, and time.

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
- Recommended Action: PROOF

The broad AI market is not enough to support LAUNCH. The quest should first prove a narrower workflow, buyer, and payment behavior.

### Example B: Solana Meme BOT

- Parent market: crypto market
- Relevant chart: Solana meme trading + BOT competition layer
- Reference Chart Quality: PARENT MARKET ONLY if only BTC/SOL price is used
- Recommended Action: HOLD / PROOF / AVOID until deeper BOT-layer evidence exists

Crypto market growth does not prove a specific bot opportunity. The controlling chart is closer to liquidity, DEX volume, latency, API depth, capital requirements, bot concentration, and substitute pressure.

### Example C: Yokohama Ramen Shop

- Parent market: national ramen market
- Relevant chart: Yokohama/local area ramen demand, rent, competition, foot traffic, and price behavior
- Reference Chart Quality: CLOSE PROXY if only Kanagawa data is available
- Recommended Action: depends on local proxy quality, not national market size

National ramen demand may be useful background, but the quest is controlled by local foot traffic, rent, competition, pricing, and operator fit.

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
- market_slope
- reward_distance
- reward_potential
- window_lifespan
- enemy_strength
- required_gear
- operator_fit
- carrier_cost
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
- Current operator position
- Reward distance
- Reward potential
- Window lifespan
- Required gear
- Enemy strength
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

Quest Map Layer now explicitly grades whether the chosen reference chart is close enough to the actual win/loss condition, preventing broad parent-market charts from producing false confidence.
