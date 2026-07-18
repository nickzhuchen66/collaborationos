# ASTER_DOCS COS Host Adapter v0.1

Status: `PROPOSED / REPLACE_BEFORE_USE`

Host: `ASTER_DOCS-SYNTHETIC`

Adopted COS level: `L1`

Host adoption decision: `not_yet_observed`

## 1. Purpose and Non-Goals

Purpose: map COS L1 functions to ASTER_DOCS host-owned governance locations.

Non-goals:

- does not modify COS Core;
- does not replace host business authority;
- does not authorize execution, cost, retry, acceptance, or promotion;
- does not create cross-host evidence by itself.

## 2. Authority Ownership

| Surface | Owner | Adapter ruling |
|---|---|---|
| COS protocols, schemas, and maturity | CollaborationOS | read-only pinned dependency |
| Host business truth | `REPLACE_BEFORE_USE_HOST_AUTHORITY` | host-owned |
| Host implementation | `outside_L1_scope` | no authority from this adapter |
| Final decision | `REPLACE_BEFORE_USE_HUMAN_ROLE` | never delegated to AI/runtime |
| COS learning submission | `not_adopted_at_L1` | no submission or promotion route |

Conflict rule: host business facts remain host-owned; COS contract conflicts
route to the human adoption owner and stop downstream use until resolved.

## 3. Role Binding

| COS function | Host role | Authority | Prohibited |
|---|---|---|---|
| project/final owner | `REPLACE_BEFORE_USE` | final host governance | delegation to AI/runtime |
| context preparer/reviewer | `REPLACE_BEFORE_USE` | prepare/review A01 | invent business facts |
| evidence submitter/admission reviewer | `REPLACE_BEFORE_USE` | prepare/review A02 | self-admit unsupported evidence |
| decision owner | `REPLACE_BEFORE_USE_HUMAN_ROLE` | final A04 disposition | post-hoc or AI final decision |
| cost owner | `REPLACE_BEFORE_USE` | A05 when triggered | unknown cost coerced to zero |
| executor/builder | `outside_L1_scope` | none | A06 or host mutation |
| independent acceptor | `outside_L1_scope` | none | acceptance claim at L1 |
| takeover owner | `REPLACE_BEFORE_USE_HUMAN_ROLE` | resolve ambiguity | implicit retry |
| learning/promotion owner | `outside_L1_scope` | none | automatic Core change |

## 4. Artifact Crosswalk

| COS artifact | Host source/output | Precedence and use |
|---|---|---|
| A01 Context Packet | `governance/cos/artifacts/A01/` | references current host truth; does not replace it |
| A02 Evidence Record | `governance/cos/artifacts/A02/` | records admitted and excluded evidence |
| A03 Role/Authority Map | `governance/cos/artifacts/A03/` | accepted host authority binding |
| A04 Decision Packet | `governance/cos/artifacts/A04/` | records human-owned decision |
| A05 Cost Decision | `governance/cos/artifacts/A05/` | used only when cost trigger exists |
| A06 Execution Handoff | `outside_L1_scope` | prohibited |
| A07 Change Acceptance | `outside_L1_scope` | prohibited |
| A08 Failure/Takeover | `outside_L1_scope` | host incident route remains available |
| A09 Learning Candidate | `outside_L1_scope` | no learning bridge adopted |

## 5. Protocol Applicability

| Protocol | Host mechanism | Disposition | Limitation |
|---|---|---|---|
| P01 Context Recovery | host context + A01 | `APPLICABLE` | manual/static |
| P02 Evidence Admission | host evidence + A02 | `APPLICABLE` | manual review |
| P03 Authority Binding | host roles + A03 | `APPLICABLE` | human acceptance required |
| P04 Decision Before Instruction | host decision + A04/A05 | `APPLICABLE` | Decision-Only |
| P05 Execution Handoff | none | `NOT_APPLICABLE_AT_L1` | no A06 |
| P06 Acceptance/Failure | host incident governance only | `NOT_APPLICABLE_AT_L1` | no A07 claim |
| P07 Learning/Promotion | none | `NOT_APPLICABLE_AT_L1` | no A09 or promotion |

## 6. Domain Extension Boundary

Host-specific ontology, business schema, and project rules remain under:

- `REPLACE_BEFORE_USE_HOST_DOMAIN_LOCATIONS`

## 7. Failure and Takeover Route

- Failure evidence root: `governance/cos/failures/`
- Stable public error owner: `REPLACE_BEFORE_USE_ROLE`
- Takeover owner: `REPLACE_BEFORE_USE_HUMAN_ROLE`
- Retry rule: `no implicit retry; separate decision required`
- Sensitive-data handling: `REPLACE_BEFORE_USE_HOST_POLICY`

## 8. Learning Bridge

- Full host evidence stays at: `REPLACE_BEFORE_USE_HOST_PATH`
- Redaction owner: `not_yet_assigned`
- Submission path: `not_adopted_at_L1`
- Automatic promotion: `false`

## 9. Permission Envelope

```text
automatic_apply=false
automatic_acceptance=false
automatic_retry=false
automatic_promotion=false
automatic_canonical_write=false
automatic_external_call=false
automatic_cost_approval=false
```

Additional host-specific false permissions:

- `host_access_authorized=false`
- `runtime_authorized=false`
- `production_authorized=false`

## 10. Acceptance and Limitations

- Adapter reviewer: `REPLACE_BEFORE_USE_HUMAN_ROLE`
- Human acceptance reference: `not_yet_observed`
- Known limitations: `historical_rehearsal_not_yet_run`
- Next permitted adoption gate: `complete_L1_review_only`

