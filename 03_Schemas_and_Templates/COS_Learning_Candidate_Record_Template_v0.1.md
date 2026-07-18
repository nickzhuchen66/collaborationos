# COS Learning Candidate Record Template v0.1

> Manual view of `COS_Learning_Candidate_Record_v0.1.schema.json`. The accepted record is strict JSON. Labels below are one-to-one with schema fields; no aliases or additional maturity/route values are allowed.

## Identity

- `artifact_id`:
- `candidate_id`:
- `artifact_lifecycle`:
- `created_at` (RFC3339 with timezone):
- `source_authority`:

## Target

- `protocol_id`: `COS-P07`
- `clause_id`:
- `contract_version`: `v0.1`
- `scope_predicates`:
- `scope_digest`:

## Intake

- `submission_ref` / `submission_checksum`:
- `host_submitter_claim` (untrusted/source-local):
- `cos_intake_registrar` (current accepted A03 exact tuple):
- `crosswalk_inventory_digest`:

Identity equality between host submitter and registrar grants nothing.

## Source cohort and accepted bindings

For each `source_cohort` event record authoritative host identity/source, alias, structural fingerprint/dimensions, event/run IDs, actual scope and positive/failure/acceptance/takeover truth. Bind current accepted event IDs/checksums for `a02`, `a03`, and applicable `a07`/`a08`.

## Disclosure and routing

- `disclosure`: observation, redaction result, four forbidden-content booleans and reason.
- `routing.submitted_route`: untrusted claim.
- `routing.reviewed_route`: closed P07 route.
- `routing.split_children`: distinct IDs/scopes/owners only for `MIXED_SPLIT`.

## Maturity

Keep separate `current_observation`, `current_state`, `derived_ceiling`, `recommended_state` and `final_state`. Bind cohort, host-policy and limitation-policy digests. `PROMOTED_CORE` is never a derived ceiling.

## Review and promotion lineage

- `authority_resolution`: exact reviewer, promotion-owner and canonical-owner A03 tuples, action-policy digest and source-bound self-review exception state.
- `review_chain`: append-only event IDs, sequence/predecessor checksums, exact reviewer tuple, route, ceiling, recommendation and time.
- `promotion_lineage`: frozen basis review head, human Decision/Build Log, separately authorized Core change/release and final append-only event.
- A Decision never binds a future event or mutable whole-record checksum.

## History, host adoption and automation

- `supersession`: exact bidirectional registry-backed lineage.
- `host_adoption`: separate host-local status/Decision.
- `automation`: all twelve fields are required `false`; missing/unknown fails.

## Protocol trace

- `stages`: all ten P07 stages in exact order.
- `protocol_outcome`: `success | partial_success | legal_stop | failed`.
- `limitations`: policy-classified required/optional items.
- `expected_assertion`: fixture-only conformance identity and reached state.

This template does not authorize promotion, canonical write/release, host adoption, runtime or external calls.
