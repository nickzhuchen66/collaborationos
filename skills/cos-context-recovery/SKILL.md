---
name: cos-context-recovery
description: Prepare or inspect a bounded COS A01 Context Packet from approved source facts, preserving precedence, conflicts, superseded facts, unknowns, and limitations. Use when project state is stale, distributed, disputed, or needs a self-contained handoff before any Decision or instruction.
---

# COS Context Recovery

Prepare an A01 draft. Never accept it or infer business truth.

## Procedure

1. Read `references/contract.md`; verify `references/source-bindings.json` against an explicitly supplied COS repository root.
2. Freeze purpose, in-scope, out-of-scope, and RFC3339 UTC cutoff before reading approved source content.
3. Inventory required and optional source identities, authority classes, and freshness rules.
4. Record source dispositions without choosing a winner: `authoritative_current`, `current_supplemental`, `stale`, `conflicting`, `missing`, `unknown`, or `unreadable`.
5. Classify each state item exactly once as current, decided, pending, blocked, or superseded.
6. Keep unknown, not-observed, and not-attempted separate from zero, false, and not-applicable.
7. Record conflicts, limitations, lineage, and the human owner required to resolve each gap.
8. Produce a JSON A01 draft conforming to the canonical schema and a concise human summary.
9. Run the public validator. Route validation failure to the artifact owner; do not repair authority facts by assumption.
10. Stop for independent human review.

## Output boundary

Return the A01 draft or findings, source and limitation summary, unresolved
human gates, `decision_created=false`, and `execution_authorized=false`.

Never discover sources automatically, read a Host without authority, expose
payloads, start P02/P03/P04, or retry after a stop.
