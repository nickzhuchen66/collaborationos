# COS Role / Authority Binding Protocol v0.1

Repository role: `FORMAL M5-A IMPLEMENTATION ARTIFACT`  
Conformance mode: `MANUAL / STATIC ONLY`  
Release status: `PUBLIC_MANUAL_STATIC_BASELINE`  
Protocol ID: `COS-P03`  
Canonical artifact: `COS-A03 Role & Authority Map`  
Depends on: `accepted COS-A01`  
Runtime / production: `NOT IMPLEMENTED`

## 1. Purpose

P03 binds functional roles to actors, authority domains, explicit permissions and human-ended takeover chains for one governed scope. It determines who may propose, decide, execute, review, accept and take over; it does not decide what the business choice should be.

P03 must consume an accepted, current A01. It produces A03 only and never auto-starts P02, P04 or execution.

## 2. Inputs and authority

Required inputs：accepted A01 artifact ID/checksum/cutoff/limitations; actor registry; authority sources; governed scope; functional role requirements; complete permission registry; separation-of-duty policy; takeover requirements; human acceptance authority.

Draft, rejected, superseded or legal-stop A01 cannot support successful P03. If A01 becomes stale or superseded during binding, P03 legal-stops and routes back to P01.

## 3. Exact clauses

`P03-C01 Accepted-context prerequisite`  
Verify A01 lifecycle, checksum and cutoff before binding and again before acceptance.

`P03-C02 Functional role taxonomy`  
Roles are reusable functions; actors are host instances. `proposer`, `builder`, `executor`, `evaluator`, `reviewer`, `acceptor` and `takeover_owner` remain separate bindings. Combined implicit roles such as `builder_executor` are invalid.

`P03-C03 Human final authority`  
Exactly one human vision/final authority is required for each governed scope. AI, runtime, validator, CPO, builder and organization-only references cannot be the final endpoint.

`P03-C04 Scope-specific owners`  
Decision, cost, execution, acceptance, takeover, promotion and canonical release owners are explicit. The same human may hold several domains only through separate bindings.

`P03-C05 Explicit deny-by-default permissions`  
Every registry entry is required. Missing entry/field is `failed/schema_invalid`. Each entry records `grant_status`, `declared_allowed` and derived `effective_allowed`. Only `valid + true` allows action. Unknown/malformed with no trustworthy declaration uses `not_observed + false`; it is distinct from a missing entry and from explicit false.

`P03-C06 Separation of decision, execution and acceptance`  
Building/executing does not grant Decision or acceptance. Self-acceptance requires an explicit human exception request and Decision; it is never automatic.

`P03-C07 Missing owner and mismatch`  
Missing human owner, duplicate final owner, authority-source mismatch or AI final authority yields legal stop. P03 does not invent an actor or permission.

`P03-C08 Takeover chain`  
Dangerous capabilities have ordered triggers, acknowledgement owner and final human endpoint. Takeover cannot bypass Decision or permission gates.

`P03-C09 Challenge and escalation`  
Authorized participants may challenge. Permission escalation creates a request and legal stop pending explicit human Decision.

`P03-C10 Human acceptance`  
A03 is accepted by the authorized human authority owner. Technical review is evidence, not final acceptance.

## 4. Functional role taxonomy

Required/reusable roles: `vision_owner`, `authority_owner`, `decision_owner`, `context_preparer`, `context_reviewer`, `architect_reviewer`, `proposer`, `builder`, `executor`, `evaluator`, `reviewer`, `acceptor`, `takeover_owner`, `domain_expert`, `external_mirror`, `host_adapter_maintainer`, `cos_cpo`.

Actor kinds: `human`, `ai_agent`, `deterministic_system`, `organization_ref`. An organization reference must resolve to an accountable human and cannot be the final responsibility endpoint itself.

## 5. Permission registry

Every A03 contains all entries below:

`read_context`, `prepare_artifact`, `propose`, `challenge`, `edit_authorized_scope`, `external_call`, `incur_cost`, `perform_irreversible_action`, `make_decision`, `accept_result`, `takeover`, `promote_core`, `canonical_write`, `release_product`.

Each entry contains scope, granting authority, effective time, expiry/revocation, constraints and:

- `grant_status`: `valid`, `expired`, `revoked`, `unknown`, `malformed`;
- `declared_allowed`: JSON boolean `true`/`false` or string `not_observed`;
- `effective_allowed`: JSON boolean.

Mechanical truth rules:

| grant status | declared | effective | meaning |
|---|---|---:|---|
| valid | true | true | allowed in exact scope |
| valid | false | false | normal explicit deny |
| expired/revoked | true or false | false | historical declaration, no current action |
| unknown/malformed | not_observed | false | evidence-preserving deny-to-act |

All other combinations are schema-invalid. No role name implicitly grants a dangerous permission.

## 6. Ordered stages

1. `accepted_context_consumption`;
2. `authority_domain_inventory`;
3. `actor_registry`;
4. `functional_role_binding`;
5. `permission_binding`;
6. `separation_of_duty_check`;
7. `takeover_chain_binding`;
8. `authority_mismatch_check`;
9. `human_authority_acceptance`;
10. `automated_permission_enforcement`, fixed `disabled` in M5-A.

P03 required stages cannot be skipped. Downstream stages after a legal stop or failure are `not_attempted`, never rewritten as skipped/completed.

## 7. State, outcomes and acceptance

P03 stage status uses `completed`, `skipped`, `disabled`, `not_attempted`, `legal_stop`, `failed`. Its top-level outcome is only `success`, `legal_stop` or `failed`; `partial_success` is forbidden and a claimed partial outcome fails validation.

Reduction priority is invoked failure, required legal stop, success. A03 lifecycle is `draft`, `under_review`, `accepted`, `rejected`, `superseded` and is independent of protocol outcome.

Successful A03 acceptance requires exactly one human final authority, complete authority-domain ownership, complete permission registry, resolved separation-of-duty status, human-ended takeover chains, current accepted A01 lineage and authorized human acceptance.

## 8. Failure, recovery and takeover

Legal stop examples: missing human final owner, authority mismatch, AI final authority, permission escalation, self-acceptance conflict, missing human takeover endpoint, superseded A01.  
Failed examples: missing permission entry, malformed permission truth-state, merged implicit role, unsupported partial success, downstream auto-start.

Stable failure envelopes are secret-safe and record last safe checkpoint, side effects, retryability, takeover owner and evidence. No implicit retry or permission escalation is authorized.

## 9. Dependency and downstream boundary

P01 precedes P03. After accepted A01, P02 and P03 may prepare independently. Future P04 may start only with accepted A02 plus accepted A03 and verified shared A01 artifact ID/checksum/cutoff lineage.

M5-A does not create A02, implement P04, start P04/P05, execute permissions or write to a host.

## 10. Conformance and host adapter points

M5-A fixtures cover human final authority, mismatch, permission completeness/truth-state, separation of duty, takeover, superseded context, unsupported partial success and no downstream auto-start (N06-N12, N15-N16, N22-N24).

Host adapters may map actor identities and authority source references. They may not redefine the Core role taxonomy, make a domain role final COS authority, grant undeclared permission, reverse-control host business Roadmap, or copy host business schema into A03.

Known limitations: manual/static candidate only; no enforcement runtime, CLI, Skill, SDK, production integration, cross-host validation or product release.
