#!/usr/bin/env python3
"""Dependency-free helpers for the public CollaborationOS Wave 1 toolkit."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[1]
DISCOVERED_COS_ROOT = REPO_ROOT
WORKFLOW_STATE_SCHEMA = REPO_ROOT / "workflows" / "decision-only" / "COS_Decision_Only_Workflow_State_v0.1.schema.json"
BINDING_RELATIVE_PATHS = (
    Path("skills/cos-context-recovery/references/source-bindings.json"),
    Path("skills/cos-role-authority-binding/references/source-bindings.json"),
    Path("skills/cos-decision-packet-preparation/references/source-bindings.json"),
    Path("skills/cos-review-circuit-breaker/references/source-bindings.json"),
    Path("workflows/decision-only/source-bindings.json"),
)
SCHEMA_NAMES = {
    "A01": "COS_Context_Packet_v0.1.schema.json",
    "A02": "COS_Evidence_Record_v0.1.schema.json",
    "A03": "COS_Role_Authority_Map_v0.1.schema.json",
    "A04": "COS_Decision_Packet_v0.1.schema.json",
}
EXPECTED_TYPES = {
    "A01": "COS-A01",
    "A02": "COS-A02",
    "A03": "COS-A03",
    "A04": "COS-A04",
}
PERMISSION_IDS = {
    "read_context",
    "prepare_artifact",
    "propose",
    "challenge",
    "edit_authorized_scope",
    "external_call",
    "incur_cost",
    "perform_irreversible_action",
    "make_decision",
    "accept_result",
    "takeover",
    "promote_core",
    "canonical_write",
    "release_product",
}
RFC3339_UTC = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z$")


class DuplicateKeyError(ValueError):
    pass


class ValidationFailure(ValueError):
    pass


def _reject_duplicates(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_reject_duplicates)


def canonical_bytes(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=True, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_source_bindings(cos_root: Path | None = None) -> dict[str, Any]:
    root = resolve_cos_root(cos_root)
    checked = 0
    binding_files: list[str] = []
    for relative_binding_path in BINDING_RELATIVE_PATHS:
        binding_path = root / relative_binding_path
        if not binding_path.is_file():
            raise ValidationFailure(f"missing public binding file: {binding_path}")
        binding = load_json(binding_path)
        sources = binding.get("sources")
        if not isinstance(sources, list) or not sources:
            raise ValidationFailure(f"invalid or empty sources: {binding_path}")
        for row in sources:
            if not isinstance(row, dict) or set(row) != {"role", "path", "sha256"}:
                raise ValidationFailure(f"invalid source-binding row: {binding_path}")
            source = _resolve_repo_path(row["path"], root)
            observed = sha256_file(source)
            if observed != row["sha256"]:
                raise ValidationFailure(
                    f"source hash mismatch for {row['path']}: expected={row['sha256']} observed={observed}"
                )
            checked += 1
        binding_files.append(relative_binding_path.as_posix())
    return {
        "verified": True,
        "binding_files": binding_files,
        "canonical_sources": checked,
        "authority_effect": "none",
    }


def resolve_cos_root(raw: Path | None = None) -> Path:
    candidate = (raw or DISCOVERED_COS_ROOT).resolve()
    expected = candidate / "03_Schemas_and_Templates" / SCHEMA_NAMES["A01"]
    if not expected.is_file():
        if raw is None:
            raise ValidationFailure("COS repository was not discovered; pass --cos-root explicitly")
        raise ValidationFailure(f"invalid COS repository root: {candidate}")
    return candidate


def schema_path(kind: str, cos_root: Path | None = None) -> Path:
    if kind not in SCHEMA_NAMES:
        raise ValidationFailure(f"unsupported artifact kind: {kind}")
    return resolve_cos_root(cos_root) / "03_Schemas_and_Templates" / SCHEMA_NAMES[kind]


def _json_type_matches(value: Any, expected: str) -> bool:
    if expected == "object":
        return isinstance(value, dict)
    if expected == "array":
        return isinstance(value, list)
    if expected == "string":
        return isinstance(value, str)
    if expected == "boolean":
        return isinstance(value, bool)
    if expected == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if expected == "number":
        return isinstance(value, (int, float)) and not isinstance(value, bool)
    if expected == "null":
        return value is None
    return False


def _resolve_ref(root: dict[str, Any], ref: str) -> dict[str, Any]:
    if not ref.startswith("#/"):
        raise ValidationFailure(f"unsupported non-local $ref: {ref}")
    current: Any = root
    for raw in ref[2:].split("/"):
        token = raw.replace("~1", "/").replace("~0", "~")
        current = current[token]
    if not isinstance(current, dict):
        raise ValidationFailure(f"$ref does not resolve to an object: {ref}")
    return current


def _is_valid(instance: Any, schema: dict[str, Any], root: dict[str, Any]) -> bool:
    issues: list[str] = []
    _validate(instance, schema, root, "$", issues)
    return not issues


def _validate(instance: Any, schema: dict[str, Any], root: dict[str, Any], path: str, issues: list[str]) -> None:
    if "$ref" in schema:
        _validate(instance, _resolve_ref(root, schema["$ref"]), root, path, issues)
        return

    for branch in schema.get("allOf", []):
        _validate(instance, branch, root, path, issues)

    if "oneOf" in schema:
        matches = sum(_is_valid(instance, branch, root) for branch in schema["oneOf"])
        if matches != 1:
            issues.append(f"{path}: expected exactly one oneOf branch, observed {matches}")
            return

    if "not" in schema and _is_valid(instance, schema["not"], root):
        issues.append(f"{path}: value matches forbidden schema")

    if "if" in schema:
        selected = schema.get("then") if _is_valid(instance, schema["if"], root) else schema.get("else")
        if selected:
            _validate(instance, selected, root, path, issues)

    if "const" in schema and instance != schema["const"]:
        issues.append(f"{path}: expected const {schema['const']!r}")
    if "enum" in schema and instance not in schema["enum"]:
        issues.append(f"{path}: value not in enum")

    expected_type = schema.get("type")
    if expected_type:
        allowed_types = [expected_type] if isinstance(expected_type, str) else expected_type
        if not any(_json_type_matches(instance, item) for item in allowed_types):
            issues.append(f"{path}: expected type {allowed_types}, observed {type(instance).__name__}")
            return

    if isinstance(instance, dict):
        required = schema.get("required", [])
        for key in required:
            if key not in instance:
                issues.append(f"{path}: missing required property {key}")
        properties = schema.get("properties", {})
        if schema.get("additionalProperties") is False:
            for key in instance:
                if key not in properties:
                    issues.append(f"{path}: additional property {key}")
        for key, value in instance.items():
            if key in properties:
                _validate(value, properties[key], root, f"{path}/{key}", issues)

    if isinstance(instance, list):
        if len(instance) < schema.get("minItems", 0):
            issues.append(f"{path}: fewer than minItems")
        if "maxItems" in schema and len(instance) > schema["maxItems"]:
            issues.append(f"{path}: more than maxItems")
        if schema.get("uniqueItems"):
            fingerprints = [canonical_bytes(value) for value in instance]
            if len(fingerprints) != len(set(fingerprints)):
                issues.append(f"{path}: array items are not unique")
        item_schema = schema.get("items")
        if isinstance(item_schema, dict):
            for index, value in enumerate(instance):
                _validate(value, item_schema, root, f"{path}/{index}", issues)

    if isinstance(instance, str):
        if len(instance) < schema.get("minLength", 0):
            issues.append(f"{path}: shorter than minLength")
        if "maxLength" in schema and len(instance) > schema["maxLength"]:
            issues.append(f"{path}: longer than maxLength")
        if "pattern" in schema and re.search(schema["pattern"], instance) is None:
            issues.append(f"{path}: does not match pattern")
        if schema.get("format") == "date-time":
            if not RFC3339_UTC.fullmatch(instance):
                issues.append(f"{path}: expected RFC3339 UTC timestamp")
            else:
                try:
                    datetime.fromisoformat(instance.replace("Z", "+00:00"))
                except ValueError:
                    issues.append(f"{path}: invalid calendar timestamp")

    if isinstance(instance, (int, float)) and not isinstance(instance, bool):
        if "minimum" in schema and instance < schema["minimum"]:
            issues.append(f"{path}: below minimum")


def validate_schema(instance: Any, schema_path: Path) -> list[str]:
    schema = load_json(schema_path)
    issues: list[str] = []
    _validate(instance, schema, schema, "$", issues)
    return issues


def unwrap_artifact(value: Any) -> dict[str, Any]:
    if isinstance(value, dict) and "artifact" in value and isinstance(value["artifact"], dict):
        return value["artifact"]
    if isinstance(value, dict):
        return value
    raise ValidationFailure("artifact input must be a JSON object")


def validate_artifact(kind: str, path: Path, cos_root: Path | None = None) -> tuple[dict[str, Any], list[str]]:
    artifact = unwrap_artifact(load_json(path))
    issues = validate_schema(artifact, schema_path(kind, cos_root))
    if artifact.get("artifact_type") != EXPECTED_TYPES[kind]:
        issues.append(f"$: artifact_type must be {EXPECTED_TYPES[kind]}")
    issues.extend(validate_semantics(kind, artifact))
    return artifact, sorted(set(issues))


def validate_semantics(kind: str, artifact: dict[str, Any]) -> list[str]:
    issues: list[str] = []
    protocol_run = artifact.get("protocol_run", {})
    if protocol_run.get("downstream_started") is True:
        issues.append("$: downstream_started must remain false")

    if kind == "A01":
        if artifact.get("artifact_lifecycle") == "accepted":
            if protocol_run.get("outcome") not in {"success", "partial_success"}:
                issues.append("$: accepted A01 requires success or partial_success")
            if artifact.get("review", {}).get("result") != "accepted":
                issues.append("$: accepted A01 requires accepted independent review")
    elif kind == "A02":
        if artifact.get("artifact_lifecycle") == "accepted":
            if protocol_run.get("outcome") not in {"success", "partial_success"}:
                issues.append("$: accepted A02 requires success or partial_success")
            if artifact.get("acceptance_event", {}).get("result") != "pass":
                issues.append("$: accepted A02 requires a passing acceptance event")
    elif kind == "A03":
        permission_matrix = artifact.get("permission_matrix", {})
        observed_permissions = set(permission_matrix) if isinstance(permission_matrix, dict) else set()
        if observed_permissions != PERMISSION_IDS or len(permission_matrix) != len(PERMISSION_IDS):
            issues.append("$: permission_matrix must contain the exact 14-entry registry")
        for permission_id, row in permission_matrix.items():
            if not isinstance(row, dict):
                issues.append(f"$/permission_matrix/{permission_id}: permission row must be an object")
                continue
            allowed = row.get("grant_status") == "valid" and row.get("declared_allowed") is True
            if row.get("effective_allowed") is not allowed:
                issues.append(f"$/permission_matrix/{permission_id}: effective_allowed derivation mismatch")
        if artifact.get("artifact_lifecycle") == "accepted":
            if protocol_run.get("outcome") != "success":
                issues.append("$: accepted A03 requires success")
            if artifact.get("acceptance", {}).get("result") != "accepted":
                issues.append("$: accepted A03 requires human acceptance")
    elif kind == "A04":
        if artifact.get("p05_started") is not False:
            issues.append("$: p05_started must remain false")
        if artifact.get("artifact_lifecycle") == "accepted":
            if protocol_run.get("outcome") != "success":
                issues.append("$: accepted A04 requires success")
            if artifact.get("acceptance_event", {}).get("result") != "pass":
                issues.append("$: accepted A04 requires a passing acceptance event")
        disposition = artifact.get("decision_disposition")
        if disposition in {"rejected", "deferred", "needs_information", "not_decided"}:
            if artifact.get("eligible_for_p05_evaluation") is not False:
                issues.append("$: non-approved Decision cannot be eligible for P05 evaluation")
    return issues


def _assert_equal(issues: list[str], label: str, left: Any, right: Any) -> None:
    if left != right:
        issues.append(f"{label}: relational binding mismatch")


def validate_decision_only_relations(artifacts: dict[str, dict[str, Any]]) -> list[str]:
    a01, a02, a03, a04 = (artifacts[key] for key in ("A01", "A02", "A03", "A04"))
    issues: list[str] = []
    lineage = a04.get("common_lineage", {})
    a01_ref = lineage.get("a01", {})
    a02_ref = lineage.get("a02", {})
    a03_ref = lineage.get("a03", {})

    _assert_equal(issues, "A01 identity", a01.get("artifact_id"), a01_ref.get("artifact_id"))
    _assert_equal(issues, "A02 identity", a02.get("artifact_id"), a02_ref.get("artifact_id"))
    _assert_equal(issues, "A03 identity", a03.get("artifact_id"), a03_ref.get("artifact_id"))

    for label, ref in (("A01", a01_ref), ("A02", a02_ref), ("A03", a03_ref)):
        if ref.get("artifact_lifecycle") != "accepted" or ref.get("current") is not True:
            issues.append(f"{label} common-lineage reference is not accepted/current")

    a03_context = a03.get("context_ref", {})
    a02_context = a02.get("context_ref", {})
    for label, ref in (("A03 context", a03_context), ("A02 context", a02_context)):
        _assert_equal(issues, f"{label} artifact_id", ref.get("artifact_id"), a01_ref.get("artifact_id"))
        _assert_equal(issues, f"{label} checksum", ref.get("checksum"), a01_ref.get("checksum"))
        _assert_equal(issues, f"{label} cutoff", ref.get("cutoff"), a01_ref.get("cutoff"))

    a02_acceptance = a02.get("acceptance_event", {})
    decision_owner = a04.get("decision_owner_binding", {})
    a04_acceptance = a04.get("acceptance_event", {})
    for label, ref in (("A02 acceptance", a02_acceptance), ("A04 owner", decision_owner), ("A04 acceptance", a04_acceptance)):
        _assert_equal(issues, f"{label} A03 id", ref.get("accepted_a03_artifact_id"), a03_ref.get("artifact_id"))
        _assert_equal(issues, f"{label} A03 checksum", ref.get("accepted_a03_artifact_checksum"), a03_ref.get("checksum"))

    actor_ids = {row.get("actor_id") for row in a03.get("actors", [])}
    binding_by_id = {row.get("binding_id"): row for row in a03.get("role_bindings", [])}
    owner_binding = binding_by_id.get(decision_owner.get("accepted_a03_binding_id"))
    if owner_binding is None:
        issues.append("A04 decision owner binding is absent from A03")
    else:
        _assert_equal(issues, "A04 decision owner actor", owner_binding.get("actor_id"), decision_owner.get("actor_id"))
        if owner_binding.get("functional_role") != "decision_owner":
            issues.append("A04 decision owner binding is not the decision_owner role")
    if decision_owner.get("actor_id") not in actor_ids or decision_owner.get("actor_kind") != "human":
        issues.append("A04 decision owner must resolve to an A03 human actor")
    return sorted(set(issues))


def _resolve_repo_path(raw: str, cos_root: Path | None = None) -> Path:
    root = resolve_cos_root(cos_root)
    candidate = (root / raw).resolve() if not Path(raw).is_absolute() else Path(raw).resolve()
    try:
        candidate.relative_to(root)
    except ValueError as exc:
        raise ValidationFailure(f"input path escapes COS root: {raw}") from exc
    return candidate


def _resolve_output(raw: Path, output_root: Path | None = None) -> Path:
    if output_root is None:
        raise ValidationFailure("--output-root is required for output-producing commands")
    root = output_root.resolve()
    candidate = raw.resolve() if raw.is_absolute() else (root / raw).resolve()
    try:
        candidate.relative_to(root)
    except ValueError as exc:
        raise ValidationFailure(f"output path escapes the explicit output root: {raw}") from exc
    return candidate


def run_decision_only(spec_path: Path, cos_root: Path | None = None) -> dict[str, Any]:
    root = resolve_cos_root(cos_root)
    spec = load_json(spec_path)
    required = {"workflow_run_id", "as_of", "artifacts"}
    if not isinstance(spec, dict) or set(spec) != required:
        raise ValidationFailure(f"workflow spec must contain exactly {sorted(required)}")
    if set(spec["artifacts"]) != {"A01", "A02", "A03", "A04"}:
        raise ValidationFailure("workflow artifacts must contain exactly A01/A02/A03/A04")

    artifacts: dict[str, dict[str, Any]] = {}
    artifact_results: dict[str, Any] = {}
    all_issues: list[str] = []
    stage_failures: dict[str, bool] = {}
    for kind in ("A01", "A02", "A03", "A04"):
        path = _resolve_repo_path(spec["artifacts"][kind], root)
        artifact, issues = validate_artifact(kind, path, root)
        schema_issues = validate_schema(artifact, schema_path(kind, root))
        artifacts[kind] = artifact
        artifact_results[kind] = {
            "path": str(path.relative_to(root)),
            "sha256": sha256_file(path),
            "artifact_id": artifact.get("artifact_id"),
            "schema_valid": not schema_issues,
            "semantic_valid": not issues,
            "issues": issues,
        }
        stage_failures[kind] = bool(issues)
        all_issues.extend(f"{kind}: {issue}" for issue in issues)

    lifecycle_checks = {
        "A01": artifacts["A01"].get("artifact_lifecycle") == "accepted",
        "A02": artifacts["A02"].get("artifact_lifecycle") == "accepted",
        "A03": artifacts["A03"].get("artifact_lifecycle") == "accepted",
        "A04": artifacts["A04"].get("artifact_lifecycle") == "accepted",
    }
    for kind, passed in lifecycle_checks.items():
        if not passed:
            all_issues.append(f"{kind}: artifact is not accepted")
            stage_failures[kind] = True
    relation_issues = validate_decision_only_relations(artifacts)
    all_issues.extend(relation_issues)
    stage_failures["A04"] = stage_failures["A04"] or bool(relation_issues)

    failed = bool(all_issues)
    disposition = artifacts["A04"].get("decision_disposition")
    terminal = "failed_closed" if failed else "decision_recorded_no_execution"
    stage_definitions = [
        ("context_recovery", "A01"),
        ("evidence_admission_external_prerequisite", "A02"),
        ("authority_binding", "A03"),
        ("decision_record", "A04"),
    ]
    first_failure_seen = False
    stages: list[dict[str, str]] = []
    for stage_id, kind in stage_definitions:
        if first_failure_seen:
            status = "not_attempted"
        elif stage_failures[kind]:
            status = "failed"
            first_failure_seen = True
        else:
            status = "completed"
        stages.append({"stage_id": stage_id, "status": status})
    stages.append({"stage_id": "execution_handoff", "status": "not_attempted"})
    return {
        "schema_version": "0.1-public",
        "workflow_id": "COS-WF02",
        "workflow_run_id": spec["workflow_run_id"],
        "observed_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "as_of": spec["as_of"],
        "mode": "manual_static_decision_only",
        "artifacts": artifact_results,
        "stages": stages,
        "outcome": "failed" if failed else "success",
        "terminal_state": terminal,
        "decision_disposition": disposition if not failed else "not_reduced",
        "record_accepted": not failed,
        "eligible_for_p05_evaluation_observed": artifacts["A04"].get("eligible_for_p05_evaluation") if not failed else False,
        "p05_started": False,
        "execution_authorized": False,
        "host_access": False,
        "external_calls": 0,
        "incremental_external_cost_usd": 0,
        "automatic_retry": False,
        "issues": sorted(set(all_issues)),
        "authority_effect": "none",
    }


@dataclass(frozen=True)
class CircuitReason:
    code: str
    detail: str


def assess_circuit_breaker(facts: dict[str, Any]) -> dict[str, Any]:
    required = {
        "gate_id",
        "development_lab_status",
        "governed_candidate_number",
        "review_count",
        "elapsed_engineer_hours",
        "in_scope_p1_families",
        "new_root_cause_family",
        "contract_growth_after_freeze",
        "review_coverage_complete",
        "effective_entry_required",
        "effective_entry_reached",
        "preflight_engine_count",
        "effective_engine_count",
        "subject_oracle_observer_independent",
        "authority_or_ownership_ambiguity",
        "repeated_checklist_failure_family",
        "short_causal_model_available",
        "human_budget_override",
    }
    if set(facts) != required:
        missing = sorted(required - set(facts))
        extra = sorted(set(facts) - required)
        raise ValidationFailure(f"circuit facts key mismatch; missing={missing}, extra={extra}")

    reasons: list[CircuitReason] = []
    candidate = facts["governed_candidate_number"]
    p1_count = facts["in_scope_p1_families"]
    elapsed = facts["elapsed_engineer_hours"]
    if candidate not in {0, 1, 2}:
        reasons.append(CircuitReason("INVALID_CANDIDATE_NUMBER", "candidate number must be 0, 1 or 2"))
    if candidate == 2 and p1_count > 0:
        reasons.append(CircuitReason("CANDIDATE_02_BLOCKED", "Candidate-02 retains an in-scope P1"))
    if p1_count > 3:
        reasons.append(CircuitReason("P1_FAMILY_BUDGET_EXCEEDED", "more than three in-scope P1 families"))
    if facts["new_root_cause_family"]:
        reasons.append(CircuitReason("NEW_ROOT_CAUSE_FAMILY", "new root-cause family appeared after freeze"))
    if facts["contract_growth_after_freeze"]:
        reasons.append(CircuitReason("CONTRACT_GROWTH_AFTER_FREEZE", "contract or scope grew after freeze"))
    if not facts["review_coverage_complete"]:
        reasons.append(CircuitReason("REVIEW_COVERAGE_INCOMPLETE", "incomplete coverage cannot support PASS"))
    if elapsed >= 10 and not facts["human_budget_override"]:
        reasons.append(CircuitReason("HARD_TIME_BUDGET", "ten-hour hard budget reached without human override"))
    elif elapsed >= 4 and not facts["human_budget_override"]:
        reasons.append(CircuitReason("AUTOMATIC_PAUSE_TIME", "four-hour automatic pause threshold reached"))
    if facts["effective_entry_required"]:
        if not facts["effective_entry_reached"]:
            reasons.append(CircuitReason("EFFECTIVE_ENTRY_NOT_REACHED", "required effective entry was not reached"))
        if facts["preflight_engine_count"] != 0 or facts["effective_engine_count"] != 1:
            reasons.append(CircuitReason("ENGINE_TOPOLOGY_INVALID", "required topology is preflight=0/effective=1"))
    if not facts["subject_oracle_observer_independent"]:
        reasons.append(CircuitReason("PROOF_INDEPENDENCE_MISSING", "subject, oracle and observer are not independent"))
    if facts["authority_or_ownership_ambiguity"]:
        reasons.append(CircuitReason("AUTHORITY_OR_OWNERSHIP_AMBIGUITY", "authority, mutation or ownership is ambiguous"))
    if facts["repeated_checklist_failure_family"]:
        reasons.append(CircuitReason("REPEATED_CHECKLIST_FAILURE", "a frozen checklist failure family repeated"))
    if not facts["short_causal_model_available"]:
        reasons.append(CircuitReason("NO_SHORT_CAUSAL_MODEL", "candidate success cannot be explained briefly"))

    if reasons:
        if any(reason.code == "CANDIDATE_02_BLOCKED" for reason in reasons):
            next_action = "CANDIDATE_LINEAGE_STOP"
        elif any(reason.code in {"NEW_ROOT_CAUSE_FAMILY", "CONTRACT_GROWTH_AFTER_FREEZE", "P1_FAMILY_BUDGET_EXCEEDED"} for reason in reasons):
            next_action = "ARCHITECTURE_RESET_REQUIRED"
        else:
            next_action = "PAUSE_FOR_HUMAN_DECISION"
        state = "TRIPPED"
    elif candidate == 1 and p1_count > 0:
        next_action = "ONE_CONSOLIDATED_CANDIDATE_02"
        state = "ARMED"
    elif candidate == 0 and facts["development_lab_status"] != "PASS":
        next_action = "CONTINUE_DEVELOPMENT_LAB"
        state = "CLEAR"
    else:
        next_action = "READY_TO_REQUEST_NEXT_GATE"
        state = "CLEAR"

    return {
        "schema_version": "0.1-public",
        "assessment_type": "COS_REVIEW_CIRCUIT_BREAKER",
        "gate_id": facts["gate_id"],
        "circuit_breaker_state": state,
        "recommended_next_action": next_action,
        "reasons": [reason.__dict__ for reason in reasons],
        "authority_effect": "none",
        "work_authorized": False,
        "automatic_retry": False,
        "allowed_next_actions": [next_action],
        "forbidden_next_actions": ["implicit_retry", "host_access", "execution", "governance_landing"],
    }


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(canonical_bytes(value))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    validate_cmd = sub.add_parser("validate-artifact")
    validate_cmd.add_argument("--kind", choices=sorted(SCHEMA_NAMES), required=True)
    validate_cmd.add_argument("--input", type=Path, required=True)
    validate_cmd.add_argument("--cos-root", type=Path)

    bindings_cmd = sub.add_parser("verify-bindings")
    bindings_cmd.add_argument("--cos-root", type=Path)

    workflow_cmd = sub.add_parser("decision-only")
    workflow_cmd.add_argument("--input", type=Path, required=True)
    workflow_cmd.add_argument("--output", type=Path, required=True)
    workflow_cmd.add_argument("--cos-root", type=Path)
    workflow_cmd.add_argument("--output-root", type=Path)

    circuit_cmd = sub.add_parser("assess-review")
    circuit_cmd.add_argument("--input", type=Path, required=True)
    circuit_cmd.add_argument("--output", type=Path, required=True)
    circuit_cmd.add_argument("--cos-root", type=Path)
    circuit_cmd.add_argument("--output-root", type=Path)

    args = parser.parse_args(argv)
    try:
        if args.command == "validate-artifact":
            root = resolve_cos_root(args.cos_root)
            verify_source_bindings(root)
            _, issues = validate_artifact(args.kind, _resolve_repo_path(str(args.input), root), root)
            print(json.dumps({"valid": not issues, "issues": issues}, indent=2))
            return 0 if not issues else 2
        if args.command == "verify-bindings":
            print(json.dumps(verify_source_bindings(args.cos_root), indent=2))
            return 0
        if args.command == "decision-only":
            root = resolve_cos_root(args.cos_root)
            verify_source_bindings(root)
            input_path = _resolve_repo_path(str(args.input), root)
            output_path = _resolve_output(args.output, args.output_root)
            result = run_decision_only(input_path, root)
            write_json(output_path, result)
            print(json.dumps({"outcome": result["outcome"], "output": str(output_path)}, indent=2))
            return 0 if result["outcome"] == "success" else 2
        if args.command == "assess-review":
            root = resolve_cos_root(args.cos_root)
            verify_source_bindings(root)
            input_path = _resolve_repo_path(str(args.input), root)
            output_path = _resolve_output(args.output, args.output_root)
            result = assess_circuit_breaker(load_json(input_path))
            write_json(output_path, result)
            print(json.dumps({"state": result["circuit_breaker_state"], "output": str(output_path)}, indent=2))
            return 0
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(json.dumps({"error": type(exc).__name__, "message": str(exc)}), file=sys.stderr)
        return 2
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
