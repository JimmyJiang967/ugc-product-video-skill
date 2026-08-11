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

## Community edition boundary

The public repository contains the reusable methodology, provider-neutral capability contracts, deterministic validators, and original test fixtures. It does not contain customer briefs, private platform integrations, paid customer assets, production credentials, or customer-specific tuning.

This project is not affiliated with or endorsed by CapCut, Xiaohongshu, TikTok, or any video-generation provider.

## Validation status

The included Skill structure, Python validators, positive fixtures, and negative regression checks are validated locally. Direct end-to-end acceptance in any live video-generation platform is still pending and depends on the adapters available in that environment.

