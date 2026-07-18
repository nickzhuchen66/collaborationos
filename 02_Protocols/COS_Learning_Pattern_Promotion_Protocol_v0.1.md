# COS Learning / Pattern Promotion Protocol v0.1

Status: `M5-D CANDIDATE / MANUAL_STATIC_ONLY`  
Protocol ID: `COS-P07`  
Primary artifact: `COS-A09 Learning Candidate Record`  
Dependencies: accepted/current `COS-P02`, `COS-P03`, `COS-P06`  
External calls: `0`  
Incremental external cost: `US$0`

## 1. Purpose

P07 turns admitted, authority-bound host evidence into a reviewed COS learning candidate. It never admits evidence, creates authority, promotes Core, writes canonical files, releases a product or applies a result to a host.

## 2. Seven-layer authority model

1. Host event and host-local authority retain complete business evidence.
2. Learning Submission carries only redacted, untrusted transport claims.
3. Accepted A02 and A07/A08 own admitted evidence and execution/failure facts.
4. A09 owns candidate derivation, append-only review and recommendation.
5. An exact human promotion Decision and Build Log own promotion disposition.
6. A separately authorized actor owns canonical Core change/release.
7. Host adoption requires a separate adapter review and host-local Decision.

A03 is the sole actor, role, domain and permission authority. Identity equality, prose similarity and artifact-local allowlists grant nothing.

## 3. Clauses

### P07-C01 Source, current-event and identity binding

Every required A02/A03/A07/A08 source binds path/ref, artifact ID/checksum, current accepted event ID/checksum, authority and cutoff. Honest absence, supersession or not-yet-current evidence legal-stops. A claimed-current contradiction, checksum mismatch, dangling reference, duplicate or cross-type identity collision fails.

### P07-C02 Disclosure and redaction

COS retains minimum safe references only. Unavailable/not-observed review legal-stops. Observed failed review without forbidden payload legal-stops with reason. Detected secret, NDA, PII, forbidden business payload or `passed` contradiction fails. Source-bound `passed` plus all forbidden predicates false may continue.

### P07-C03 Host submitter versus COS registrar

`host_submitter_claim` is source-local and untrusted. `cos_intake_registrar` separately resolves a current accepted A03 `proposer` binding and `propose=true` for `cos:a09:intake:{candidate_id}`. Identity equality grants nothing.

### P07-C04 Exhaustive Learning Submission crosswalk

The crosswalk inventory must equal the bound Learning Submission schema leaf inventory. Every field maps exactly once to submitted claims or validation-only disposition. Unknown/nested unknown fields, duplicates, aliases, generic extension objects and silent drops fail. `HOST_DOMAIN_EXTENSION` is normalized only to `DOMAIN_EXTENSION_ONLY`.

### P07-C05 Route and split ownership

Reviewed route is exactly `COS_CORE_CANDIDATE`, `DOMAIN_EXTENSION_ONLY`, `AI_NATIVE_CAPABILITY`, `MIXED_SPLIT` or `REJECT_NO_COS_RELEVANCE`. Mixed split requires distinct child IDs, non-overlapping scopes, destinations and owners. Domain/AI/reject routes cannot alias Core.

### P07-C06 Cohort and maturity ceiling

The packet freezes an order-independent cohort registry, authoritative host aliases, structural-difference dimensions, common scope and limitation policy. Same-host validation requires distinct accepted runs. Cross-host support requires at least two authoritative hosts with a source-bound structural difference and exact clause/version/common scope. Project count, article similarity, copied tests and file presence do not raise maturity. Only policy-declared optional limitations may yield partial success; no promotion prerequisite is waivable.

### P07-C07 Review and supersede integrity

A09 review events form one append-only checksum chain. A packet-external, order-independent global registry rejects duplicate identities before map construction and requires bidirectional predecessor/successor supersede links. Missing counterpart legal-stops; mismatch, fork, cycle, overwrite, deletion or order dependence fails.

### P07-C08 Exact authority policy

P07 owns a closed restriction policy that only narrows A03:

| Artifact/action | Role | A03 domain | Scope | Permission |
|---|---|---|---|---|
| A09/register | proposer | final_direction | `cos:a09:intake:{candidate_id}` | propose |
| A09/accept review | reviewer | acceptance | `cos:a09:review:{candidate_id}` | accept_result |
| promotion Decision | decision_owner | promotion | exact clause/version/scope digest | make_decision + promote_core |
| canonical change | authority_owner | canonical_release | same exact scope | canonical_write |
| Core release | authority_owner | canonical_release | same exact scope | release_product |

The promotion owner is the unique current human promotion-domain owner with `decision_owner`; the P03 final-human endpoint is verified separately. Missing/unknown/wrong/stale tuples and policy checksum mismatch fail.

### P07-C09 Self-review exception

Default deny. An exception binds request ID/checksum, candidate, exact scope, actor/roles, reason and time window plus a separate current human Decision ID/checksum and A03 source. It never merges permissions or grants promotion/canonical authority.

### P07-C10 Non-circular promotion lineage

1. Freeze accepted review-head ID/checksum, candidate ID/checksum, source-set digest and exact clause/version/scope.
2. Exact human promotion owner issues `approve|reject|defer`; Build Log binds Decision ID/checksum and the same target.
3. Only after `approve`, the separate canonical owner produces a versioned Core change/release manifest binding that Decision and review head.
4. A new append-only A09 event may then record `PROMOTED_CORE` and bind all prior IDs/paths/checksums.

The Decision cannot bind a future event or mutable whole-record checksum. P07 never performs steps 2 or 3; it validates and records facts only.

### P07-C11 No automation, runtime or host apply

The A09 contract requires twelve false flags: automatic submission, evidence admission, review acceptance, maturity transition, Decision, apply, promotion, canonical write, release, host adoption, external call and runtime invocation. Missing/unknown fails. M5-D contains no executable surface.

## 4. Ordered stages

1. `bind_candidate_sources`
2. `validate_disclosure_and_redaction`
3. `verify_evidence_admission_and_reachability`
4. `classify_route_and_split_ownership`
5. `derive_maturity_ceiling`
6. `resolve_independent_reviewer_authority`
7. `record_candidate_review_recommendation`
8. `bind_human_promotion_decision_if_required`
9. `record_promotion_or_nonpromotion_disposition`
10. `reduce_p07_outcome`

Stage status is `completed|skipped|disabled|not_attempted|legal_stop|failed`. Missing/unavailable/not-yet-effective required facts legal-stop. Stale, wrong-role/scope/source/checksum, non-human or contradictory facts fail. Later unentered stages are `not_attempted`; reduction cannot overwrite an earlier stop/failure.

Top-level outcome is `success|partial_success|legal_stop|failed`, reduced in priority order failed, legal stop, policy-qualified partial success, success.

## 5. Outputs and boundaries

P07 outputs one structurally valid and semantically qualified A09 or a rejected/legal-stop record. Review recommendation is `ADOPT|ADAPT|DEFER|REJECT`. `ADOPT` is not promotion. Decision `reject|defer` is valid non-promotion. Host adoption remains separate.

No automatic retry, submission, admission, Decision, promotion, write, release, apply or external call is authorized.
