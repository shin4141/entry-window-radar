# Quest Map Layer v0.1

## Purpose

Quest Map Layer helps the operator choose the right opportunity under current constraints.

It treats a market or project opportunity like an RPG/game quest: the question is not only whether the world is growing, but whether this operator can enter this area now with the current level, gear, capital, distribution, proof, and time.

Core principle:

```text
The purpose is not to predict the winning market.
The purpose is to raise the operator's starting certainty before entering a quest.
Cost compression becomes strategically meaningful when it repeats.
Repeat frequency shows possible habitat.
Paid repeat shows capture.
Retention reason shows whether capture can survive.
Relationship preservation is valid, but it must remain survivable.
AI displacement may begin by splitting standardized work away from relationship-heavy work.
The goal is not to replace people coldly.
The goal is to prevent hidden cost drag from becoming future regret.
Cost drag matters differently depending on survival sensitivity.
A relationship cost can be valid, but only if the operator can survive it or offset it.
The goal is not to force switching.
The goal is to prevent invisible cost drag from becoming payroll damage, runway loss, or future regret.
Cost drag becomes clearer when tied to a named exposure anchor.
Unknown exposure is not safety.
The goal is to prevent invisible cost drag from quietly consuming payroll, runway, or future options.
Exposure is not only what the cost is.
Exposure is what the cost consumes.
A small amount can be large if the buffer is small.
Unknown ratio is not safety.
The goal is not to force replacement.
The goal is to make hidden survival pressure visible before it becomes regret.
Relationship value is not zero because it is hard to measure.
Relationship value is not infinite because it is emotionally important.
The goal is not to replace relationships.
The goal is to see whether the relationship value actually offsets the survival cost drag, or whether split routing is needed.
Split routing is a middle path, not a free path.
Relationship value protects what the relationship gives.
Relationship damage estimates what may be lost if the relationship feels displaced.
The goal is not cold replacement.
The goal is survival-aware routing that does not create avoidable relationship damage.
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

### Survival Cost Drag

Survival Cost Drag is the ongoing cost burden created by preserving an existing provider, workflow, relationship, or manual process when a cheaper/faster equivalent option may exist.

It answers:

```text
If we keep paying the old cost, does that cost begin to threaten survival, hiring, payroll, runway, or operational resilience?
```

Important framing:

Relationship preservation is not wrong.

The question is whether the relationship-maintenance cost remains survivable.

Example:

Company A:

- long-term relationship
- human/manual work
- 10,000 yen per job
- normal or slow delivery
- sometimes sends work back to the customer

Company B:

- similar perceived output
- faster delivery
- 3,000 yen per job
- first trial free

If the job repeats monthly:

- cost saving from B may be 7,000 yen per month
- annual saving may be 84,000 yen

If Company A returns only about 50,000 yen per year in uncertain work, the operator must ask:

- Is preserving Company A worth the net cost?
- Can the company absorb the difference?
- Does keeping A force cuts elsewhere?
- Does the relationship value justify the survival drag?

### Actual Cashflow Sensitivity

Actual Cashflow Sensitivity indicates how strongly a visible cost drag affects the operator's real cashflow, payroll safety, runway, investment capacity, or survival.

It answers:

```text
Can this operator absorb the cost drag without damaging survival or future options?
```

Important framing:

This is not a moral judgment against loyalty or relationships.

It is a survival check.

The same cost drag can be:

- acceptable for a cash-rich company
- painful for a thin-margin company
- dangerous for a company near payroll, tax, rent, debt, or runway limits

Allowed levels:

#### LOW

The operator can absorb the cost drag without harming payroll, runway, investment capacity, or resilience.

#### MEDIUM

The cost drag affects budget choices, investment capacity, or margin, but does not immediately threaten survival.

#### HIGH

The cost drag meaningfully pressures payroll, runway, tax/rent/debt capacity, hiring, or ability to compete.

#### CRITICAL

The cost drag may directly contribute to layoffs, cashflow failure, owner burnout, or business closure if left unaddressed.

#### UNKNOWN

Cashflow sensitivity is not known.

Do not treat cost drag as harmless.

Recommend naming the sensitivity or using bounded proof / split routing.

### Survival Threshold

Survival Threshold is the point where a recurring cost drag stops being a preference or relationship cost and starts threatening survival, payroll, hiring, investment, resilience, or business continuity.

It answers:

```text
At what point does inaction become survival-relevant?
```

Examples:

- If monthly savings are small compared to stable profit, Survival Cost Drag may be LOW.
- If monthly savings equal a meaningful part of payroll, rent, tax reserve, debt payment, or owner runway, Survival Cost Drag may be HIGH.
- If ignoring the drag could force layoffs, missed payments, or business closure, Regret Cost of Inaction should rise.

### Quantified Runway / Payroll Exposure

Quantified Runway / Payroll Exposure is a simple As-of estimate of what the recurring cost drag means in operational survival terms.

It answers:

```text
What concrete runway, payroll, investment, or obligation does this cost drag affect?
```

Important framing:

This is not accounting, tax advice, or a precise financial forecast.

It is a bounded survival check.

If the exposure cannot be quantified, mark UNKNOWN and do not treat the cost drag as harmless.

### Exposure Anchor

Exposure Anchor is the named obligation, buffer, or option affected by the cost drag.

Examples:

- one month of software/tool budget
- part of a tax reserve
- part of rent
- part of payroll buffer
- marketing/test budget
- emergency cash buffer
- owner runway
- one small AI automation experiment
- one contractor payment

A cost drag is more decision-relevant when it can be tied to a real exposure anchor.

### Exposure Severity

Exposure Severity indicates how strongly the cost drag affects the named exposure anchor.

Allowed levels:

#### NONE

The cost drag does not materially affect runway, payroll, obligations, or investment capacity.

#### MINOR

The cost drag is noticeable but does not change near-term decisions.

#### OPTION-LIMITING

The cost drag limits marketing, tools, experiments, hiring, or investment capacity.

#### SURVIVAL-RELEVANT

The cost drag affects payroll safety, rent/tax/debt capacity, owner runway, or business resilience.

#### CRITICAL

The cost drag may contribute directly to missed payments, layoffs, forced restructuring, owner burnout, or closure.

#### UNKNOWN

The operator has not named what the cost drag touches.

Do not assume it is safe.

### Exposure Amount

Exposure Amount is the recurring cost drag expressed as a monthly and/or annual amount.

It answers:

```text
How much cost drag are we actually talking about?
```

Examples:

- 7,000 yen per month
- 84,000 yen per year
- 30,000 yen per month
- unknown

Important rule:

If the amount is unknown, write UNKNOWN.

Do not invent numbers.

### Exposure Ratio

Exposure Ratio is the cost drag compared with the named exposure anchor.

It answers:

```text
How large is this drag relative to the thing it affects?
```

Examples:

- 84,000 yen/year as a share of annual tool budget
- 84,000 yen/year as a share of marketing test budget
- 7,000 yen/month as a share of payroll buffer
- 7,000 yen/month as a share of owner runway
- 84,000 yen/year as a share of emergency buffer

This is not accounting, tax advice, or a precise financial forecast.

It is an As-of survival sensitivity estimate.

### Exposure Ratio Quality

Exposure Ratio Quality indicates whether the ratio is based on actual known amounts or rough assumptions.

Allowed levels:

#### DIRECT

Both cost drag and exposure anchor amount are known.

#### ESTIMATED

Cost drag is known, anchor amount is estimated.

#### PARTIAL

Cost drag is known, but anchor is only qualitatively described.

#### UNKNOWN

Ratio cannot be estimated.

### Exposure Ratio Band

Exposure Ratio Band indicates how large the cost drag is relative to the exposure anchor.

Allowed levels:

#### NEGLIGIBLE

The cost drag is too small to change the decision by itself.

#### SMALL

The cost drag is noticeable but usually absorbable if the relationship value is real.

#### MEANINGFUL

The cost drag consumes a visible share of the anchor and should require an offset plan or split-routing proof.

#### LARGE

The cost drag consumes a major share of the anchor and should not be left unaddressed.

#### CRITICAL

The cost drag is large enough to threaten payroll, runway, required obligations, or near-term survival.

#### UNKNOWN

The ratio is unknown.

Do not assume safety.

The exact threshold may vary by business type.

The card should avoid pretending the bands are universal accounting rules.

### Regret Cost of Inaction

Regret Cost of Inaction is the future regret created when the operator fails to act on visible cost pressure early enough.

It answers:

```text
If we ignore this cost pressure now, what future harm may we regret?
```

Potential future harms:

- employee layoffs
- cashflow deterioration
- owner burnout
- inability to invest
- inability to compete with AI-enabled providers
- business closure
- delayed but harsher restructuring
- loss of options because the decision was postponed too long

Important framing:

The purpose is not to blame the operator for loyalty.

The purpose is to make the future cost of inaction visible before survival is damaged.

### Relationship-Preserving Displacement

Relationship-Preserving Displacement is when a buyer does not fully cut an old provider, but shifts standardized or repeatable work to a cheaper/faster AI-enabled provider.

It answers:

```text
Can the operator preserve the human relationship while routing standard repeat work elsewhere?
```

Possible routing:

- Trust-heavy work stays with Company A.
- Relationship-sensitive work stays with Company A.
- Standardized repeat work moves to Company B.
- Speed-sensitive or low-risk comparison work moves to Company B.
- Trial work is used to test equivalence before deeper switching.

This is not "replace all relationships."

It is "separate the parts of the relationship that require trust from the parts that are standardized and cost-compressible."

### Reciprocal Relationship Value

Reciprocal Relationship Value is the value returned by the existing relationship, such as referrals, work sent back, emergency help, local trust, goodwill, information flow, introductions, or reputation.

It answers:

```text
What does the old relationship give back, and is that value greater than the cost drag?
```

Types:

- direct returned revenue
- referrals
- emergency support
- reputation protection
- local network access
- future option value
- personal trust
- non-monetary stability

Important rule:

Do not reduce all relationships to money.

But if the operator keeps a costly relationship, the non-monetary value should be named rather than assumed.

### Relationship Value Coverage

Relationship Value Coverage indicates how much of the visible cost drag is offset by the reciprocal value of the existing relationship.

It answers:

```text
Does the relationship give back enough value to justify the ongoing cost drag?
```

Important framing:

This is not a command to cut relationships.

This is not a claim that all relationships are financial.

It is an As-of check to prevent vague loyalty from hiding survival-relevant cost pressure.

### Reciprocal Value Amount

Reciprocal Value Amount is the visible or estimated value returned by the existing relationship.

It may include:

- direct returned work
- referrals
- emergency support
- local trust
- reputation protection
- bundled or hidden services
- useful information flow
- introductions
- future option value
- personal trust or reliability

Important rule:

Monetary value should be named when available.

Non-monetary value should be described rather than ignored.

### Reciprocal Value Coverage Ratio

Reciprocal Value Coverage Ratio compares visible reciprocal value against the cost drag or saving opportunity.

Example:

- Cost drag / saving opportunity: 84,000 yen per year
- Returned work: about 50,000 yen per year, uncertain
- Coverage ratio: about 60%, before switching damage risk and qualitative value

This is not a precise forecast.

It is a visibility tool.

### Relationship Value Quality

Relationship Value Quality indicates how grounded the relationship-value estimate is.

Allowed levels:

#### DIRECT

Returned work, referrals, or support are documented or recently observed.

#### ESTIMATED

Value is estimated from past patterns.

#### QUALITATIVE

Relationship value exists but is not easily monetized.

#### CLAIMED

Relationship is said to matter, but the value is not named.

#### UNKNOWN

Relationship value is not known.

### Relationship Value Coverage Band

Relationship Value Coverage Band indicates whether reciprocal value offsets the visible cost drag.

Allowed levels:

#### FULLY OFFSETS

Reciprocal value clearly covers the cost drag and switching damage risk.

Keeping may be justified if Carrier Fit and survival exposure are acceptable.

#### PARTIALLY OFFSETS

Relationship value covers part of the cost drag.

Split routing, negotiation, or offset planning may be appropriate.

#### DOES NOT OFFSET

Relationship value appears lower than the cost drag.

Passive loyalty becomes harder to justify unless non-monetary value is strong and survivable.

#### QUALITATIVE ONLY

Relationship value may be real but cannot be compared directly.

Name the non-monetary value and use split routing or proof rather than cold replacement.

#### UNKNOWN

Do not assume the relationship offsets the cost drag.

Recommend naming value, measuring returned work, or running bounded split-routing proof.

### Relationship Damage Severity

Relationship Damage Severity is the expected harm if the existing provider, partner, or relationship-heavy company feels displaced, bypassed, compared, or partially replaced.

It answers:

```text
If we split-route or test a cheaper provider, how bad is the downside if the old relationship is damaged?
```

Important framing:

Split routing can preserve relationships, but it is not risk-free.

Some relationships tolerate partial routing.

Some relationships interpret partial routing as betrayal, distrust, or loss of loyalty.

### Relationship Damage Channels

Relationship damage may appear through:

- loss of referrals
- reduced returned work
- reduced emergency support
- reputational damage
- social conflict
- local network damage
- worse pricing or lower priority from Company A
- refusal to cooperate later
- loss of hidden bundled value
- emotional or personal conflict
- operational disruption

### Damage Severity Levels

#### LOW

The relationship is professional and can tolerate vendor comparison or partial routing.

#### MEDIUM

Some damage is possible, but it can likely be reduced through communication, scope separation, or careful trial design.

#### HIGH

Partial displacement may reduce referrals, trust, priority, or local reputation.

Split routing must be carefully bounded or negotiated.

#### CRITICAL

Even partial displacement may destroy an essential relationship, trigger serious social or reputational harm, or remove support that the operator cannot replace.

Do not proceed without an explicit protection plan.

#### UNKNOWN

Damage severity is not known.

Do not assume split routing is safe.

Use careful discovery, relationship-value inventory, or non-sensitive low-risk proof.

### Relationship Damage Quality

Relationship Damage Quality indicates how grounded the damage estimate is.

Allowed levels:

#### DIRECT

Past behavior or explicit statements show how the relationship reacts to partial routing or comparison.

#### ESTIMATED

The estimate is based on relationship history, industry norms, or prior interactions.

#### QUALITATIVE

Risk is real but cannot be quantified easily.

#### UNKNOWN

No clear evidence exists.

### Damage Mitigation Option

Damage Mitigation Option is the available way to reduce relationship damage while still addressing cost drag.

Examples:

- keep Company A on trust-heavy work
- ask Company A to match price or scope on standardized work
- communicate that Company B is only for overflow or standardized tasks
- use Company B only on non-overlapping work
- run anonymous or internal comparison before external routing
- negotiate scope rather than replacing the provider
- create a smaller package for Company A
- delay split routing until survival exposure is named
- document why survival pressure requires a trial

### Net Switching Delta

Net Switching Delta is the difference between the expected saving from changing or splitting the workflow and the expected value of keeping the old relationship.

Formula-like framing:

```text
Net Switching Delta =
expected cost saving
minus expected reciprocal relationship value
minus switching damage risk
```

This is not a precise financial forecast.

It is an As-of reasoning tool.

Example:

- Cost saving: 84,000 yen per year
- Expected reciprocal work: 50,000 yen per year, uncertain
- Switching damage risk: unknown

Interpretation:

The operator should not automatically switch.

But the operator must not ignore that preserving the old relationship has a real cost that must be justified, offset, or split-routed.

### Switching Damage Risk

Switching Damage Risk is the harm created by reducing or replacing the old provider.

It may include:

- loss of referrals
- reputational damage
- emergency support loss
- social conflict
- reduced trust in the local network
- loss of bundled or hidden services
- lower quality in edge cases
- legal or operational risk
- relationship damage that exceeds direct cost savings

Important rule:

If Switching Damage Risk is high, prefer split routing or negotiation over full replacement.

### Split Routing Option

Split Routing Option is a strategy where the operator does not fully switch providers, but divides work by risk, trust, standardization, and cost compression.

Examples:

- keep relationship-heavy work with the incumbent
- move standardized repeat work to the AI-enabled provider
- test low-risk tasks first
- negotiate scope or price with the incumbent
- use the new provider as a benchmark before switching
- keep both providers while measuring actual outcomes

Core principle:

The best action may be neither loyalty nor replacement.

It may be controlled decomposition.

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

### Paid Repeat Signal

Paid Repeat Signal is evidence that a buyer is willing to pay again for the same or similar compressed workflow after an initial trial, proof, or first delivery.

It answers:

```text
Did the buyer only try it once, or did they show that this can become repeat revenue, trust, and habitat?
```

Why it matters:

Repeat Frequency / Order Volume shows that a workflow may recur.

Paid Repeat Signal shows that the operator can actually capture recurring value.

A workflow can have high repeat frequency but still fail if:

- the buyer likes the free trial but does not pay
- the buyer can self-serve with free tools
- the output is not trusted enough
- the incumbent relationship wins
- the compressed price is attractive but not worth switching
- the buyer only wanted a one-time experiment

Allowed levels:

#### NONE

No paid repeat signal.

Trial, curiosity, or free usage only.

Usually do not recommend LAUNCH.

#### WEAK

Buyer expresses interest but has not paid or committed.

May justify another bounded PROOF, not broad build.

#### PARTIAL

Buyer pays once after a free trial, or verbally commits to repeat under conditions.

Supports PROOF continuation, not full LAUNCH.

#### STRONG

Buyer pays again for the same workflow, requests repeat delivery, or introduces a similar repeat buyer.

May support SHORT CYCLE, INCUBATE, or LAUNCH depending on Window Lifespan, Carrier Fit, and Enemy Strength.

#### UNKNOWN

No evidence collected.

Do not recommend LAUNCH.

### Repeat Retention Reason

Repeat Retention Reason is the reason a buyer pays again, requests repeat delivery, or introduces a similar buyer after an initial trial or first paid proof.

It answers:

```text
Was the repeat payment caused by a durable advantage, or by a temporary/fragile reason?
```

Why it matters:

Paid Repeat Signal shows that repeat value was captured.

Repeat Retention Reason explains whether that value can persist, compound, or spread.

Allowed categories:

#### PRICE

Buyer repeats because the compressed price is meaningfully lower.

#### SPEED

Buyer repeats because delivery is faster.

#### OUTPUT EQUIVALENCE

Buyer repeats because the output is good enough compared with the old provider/workflow.

#### TRUST

Buyer repeats because the operator or delivery process became trusted.

#### URGENCY

Buyer repeats because the buyer has recurring time pressure or operational urgency.

#### NO BETTER ALTERNATIVE

Buyer repeats because alternatives are worse, slower, too expensive, or too hard to use.

#### WORKFLOW FIT

Buyer repeats because the solution fits the buyer's actual workflow with low friction.

#### RELATIONSHIP / FAVOR

Buyer repeats mainly because of personal relationship, courtesy, or one-off goodwill.

This is weaker than durable retention.

#### DISCOUNT-ONLY

Buyer repeats only while the offer is unusually cheap or free-like.

This is fragile and should lower confidence.

#### UNKNOWN

The reason for repeat is not known.

Do not treat repeat payment as durable habitat evidence.

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

### Example H: Free Trial With Praise But No Payment

- Relevant quest: AI-low-adoption manual workflow compression
- Trial result: free first trial completed
- Buyer response: "this is useful"
- Paid Repeat Signal: WEAK
- Recommended Action: PROOF, not LAUNCH

Free trial satisfaction is useful evidence, but it is not the same as paid repeat.

### Example I: Paid Second Job After Free Trial

- Relevant quest: repeatable compressed workflow
- Trial result: free first trial completed
- Buyer response: pays for the second job
- Paid Repeat Signal: PARTIAL
- Recommended Action: continue PROOF or consider SHORT CYCLE if window lifespan is short

One paid follow-up shows capture may be possible, but it is not enough by itself to justify broad build.

### Example J: Repeated Payment Or Similar Buyer Referral

- Relevant quest: repeatable workflow habitat
- Buyer response: pays repeatedly or introduces similar buyers
- Paid Repeat Signal: STRONG
- Recommended Action: consider INCUBATE / LAUNCH / SHORT CYCLE depending on window lifespan, enemy strength, and Carrier Fit

Paid repeat is stronger than stated interest because it shows the operator can capture recurring value.

### Example K: One-Off Annual Workflow

- Relevant quest: annual or one-time workflow compression
- Paid Repeat Signal: weak unless the same workflow repeats or similar buyers exist
- Recommended Action: SALVAGE / PROOF, not broad build

Even if the buyer pays once, the signal remains limited when the workflow itself does not repeat.

### Example L: Repeat Because It Is Faster And Cheaper Enough

- Relevant quest: repeatable compressed workflow
- Buyer response: pays again because output was good enough, faster, and cheaper
- Repeat Retention Reason: PRICE + SPEED + OUTPUT EQUIVALENCE
- Recommended Action: continue PROOF; consider INCUBATE if repeat frequency and Carrier Fit are strong

The repeat is more durable when the buyer returns for reasons that can survive beyond novelty.

### Example M: Repeat Because It Is Discounted

- Relevant quest: repeatable workflow trial
- Buyer response: pays again only because of a large discount
- Repeat Retention Reason: DISCOUNT-ONLY
- Recommended Action: PROOF / HOLD, not LAUNCH

Discount-only retention may reveal weak Payment / Revenue Capture.

### Example N: Repeat Because Trust And Workflow Fit Improved

- Relevant quest: monthly compressed workflow
- Buyer response: pays again because they trust the operator and the workflow fits their monthly process
- Repeat Retention Reason: TRUST + WORKFLOW FIT
- Recommended Action: INCUBATE may be considered if repeat frequency and paid repeat remain strong

Trust can support a durable habitat only if delivery remains repeatable and Carrier Fit stays healthy.

### Example O: Repeat As A Favor

- Relevant quest: one buyer repeat after trial
- Buyer response: pays again as a personal favor or courtesy
- Repeat Retention Reason: RELATIONSHIP-FAVOR
- Recommended Action: do not treat as market proof

Goodwill can be useful socially, but it should not be mistaken for durable market demand.

### Relationship Cost Example A: Visible Survival Cost Drag

- Old provider: 10,000 yen per repeated job
- New AI-enabled provider: equivalent output for 3,000 yen
- Reciprocal relationship value: old provider occasionally sends 50,000 yen/year of work
- Expected saving: 84,000 yen/year if the job repeats monthly
- Recommended interpretation: do not automatically switch; the old relationship now has visible Survival Cost Drag

Consider split routing, negotiation, or a proof trial before full replacement.

### Relationship Cost Example B: High Switching Damage Risk

- Old provider: deep trust, emergency support, and high referral value
- Switching Damage Risk: HIGH
- Recommended action: PROOF with split routing or negotiation, not full switch

Relationship value may justify keeping trust-heavy work with the incumbent while testing standardized work elsewhere.

### Relationship Cost Example C: Weak Reciprocal Value And Standardized Output

- Old provider: weak reciprocal value, high cost, slow delivery, and standardized output
- New provider: low trial friction and output equivalence
- Recommended action: PROOF or SHORT CYCLE depending on paid repeat and window lifespan

The operator should test the cheaper/faster route without treating it as automatic permission for broad replacement.

### Relationship Cost Example D: Regret Cost of Inaction

- Operator response: refuses to address cost drag until layoffs or closure become necessary
- Interpretation: this is Regret Cost of Inaction
- Recommended action: surface the risk early, name offsets, and avoid passive inaction

The Quest Map should make survival pressure visible before the operator loses options.

### Cashflow Sensitivity Example A: Absorbable Relationship Cost

- Annual saving: 84,000 yen
- Company condition: profitable with enough buffer
- Actual Cashflow Sensitivity: LOW
- Recommended interpretation: relationship preservation may be acceptable if relationship value is real

The cost drag still should be named, but it does not force a survival action.

### Cashflow Sensitivity Example B: Thin-Margin Constraint

- Annual saving: 84,000 yen
- Company condition: thin-margin and unable to invest in necessary tools or marketing
- Actual Cashflow Sensitivity: MEDIUM / HIGH
- Recommended interpretation: do not ignore cost drag; consider split routing or negotiation

The same cost difference matters more when it blocks future options.

### Cashflow Sensitivity Example C: Survival-Relevant Drag

- Cost drag contributes to inability to pay staff, tax, rent, or debt
- Actual Cashflow Sensitivity: CRITICAL
- Recommended interpretation: Regret Cost of Inaction is HIGH; passive loyalty is not enough

A survival action is required before cost drag becomes payroll damage, runway loss, or closure.

### Cashflow Sensitivity Example D: Claimed Relationship Value

- Relationship value is claimed but not named
- Actual Cashflow Sensitivity: UNKNOWN
- Recommended interpretation: name the relationship value or test split routing

Do not assume the cost is harmless when sensitivity is unknown.

### Exposure Example A: Minor Tool Budget Exposure

- Annual cost drag: 84,000 yen
- Company condition: strong profit and cash buffer
- Exposure Severity: MINOR
- Exposure Anchor: tool budget or general overhead
- Recommended interpretation: relationship preservation may be acceptable if relationship value is real

The exposure is named, but it does not force a survival action.

### Exposure Example B: Option-Limiting Budget Exposure

- Annual cost drag: 84,000 yen
- Company condition: thin-margin and unable to fund marketing or AI tools
- Exposure Severity: OPTION-LIMITING
- Exposure Anchor: marketing budget / tool budget / investment capacity
- Recommended interpretation: passive loyalty requires an offset plan

The cost drag matters because it consumes future options.

### Exposure Example C: Survival-Relevant Obligation Exposure

- Annual cost drag contributes to payroll, rent, or tax stress
- Exposure Severity: SURVIVAL-RELEVANT or CRITICAL
- Exposure Anchor: payroll / rent / tax reserve / owner runway
- Recommended interpretation: Regret Cost of Inaction is HIGH

Use split routing, negotiation, scope reduction, or another survival action.

### Exposure Example D: Unknown Exposure

- Relationship value is claimed, but exposure is unknown
- Exposure Severity: UNKNOWN
- Recommended interpretation: do not assume the cost is harmless

Name the exposure anchor before accepting passive loyalty.

### Exposure Ratio Example A: Small Share Of Tool Budget

- Cost drag: 84,000 yen/year
- Exposure Anchor Amount: tool budget is 1,000,000 yen/year
- Exposure Ratio: 8.4%
- Exposure Ratio Band: SMALL / MEANINGFUL depending on context
- Recommended interpretation: relationship preservation may be acceptable if relationship value is real

The cost is visible, but the ratio may not require urgency when the anchor is healthy.

### Exposure Ratio Example B: Large Share Of Tool Budget

- Cost drag: 84,000 yen/year
- Exposure Anchor Amount: tool budget is 100,000 yen/year
- Exposure Ratio: 84%
- Exposure Ratio Band: LARGE
- Recommended interpretation: passive loyalty needs an offset plan or split-routing proof

The same absolute cost becomes much more decision-relevant when it consumes most of the anchor.

### Exposure Ratio Example C: Payroll Buffer Share

- Cost drag: 7,000 yen/month
- Exposure Anchor Amount: payroll buffer is 50,000 yen/month
- Exposure Ratio: 14%
- Exposure Ratio Band: MEANINGFUL
- Recommended interpretation: do not ignore; test split routing or name the offset plan

A modest absolute amount can matter when the buffer is narrow.

### Exposure Ratio Example D: Unknown Anchor Amount

- Cost drag: known
- Exposure Anchor Amount: unknown
- Exposure Ratio Quality: PARTIAL / UNKNOWN
- Recommended interpretation: name the anchor amount before treating the cost as safe

Unknown ratio should trigger measurement, not cold replacement.

### Relationship Value Example A: Partially Offsetting Returned Work

- Cost drag: 84,000 yen/year
- Reciprocal Value Amount: old provider returns about 50,000 yen/year in uncertain work
- Reciprocal Value Coverage Ratio: about 60%
- Relationship Value Coverage Band: PARTIALLY OFFSETS
- Recommended interpretation: do not cold switch; consider split routing or negotiation because relationship value exists but may not fully offset cost drag

The relationship gives back real value, but the uncovered drag still needs a proof or offset plan.

### Relationship Value Example B: Fully Offsetting Relationship

- Cost drag: 84,000 yen/year
- Reciprocal Value Amount: old provider reliably sends 150,000 yen/year of work plus emergency support
- Relationship Value Coverage Band: FULLY OFFSETS
- Recommended interpretation: keeping may be reasonable if cashflow sensitivity is low and switching damage is meaningful

Strong reciprocal value can justify preserving the relationship when the cost remains survivable.

### Relationship Value Example C: Claimed But Unnamed Loyalty

- Cost drag: 84,000 yen/year
- Claimed relationship value: "we have known them for years"
- Relationship Value Quality: CLAIMED
- Recommended interpretation: name the actual value or run bounded split-routing proof

Do not let vague loyalty hide survival drag.

### Relationship Value Example D: Qualitative Trust Value

- Reciprocal value: local reputation protection and emergency support that cannot be monetized easily
- Relationship Value Coverage Band: QUALITATIVE ONLY
- Recommended interpretation: preserve relationship-heavy work, but still test standardized repeat work if cost drag is meaningful

Qualitative value should be named and protected, not treated as either zero or infinite.

### Relationship Damage Example A: Professional Provider

- Existing provider: professional and commonly works alongside other vendors
- Relationship Damage Severity: LOW
- Recommended interpretation: split routing may be safe if output equivalence and cost drag justify proof

Use a bounded test rather than treating split routing as automatic permission to replace the relationship.

### Relationship Damage Example B: Referral-Sensitive Provider

- Existing provider: sends referrals and may reduce them if they feel bypassed
- Relationship Damage Severity: HIGH
- Recommended interpretation: do not casually split-route

Use negotiation, scope separation, or protected proof before visible routing changes.

### Relationship Damage Example C: Essential Local Support

- Existing provider: essential to local reputation and emergency support
- Relationship Damage Severity: CRITICAL
- Recommended interpretation: only consider split routing if survival exposure is serious and mitigation is named

Protect relationship-heavy work unless survival pressure makes a bounded mitigation plan necessary.

### Relationship Damage Example D: Unknown Reaction

- Existing provider: reaction to partial routing is unknown
- Relationship Damage Severity: UNKNOWN
- Recommended interpretation: do not assume split routing is safe

Name likely damage channels before acting.

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
- Do not recommend LAUNCH without at least PARTIAL Paid Repeat Signal.
- Do not move from PROOF to LAUNCH unless Paid Repeat Signal, Output Equivalence, Payment / Revenue Capture, Operator Fit, and Carrier Fit are all strong enough.
- If Repeat Frequency is HIGH but Paid Repeat Signal is NONE or UNKNOWN, remain at PROOF or HOLD.
- If Paid Repeat Signal is STRONG but Window Lifespan is short, consider SHORT CYCLE rather than long-term habitat.
- If Paid Repeat Signal is STRONG and Window Lifespan is long, consider INCUBATE or LAUNCH depending on Carrier Fit and Enemy Strength.
- Paid Repeat Signal should not override Reference Chart Quality. Strong-looking repeat interest from a weak or overly broad chart must lower confidence.
- Free trial satisfaction is not the same as Paid Repeat Signal.
- Paid Repeat Signal is stronger when the Repeat Retention Reason is PRICE + SPEED + OUTPUT EQUIVALENCE + WORKFLOW FIT.
- TRUST strengthens long-term habitat only if delivery remains repeatable and Carrier Fit is healthy.
- URGENCY can justify SHORT CYCLE if the window is short, or INCUBATE if the workflow repeats long-term.
- NO BETTER ALTERNATIVE can support PROOF or INCUBATE, but should be rechecked because alternatives may appear.
- RELATIONSHIP / FAVOR should not justify LAUNCH.
- DISCOUNT-ONLY should not justify LAUNCH and may indicate weak Payment / Revenue Capture.
- UNKNOWN should keep the quest at PROOF or HOLD.
- Do not move from PROOF to LAUNCH only because a buyer paid again; require a retention reason that can repeat beyond one buyer.
- Repeat Retention Reason must be considered with Repeat Frequency, Paid Repeat Signal, Carrier Fit, Enemy Strength, and Reference Chart Quality.
- Do not recommend full switching only because a cheaper provider exists.
- If Reciprocal Relationship Value is high, consider split routing or negotiation before replacement.
- If Survival Cost Drag is high and Regret Cost of Inaction is high, do not allow "relationship" to hide the survival risk.
- If Net Switching Delta favors switching but Switching Damage Risk is high, recommend split routing or bounded trial.
- If Split Routing Option exists, prefer it before full replacement when relationship value is meaningful.
- If a company keeps the old relationship despite clear cost drag, the card should name what must offset that cost: increased sales, reciprocal work, price negotiation, scope reduction, or other cost savings.
- If the operator cannot offset the cost drag, recommend PROOF / HOLD / split routing rather than passive inaction.
- Relationship preservation is valid only when the cost remains survivable or is offset by named value.
- Do not treat Survival Cost Drag as LOW unless Actual Cashflow Sensitivity is LOW or directly named.
- If Actual Cashflow Sensitivity is UNKNOWN, avoid passive inaction. Recommend naming the cashflow sensitivity, running a bounded proof, or split routing.
- If Actual Cashflow Sensitivity is HIGH or CRITICAL, Regret Cost of Inaction should increase unless the relationship value clearly offsets the cost.
- If Reciprocal Relationship Value is high but Actual Cashflow Sensitivity is HIGH, recommend negotiation, split routing, scope reduction, or explicit offset planning.
- If Net Switching Delta favors keeping but Actual Cashflow Sensitivity is HIGH, require a named offset plan.
- If cost drag threatens payroll, runway, or survival, the decision becomes survival-relevant, not merely preference-relevant.
- If Actual Cashflow Sensitivity is HIGH or CRITICAL, Quantified Runway / Payroll Exposure should be named before passive loyalty is accepted.
- If Exposure Severity is UNKNOWN, recommend naming the exposure anchor, split routing, negotiation, or bounded proof.
- If Exposure Severity is OPTION-LIMITING, require a Required Offset Plan before maintaining the old cost unchanged.
- If Exposure Severity is SURVIVAL-RELEVANT or CRITICAL, Regret Cost of Inaction should be HIGH unless there is a named offset or strong reciprocal relationship value.
- If Reciprocal Relationship Value is high but Exposure Severity is SURVIVAL-RELEVANT, recommend negotiation, split routing, scope reduction, or explicit offset planning.
- If Exposure Anchor is only vague, lower confidence.
- Do not turn an unknown exposure into a switching recommendation. Unknown exposure should trigger measurement, not cold replacement.
- If Exposure Ratio is UNKNOWN, do not treat the cost drag as harmless.
- If Exposure Ratio Band is MEANINGFUL or higher, Required Offset Plan should not be NONE.
- If Exposure Ratio Band is LARGE or CRITICAL, Regret Cost of Inaction should rise unless there is strong named reciprocal relationship value or a clear offset plan.
- If Exposure Ratio Quality is PARTIAL or UNKNOWN, lower confidence and recommend naming the anchor amount before stronger action.
- If cost drag is small in absolute amount but large relative to the exposure anchor, do not dismiss it.
- If cost drag is large in absolute amount but small relative to healthy cashflow, avoid unnecessary urgency.
- Exposure Ratio must be considered with Reciprocal Relationship Value, Switching Damage Risk, Split Routing Option, Carrier Fit, and Reference Chart Quality.
- Do not recommend cold replacement from Exposure Ratio alone. Use it to judge urgency, offset planning, and proof priority.
- Do not treat relationship value as zero just because it is hard to quantify.
- Do not treat relationship value as infinite just because it is emotionally important.
- If Relationship Value Quality is CLAIMED or UNKNOWN, do not use it to justify passive inaction under high cost drag.
- If Relationship Value Coverage is FULLY OFFSETS and Actual Cashflow Sensitivity is LOW, keeping may be reasonable.
- If Relationship Value Coverage is PARTIALLY OFFSETS and Exposure Ratio is MEANINGFUL or higher, prefer split routing, negotiation, or explicit offset planning.
- If Relationship Value Coverage DOES NOT OFFSET and Survival Cost Drag is HIGH, Regret Cost of Inaction should rise.
- If Relationship Value is QUALITATIVE ONLY, the card should name the qualitative value and avoid cold replacement.
- Relationship Value Coverage must be considered with Switching Damage Risk, Exposure Ratio, Survival Threshold, Carrier Fit, and Split Routing Option.
- Do not recommend full replacement from Relationship Value Coverage alone.
- Prefer relationship-preserving decomposition when relationship value is meaningful but cost drag is also real.
- Do not treat Split Routing Option as safe if Relationship Damage Severity is HIGH, CRITICAL, or UNKNOWN.
- If Relationship Damage Severity is LOW or MEDIUM, bounded split routing may be appropriate if cost drag is meaningful.
- If Relationship Damage Severity is HIGH, prefer negotiation, scope separation, or carefully protected proof before split routing.
- If Relationship Damage Severity is CRITICAL, do not recommend split routing unless Survival Threshold is NEAR/BREACHED and a damage mitigation plan exists.
- If Relationship Damage Severity is UNKNOWN, recommend naming the damage channel before acting.
- If Relationship Value Coverage is FULLY OFFSETS and Relationship Damage Severity is HIGH/CRITICAL, HOLD may be appropriate.
- If Survival Cost Drag is HIGH but Relationship Damage Severity is HIGH, recommend survival-bounded negotiation or protected proof, not passive inaction and not cold replacement.
- Relationship Damage Severity must be considered with Relationship Value Coverage, Exposure Ratio, Actual Cashflow Sensitivity, Switching Damage Risk, and Carrier Fit.
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
- survival_cost_drag
- actual_cashflow_sensitivity
- survival_threshold
- cashflow_sensitivity_note
- required_offset_plan
- quantified_runway_payroll_exposure
- exposure_anchor
- exposure_severity
- exposure_note
- exposure_amount
- exposure_anchor_amount
- exposure_ratio
- exposure_ratio_quality
- exposure_ratio_band
- exposure_ratio_note
- regret_cost_of_inaction
- reciprocal_relationship_value
- reciprocal_value_amount
- reciprocal_value_coverage_ratio
- relationship_value_quality
- relationship_value_coverage_band
- relationship_value_note
- relationship_damage_severity
- relationship_damage_quality
- relationship_damage_channels
- damage_mitigation_option
- damage_mitigation_note
- net_switching_delta
- switching_damage_risk
- split_routing_option
- relationship_preserving_displacement_note
- repeat_frequency_order_volume
- repeat_frequency_note
- paid_repeat_signal
- paid_repeat_note
- repeat_retention_reason
- repeat_retention_note
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
- Survival Cost Drag: LOW / MEDIUM / HIGH / UNKNOWN
- Actual Cashflow Sensitivity: LOW / MEDIUM / HIGH / CRITICAL / UNKNOWN
- Survival Threshold: NOT NEAR / APPROACHING / NEAR / BREACHED / UNKNOWN
- Cashflow Sensitivity Note: one sentence explaining whether the cost drag is absorbable, painful, survival-relevant, or unknown
- Required Offset Plan: NONE / NEGOTIATE / SPLIT ROUTING / INCREASE SALES / CUT OTHER COSTS / NAME RELATIONSHIP VALUE / UNKNOWN
- Quantified Runway / Payroll Exposure: NONE / MINOR / OPTION-LIMITING / SURVIVAL-RELEVANT / CRITICAL / UNKNOWN
- Exposure Anchor: payroll / rent / tax reserve / debt / tool budget / marketing budget / hiring / owner runway / emergency buffer / investment capacity / unknown
- Exposure Note: one sentence explaining what the cost drag actually affects
- Exposure Amount: monthly / annual / unknown
- Exposure Anchor Amount: known amount / estimated amount / unknown
- Exposure Ratio: percentage or qualitative ratio / unknown
- Exposure Ratio Quality: DIRECT / ESTIMATED / PARTIAL / UNKNOWN
- Exposure Ratio Band: NEGLIGIBLE / SMALL / MEANINGFUL / LARGE / CRITICAL / UNKNOWN
- Exposure Ratio Note: one sentence explaining whether the drag is small, meaningful, large, critical, or unknown relative to the named anchor
- Regret Cost of Inaction: LOW / MEDIUM / HIGH / UNKNOWN
- Reciprocal Relationship Value: LOW / MEDIUM / HIGH / UNKNOWN
- Reciprocal Value Amount: amount / qualitative value / unknown
- Reciprocal Value Coverage Ratio: percentage / qualitative / unknown
- Relationship Value Quality: DIRECT / ESTIMATED / QUALITATIVE / CLAIMED / UNKNOWN
- Relationship Value Coverage Band: FULLY OFFSETS / PARTIALLY OFFSETS / DOES NOT OFFSET / QUALITATIVE ONLY / UNKNOWN
- Relationship Value Note: one sentence explaining what the relationship gives back and whether it offsets the visible cost drag
- Relationship Damage Severity: LOW / MEDIUM / HIGH / CRITICAL / UNKNOWN
- Relationship Damage Quality: DIRECT / ESTIMATED / QUALITATIVE / UNKNOWN
- Relationship Damage Channels: referrals / returned work / emergency support / reputation / local network / pricing priority / cooperation / hidden services / emotional conflict / operational disruption / unknown
- Damage Mitigation Option: YES / NO / UNKNOWN
- Damage Mitigation Note: one sentence explaining how split routing or proof can be done without unnecessary relationship damage
- Net Switching Delta: FAVOR KEEPING / FAVOR SPLIT ROUTING / FAVOR SWITCHING / UNKNOWN
- Switching Damage Risk: LOW / MEDIUM / HIGH / UNKNOWN
- Split Routing Option: YES / NO / UNKNOWN
- Relationship-Preserving Displacement Note: one sentence explaining whether the old relationship can be preserved while standardized work is partially moved
- Repeat Frequency / Order Volume
- Repeat Frequency Note
- Paid Repeat Signal
- Paid Repeat Note
- Repeat Retention Reason: PRICE / SPEED / OUTPUT EQUIVALENCE / TRUST / URGENCY / NO BETTER ALTERNATIVE / WORKFLOW FIT / RELATIONSHIP-FAVOR / DISCOUNT-ONLY / UNKNOWN
- Repeat Retention Note: one sentence explaining why the buyer repeated and whether that reason can generalize
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

Quest Map Layer now evaluates whether split routing itself may damage the existing relationship by adding Relationship Damage Severity, Relationship Damage Quality, Relationship Damage Channels, Damage Mitigation Option, and Damage Mitigation Note.
