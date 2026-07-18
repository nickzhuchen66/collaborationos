# COS M5-C Manual Conformance Matrix v0.1

Repository role: `M5-C CANDIDATE EVIDENCE`  
Conformance mode: `MANUAL / STATIC ONLY`  
Protocols: `COS-P05`, `COS-P06`  
Artifacts: `COS-A06`, `COS-A07`, `COS-A08`  
Runtime / production / cross-host claim: `NONE`

## Exact fixture matrix

| Fixture | Assertion | Target | Predicate |
|---|---|---|---|
| `M5C-P05-POS-01-exact-no-cost-handoff` | `M5C-AST-01` | `COS-A06` | `SEMANTIC_VALID` |
| `M5C-P05-POS-02-cost-gated-handoff` | `M5C-AST-02` | `COS-A06` | `SEMANTIC_VALID` |
| `M5C-P06-POS-01-independent-accepted` | `M5C-AST-03` | `COS-A07` | `SEMANTIC_VALID` |
| `M5C-P06-POS-02-optional-limitations-partial-success` | `M5C-AST-04` | `COS-A07` | `SEMANTIC_VALID` |
| `M5C-P05-STOP-01-eligibility-false` | `M5C-AST-05` | `COS-A06` | `SEMANTIC_VALID` |
| `M5C-P05-STOP-02-stale-or-superseded-authority` | `M5C-AST-06` | `COS-A06` | `SEMANTIC_VALID` |
| `M5C-P05-STOP-03-required-cost-unknown` | `M5C-AST-07` | `COS-A06` | `SEMANTIC_VALID` |
| `M5C-P06-STOP-01-preexecution-acceptor-unavailable` | `M5C-AST-08` | `COS-A07` | `SEMANTIC_VALID` |
| `M5C-N01-upstream-lineage-mismatch` | `M5C-AST-09` | `COS-A06` | `LINEAGE_MISMATCH` |
| `M5C-N02-forged-p05-eligibility` | `M5C-AST-10` | `COS-A06` | `FORGED_ELIGIBILITY` |
| `M5C-N03-permission-registry-missing` | `M5C-AST-11` | `COS-A06` | `SCHEMA_INVALID` |
| `M5C-N04-permission-crosswalk-widening` | `M5C-AST-12` | `COS-A06` | `PERMISSION_WIDENING` |
| `M5C-N05-builder-or-executor-self-acceptance` | `M5C-AST-13` | `COS-A06` | `SELF_ACCEPTANCE` |
| `M5C-N06-wildcard-alias-or-overlap-scope` | `M5C-AST-14` | `COS-A06` | `INVALID_PATH_SCOPE` |
| `M5C-N07-operation-precondition-mismatch` | `M5C-AST-15` | `COS-A06` | `OPERATION_PRECONDITION` |
| `M5C-N08-protected-surface-drift` | `M5C-AST-16` | `COS-A07` | `PROTECTED_DRIFT` |
| `M5C-N09-cost-or-external-permission-mismatch` | `M5C-AST-17` | `COS-A06` | `COST_PERMISSION_MISMATCH` |
| `M5C-N10-irreversible-action-without-authority` | `M5C-AST-18` | `COS-A06` | `IRREVERSIBLE_PERMISSION_MISSING` |
| `M5C-N11-posthoc-or-unreachable-acceptance` | `M5C-AST-19` | `COS-A06` | `SCHEMA_INVALID` |
| `M5C-N12-extra-missing-operation-or-transient` | `M5C-AST-20` | `COS-A07` | `OPERATION_INVENTORY_MISMATCH` |
| `M5C-N13-test-summary-without-invocation` | `M5C-AST-21` | `COS-A07` | `ASSERTION_UNREACHABLE` |
| `M5C-N14-technical-success-rewrites-business-decision` | `M5C-AST-22` | `COS-A07` | `BUSINESS_DECISION_REWRITE` |
| `M5C-N15-unknown-or-not-observed-coerced` | `M5C-AST-23` | `COS-A07` | `UNKNOWN_COERCION` |
| `M5C-N16-false-partial-success` | `M5C-AST-24` | `COS-A07` | `FALSE_PARTIAL_SUCCESS` |
| `M5C-N17-same-id-retry-or-lineage-cycle` | `M5C-AST-25` | `COS-A08` | `RETRY_LINEAGE_CYCLE` |
| `M5C-N18-a07-duplicate-fork-or-order-dependence` | `M5C-AST-26` | `COS-A07` | `EVENT_CHAIN_INVALID` |
| `M5C-N19-add-rollback-foreign-replacement` | `M5C-AST-27` | `COS-A08` | `ROLLBACK_ADD_FOREIGN` |
| `M5C-N20-modify-rollback-current-hash-mismatch` | `M5C-AST-28` | `COS-A08` | `ROLLBACK_MODIFY_HASH` |
| `M5C-N21-remove-rollback-target-occupied` | `M5C-AST-29` | `COS-A08` | `ROLLBACK_REMOVE_OCCUPIED` |
| `M5C-N22-rollback-unauthorized-or-owner-mismatch` | `M5C-AST-30` | `COS-A08` | `ROLLBACK_UNAUTHORIZED` |
| `M5C-N23-rollback-success-preserves-evidence` | `M5C-AST-31` | `COS-A08` | `SEMANTIC_VALID` |
| `M5C-N24-a08-overwrite-fork-or-cycle` | `M5C-AST-32` | `COS-A08` | `EVENT_CHAIN_INVALID` |
| `M5C-N25-failure-envelope-checkpoint-or-secret-defect` | `M5C-AST-33` | `COS-A08` | `FAILURE_ENVELOPE_INVALID` |
| `M5C-N26-takeover-owner-invalid-stale-or-nonhuman` | `M5C-AST-34` | `COS-A08` | `TAKEOVER_OWNER_INVALID` |
| `M5C-N27-takeover-scope-expansion-or-partial-state-laundering` | `M5C-AST-35` | `COS-A08` | `TAKEOVER_SCOPE_EXPANSION` |
| `M5C-N28-retry-recommendation-treated-as-authorization` | `M5C-AST-36` | `COS-A08` | `SCHEMA_INVALID` |

## Qualification boundary

All 36 exact paths and `M5C-AST-01..36` are immutable for A01. Adjacent mutation probes belong to packet Harness evidence and do not create formal fixture paths. Qualification must prove schema validity, target-predicate reachability, exact P05/P06 stage topology, the complete 14-permission registry, event-chain integrity, rollback truth tables, human authority, no implicit retry and zero executable/runtime surface.

Candidate qualification does not authorize repo copy, M5-C start, acceptance, M5-D/E, runtime or production.
