#!/usr/bin/env python3
"""Validate the human review manifest for a completed community UGC result."""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path
from typing import Any


TRUE_CHECKS = (
    "final_media_playable",
    "single_continuous_video",
    "selected_story_mode_matches",
    "one_target_product_unit",
    "no_product_duplication",
    "structural_integrity_pass",
    "product_fidelity_pass",
    "presenter_identity_pass",
    "presenter_choice_matches",
    "scene_context_pass",
    "three_action_families_pass",
    "hero_action_present",
    "final_use_result_pass",
    "purposeful_moving_ending_pass",
    "facts_and_claims_pass",
    "rights_pass",
    "speech_route_evidenced",
    "no_detached_narration",
    "voice_reviewed_with_music_muted",
    "voice_not_announcer_like",
    "mouth_gesture_action_sync_pass",
    "final_media_asr_used",
    "caption_first_word_onset_pass",
    "caption_no_future_text_exposure",
    "caption_max_two_lines",
    "caption_safe_area_pass",
    "caption_subject_avoidance_pass",
    "caption_full_readback_pass",
    "cost_reconciled",
    "full_video_watch_completed",
    "live_platform_acceptance_separate",
)


def load(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"result manifest not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid JSON at {exc.lineno}:{exc.colno}: {exc.msg}") from exc
    if not isinstance(value, dict):
        raise ValueError("top-level JSON value must be an object")
    return value


def number(value: Any, field: str, errors: list[str]) -> float | None:
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        errors.append(f"{field} must be a finite number")
        return None
    return float(value)


def nonempty(value: Any, field: str, errors: list[str]) -> None:
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{field} must be a non-empty string")


def validate(result: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if result.get("schema_version") != "community-1.0-result":
        errors.append('schema_version must equal "community-1.0-result"')
    if result.get("story_mode") not in {"direct_demo", "unboxing_to_use"}:
        errors.append("story_mode must be direct_demo or unboxing_to_use")
    nonempty(result.get("final_media_path"), "final_media_path", errors)
    nonempty(result.get("video_adapter"), "video_adapter", errors)
    nonempty(result.get("asr_adapter"), "asr_adapter", errors)
    duration = number(result.get("duration_seconds"), "duration_seconds", errors)
    if duration is not None and not 14.5 <= duration <= 15.5:
        errors.append("duration_seconds must be within 14.5–15.5")
    use_result = number(result.get("actual_use_result_seconds"), "actual_use_result_seconds", errors)
    if use_result is not None and use_result < 3:
        errors.append("actual_use_result_seconds must be at least 3")
    frozen = number(result.get("frozen_tail_seconds"), "frozen_tail_seconds", errors)
    if frozen is not None and frozen > 0.25:
        errors.append("frozen_tail_seconds must be at most 0.25")
    families = result.get("actual_action_families")
    if not isinstance(families, list) or len(set(families)) < 3:
        errors.append("actual_action_families must contain at least three distinct values")

    speech = result.get("speech")
    if not isinstance(speech, dict):
        errors.append("speech must be an object")
        speech = {}
    if speech.get("route") not in {"joint_spoken_performance", "authorized_recording_lipsync"}:
        errors.append("speech.route is invalid")
    nonempty(speech.get("route_evidence"), "speech.route_evidence", errors)
    if speech.get("detached_voice_asset_created") is not False:
        errors.append("speech.detached_voice_asset_created must be false")

    captions = result.get("captions")
    if not isinstance(captions, dict):
        errors.append("captions must be an object")
        captions = {}
    expected = {
        "status": "rendered_dynamic_asr",
        "source": "final_media_asr",
        "timing_source": "word_level_asr",
        "segmentation": "word_timed_microphrases",
        "position_strategy": "adaptive_lower_center",
    }
    for field, value in expected.items():
        if captions.get(field) != value:
            errors.append(f'captions.{field} must equal "{value}"')
    nonempty(captions.get("caption_asset_path"), "captions.caption_asset_path", errors)
    if captions.get("script_used_as_transcript") is not False:
        errors.append("captions.script_used_as_transcript must be false")
    if captions.get("observed_max_lines") not in {1, 2}:
        errors.append("captions.observed_max_lines must be 1 or 2")
    lead = number(captions.get("maximum_card_lead_seconds_observed"), "captions.maximum_card_lead_seconds_observed", errors)
    if lead is not None and lead > 0.05:
        errors.append("captions.maximum_card_lead_seconds_observed must be at most 0.05")
    future = number(captions.get("maximum_future_word_lead_seconds_observed"), "captions.maximum_future_word_lead_seconds_observed", errors)
    if future is not None and future > 0.60:
        errors.append("captions.maximum_future_word_lead_seconds_observed must be at most 0.60")
    shortest = number(captions.get("shortest_card_seconds"), "captions.shortest_card_seconds", errors)
    longest = number(captions.get("longest_card_seconds"), "captions.longest_card_seconds", errors)
    if shortest is not None and shortest < 0.4:
        errors.append("captions.shortest_card_seconds must be at least 0.4")
    if longest is not None and longest > 1.8:
        errors.append("captions.longest_card_seconds must be at most 1.8")

    cost = result.get("cost")
    if not isinstance(cost, dict):
        errors.append("cost must be an object")
        cost = {}
    nonempty(cost.get("unit"), "cost.unit", errors)
    quoted = number(cost.get("quoted_total"), "cost.quoted_total", errors)
    actual = number(cost.get("actual_total"), "cost.actual_total", errors)
    ceiling = number(cost.get("approved_ceiling"), "cost.approved_ceiling", errors)
    if actual is not None and ceiling is not None and actual > ceiling and cost.get("overage_user_approved") is not True:
        errors.append("actual cost exceeds approved ceiling without approval")
    if quoted is not None and quoted < 0 or actual is not None and actual < 0:
        errors.append("cost values must be non-negative")

    checks = result.get("checks")
    if not isinstance(checks, dict):
        errors.append("checks must be an object")
        checks = {}
    for field in TRUE_CHECKS:
        if checks.get(field) is not True:
            errors.append(f"checks.{field} must be true")

    if result.get("live_platform_acceptance_status") not in {"pending", "passed", "failed"}:
        errors.append("live_platform_acceptance_status must be pending, passed, or failed")
    return errors


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(f"usage: {Path(argv[0]).name} RESULT.json", file=sys.stderr)
        return 2
    try:
        result = load(Path(argv[1]))
    except ValueError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    errors = validate(result)
    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("PASS: reviewed UGC result satisfies community-1.0-result")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

