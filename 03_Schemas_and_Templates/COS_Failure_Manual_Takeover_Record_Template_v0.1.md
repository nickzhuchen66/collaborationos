# COS A08 Failure & Manual Takeover Record Template v0.1

Status: `M5-C CANDIDATE / HUMAN PREPARATION VIEW`

This template is the human preparation view of the strict JSON Schema. The JSON artifact is authoritative for machine conformance; this file does not grant execution or acceptance.

## Required sections

- `schema_version`
- `artifact_type`
- `artifact_id`
- `lifecycle`
- `a06_ref`
- `a07_ref`
- `execution_attempt_id`
- `prior_attempt_id`
- `events`
- `derived_head_event_id`
- `failure`
- `rollback`
- `takeover_owner`
- `takeover_acknowledged`
- `recovery_disposition`
- `scope_expanded`
- `partial_state_treated_as_acceptance`
- `retry_recommended`
- `retry_authorized`
- `new_attempt_started`
- `stages`
- `protocol_outcome`
- `unresolved_risks`
- `artifact_body_checksum`

## Preparation notes

Preserve failure-final, rollback and takeover events. A retry route is not authorization and cannot start a new attempt.

## Review

- Verify exact A01/A03/A04/A05 lineage and canonical checksums.
- Keep facts, observations, acceptance and business Decision states separate.
- Record unknown/not-observed explicitly; never coerce them to zero or pass.
- Stop on the first scope, authority, permission, checksum or rollback mismatch.
