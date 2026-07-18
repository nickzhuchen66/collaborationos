# COS A02 Evidence Record Template v0.1

Repository role: `M5-B IMPLEMENTATION ARTIFACT`  
Schema: `COS_Evidence_Record_v0.1.schema.json`  
Owner protocol: `COS-P02`  
Conformance: `MANUAL / STATIC ONLY`

> Human preparation view. JSON is canonical. Do not include secrets, credentials, personal sensitive data or host business payload.

## Identity and Context
- Artifact ID / created at / lifecycle:
- Accepted A01 ID / checksum / cutoff / current revalidation:
- Submitter actor ID:
- Reviewer actor and accepted A03 ID/checksum/binding/authority source/scope:

## Sources and Evidence
- Source ID / safe ref / authority class / requiredness:
- Availability / freshness / checksum state and observed value:
- Evidence item ID / claim ID / statement type / requirement class / safe statement:
- Conflict and grounding state:
- Interpretation ID, evidence relations, assumptions, limitations and confidence:
- Support-link ID and relation: supporting / contradicting / limiting:

## Append-only Admission Events
For every event record admission_event_id, evidence_item_id, reviewer_actor_id, accepted A03 ID/checksum/binding, event_sequence, prior event/disposition, result disposition, reason and reviewed_at. First-event prior values are explicit none. Never overwrite or delete prior events.

## Derived Current Admission
- Evidence item / derived event / disposition / decision-basis eligibility:
- Confirm current state follows the strict same-item event chain:
- Accepted limitations and unresolved unknowns:

## Protocol Run and Acceptance
- Record all nine P02 stages in order; automated_external_verification is disabled.
- Apply failed > legal stop > allowlisted partial > success.
- Record stable failure envelope for non-success.
- Record independent acceptance event and confirm A02 creates no Decision, role, permission or P05 eligibility.


## Retry-02 mechanical integrity

- Evidence, claim, interpretation, support-link, admission-event and acceptance-event identities use distinct typed prefixes and must remain pairwise disjoint.
- Current admission is a projection of the unique terminal append-only event; unknown predecessors, sequence gaps, prior-result mismatch, overwrite or deletion fail qualification.
- Acceptance binds the exact A02 artifact ID and canonical body checksum, an accepted A03 human binding, and an acceptor distinct from the submitter.


## Retry-03 relational derivation

- Every interpretation claim and evidence reference and every support-link claim/evidence reference must resolve to a declared identity in the same A02.
- `current_admission` is exactly one terminal projection per event-bearing evidence item; duplicate or missing rows fail.
- `decision_basis_eligible` is recomputed from terminal disposition, grounding, conflict, typed support reachability and accepted limitations. Stored values are never trusted alone.


## Retry-04 typed claim-evidence pairing

Resolved identities are necessary but not sufficient: every interpretation evidence reference and support link must pair an evidence item with the exact claim declared by that evidence item. Cross-claim pairing fails semantic integrity.

## Architecture-baseline typed interpretation graph

Every interpretation has a non-empty union of supporting, contradicting and limiting evidence references. The three arrays are pairwise disjoint. Each reference resolves to exactly one same-claim semantic edge of the matching relation kind, and `(claim_id, evidence_item_id, relation)` is globally unique regardless of support-link identity or ordering.
