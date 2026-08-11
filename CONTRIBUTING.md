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

By contributing, you confirm that you have the right to submit the contribution. You license the contribution under the repository's PolyForm Noncommercial License 1.0.0 and grant the project owner a perpetual, worldwide, non-exclusive, royalty-free right to use, modify, sublicense, and distribute the contribution, including under separate commercial license terms.
