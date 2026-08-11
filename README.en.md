# UGC Product Video Skill

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

## Real showcases

The following historical direct test outputs show the complete route from a product image to one 2×2 state sheet and one continuous 15-second video. They demonstrate the workflow; they are not quality benchmarks or guarantees for other providers.

GitHub READMEs do not embed repository MP4 files as native video players. The third column therefore uses an inline animated preview; click it to play the complete MP4 with sound and browser controls.

### Shoe · unboxing to on-foot result

Four states turn one product reference into an unboxing hook, close presentation, detail proof, and an on-foot ending.

<table>
  <tr><th>1 · Product image</th><th>2 · 2×2 state sheet</th><th>3 · Final video</th></tr>
  <tr>
    <td><a href="showcase/shoe/product.jpg"><img src="showcase/shoe/product-preview.jpg" width="220" alt="Shoe product input"></a></td>
    <td><a href="showcase/shoe/anchor-sheet.png"><img src="showcase/shoe/anchor-preview.jpg" width="220" alt="Shoe four-stage anchor sheet"></a></td>
    <td><a href="https://cdn.jsdelivr.net/gh/JimmyJiang967/ugc-product-video-skill@main/showcase/shoe/final-video.mp4"><img src="showcase/shoe/animated-preview.gif" width="220" alt="Animated preview of the shoe video"></a><br><a href="https://cdn.jsdelivr.net/gh/JimmyJiang967/ugc-product-video-skill@main/showcase/shoe/final-video.mp4">Play the full video with sound</a></td>
  </tr>
</table>

### Wearable device · worn state and effect proof

Because the product control was not confirmed, the sequence avoids a guessed button press and uses a restrained airflow proxy near visible vents.

<table>
  <tr><th>1 · Product image</th><th>2 · 2×2 state sheet</th><th>3 · Final video</th></tr>
  <tr>
    <td><a href="showcase/wearable-device/product.png"><img src="showcase/wearable-device/product-preview.jpg" width="220" alt="Wearable device product input"></a></td>
    <td><a href="showcase/wearable-device/anchor-sheet.png"><img src="showcase/wearable-device/anchor-preview.jpg" width="220" alt="Wearable device four-stage anchor sheet"></a></td>
    <td><a href="https://cdn.jsdelivr.net/gh/JimmyJiang967/ugc-product-video-skill@main/showcase/wearable-device/final-video.mp4"><img src="showcase/wearable-device/animated-preview.gif" width="220" alt="Animated preview of the wearable-device video"></a><br><a href="https://cdn.jsdelivr.net/gh/JimmyJiang967/ugc-product-video-skill@main/showcase/wearable-device/final-video.mp4">Play the full video with sound</a></td>
  </tr>
</table>

### Cardigan · visible details to worn result

The sequence uses a lived-in wardrobe setting, protects the garment's visible structure, and ends in a worn state without inventing material or comfort claims.

<table>
  <tr><th>1 · Product image</th><th>2 · 2×2 state sheet</th><th>3 · Final video</th></tr>
  <tr>
    <td><a href="showcase/cardigan/product.png"><img src="showcase/cardigan/product-preview.jpg" width="220" alt="Cardigan product input"></a></td>
    <td><a href="showcase/cardigan/anchor-sheet.png"><img src="showcase/cardigan/anchor-preview.jpg" width="220" alt="Cardigan four-stage anchor sheet"></a></td>
    <td><a href="https://cdn.jsdelivr.net/gh/JimmyJiang967/ugc-product-video-skill@main/showcase/cardigan/final-video.mp4"><img src="showcase/cardigan/animated-preview.gif" width="220" alt="Animated preview of the cardigan video"></a><br><a href="https://cdn.jsdelivr.net/gh/JimmyJiang967/ugc-product-video-skill@main/showcase/cardigan/final-video.mp4">Play the full video with sound</a></td>
  </tr>
</table>

See [showcase/README.md](showcase/README.md) for provenance, visible limitations, and separate media-rights terms. Permission to view the Showcase does not grant reuse rights to depicted products, trademarks, packaging, voices, or likenesses.

## Installation

Import or copy [`ugc-product-video`](ugc-product-video/) into the Skills directory supported by your AI-agent runtime. The folder contains the required `SKILL.md`, UI metadata, references, and scripts.

Example invocation:

```text
Use $ugc-product-video with my authorized product image. The confirmed facts are [facts]. The target audience is [audience], the spoken language is [language], and the maximum budget is [budget].
```

The agent should stop before a paid generation when no quote is available, the quote exceeds the approved ceiling, a required operation is unsupported, or joint spoken performance is unavailable.

## License and commercial use

The software and documentation in the current version are licensed under the [PolyForm Noncommercial License 1.0.0](LICENSE).

Allowed without a commercial license:

- personal learning, research, and testing;
- hobby projects and private experiments;
- noncommercial demonstrations and educational use covered by the license.

Separate written authorization is required for:

- client work, paid services, agency delivery, or commercial content production;
- advertising, affiliate marketing, product sales, or other revenue-generating use;
- batch production or operation intended to generate profit;
- internal use by a for-profit business;
- integration into a paid product, SaaS, API, template, workflow, or managed service;
- selling, sublicensing, or commercially redistributing this Skill or a modified version.

See [COMMERCIAL_LICENSE.md](COMMERCIAL_LICENSE.md) for practical examples and the authorization route. This is a source-available project, not an OSI-approved open-source project.

Third-party product images, trademarks, packaging, voices, likenesses, and Showcase media remain subject to their own rights. See [THIRD_PARTY_ASSETS.md](THIRD_PARTY_ASSETS.md).
