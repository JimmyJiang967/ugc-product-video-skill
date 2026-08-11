# Evidence-Led UGC Product Video Skill

[简体中文](README.zh-CN.md) | [Repository overview](README.md)

## What it does

This community Skill helps an AI agent turn authorized product images and verified selling points into one economical, truthful, presenter-led UGC product-video workflow. The default output is a 15-second vertical video with:

- product analysis before choreography;
- two or three genuinely different demonstration options;
- user-selected direct-demo or unboxing-to-use structure;
- one four-panel state sheet for story continuity;
- category-appropriate actions selected by evidence strength;
- one synchronized on-camera spoken performance;
- captions derived from the final media's real ASR timing;
- deterministic plan and result validation.

The Skill is provider-neutral. It describes required capabilities and acceptance criteria without depending on one vendor's tool names, model IDs, credit system, or private APIs.

## Why evidence-led

A product resemblance is not proof of a button, mode, material, performance result, or safe operation. The workflow routes every fact through one of four evidence modes:

| Route | Use when | Allowed demonstration |
| --- | --- | --- |
| `mechanism_led` | Exact control location and operation are confirmed | Show the precise operation and observable result |
| `state_led` | Intended state is confirmed without an unknown control | Show wear, fit, placement, loading, or another confirmed state |
| `effect_led` | The function is confirmed but its control is unknown | Show a restrained observable effect without touching a guessed control |
| `appearance_led` | Only visible appearance is confirmed | Show shape, texture, finish, color, or supported details only |

This keeps the video useful without inventing product behavior.

## Inputs

Required:

- at least one authorized product image;
- product name or neutral descriptor;
- one to three confirmed facts or selling points;
- permission to use every supplied image, logo, voice, likeness, and package design.

Optional:

- an authorized presenter image or recording;
- official product material and missing product views;
- audience, target market, spoken language, tone, CTA, story-mode preference;
- provider adapter and a user-approved budget ceiling.

## Workflow

1. Separate confirmed facts, visible features, unknowns, and prohibited claims.
2. Propose two or three feasible demonstration strategies and record their proof basis and tradeoffs.
3. Confirm presenter choice, story mode, scene, and budget before any paid call.
4. Build one 2×2 state sheet covering hook, proof, supporting evidence, and actual use/result.
5. Create one continuous 15-second performance with integrated speech where supported.
6. Review the playable draft, apply the smallest correction, then generate captions from final-media ASR.
7. Watch the final result and validate both the plan and result manifests.

## Installation

Import or copy [`create-evidence-led-ugc-product-video`](create-evidence-led-ugc-product-video/) into the Skills directory supported by your AI-agent runtime. The folder contains the required `SKILL.md`, UI metadata, references, and scripts.

Example invocation:

```text
Use $create-evidence-led-ugc-product-video with my authorized product image. The confirmed facts are [facts]. The target audience is [audience], the spoken language is [language], and the maximum budget is [budget].
```

The agent should stop before a paid generation when no quote is available, the quote exceeds the approved ceiling, a required operation is unsupported, or joint spoken performance is unavailable.

## Validation

```bash
python3 create-evidence-led-ugc-product-video/scripts/validate_ugc_plan.py examples/apparel/plan.json
python3 create-evidence-led-ugc-product-video/scripts/validate_ugc_plan.py examples/wearable-device/plan.json
python3 create-evidence-led-ugc-product-video/scripts/validate_ugc_plan.py examples/personal-care/plan.json
python3 create-evidence-led-ugc-product-video/scripts/validate_ugc_result.py examples/apparel/result.json
```

The repository also includes negative regressions that must fail:

```bash
python3 tests/run_tests.py
```

## What is not included

- private customer briefs, SOPs, screenshots, or delivery documents;
- customer or third-party product images and test videos;
- vendor-specific paid-generation adapters or credentials;
- guaranteed control over a provider's voice, face, lipsync, product fidelity, ASR, or cost;
- a claim that local schema validation equals live-platform audiovisual acceptance.

See [THIRD_PARTY_ASSETS.md](THIRD_PARTY_ASSETS.md) before adding media.

## License

Apache License 2.0 permits commercial use, modification, patent use, distribution, and private use subject to its conditions. Preserve the license and notices when redistributing modified or unmodified copies. The license does not grant rights to third-party assets, customer materials, platform trademarks, or personal likenesses.

See [LICENSE](LICENSE), [NOTICE](NOTICE), and [CONTRIBUTING.md](CONTRIBUTING.md).

## Project status

The Skill structure, validators, and bundled fixtures are tested locally. Live video quality, paid-call behavior, lipsync, ASR accuracy, and final rendering must be validated in each target platform. Direct end-to-end acceptance in a live platform is still pending.

