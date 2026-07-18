# ASTER_DOCS COS Adoption Record

Record ID: `ASTER_DOCS-COS-ADOPTION-001`

Status: `PROPOSED / REPLACE_BEFORE_USE`

Decision owner: `REPLACE_BEFORE_USE_HUMAN_DECISION_OWNER`

Effective time: `not_yet_observed`

## 1. Purpose

Use COS at L1 to make documentation decisions inspectable without granting
execution or changing the host's business authority.

## 2. Adoption Level

Selected level: `L1 Decision Governance`

Included surfaces:

- one low-sensitivity documentation decision;
- A01-A04 and A05 when cost analysis is triggered;
- one historical Decision-Only rehearsal.

Excluded surfaces:

- host repository access or mutation;
- A06 execution handoff and A07/A08 acceptance/failure claims;
- external calls, spending, deployment, runtime, and production;
- learning return and A09;
- cross-host validation claims.

## 3. Canonical COS Binding

| Item | Path or URL | SHA-256 | Version |
|---|---|---|---|
| Root package manifest | `https://raw.githubusercontent.com/nickzhuchen66/collaborationos/v0.1.0/PACKAGE_MANIFEST.json` | `0c726b28dc14edaaf40cf8996b73cfa9ebf24069ae832846c9312fdf87a2c018` | `v0.1.0` |
| Gate Pack manifest | `docs/gate-pack-v0.1/PACKAGE_MANIFEST.json` | `c850471d4045678c0cda48dfea6f8cd7f15df65eec2618dfb5c2300564531a54` | `v0.1.0` |
| Manual Operator Flow | `docs/gate-pack-v0.1/MANUAL_OPERATOR_FLOW.md` | `f6aa890dc3c6554d8423f9355a2fe79151bea735816603dcf2e67889d3dbc435` | `v0.1.0` |
| Artifact ownership | `docs/gate-pack-v0.1/ARTIFACT_SELECTION_AND_OWNERSHIP.md` | `5c0f38233b96a33ad819bcc5452c5a39da9ffe4e7005b6885299180998b52b49` | `v0.1.0` |
| Required A01-A05 schemas | `REPLACE_BEFORE_USE_SCHEMA_INVENTORY` | `REPLACE_BEFORE_USE_SCHEMA_INVENTORY_SHA256` | `v0.1.0` |

## 4. Host Authority

- Host source of truth: `REPLACE_BEFORE_USE_PATHS_AND_PRECEDENCE`
- Final project owner: `REPLACE_BEFORE_USE_HUMAN_PROJECT_OWNER`
- Decision owner: `REPLACE_BEFORE_USE_HUMAN_DECISION_OWNER`
- Cost owner: `REPLACE_BEFORE_USE_HUMAN_COST_OWNER_OR_OUT_OF_SCOPE`
- Executor/builder: `outside_L1_scope`
- Independent acceptor: `REPLACE_BEFORE_USE_FUTURE_L2_ROLE`
- Takeover owner: `REPLACE_BEFORE_USE_HUMAN_TAKEOVER_OWNER`
- Promotion/adoption owner: `REPLACE_BEFORE_USE_HUMAN_ADOPTION_OWNER`

Role overlap explicitly allowed: `none_in_this_draft`

## 5. Permission Defaults

```text
execution_authorized=false
host_access_authorized=false
external_call_authorized=false
cost_authorized=false
automatic_retry=false
automatic_acceptance=false
automatic_promotion=false
automatic_canonical_write=false
runtime_authorized=false
production_authorized=false
```

Any separately granted permission must reference a later exact host decision
and scope.

## 6. Artifact Ownership

- Entry Pointer: `governance/cos/COS_HOST_ENTRY_POINTER.md`
- Host Adapter: `governance/cos/COS_HOST_ADAPTER.md`
- A01-A05 instances: `governance/cos/artifacts/`
- Full evidence: `REPLACE_BEFORE_USE_HOST_EVIDENCE_PATH`
- Sensitive evidence owner: `REPLACE_BEFORE_USE_HUMAN_ROLE`
- Learning submission root: `not_adopted_at_L1`

## 7. Initial Rehearsal

- Historical case: `REPLACE_BEFORE_USE_LOW_SENSITIVITY_CASE`
- Rehearsal scope: `A01-A04/A05`
- Reviewer: `REPLACE_BEFORE_USE_INDEPENDENT_HUMAN_ROLE`
- Result: `NOT_YET_RUN`
- Limitations: `not_yet_observed`

## 8. Claim Ceiling

Allowed claim after human acceptance:

> ASTER_DOCS has adopted the CollaborationOS manual/static L1 decision-governance baseline at v0.1.0. Host business authority remains local.

Forbidden claims:

- COS product, runtime, or production adoption;
- cross-host validation or M6 completion;
- automatic authority, acceptance, retry, or promotion;
- modification of COS Core from the host.

## 9. Upgrade and Exit

- Upgrade owner: `REPLACE_BEFORE_USE_HUMAN_ROLE`
- Version review trigger: `new_stable_COS_release`
- Pause trigger: `authority_or_source_precedence_unresolved`
- Exit/retention rule: `REPLACE_BEFORE_USE_HOST_RULE`

## 10. Decision

Disposition: `NOT_YET_DECIDED`

Conditions: `Complete A01/A03, historical rehearsal, checklist, and human review.`

Decision reference: `not_yet_observed`

