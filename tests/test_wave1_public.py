from __future__ import annotations

import copy
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT / "tools"))

import cos_wave1  # noqa: E402


def load_fixture(path: str) -> dict:
    return json.loads((REPO_ROOT / path).read_text(encoding="utf-8"))["artifact"]


def build_aligned_artifacts() -> dict[str, dict]:
    a01 = load_fixture("05_Conformance/M5A/fixtures/M5A-P01-POS-01-context-success.json")
    a02 = load_fixture("05_Conformance/M5B/fixtures/M5B-P02-POS-01-evidence-admitted.json")
    a03 = load_fixture("05_Conformance/M5A/fixtures/M5A-P03-POS-01-authority-success.json")
    a04 = load_fixture("05_Conformance/M5B/fixtures/M5B-P04-POS-01-human-decision-approved.json")

    a01["artifact_id"] = "COS-A01-M5A-ACCEPTED"
    a01["recovery_scope"]["as_of"] = "2026-07-15T00:00:00Z"
    a03["artifact_id"] = "COS-A03-M5A-ACCEPTED"
    a03["context_ref"].update(
        {
            "artifact_id": "COS-A01-M5A-ACCEPTED",
            "checksum": "1" * 64,
            "cutoff": "2026-07-15T00:00:00Z",
        }
    )
    a03["actors"].append(
        {
            "actor_id": "human-decision-owner",
            "actor_kind": "human",
            "safe_identity_ref": "cos:actor/human-decision-owner",
            "accountability_owner_actor_id": "human-decision-owner",
        }
    )
    a03["role_bindings"].append(
        {
            "binding_id": "binding-decision-owner",
            "functional_role": "decision_owner",
            "actor_id": "human-decision-owner",
            "scope": "M5-B evidence and decision packet",
            "authority_source_ref": "cos:decision/COS-019",
            "effective_at": "2026-07-15T00:00:00Z",
            "expires_at": "2026-12-31T23:59:59Z",
        }
    )
    return {"A01": a01, "A02": a02, "A03": a03, "A04": a04}


class PublicWave1Test(unittest.TestCase):
    def setUp(self) -> None:
        self.artifacts = build_aligned_artifacts()

    def write_run(self, root: Path, artifacts: dict[str, dict] | None = None) -> Path:
        selected = artifacts or self.artifacts
        paths: dict[str, str] = {}
        for kind, artifact in selected.items():
            path = root / f"{kind.lower()}.json"
            path.write_text(json.dumps(artifact, indent=2) + "\n", encoding="utf-8")
            paths[kind] = str(path)
        spec = root / "run.json"
        spec.write_text(
            json.dumps(
                {
                    "workflow_run_id": "wf02-public-test",
                    "as_of": "2026-07-23T00:00:00Z",
                    "artifacts": paths,
                },
                indent=2,
            )
            + "\n",
            encoding="utf-8",
        )
        return spec

    def circuit_facts(self) -> dict:
        return {
            "gate_id": "PUBLIC-TEST-GATE",
            "development_lab_status": "PASS",
            "governed_candidate_number": 1,
            "review_count": 1,
            "elapsed_engineer_hours": 2.0,
            "in_scope_p1_families": 0,
            "new_root_cause_family": False,
            "contract_growth_after_freeze": False,
            "review_coverage_complete": True,
            "effective_entry_required": False,
            "effective_entry_reached": False,
            "preflight_engine_count": 0,
            "effective_engine_count": 0,
            "subject_oracle_observer_independent": True,
            "authority_or_ownership_ambiguity": False,
            "repeated_checklist_failure_family": False,
            "short_causal_model_available": True,
            "human_budget_override": False,
        }

    def test_public_source_bindings_match(self) -> None:
        result = cos_wave1.verify_source_bindings(REPO_ROOT)
        self.assertTrue(result["verified"])
        self.assertEqual(16, result["canonical_sources"])

    def test_positive_artifacts_pass(self) -> None:
        with tempfile.TemporaryDirectory(dir=REPO_ROOT / "tests") as raw:
            root = Path(raw)
            self.write_run(root)
            for kind in ("A01", "A02", "A03", "A04"):
                _, issues = cos_wave1.validate_artifact(kind, root / f"{kind.lower()}.json", REPO_ROOT)
                self.assertEqual([], issues, f"{kind}: {issues}")

    def test_decision_only_stops_before_execution(self) -> None:
        with tempfile.TemporaryDirectory(dir=REPO_ROOT / "tests") as raw:
            result = cos_wave1.run_decision_only(self.write_run(Path(raw)), REPO_ROOT)
        self.assertEqual("decision_recorded_no_execution", result["terminal_state"])
        self.assertFalse(result["p05_started"])
        self.assertFalse(result["execution_authorized"])
        self.assertEqual("none", result["authority_effect"])

    def test_lineage_mismatch_fails_closed(self) -> None:
        artifacts = copy.deepcopy(self.artifacts)
        artifacts["A03"]["context_ref"]["checksum"] = "f" * 64
        with tempfile.TemporaryDirectory(dir=REPO_ROOT / "tests") as raw:
            result = cos_wave1.run_decision_only(self.write_run(Path(raw), artifacts), REPO_ROOT)
        self.assertEqual("failed_closed", result["terminal_state"])
        self.assertFalse(result["execution_authorized"])
        self.assertEqual("not_attempted", result["stages"][-1]["status"])

    def test_missing_permission_fails(self) -> None:
        artifact = copy.deepcopy(self.artifacts["A03"])
        del artifact["permission_matrix"]["release_product"]
        with tempfile.TemporaryDirectory(dir=REPO_ROOT / "tests") as raw:
            path = Path(raw) / "a03.json"
            path.write_text(json.dumps(artifact), encoding="utf-8")
            _, issues = cos_wave1.validate_artifact("A03", path, REPO_ROOT)
        self.assertTrue(any("permission_matrix" in issue for issue in issues))

    def test_duplicate_json_key_fails(self) -> None:
        with tempfile.TemporaryDirectory(dir=REPO_ROOT / "tests") as raw:
            path = Path(raw) / "duplicate.json"
            path.write_text('{"artifact_id":"one","artifact_id":"two"}\n', encoding="utf-8")
            with self.assertRaises(cos_wave1.DuplicateKeyError):
                cos_wave1.load_json(path)

    def test_candidate_two_with_blocker_stops_lineage(self) -> None:
        facts = self.circuit_facts()
        facts["governed_candidate_number"] = 2
        facts["review_count"] = 2
        facts["in_scope_p1_families"] = 1
        result = cos_wave1.assess_circuit_breaker(facts)
        self.assertEqual("TRIPPED", result["circuit_breaker_state"])
        self.assertEqual("CANDIDATE_LINEAGE_STOP", result["recommended_next_action"])
        self.assertFalse(result["work_authorized"])

    def test_four_hour_threshold_pauses(self) -> None:
        facts = self.circuit_facts()
        facts["elapsed_engineer_hours"] = 4
        result = cos_wave1.assess_circuit_breaker(facts)
        self.assertEqual("TRIPPED", result["circuit_breaker_state"])

    def test_workflow_result_matches_public_state_schema(self) -> None:
        with tempfile.TemporaryDirectory(dir=REPO_ROOT / "tests") as raw:
            result = cos_wave1.run_decision_only(self.write_run(Path(raw)), REPO_ROOT)
        issues = cos_wave1.validate_schema(result, cos_wave1.WORKFLOW_STATE_SCHEMA)
        self.assertEqual([], issues)

    def test_decision_only_cli_reaches_no_execution_terminal(self) -> None:
        with tempfile.TemporaryDirectory(dir=REPO_ROOT / "tests") as raw:
            root = Path(raw)
            spec = self.write_run(root)
            output = root / "output" / "state.json"
            completed = subprocess.run(
                [
                    sys.executable,
                    str(REPO_ROOT / "tools" / "cos_wave1.py"),
                    "decision-only",
                    "--cos-root",
                    str(REPO_ROOT),
                    "--input",
                    str(spec),
                    "--output",
                    str(output),
                    "--output-root",
                    str(root / "output"),
                ],
                check=False,
                capture_output=True,
                text=True,
                env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
            )
            state = json.loads(output.read_text(encoding="utf-8"))
        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertEqual("decision_recorded_no_execution", state["terminal_state"])
        self.assertFalse(state["execution_authorized"])

    def test_circuit_cli_uses_public_profile(self) -> None:
        with tempfile.TemporaryDirectory(dir=REPO_ROOT / "tests") as raw:
            root = Path(raw)
            facts_path = root / "facts.json"
            facts = self.circuit_facts()
            facts["governed_candidate_number"] = 2
            facts["review_count"] = 2
            facts["in_scope_p1_families"] = 1
            facts_path.write_text(json.dumps(facts) + "\n", encoding="utf-8")
            output = root / "output" / "assessment.json"
            completed = subprocess.run(
                [
                    sys.executable,
                    str(REPO_ROOT / "tools" / "cos_wave1.py"),
                    "assess-review",
                    "--cos-root",
                    str(REPO_ROOT),
                    "--input",
                    str(facts_path),
                    "--output",
                    str(output),
                    "--output-root",
                    str(root / "output"),
                ],
                check=False,
                capture_output=True,
                text=True,
                env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"},
            )
            state = json.loads(output.read_text(encoding="utf-8"))
        self.assertEqual(0, completed.returncode, completed.stderr)
        self.assertEqual("CANDIDATE_LINEAGE_STOP", state["recommended_next_action"])
        self.assertFalse(state["work_authorized"])


if __name__ == "__main__":
    unittest.main()
