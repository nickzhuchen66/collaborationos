# COS A07 Change & Acceptance Packet Template v0.1

Status: `M5-C CANDIDATE / HUMAN PREPARATION VIEW`

This template is the human preparation view of the strict JSON Schema. The JSON artifact is authoritative for machine conformance; this file does not grant execution or acceptance.

## Required sections

- `schema_version`
- `artifact_type`
- `artifact_id`
- `lifecycle`
- `a06_ref`
- `execution_attempt_id`
- `builder_actor_id`
- `result_acceptor`
- `builder_evidence_events`
- `derived_builder_head_event_id`
- `expected_operations`
- `observed_operations`
- `protected_surface_parity`
- `transient_paths`
- `side_effect_state`
- `test_evidence`
- `builder_execution_result`
- `optional_limitations`
- `required_acceptance_items_passed`
- `business_disposition_observed`
- `business_disposition_after`
- `acceptance_event`
- `stages`
- `protocol_outcome`
- `failure_envelope`
- `artifact_body_checksum`

## Preparation notes

Append builder evidence first; an independently authorized human records the result acceptance event against the final evidence head.

## Review

- Verify exact A01/A03/A04/A05 lineage and canonical checksums.
- Keep facts, observations, acceptance and business Decision states separate.
- Record unknown/not-observed explicitly; never coerce them to zero or pass.
- Stop on the first scope, authority, permission, checksum or rollback mismatch.
