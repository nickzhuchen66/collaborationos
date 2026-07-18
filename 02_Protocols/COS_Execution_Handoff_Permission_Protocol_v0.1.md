# COS P05 Execution Handoff & Permission Protocol v0.1

Status: `M5-C CANDIDATE / MANUAL-STATIC CONTRACT / NOT RUNTIME`

## Purpose

P05 converts an accepted Decision into one independently accepted, exact, time-bound execution handoff. It does not execute, retry, publish, promote or canonical-write.

## Required inputs and ownership

- accepted/current A01, A03 and A04 with common lineage;
- accepted/current A05 whenever the cost trigger applies;
- A03 remains sole actor, role, permission and takeover authority;
- A04 remains sole business Decision authority; A05 only supplies the cost-gate result.

## Contract

1. Derive `execution_may_start` only from the eight frozen predicates in proposal P05-C01. Any false, unknown or not-observed predicate denies start.
2. Bind one immutable attempt ID and closed ADD/MODIFY/REMOVE inventories. Reject absolute, escaping, wildcard, symlink, alias, duplicate and ancestor-overlap paths.
3. Preserve the complete accepted-A03 14-permission projection. Operations are not permissions. Paid calls require `external_call`, `incur_cost` and accepted A05. Rollback is not a permission.
4. Freeze repository/environment, cost, secrets, side effects, acceptance checks, preimages, protected surfaces, rollback predicates, stop threshold and human takeover owner before acceptance.
5. Separate issuer, builder, executor, human handoff acceptor, result acceptor and takeover owner. Builder/executor self-acceptance is forbidden.
6. Bind the acceptance event to the canonical A06 body checksum. Mutation after acceptance invalidates the handoff.
7. P05 issues an accepted or rejected A06 only. A new attempt requires a new identity and explicit human authorization.

## Ordered stages

`bind_upstream_authority -> validate_decision_and_cost_eligibility -> freeze_attempt_scope_and_preconditions -> resolve_permissions_and_environment -> freeze_acceptance_and_recovery_contract -> record_independent_handoff_acceptance -> issue_accepted_execution_handoff -> reduce_p05_outcome`

Stage status: `completed | skipped | disabled | not_attempted | legal_stop | failed`. Outcome: `success | partial_success | legal_stop | failed`. Invoked failure outranks legal stop; partial success is not allowed to hide a required gap.

## Invariants

- no A03 permission expansion;
- no action before independent A06 acceptance;
- no unknown cost action;
- no path outside exact scope;
- no implicit execution, retry, promotion or canonical write;
- external calls and production connection remain zero in this M5-C implementation.
