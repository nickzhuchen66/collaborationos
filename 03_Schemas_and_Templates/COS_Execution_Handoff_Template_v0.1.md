# COS A06 Execution Handoff Template v0.1

Status: `M5-C CANDIDATE / HUMAN PREPARATION VIEW`

This template is the human preparation view of the strict JSON Schema. The JSON artifact is authoritative for machine conformance; this file does not grant execution or acceptance.

## Required sections

- `schema_version`
- `artifact_type`
- `artifact_id`
- `lifecycle`
- `lineage`
- `execution_attempt_id`
- `actors`
- `operations`
- `protected_surfaces`
- `environment`
- `permission_projection`
- `cost_contract`
- `start_predicates`
- `acceptance_plan`
- `rollback_contract`
- `stages`
- `protocol_outcome`
- `limitations`
- `artifact_body_checksum`
- `acceptance_event`

## Preparation notes

Freeze attempt scope, complete 14-permission projection, environment, cost, acceptance and rollback before human handoff acceptance.

## Review

- Verify exact A01/A03/A04/A05 lineage and canonical checksums.
- Keep facts, observations, acceptance and business Decision states separate.
- Record unknown/not-observed explicitly; never coerce them to zero or pass.
- Stop on the first scope, authority, permission, checksum or rollback mismatch.
