# COS A03 Role & Authority Map Template v0.1

Repository role: `FORMAL M5-A IMPLEMENTATION ARTIFACT`  
Conformance mode: `MANUAL / STATIC ONLY`  
Release status: `PUBLIC_MANUAL_STATIC_BASELINE`  
Schema: `COS_Role_Authority_Map_v0.1.schema.json`  
Owner protocol: `COS-P03`

> This view supports human preparation and acceptance. A03 is the sole canonical role/permission artifact. Do not infer authority from an actor's capability, title or A01 participation.

## Identity and Context

- Artifact ID / created at / source authority:
- Governed scope:
- Accepted A01 artifact ID/checksum/cutoff:
- A01 limitations accepted:
- Confirm A01 is current and lifecycle=`accepted`:

## Actor Registry

For each actor:

- Actor ID / kind (`human / ai_agent / deterministic_system / organization_ref`):
- Safe identity ref:
- Accountable human owner actor ID:

## Role Bindings

Create separate entries for every functional role. Never merge builder/executor or infer permissions from role names.

- Binding ID / functional role / actor ID:
- Exact scope / authority source:
- Effective / expiry:

## Authority Domains

Assign final direction, decision, cost, execution, acceptance, takeover, promotion and canonical release separately. Final direction must resolve to exactly one human.

## Permission Matrix

Complete all 14 entries: `read_context`, `prepare_artifact`, `propose`, `challenge`, `edit_authorized_scope`, `external_call`, `incur_cost`, `perform_irreversible_action`, `make_decision`, `accept_result`, `takeover`, `promote_core`, `canonical_write`, `release_product`.

For each permission:

- Actor IDs / exact scope / granting authority:
- `grant_status`:
- `declared_allowed`: boolean or `not_observed`:
- Derived `effective_allowed`:
- Effective / expiry / revocation:
- Constraints:

Only `valid + true` can be effectively allowed. Unknown/malformed declarations remain `not_observed + false`. A missing entry is schema failure, not unknown evidence.

## Separation of Duty

- Builder/executor/evaluator/acceptor conflicts:
- Open or resolved status:
- Human exception Decision, if any:
- Self-acceptance allowed only by accepted exception:

## Takeover and Escalation

- Dangerous capability / trigger:
- Ordered actor chain:
- Acknowledgement owner:
- Final human endpoint:
- Permission escalation route and legal-stop owner:

## Gaps and Lineage

- Missing owners / mismatches / unknowns / limitations:
- Supersedes / superseded by:

## Protocol Run and Human Acceptance

Record all ten P03 stages. `automated_permission_enforcement` is disabled. P03 supports `success / legal_stop / failed`, never partial success, and must not start downstream protocols.

- Human acceptor actor ID / authority source / accepted at:
- Assertion evidence:
- Result and artifact lifecycle:
