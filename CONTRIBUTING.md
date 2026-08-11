# Contributing

Thank you for improving the community edition.

## Ground rules

- Submit reusable methods, not customer-specific prompts or private platform routes.
- Do not submit customer briefs, credentials, paid outputs, copyrighted test media, faces, voices, logos, or product images without explicit redistribution rights.
- Keep the core provider-neutral. Optional adapters should be isolated and clearly licensed.
- Preserve the evidence routes and never weaken claims, rights, cost, or final-media ASR safeguards.
- Add or update a reproducible fixture for behavior changes.
- Do not describe local validation as live-platform audiovisual acceptance.

## Before opening a pull request

Run:

```bash
python3 tests/run_tests.py
python3 /path/to/skill-creator/scripts/quick_validate.py ugc-product-video
```

Explain what changed, why it is reusable, which tests cover it, and any remaining live-platform validation gap.

By contributing, you agree that your contribution is licensed under Apache License 2.0 and that you have the right to submit it.
