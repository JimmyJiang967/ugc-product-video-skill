#!/usr/bin/env python3
"""Run positive fixtures and targeted negative regressions without dependencies."""

from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
from types import ModuleType


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "ugc-product-video"


def module(name: str, path: Path) -> ModuleType:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded


plan_validator = module("plan_validator", SKILL / "scripts" / "validate_ugc_plan.py")
result_validator = module("result_validator", SKILL / "scripts" / "validate_ugc_result.py")


def read(relative: str) -> dict:
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def expect_pass(label: str, errors: list[str]) -> None:
    if errors:
        raise AssertionError(f"{label} should pass:\n" + "\n".join(errors))
    print(f"PASS {label}")


def expect_fail(label: str, errors: list[str], contains: str) -> None:
    if not errors:
        raise AssertionError(f"{label} should fail")
    if not any(contains in error for error in errors):
        raise AssertionError(f"{label} failed for the wrong reason: {errors}")
    print(f"PASS {label} rejected")


def main() -> int:
    apparel = read("examples/apparel/plan.json")
    wearable = read("examples/wearable-device/plan.json")
    care = read("examples/personal-care/plan.json")
    result = read("examples/apparel/result.json")

    expect_pass("apparel plan", plan_validator.validate(apparel))
    expect_pass("wearable-device plan", plan_validator.validate(wearable))
    expect_pass("personal-care plan", plan_validator.validate(care))
    expect_pass("reviewed result manifest", result_validator.validate(result))

    guessed_control = copy.deepcopy(wearable)
    guessed_control["demonstration"]["ledger"][1]["precise_control_action"] = True
    expect_fail("unknown-control regression", plan_validator.validate(guessed_control), "effect_led cannot use a precise control")

    early_caption = copy.deepcopy(apparel)
    early_caption["captions"]["max_card_lead_seconds"] = 0.3
    expect_fail("early-caption regression", plan_validator.validate(early_caption), "must be at most 0.05")

    duplicate_action = copy.deepcopy(apparel)
    duplicate_action["demonstration"]["action_families"] = ["hold", "hold", "hold"]
    expect_fail("repetitive-action regression", plan_validator.validate(duplicate_action), "three distinct")

    unapproved_overage = copy.deepcopy(care)
    unapproved_overage["budget"]["estimated_total"] = 300
    expect_fail("budget-overage regression", plan_validator.validate(unapproved_overage), "exceeds ceiling")

    script_caption = copy.deepcopy(result)
    script_caption["captions"]["script_used_as_transcript"] = True
    expect_fail("script-caption regression", result_validator.validate(script_caption), "must be false")

    frozen_tail = copy.deepcopy(result)
    frozen_tail["frozen_tail_seconds"] = 2.0
    expect_fail("frozen-tail regression", result_validator.validate(frozen_tail), "at most 0.25")

    print("PASS all community tests")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
