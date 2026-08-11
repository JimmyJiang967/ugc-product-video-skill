# Evidence-Led UGC Product Video Skill

[English](README.en.md) | [简体中文](README.zh-CN.md)

An open, provider-neutral AI Skill for planning and reviewing truthful 15-second presenter-led UGC product videos. It turns authorized product visuals and verified facts into product-specific demonstration strategies, a four-stage visual plan, synchronized spoken performance, and final-media ASR captions.

This repository is licensed under [Apache License 2.0](LICENSE), including commercial use, modification, and redistribution subject to the license terms.

## Quick start

Install or import the folder [`create-evidence-led-ugc-product-video`](create-evidence-led-ugc-product-video/) into a compatible Skill runtime, then invoke:

```text
Use $create-evidence-led-ugc-product-video to analyze my authorized product image and verified facts, propose truthful demonstration strategies, and create a 15-second UGC product-video plan.
```

Run the local checks:

```bash
python3 create-evidence-led-ugc-product-video/scripts/validate_ugc_plan.py examples/apparel/plan.json
python3 create-evidence-led-ugc-product-video/scripts/validate_ugc_plan.py examples/wearable-device/plan.json
python3 create-evidence-led-ugc-product-video/scripts/validate_ugc_plan.py examples/personal-care/plan.json
python3 create-evidence-led-ugc-product-video/scripts/validate_ugc_result.py examples/apparel/result.json
```

## Real showcases

These historical direct test outputs show the complete workflow from one product image to a 2×2 state sheet and then a 15-second presenter-led video. They are included as workflow evidence, not as a benchmark or a guarantee of identical output in another provider.

### Shoe · unboxing to on-foot result

The sequence moves from a product-only reference to four planned states: unboxing, close presentation, detail proof, and an on-foot ending.

<table>
  <tr><th>1 · Product image</th><th>2 · 2×2 state sheet</th><th>3 · Final video</th></tr>
  <tr>
    <td><a href="showcase/shoe/product.jpg"><img src="showcase/shoe/product-preview.jpg" width="220" alt="Shoe product input"></a></td>
    <td><a href="showcase/shoe/anchor-sheet.png"><img src="showcase/shoe/anchor-preview.jpg" width="220" alt="Shoe four-stage anchor sheet"></a></td>
    <td><a href="showcase/shoe/final-video.mp4"><img src="showcase/shoe/final-video-preview.jpg" width="220" alt="Shoe final-video preview"></a><br><a href="showcase/shoe/final-video.mp4">Watch the 15-second video</a></td>
  </tr>
</table>

### Wearable device · wear state and restrained effect proof

When a function is confirmed but the control is not visible, the plan avoids inventing a button press and demonstrates the worn state plus a modest airflow proxy.

<table>
  <tr><th>1 · Product image</th><th>2 · 2×2 state sheet</th><th>3 · Final video</th></tr>
  <tr>
    <td><a href="showcase/wearable-device/product.png"><img src="showcase/wearable-device/product-preview.jpg" width="220" alt="Wearable device product input"></a></td>
    <td><a href="showcase/wearable-device/anchor-sheet.png"><img src="showcase/wearable-device/anchor-preview.jpg" width="220" alt="Wearable device four-stage anchor sheet"></a></td>
    <td><a href="showcase/wearable-device/final-video.mp4"><img src="showcase/wearable-device/final-video-preview.jpg" width="220" alt="Wearable device final-video preview"></a><br><a href="showcase/wearable-device/final-video.mp4">Watch the 15-second video</a></td>
  </tr>
</table>

### Cardigan · garment detail to worn result

The product image is translated into a lived-in wardrobe sequence that preserves visible garment details and ends in an actual worn state without claiming unverified material or comfort properties.

<table>
  <tr><th>1 · Product image</th><th>2 · 2×2 state sheet</th><th>3 · Final video</th></tr>
  <tr>
    <td><a href="showcase/cardigan/product.png"><img src="showcase/cardigan/product-preview.jpg" width="220" alt="Cardigan product input"></a></td>
    <td><a href="showcase/cardigan/anchor-sheet.png"><img src="showcase/cardigan/anchor-preview.jpg" width="220" alt="Cardigan four-stage anchor sheet"></a></td>
    <td><a href="showcase/cardigan/final-video.mp4"><img src="showcase/cardigan/final-video-preview.jpg" width="220" alt="Cardigan final-video preview"></a><br><a href="showcase/cardigan/final-video.mp4">Watch the 15-second video</a></td>
  </tr>
</table>

See [showcase/README.md](showcase/README.md) for provenance, limitations, and media-rights terms. The Showcase media is not licensed under Apache-2.0; permission to view it in this repository does not grant reuse rights to depicted products, trademarks, packaging, voices, or likenesses.

## Community edition boundary

The public repository contains the reusable methodology, provider-neutral capability contracts, deterministic validators, original test fixtures, and the explicitly authorized Showcase above. It does not contain customer briefs, private platform integrations, production credentials, or customer-specific tuning.

This project is not affiliated with or endorsed by CapCut, Xiaohongshu, TikTok, or any video-generation provider.

## Validation status

The included Skill structure, Python validators, positive fixtures, and negative regression checks are validated locally. Direct end-to-end acceptance in any live video-generation platform is still pending and depends on the adapters available in that environment.
