# COS Evidence Admission & Grounding Protocol v0.1

Repository role: `M5-B IMPLEMENTATION ARTIFACT`  
Conformance mode: `MANUAL / STATIC ONLY`  
Release status: `PUBLIC_MANUAL_STATIC_BASELINE`  
Protocol ID: `COS-P02`  
Canonical artifact: `COS-A02 Evidence Record`  
Depends on: accepted/current `COS-A01`  
Runtime / production: `NOT IMPLEMENTED`

## 1. Purpose

P02 determines which observations, reports, calculations, judgments and interpretations are sufficiently identified, grounded and independently reviewed to influence a Decision. It preserves unknowns, conflicts and limitations without promoting A02 to ground truth, business authority, permission or Decision.

## 2. Inputs and participants

Inputs: accepted/current A01 ID/checksum/cutoff; frozen required/optional source inventory; safe source identities and observed checksums; evidence items and claims; submitter; A03-bound independent reviewer; takeover owner.

Submitter may prepare evidence but cannot admit or accept it. Reviewer authority resolves through accepted A03. Any exception requires a scope-exact accepted human Decision and cannot be self-approved.

## 3. Exact clauses

`P02-C01 Accepted context prerequisite`  
Verify accepted/current A01 ID/checksum/cutoff at protocol start and again before A02 acceptance. Any mismatch or supersession is a legal stop.

`P02-C02 Source identity and integrity`  
Every source has stable identity, authority class, required/optional class, availability, freshness and observed/not-observed checksum state. Filename, path order and model preference are not identity.

`P02-C03 Evidence and interpretation separation`  
Evidence item, claim, interpretation and support-link identities are type-specific and cross-type unique. Interpretations explicitly reference supporting, contradicting and limiting evidence plus assumptions, limitations and confidence.

`P02-C04 Admission disposition`  
Allowed dispositions are admitted, admitted_with_limitations, excluded and not_observed. Limited admission requires grounded, non-conflicted evidence and reviewer-accepted limitations. Unresolved conflict is never Decision-basis eligible.

`P02-C05 Grounding reachability`  
Each admitted item has a source/checksum and a typed supporting, contradicting or limiting link to a claim. Source existence is not proof and grounding is not ground truth.

`P02-C06 Orthogonal unknown/conflict state`  
Availability, freshness, conflict, grounding, admission and derived basis eligibility are separate closed states. Unknown is not zero. Excluded, ungrounded, unresolved-conflict and non-observed items are not basis eligible.

`P02-C07 Independent append-only admission review`  
Every admission Decision creates a stable type-specific append-only admission_event_id bound to evidence item, reviewer actor, accepted A03 ID/checksum/binding, event sequence, prior event/disposition, result disposition, reason and reviewed time. First-event prior values are explicit none. Cross-type identity reuse, overwrite, deletion, unknown predecessor, duplicate sequence, cycle, broken lineage and prior-disposition mismatch fail. Current admission derives only from the strict same-item event chain.

`P02-C08 Partial-success narrowing`  
Partial success exists only when required inventory is non-empty, every required item is admitted with no required gap/conflict, at least one optional item is excluded or grounded/non-conflicted limited, all limitations are accepted by an authorized reviewer and no invoked stage failed or legal-stopped. Required gaps legal-stop; structural forgery fails.

`P02-C09 Non-authority and downstream boundary`  
A02 cannot decide an option, grant permission or create P05 eligibility. P04 may reference only derived basis-eligible item IDs and does not auto-start from A02 acceptance.

`P02-C10 Failure and recovery`  
Schema, parse, checksum and identity failures are failed. Required evidence or authority insufficiency legal-stops. Outcomes and technical failures are separate. No implicit retry or external side effect is authorized.

## 4. Ordered stages

1. accepted_context_binding;
2. source_inventory_integrity;
3. evidence_interpretation_classification;
4. admission_grounding_evaluation;
5. conflict_unknown_limitation_recording;
6. independent_admission_review;
7. a02_acceptance;
8. archive_lineage;
9. automated_external_verification, fixed disabled.

## 5. Reduction and acceptance

Stage statuses: completed, skipped, disabled, not_attempted, legal_stop, failed. Reduction: invoked failed > required legal stop > allowlisted partial success > success. A02 acceptance is a separate append-only event and requires current A01, reviewer/A03 binding, identity isolation, valid admission lineage and explicit assertions.

## 6. Failure envelope and limitations

Non-success carries code, public_message, retryable, side_effect_occurred, last_safe_checkpoint, manual_takeover_required, owner_role and evidence_refs. Raw exceptions, secrets, credentials and unsafe host paths are forbidden.

Known limitations: manual/static only; no external verification, runtime, host business truth, cross-host or production claim.

## 7. Acceptance action scope policy

A03 remains the sole authority for actor, role, binding, governed scope, authority source and validity. This P02-owned policy only narrows which acceptance action may occur inside that valid authority tuple. Exact tuple lookup and exact set membership are mandatory; prefix, substring, hierarchy and artifact-carried allowlists have no authority.

<!-- COS_ACCEPTANCE_SCOPE_POLICY_BEGIN -->
```json
{
  "canonicalization": "UTF-8 JSON; sort_keys=true; separators=(',', ':'); ensure_ascii=false; ordered row array",
  "owner_protocol_id": "COS-P02",
  "policy_rows": [
    {
      "allowed_acceptance_scopes": [
        "M5-B manual static acceptance"
      ],
      "artifact_type": "COS-A02",
      "governed_scope": "M5-B evidence and decision packet",
      "required_role": "evidence_reviewer"
    },
    {
      "allowed_acceptance_scopes": [
        "M5-B manual static acceptance"
      ],
      "artifact_type": "COS-A04",
      "governed_scope": "M5-B evidence and decision packet",
      "required_role": "decision_owner"
    },
    {
      "allowed_acceptance_scopes": [
        "M5-B manual static acceptance"
      ],
      "artifact_type": "COS-A05",
      "governed_scope": "M5-B evidence and decision packet",
      "required_role": "cost_owner"
    }
  ]
}
```
<!-- COS_ACCEPTANCE_SCOPE_POLICY_END -->
