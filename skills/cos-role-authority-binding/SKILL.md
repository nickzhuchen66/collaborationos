---
name: cos-role-authority-binding
description: Prepare or inspect a COS A03 Role and Authority Map with explicit actors, functional roles, deny-by-default permissions, separation of duty, escalation, and human-ended takeover. Use when project roles, decision ownership, acceptance authority, permissions, or takeover responsibility are ambiguous.
---

# COS Role and Authority Binding

Prepare an A03 draft from an accepted/current A01. Do not grant authority by
capability, title, or composition.

## Procedure

1. Read `references/contract.md`, verify its source bindings, then verify the accepted A01 identity, lifecycle, cutoff, and limitations.
2. Inventory actor facts separately from reusable functional roles.
3. Resolve final consequential authority to exactly one human for the governed scope.
4. Bind decision, cost, execution, acceptance, takeover, promotion, and canonical-release owners separately.
5. Complete the exact 14-entry permission registry. Missing is schema failure; unknown is `not_observed` and deny-to-act.
6. Derive `effective_allowed=true` only from `grant_status=valid` plus `declared_allowed=true` in the exact scope and time window.
7. Check builder, executor, evaluator, and acceptor separation.
8. Bind dangerous capabilities to an acknowledgement owner and final human takeover endpoint.
9. Produce a JSON A03 draft and a concise authority-gap summary.
10. Run the public validator, then stop for authorized human acceptance.

## Output boundary

Return the A03 draft or findings, unresolved owners, mismatches, and escalation
routes. State `permissions_enforced_at_runtime=false`,
`downstream_started=false`, and `execution_authorized=false`.

Never infer permission from a role, make an AI the final authority, merge
functional roles, start P04, or resolve a missing human owner automatically.
