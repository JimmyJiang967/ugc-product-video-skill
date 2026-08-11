---
name: create-evidence-led-ugc-product-video
description: Create a truthful, economical, presenter-led 15-second vertical UGC product-video plan and finished-video review from authorized product images and verified facts. Use for direct-to-camera product demonstrations, unboxing-to-use videos, creator-style feature introductions, wearable or apparel showcases, talking-presenter ads, four-stage anchor sheets, synchronized spoken performance, and dynamic captions derived from final-media ASR. Use when product actions must adapt to the evidence instead of relying on hard-coded category recipes or guessed controls.
---

# Create an Evidence-Led UGC Product Video

Turn authorized product visuals and verified facts into one continuous, provider-neutral 9:16 UGC product-video workflow. Default to 15 seconds, one presenter, one target product unit, one four-panel state sheet, one video generation, and final-media ASR captions.

## Positioning

Produce a practical creative plan and, when the runtime provides the required capabilities, one finished playable video. Do not claim that a plan, schema pass, or local validator proves live-platform audiovisual quality.

Do not:

- invent product functions, controls, specifications, materials, performance, endorsement, ownership, or personal experience;
- hard-code actions by product category;
- create detached AI narration for a visible talking presenter;
- generate subtitles from the draft script;
- duplicate the target product, detach unsupported parts, or reveal unsupported surfaces;
- spend money without a quote and explicit user approval;
- expose customer materials, private adapters, credentials, or unlicensed media.

## Inputs

Require:

- one or more authorized product images;
- a product name or neutral descriptor;
- one to three confirmed facts or selling points;
- confirmation that supplied images, logos, voices, likenesses, and packaging may be used.

Accept optionally:

- an authorized presenter image or recording;
- official product material and missing product views;
- target audience, market, language, tone, CTA, story preference, and casting preference;
- a provider adapter and an approved cost ceiling.

Keep the conversation language separate from the video's spoken language.

## Workflow

### 1. Audit rights and evidence

Read `references/safety-and-rights.md`. Separate:

- user-confirmed facts;
- visible features supported by supplied views;
- unsupported or ambiguous operations;
- prohibited claims and missing rights.

Stop when a required asset lacks permission or the requested demonstration would be unsafe or deceptive.

### 2. Analyze the product before choosing actions

Read `references/evidence-and-actions.md`.

For every selected fact, determine the strongest truthful evidence route:

- `mechanism_led`: exact control location and operation are confirmed;
- `state_led`: intended state is confirmed without relying on an unknown control;
- `effect_led`: function is confirmed but its control or sequence is unknown;
- `appearance_led`: only visible appearance is confirmed.

Infer candidate demonstrations, never product facts. Allow a precise press, twist, open, spray, attach, or switch only for `mechanism_led` evidence with confirmed operation.

### 3. Propose strategies and obtain one compact choice

Propose two or three materially different, feasible strategies in the conversation language. For each, state:

- its four-stage action arc;
- category-defining hero action;
- facts demonstrated and evidence routes;
- unsupported operations omitted;
- creative and proof tradeoff.

When only one safe route exists, explain why alternatives are unsupported and ask for approval of that route. For product-only input, also ask for `adult_male_presenting`, `adult_female_presenting`, or `open_match`; never infer gender, ethnicity, or nationality from the product category.

### 4. Confirm story, scene, and economics

Read `references/budget-and-adapters.md`.

Offer exactly two default story modes:

- `direct_demo`: presenter begins with the product and demonstrates it immediately;
- `unboxing_to_use`: presenter reveals the product from supplied or explicitly approved generic packaging, then uses it.

Default to a lived-in, category-appropriate environment with depth and ordinary context. Use a blank wall, seamless studio, or ecommerce sweep only when the user selects it.

Inspect provider capabilities and obtain an actual quote without spending. Default to at most one paid state-sheet generation and one paid video generation. Stop before payment when the quote is absent, exceeds the approved ceiling, or the provider cannot produce one continuous synchronized spoken performance.

### 5. Build one four-panel state sheet

Read `references/fidelity-presenter-and-scene.md`.

Create one 2×2 composite containing four distinct states:

- `direct_demo`: category hook → primary feature action → supporting evidence → actual use/result;
- `unboxing_to_use`: package setup → product reveal → feature action → actual use/result.

Require one target-product inventory, supported views, consistent presenter identity, correct human/product scale, stable structure, plausible grip, lived-in scene continuity, and at least three action families. Make the final use/result state last at least three seconds in the video.

Show the sheet for approval before any paid video generation. Do not animate the literal collage; use its individual states as continuity anchors.

### 6. Write and direct one synchronized performance

Read `references/speech-and-captions.md`.

Use one connected thought rather than a feature list. For English, target roughly 22–32 spoken words in 15 seconds. Bind each spoken fact to its visible action. Include one motivated 0.25–0.45 second pause and a purposeful, moving ending.

Generate speech as part of the visible performance when supported, or use an authorized recording to drive the visible mouth. Do not generate a separate voiceover for a talking presenter. Judge naturalness in the returned video with music muted.

### 7. Validate the plan before generation

Create a `community-1.0` JSON plan using the field contract demonstrated in the repository examples. Run:

```bash
python3 scripts/validate_ugc_plan.py <plan.json>
```

Resolve every error before paid media generation. A validator pass confirms the manifest contract only.

### 8. Generate, inspect, and fix economically

Prefer one continuous 15-second generation. Record job IDs and require a playable terminal result; progress percentages are not completion.

Watch the entire draft and inspect product fidelity, inventory, scene, action rhythm, ending motion, speech naturalness, mouth/action synchronization, facts, rights, and actual cost. Apply the smallest affected-layer fix. Do not buy another video generation without a new quote and explicit approval.

### 9. Produce captions from final-media ASR

After the final spoken video and final mix exist, use any available real-ASR adapter on that final media or its unchanged final speech track. Require word-level timestamps or derive them from the unchanged final speech before segmentation.

Use `word_timed_microphrases`:

- start each card no more than 0.05 seconds before its first audible word;
- do not reveal a word whose spoken start is more than 0.60 seconds after the card appears;
- split on meaning and pauses, usually 2–6 English words per card;
- use at most two lines and adaptive lower-center placement;
- avoid the product, visible mouth, hands, hero action, and platform UI.

Never use the draft script as the transcript or timing source. If reliable ASR is unavailable, disclose an uncaptioned partial result or obtain approval for another real-ASR adapter.

### 10. Review and deliver

Create a `community-1.0-result` JSON review manifest and run:

```bash
python3 scripts/validate_ugc_result.py <result.json>
```

Watch the final result at normal speed and with music muted. Deliver one playable result plus a concise summary of verified facts, selected strategy, adapter route, actual cost when exposed, checks passed, limitations, and whether live-platform acceptance remains pending.

## Output Contract

Return:

1. one approved product analysis and selected strategy;
2. one approved 2×2 state sheet or a truthful explanation of why generation stopped;
3. one continuous 15-second vertical video when the runtime supports it;
4. final-media ASR captions when reliable timing is available;
5. the plan and result manifests;
6. explicit cost, rights, tool-failure, and live-platform validation boundaries.

## Final Self-Check

Reject or stop when:

- any claim lacks evidence;
- a precise operation uses a guessed control;
- three stages repeat holding, pointing, or inspection;
- the final state is not actual use/result for a usable product;
- the presenter or target product duplicates or changes identity;
- the scene defaults to a blank wall without user choice;
- speech is detached, synthetic-sounding, or out of sync;
- subtitles precede speech or come from the script;
- a paid call lacks a quote or approval;
- a local pass is being presented as live-platform acceptance.

