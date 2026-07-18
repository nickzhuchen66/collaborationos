# COS M5-A Manual Conformance Matrix v0.1

Repository role: `FORMAL M5-A IMPLEMENTATION EVIDENCE`  
Conformance mode: `MANUAL / STATIC ONLY`  
Release status: `PUBLIC_MANUAL_STATIC_BASELINE`  
Protocols: `COS-P01`, `COS-P03`  
Artifacts: `COS-A01`, `COS-A03`  
Runtime / production / cross-host claim: `NONE`

## 1. Qualification contract

Every fixture is a test envelope containing a target schema, expected schema validity, named assertions, expected protocol outcome, expected artifact lifecycle and the tested artifact. Schema invalidity is only a valid test result when the scenario explicitly expects it. Semantic negative scenarios must hit their named predicate; an unrelated parse/schema failure does not count.

The local static qualifier implements only the JSON Schema Draft 2020-12 keyword subset exercised by the two formal M5-A schemas. It is bounded implementation evidence, not a general validator, CLI, runtime or production capability.

## 2. Positive controls

| Fixture | Assertion | Expected |
|---|---|---|
| `M5A-P01-POS-01-context-success.json` | `M5A-AST-P01-POS` | A01 schema valid; P01 success; lifecycle accepted |
| `M5A-P03-POS-01-authority-success.json` | `M5A-AST-P03-POS` | A03 schema valid; P03 success; lifecycle accepted; downstream false |

## 3. Negative and boundary scenarios

| Scenario | Fixture | Assertion ID(s) | Schema | Expected protocol/artifact result | Mechanical predicate |
|---|---|---|---|---|---|
| N01 | `M5A-N01-required-source-stale.json` | `M5A-AST-01` | valid | legal_stop / rejected | required source disposition stale |
| N02 | `M5A-N02-optional-source-stale.json` | `M5A-AST-02` | valid | partial_success / accepted | optional stale + limitation + reviewer acceptance |
| N03 | `M5A-N03-formal-source-conflict.json` | `M5A-AST-03` | valid | legal_stop / rejected | unresolved formal conflict retained |
| N04 | `M5A-N04-checksum-mismatch.json` | `M5A-AST-04` | valid | failed / rejected | qualifier independently hashes frozen expected Test Fact bytes and fixture observed bytes; artifact digest must equal observed and differ from expected; subsequent stages not_attempted and side effect false |
| N05 | `M5A-N05-state-classification-collision.json` | `M5A-AST-05` | valid | failed / rejected | same item_id appears in multiple state arrays |
| N06 | `M5A-N06-missing-human-final-authority.json` | `M5A-AST-06` | valid | legal_stop / rejected | final owner does not resolve to registered human |
| N07 | `M5A-N07-authority-source-mismatch.json` | `M5A-AST-07` | valid | legal_stop / rejected | binding authority source mismatches governed source |
| N08 | `M5A-N08-ai-final-authority.json` | `M5A-AST-08` | valid | legal_stop / rejected | final owner actor kind is ai_agent |
| N09 | `M5A-N09-missing-permission-entry.json` | `M5A-AST-09`, `M5A-AST-24B` | invalid | failed / rejected | required permission entry absent |
| N10 | `M5A-N10-permission-escalation.json` | `M5A-AST-10` | valid | legal_stop / rejected | unknown declaration deny-to-act pending human Decision |
| N11 | `M5A-N11-self-acceptance-conflict.json` | `M5A-AST-11` | valid | legal_stop / rejected | builder + acceptor conflict without exception |
| N12 | `M5A-N12-takeover-without-human-endpoint.json` | `M5A-AST-12` | valid | legal_stop / rejected | takeover final endpoint is not human |
| N13 | `M5A-N13-unknown-coerced-to-zero.json` | `M5A-AST-13` | invalid | failed / rejected | unknown array contains numeric zero |
| N14 | `M5A-N14-host-payload-or-secret-leak.json` | `M5A-AST-14` | valid | failed / rejected | sensitive marker found in candidate artifact |
| N15 | `M5A-N15-context-superseded-during-p03.json` | `M5A-AST-15` | invalid | legal_stop / rejected | A01 lifecycle superseded and verified_current false |
| N16 | `M5A-N16-unauthorized-downstream-start.json` | `M5A-AST-16` | invalid | failed / rejected | downstream_started true violates fixed false |
| N17 | `M5A-N17-invoked-optional-stage-failed.json` | `M5A-AST-17` | valid | failed / rejected | optional invoked=true and status failed forces failed |
| N18 | `M5A-N18-optional-stage-skipped.json` | `M5A-AST-18` | valid | success / accepted | no declared optional source/limitation; skipped not invoked |
| N19 | `M5A-N19-disabled-stages-recorded.json` | `M5A-AST-19A/B` | valid | P01/P03 success | external resolution and automated enforcement disabled and observable |
| N20 | `M5A-N20-downstream-not-attempted-after-stop.json` | `M5A-AST-20` | valid | legal_stop / rejected | stages after legal stop are not_attempted except fixed disabled |
| N21 | `M5A-N21-partial-success-accepted-with-limitations.json` | `M5A-AST-21` | valid | partial_success / accepted | declared source_id missing/stale/unreadable + accepted limitation |
| N22 | `M5A-N22-p03-partial-success-rejected.json` | `M5A-AST-22` | invalid | unsupported partial_success / rejected | P03 outcome enum excludes partial_success |
| N23 | `M5A-N23-a01-participant-authority-laundering.json` | `M5A-AST-23`, `23B`-`23H` | mixed as specified | failed/legal_stop / rejected | primary participant grant invalid; related variants prove self-accept, expiry, reviewer mismatch, A03/bootstrap exclusivity, frozen actor-kind resolution, not-yet-effective and unregistered actor rejection |
| N24 | `M5A-N24-unknown-permission-declaration.json` | `M5A-AST-24A/B/C` | mixed as specified | success primary / accepted | unknown=not_observed+false valid; missing entry invalid; valid explicit false valid |

## 4. State and outcome reachability

Required aggregate coverage:

- Stage status: `completed`, `skipped`, `disabled`, `not_attempted`, `legal_stop`, `failed`;
- P01 outcomes: `success`, `partial_success`, `legal_stop`, `failed`;
- P03 outcomes: `success`, `legal_stop`, `failed`; `partial_success` must be rejected;
- Non-success runs include the complete stable failure envelope;
- Review/archive cannot lower the reduction priority from failed or legal stop.

Key vectors:

| Assertion | Stage vector | Expected reduction |
|---|---|---|
| `M5A-AST-17` | supplemental invoked + failed; later not_attempted | failed |
| `M5A-AST-18` | supplemental skipped + not invoked; external disabled | success |
| `M5A-AST-19A/B` | fixed external/enforcement stages disabled | success if all required stages pass |
| `M5A-AST-20` | required stage legal_stop; downstream not_attempted | legal_stop |
| `M5A-AST-21` | required complete; optional limitation; review complete | partial_success + accepted-with-limitations |
| `M5A-AST-22` | P03 attempts unsupported partial_success | schema invalid + rejected |
| `M5A-AST-23` | A01 participant fact carries permission field | schema invalid + no authority grant |
| `M5A-AST-24A/B/C` | unknown declaration / missing entry / explicit false | valid deny / schema failed / valid deny |

Retry-02 P01-C08/bootstrap closure vectors:

| Assertion | Related variant in N23 | Schema | Required result |
|---|---|---|---|
| `M5A-AST-23B` | preparer and reviewer are the same actor without accepted human exception | valid | P01 legal_stop; A01 rejected |
| `M5A-AST-23C` | bootstrap expires before cutoff/review | valid | P01 legal_stop; A01 rejected |
| `M5A-AST-23D` | review actor ID differs from declared reviewer | valid | P01 legal_stop; A01 rejected |
| `M5A-AST-23E` | accepted A03 reference and bootstrap coexist | invalid by exclusive authority branch | P01 failed; A01 rejected |
| `M5A-AST-23F` | bootstrap human_actor_ref resolves to AI-labelled actor ref | valid shape, invalid authority semantics | P01 legal_stop; A01 rejected |
| `M5A-AST-23G` | bootstrap effective_at is later than cutoff and review time | valid | P01 legal_stop; A01 rejected |
| `M5A-AST-23H` | bootstrap actor ref is absent from independently frozen actor authority facts | valid shape, unverified authority | P01 legal_stop; A01 rejected |

Retry-03 actor authority oracle freezes `ACTOR_AUTHORITY_FACTS.json` with owner, source, canonical facts checksum and actor-kind mappings. The positive P01 bootstrap must resolve to a registered `human`; known AI and unregistered refs must legal-stop. The qualifier recomputes the fact checksum and compares both `effective_at <= cutoff` and `effective_at <= reviewed_at`.

Retry-02 checksum oracle contract:

1. `TEST_FACT_SNAPSHOT.json` freezes expected source bytes and expected SHA-256 independently from N04.
2. N04 contains observed source bytes and an observed digest, but no expected digest.
3. Qualifier recomputes both digests, checks the snapshot's expected digest, checks the artifact digest equals observed, and requires observed != expected.
4. N04 also requires a required source, integrity stage failed/invoked, no side effect, all later non-disabled stages not_attempted, top-level failed and lifecycle rejected.

Retry-02 time-format qualification uses strict timezone-aware RFC 3339 positive and negative self-tests. This packet-local assertion remains static Harness evidence, not a general JSON Schema implementation.

## 5. Boundary assertions

1. A01 participant facts never bind a role or grant permission; A03 is the sole canonical role/permission artifact.
2. Future P04 requires accepted A02 plus accepted A03 and verified common accepted A01 artifact ID/checksum/cutoff lineage.
3. No fixture creates A02, P04, P05, runtime, external call, cost, promotion or canonical write.
4. No host-specific business schema, payload, secret or production data is used.
5. Local static qualification cannot be promoted to runtime, end-to-end, cross-host or production evidence.

## 6. Manual disposition

### 6.1 Packet-only candidate qualification

This pre-copy mode requires exact 26 fixture names, all expected schema-validity results, all named assertion predicates, full state/outcome reachability, exact `33 ADD + 2 MODIFY + 0 REMOVE` candidate scope, protected repo parity, absence of all 33 ADD targets in the formal repo and exact preimages for both MODIFY targets.

### 6.2 Post-copy implementation qualification

This mode requires all 35 formal repo targets to equal the frozen candidate hashes, exact `33 ADD + 2 MODIFY + 0 REMOVE` execution scope, protected repo parity, no forbidden scope, exact 26 fixture names, all expected schema-validity results, all named assertion predicates and full state/outcome reachability.

### 6.3 Formal M5-A acceptance

Formal acceptance requires independent post-implementation conformance plus a later Final Human Decision Owner acceptance. It cannot be inferred from packet-only candidate qualification or local post-copy implementation qualification alone.

Any unexplained mismatch is a hard stop. No implicit retry or test relaxation is allowed; a byte change after freeze requires a new candidate identity.
