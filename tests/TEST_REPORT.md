# Community Edition Local Test Report

## Scope

The community repository uses three differentiated, original fixtures:

1. Apparel — front-view fidelity, intact garment continuity, open-match casting, and worn-result ending.
2. Wearable device — confirmed effect with unknown controls, requiring `state_led` and `effect_led` evidence without a guessed button press.
3. Personal care — confirmed removable cap and pump mechanism, unboxing-to-use structure, and a safe external mist action.

## Reproducible inputs

Each case includes an original repository-owned SVG, a complete request, and a `community-1.0` plan manifest. The apparel case also includes a positive `community-1.0-result` review-manifest fixture.

## Automated checks

`tests/run_tests.py` validates all three positive plans and the positive result manifest. It also confirms rejection of:

- a guessed control under `effect_led` evidence;
- captions that appear too early;
- three repeated action families;
- an unapproved budget overage;
- script-derived captions;
- a frozen final tail.

## Validation boundary

These are deterministic schema and regression tests. The referenced output paths in the result fixture are illustrative and no example video is represented as a real render. Live video generation, lipsync, voice naturalness, product fidelity, final-media ASR accuracy, caption rendering, and full audiovisual review remain platform-specific end-to-end tests and are currently pending.

