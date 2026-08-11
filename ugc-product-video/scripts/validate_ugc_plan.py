#!/usr/bin/env python3
"""Validate a provider-neutral community UGC production plan."""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path
from typing import Any


STORY_ROLES = {
    "direct_demo": ["category_hook", "primary_feature_action", "supporting_evidence", "use_result"],
    "unboxing_to_use": ["package_setup", "product_reveal", "feature_action", "use_result"],
}
EVIDENCE_ROUTES = {"mechanism_led", "state_led", "effect_led", "appearance_led"}
PRESENTER_CHOICES = {
    "adult_male_presenting",
    "adult_female_presenting",
    "open_match",
    "supplied_authorized_presenter",
}
SOURCES = {"user_confirmed", "visible_in_authorized_asset", "authorized_official_material"}


def load(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"plan not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid JSON at {exc.lineno}:{exc.colno}: {exc.msg}") from exc
    if not isinstance(value, dict):
        raise ValueError("top-level JSON value must be an object")
    return value


def object_(value: Any, field: str, errors: list[str]) -> dict[str, Any]:
    if not isinstance(value, dict):
        errors.append(f"{field} must be an object")
        return {}
    return value


def text(value: Any, field: str, errors: list[str]) -> str:
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{field} must be a non-empty string")
        return ""
    return value.strip()


def texts(value: Any, field: str, errors: list[str], *, minimum: int = 0) -> list[str]:
    if not isinstance(value, list) or not all(isinstance(item, str) and item.strip() for item in value):
        errors.append(f"{field} must be an array of non-empty strings")
        return []
    if len(value) < minimum:
        errors.append(f"{field} must contain at least {minimum} item(s)")
    return value


def number(value: Any, field: str, errors: list[str]) -> float | None:
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        errors.append(f"{field} must be a finite number")
        return None
    return float(value)


def validate(plan: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if plan.get("schema_version") != "community-1.0":
        errors.append('schema_version must equal "community-1.0"')

    product = object_(plan.get("product"), "product", errors)
    text(product.get("name"), "product.name", errors)
    assets = product.get("authorized_assets")
    if not isinstance(assets, list) or not assets:
        errors.append("product.authorized_assets must contain at least one asset")
        assets = []
    for index, asset in enumerate(assets):
        item = object_(asset, f"product.authorized_assets[{index}]", errors)
        text(item.get("id"), f"product.authorized_assets[{index}].id", errors)
        text(item.get("description"), f"product.authorized_assets[{index}].description", errors)
        if item.get("permission_confirmed") is not True:
            errors.append(f"product.authorized_assets[{index}].permission_confirmed must be true")

    facts = product.get("confirmed_facts")
    if not isinstance(facts, list) or not 1 <= len(facts) <= 3:
        errors.append("product.confirmed_facts must contain 1–3 facts")
        facts = []
    fact_ids: set[str] = set()
    for index, fact in enumerate(facts):
        item = object_(fact, f"product.confirmed_facts[{index}]", errors)
        fact_id = text(item.get("id"), f"product.confirmed_facts[{index}].id", errors)
        if fact_id in fact_ids:
            errors.append(f"product.confirmed_facts[{index}].id must be unique")
        fact_ids.add(fact_id)
        text(item.get("claim"), f"product.confirmed_facts[{index}].claim", errors)
        if item.get("source") not in SOURCES:
            errors.append(f"product.confirmed_facts[{index}].source must be one of {sorted(SOURCES)}")

    texts(product.get("visible_features"), "product.visible_features", errors, minimum=1)
    texts(product.get("unknowns"), "product.unknowns", errors)
    texts(product.get("prohibited_claims"), "product.prohibited_claims", errors)
    if product.get("analysis_completed_before_options") is not True:
        errors.append("product.analysis_completed_before_options must be true")

    creative = object_(plan.get("creative"), "creative", errors)
    story_mode = creative.get("story_mode")
    if story_mode not in STORY_ROLES:
        errors.append(f"creative.story_mode must be one of {sorted(STORY_ROLES)}")
    duration = number(creative.get("target_duration_seconds"), "creative.target_duration_seconds", errors)
    if duration is not None and abs(duration - 15.0) > 0.01:
        errors.append("creative.target_duration_seconds must equal 15")
    if creative.get("aspect_ratio") != "9:16":
        errors.append('creative.aspect_ratio must equal "9:16"')
    if creative.get("scene_mode") not in {"lived_in_ugc", "user_selected_studio"}:
        errors.append("creative.scene_mode must be lived_in_ugc or user_selected_studio")
    if creative.get("scene_mode") == "user_selected_studio" and creative.get("studio_user_selected") is not True:
        errors.append("user_selected_studio requires creative.studio_user_selected=true")
    if creative.get("scene_mode") == "lived_in_ugc" and creative.get("studio_user_selected") is not False:
        errors.append("lived_in_ugc requires creative.studio_user_selected=false")
    texts(creative.get("lived_in_context_cues"), "creative.lived_in_context_cues", errors, minimum=2)
    for field in ("conversation_language", "spoken_language", "target_market"):
        text(creative.get(field), f"creative.{field}", errors)

    input_mode = creative.get("presenter_input_mode")
    if input_mode not in {"product_only", "product_and_presenter"}:
        errors.append("creative.presenter_input_mode must be product_only or product_and_presenter")
    choice = creative.get("presenter_choice")
    if choice not in PRESENTER_CHOICES:
        errors.append(f"creative.presenter_choice must be one of {sorted(PRESENTER_CHOICES)}")
    if input_mode == "product_only":
        if choice == "supplied_authorized_presenter":
            errors.append("product_only cannot use supplied_authorized_presenter")
        if creative.get("presenter_choice_user_confirmed") is not True:
            errors.append("product_only requires presenter_choice_user_confirmed=true")
    if input_mode == "product_and_presenter" and choice != "supplied_authorized_presenter":
        errors.append("product_and_presenter must use supplied_authorized_presenter")
    if choice == "open_match" and not text(creative.get("open_match_basis"), "creative.open_match_basis", errors):
        pass
    if creative.get("no_category_stereotype_casting") is not True:
        errors.append("creative.no_category_stereotype_casting must be true")

    demo = object_(plan.get("demonstration"), "demonstration", errors)
    options = demo.get("options")
    only_safe = demo.get("only_one_safe_route")
    if only_safe not in {True, False}:
        errors.append("demonstration.only_one_safe_route must be boolean")
        only_safe = False
    if not isinstance(options, list):
        errors.append("demonstration.options must be an array")
        options = []
    expected_counts = {1} if only_safe else {2, 3}
    if len(options) not in expected_counts:
        errors.append("demonstration.options must contain 2–3 routes, or one documented safe route")
    option_ids: set[str] = set()
    for index, option in enumerate(options):
        item = object_(option, f"demonstration.options[{index}]", errors)
        option_id = text(item.get("id"), f"demonstration.options[{index}].id", errors)
        if option_id in option_ids:
            errors.append(f"demonstration.options[{index}].id must be unique")
        option_ids.add(option_id)
        for field in ("label", "four_stage_arc", "hero_action", "evidence_basis", "omitted_unknowns", "tradeoff"):
            text(item.get(field), f"demonstration.options[{index}].{field}", errors)
    selected = text(demo.get("selected_option_id"), "demonstration.selected_option_id", errors)
    if selected and selected not in option_ids:
        errors.append("demonstration.selected_option_id must match an option")
    if demo.get("selection_user_confirmed") is not True:
        errors.append("demonstration.selection_user_confirmed must be true")

    ledger = demo.get("ledger")
    if not isinstance(ledger, list) or not ledger:
        errors.append("demonstration.ledger must contain fact-action mappings")
        ledger = []
    ledger_ids: set[str] = set()
    for index, mapping in enumerate(ledger):
        item = object_(mapping, f"demonstration.ledger[{index}]", errors)
        mapping_id = text(item.get("id"), f"demonstration.ledger[{index}].id", errors)
        ledger_ids.add(mapping_id)
        if item.get("fact_id") not in fact_ids:
            errors.append(f"demonstration.ledger[{index}].fact_id must reference a confirmed fact")
        route = item.get("evidence_route")
        if route not in EVIDENCE_ROUTES:
            errors.append(f"demonstration.ledger[{index}].evidence_route must be one of {sorted(EVIDENCE_ROUTES)}")
        for field in ("action", "observable_response", "required_view", "safe_wording", "prohibited_implication"):
            text(item.get(field), f"demonstration.ledger[{index}].{field}", errors)
        precise = item.get("precise_control_action")
        if precise not in {True, False}:
            errors.append(f"demonstration.ledger[{index}].precise_control_action must be boolean")
        if precise is True and not (
            route == "mechanism_led"
            and item.get("control_location_confirmed") is True
            and item.get("operation_method_confirmed") is True
        ):
            errors.append(f"demonstration.ledger[{index}] precise control requires confirmed mechanism_led evidence")
        if route == "effect_led" and precise is True:
            errors.append(f"demonstration.ledger[{index}] effect_led cannot use a precise control")
    if demo.get("hero_action_ledger_id") not in ledger_ids:
        errors.append("demonstration.hero_action_ledger_id must reference a ledger item")
    families = texts(demo.get("action_families"), "demonstration.action_families", errors, minimum=3)
    if len(set(families)) < 3:
        errors.append("demonstration.action_families must contain at least three distinct values")
    if demo.get("single_target_product_unit") is not True:
        errors.append("demonstration.single_target_product_unit must be true")
    if demo.get("unsupported_detachable_parts") not in ([], None):
        errors.append("demonstration.unsupported_detachable_parts must be empty")

    anchor = object_(plan.get("anchor_sheet"), "anchor_sheet", errors)
    if anchor.get("layout") != "2x2_composite":
        errors.append('anchor_sheet.layout must equal "2x2_composite"')
    if anchor.get("generation_count") != 1:
        errors.append("anchor_sheet.generation_count must equal 1")
    if anchor.get("user_approved") is not True:
        errors.append("anchor_sheet.user_approved must be true")
    panels = anchor.get("panels")
    if not isinstance(panels, list) or len(panels) != 4:
        errors.append("anchor_sheet.panels must contain exactly four panels")
        panels = []
    roles = [panel.get("role") for panel in panels if isinstance(panel, dict)]
    expected_roles = STORY_ROLES.get(story_mode)
    if expected_roles and roles != expected_roles:
        errors.append(f"anchor_sheet panel roles must equal {expected_roles}")
    for index, panel in enumerate(panels):
        item = object_(panel, f"anchor_sheet.panels[{index}]", errors)
        text(item.get("action"), f"anchor_sheet.panels[{index}].action", errors)
        text(item.get("state_change"), f"anchor_sheet.panels[{index}].state_change", errors)
    for field in ("product_fidelity_lock", "presenter_identity_lock", "human_scale_lock", "scene_continuity_lock", "same_unit_state_flow"):
        if anchor.get(field) is not True:
            errors.append(f"anchor_sheet.{field} must be true")

    production = object_(plan.get("production"), "production", errors)
    if production.get("route") != "single_continuous_15s":
        errors.append('production.route must equal "single_continuous_15s"')
    if production.get("joint_spoken_performance_available") is not True and production.get("authorized_recording_available") is not True:
        errors.append("production requires joint spoken performance or an authorized recording")
    if production.get("detached_narration_planned") is not False:
        errors.append("production.detached_narration_planned must be false")
    text(production.get("video_adapter"), "production.video_adapter", errors)
    text(production.get("asr_adapter"), "production.asr_adapter", errors)

    budget = object_(plan.get("budget"), "budget", errors)
    text(budget.get("unit"), "budget.unit", errors)
    estimate = number(budget.get("estimated_total"), "budget.estimated_total", errors)
    ceiling = number(budget.get("approved_ceiling"), "budget.approved_ceiling", errors)
    if estimate is not None and estimate < 0:
        errors.append("budget.estimated_total must be non-negative")
    if ceiling is not None and ceiling <= 0:
        errors.append("budget.approved_ceiling must be greater than zero")
    if budget.get("quote_obtained") is not True:
        errors.append("budget.quote_obtained must be true")
    if budget.get("user_approved") is not True:
        errors.append("budget.user_approved must be true")
    if estimate is not None and ceiling is not None and estimate > ceiling and budget.get("overage_user_approved") is not True:
        errors.append("budget estimate exceeds ceiling without overage approval")
    if budget.get("paid_anchor_calls") != 1:
        errors.append("budget.paid_anchor_calls must equal 1")
    if budget.get("paid_video_calls") != 1:
        errors.append("budget.paid_video_calls must equal 1")

    performance = object_(plan.get("performance"), "performance", errors)
    text(performance.get("spoken_line"), "performance.spoken_line", errors)
    if performance.get("one_connected_thought") is not True:
        errors.append("performance.one_connected_thought must be true")
    pause = number(performance.get("planned_pause_seconds"), "performance.planned_pause_seconds", errors)
    if pause is not None and not 0.25 <= pause <= 0.45:
        errors.append("performance.planned_pause_seconds must be 0.25–0.45")
    if performance.get("facts_bound_to_actions") is not True:
        errors.append("performance.facts_bound_to_actions must be true")
    if performance.get("purposeful_moving_ending") is not True:
        errors.append("performance.purposeful_moving_ending must be true")
    if performance.get("planned_use_result_seconds", 0) < 3:
        errors.append("performance.planned_use_result_seconds must be at least 3")

    captions = object_(plan.get("captions"), "captions", errors)
    expected_caption_values = {
        "source": "final_media_asr",
        "timing_source": "word_level_asr",
        "segmentation": "word_timed_microphrases",
        "position_strategy": "adaptive_lower_center",
    }
    for field, expected in expected_caption_values.items():
        if captions.get(field) != expected:
            errors.append(f'captions.{field} must equal "{expected}"')
    if captions.get("script_used_as_transcript") is not False:
        errors.append("captions.script_used_as_transcript must be false")
    if captions.get("max_lines") != 2:
        errors.append("captions.max_lines must equal 2")
    lead = number(captions.get("max_card_lead_seconds"), "captions.max_card_lead_seconds", errors)
    if lead is not None and lead > 0.05:
        errors.append("captions.max_card_lead_seconds must be at most 0.05")
    future = number(captions.get("max_future_word_lead_seconds"), "captions.max_future_word_lead_seconds", errors)
    if future is not None and future > 0.60:
        errors.append("captions.max_future_word_lead_seconds must be at most 0.60")
    targets = set(texts(captions.get("avoidance_targets"), "captions.avoidance_targets", errors))
    required_targets = {"product", "visible_mouth", "hands", "hero_action", "platform_ui"}
    if not required_targets.issubset(targets):
        errors.append(f"captions.avoidance_targets must include {sorted(required_targets)}")
    if captions.get("failure_policy") != "disclose_partial_or_request_real_asr_fallback":
        errors.append("captions.failure_policy is invalid")

    qa = object_(plan.get("quality_gates"), "quality_gates", errors)
    for field in (
        "full_video_watch_required",
        "music_muted_voice_review_required",
        "critical_frame_fidelity_review_required",
        "final_caption_timing_review_required",
        "rights_review_required",
        "live_platform_acceptance_separate",
    ):
        if qa.get(field) is not True:
            errors.append(f"quality_gates.{field} must be true")

    return errors


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(f"usage: {Path(argv[0]).name} PLAN.json", file=sys.stderr)
        return 2
    try:
        plan = load(Path(argv[1]))
    except ValueError as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    errors = validate(plan)
    if errors:
        print("FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("PASS: provider-neutral UGC plan satisfies community-1.0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

