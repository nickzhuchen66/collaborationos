# COS P06 Independent Acceptance, Failure & Takeover Protocol v0.1

Status: `M5-C CANDIDATE / MANUAL-STATIC CONTRACT / NOT RUNTIME`

## Purpose

P06 verifies one accepted A06 attempt, keeps builder evidence separate from independent acceptance, and preserves failure, rollback and takeover as append-only facts.

## Contract

1. Bind one accepted/current/non-expired A06 and exact attempt ID.
2. Record builder evidence as an append-only A07 event chain. Stable event ID, sequence, prior ID/checksum and canonical event checksum are mandatory; the current head is derived.
3. Recompute exact operation inventory, pre/postimages, protected parity, transients, side effects, test invocation and assertion reachability against A06.
4. Resolve the independent result acceptor through accepted A03 acceptance authority and `accept_result=true`. Self-acceptance and role/scope/source laundering fail closed.
5. Keep artifact lifecycle, protocol outcome, builder result, acceptance result and A04 business disposition separate.
6. Append failure-final, rollback and takeover events to A08. Unknown/not-observed facts remain explicit and history is never overwritten.
7. Rollback truth table: ADD deletes only an owner-matched authorized postimage; MODIFY restores only from exact current postimage to frozen preimage; REMOVE recreates only when absent and preimage valid. Any mismatch routes to manual takeover.
8. Manual takeover requires a current human A03 takeover binding and cannot widen scope. A retry recommendation/request is non-operative; a new attempt needs a new accepted A06 and human authorization.

## Ordered stages

`bind_execution_handoff -> admit_builder_change_evidence -> verify_scope_integrity_and_side_effects -> verify_tests_and_assertion_reachability -> resolve_independent_acceptor_authority -> record_independent_acceptance -> record_failure_final -> evaluate_and_record_rollback -> acknowledge_manual_takeover -> reduce_p06_outcome`

## Invariants

- builder evidence is not acceptance;
- technical success/rollback cannot rewrite A04;
- no required gap can reduce to partial success;
- A07/A08 event identity is unique, append-only, acyclic and order-independent;
- no implicit retry, history deletion, production execution, promotion or canonical write.
