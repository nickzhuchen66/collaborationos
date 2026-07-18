# COS Context Recovery Protocol v0.1

Repository role: `FORMAL M5-A IMPLEMENTATION ARTIFACT`  
Conformance mode: `MANUAL / STATIC ONLY`  
Release status: `PUBLIC_MANUAL_STATIC_BASELINE`  
Protocol ID: `COS-P01`  
Canonical artifact: `COS-A01 Context Packet`  
Runtime / production: `NOT IMPLEMENTED`

## 1. Purpose

P01在明确scope与cutoff下恢复当前状态、既有Decision、未决项、阻塞、superseded历史及其来源资格，形成可由未参与前序对话者独立复核的A01。

P01不创造Decision，不裁决业务真相，不授予执行、成本、promotion或canonical write权限，也不替代host或COS authority。

## 2. Inputs and authority

Required inputs：

1. recovery request、purpose、in/out scope与`as_of` cutoff；
2. required authority source register及optional supplemental source classes；
3. source safe references、authority classes、freshness rules和observed checksums；
4. current accepted A03 reference，或只授权A01 acceptance的可验证`bootstrap_authority_ref`；
5. context preparer、independent reviewer和manual takeover owner。

来源身份不得按mtime、文件名、路径顺序或AI偏好推断。A01只能复述来源记录，不可升级为Decision或business truth。

## 3. Participants and permissions

| Participant | May | Must not |
|---|---|---|
| context requester | declare purpose and scope | accept unreviewed A01 |
| context preparer | inventory, verify and assemble | self-accept or create Decision |
| context reviewer | check sources, states and limitations | rewrite canonical source |
| source authority owner | resolve source conflict/staleness | delegate final authority implicitly |
| takeover owner | receive legal stop/failure | auto-retry or bypass authority |
| host adapter maintainer | provide safe mappings | copy host business payload into Core |

Permissions are consumed from accepted A03. Before A03 exists, bootstrap authority is limited to A01 acceptance and must contain authority source, checksum, human actor, governed scope, effective time and expiry/supersede condition.

## 4. Exact clauses

`P01-C01 Scope and cutoff`  
Every run declares safe host/project identity, purpose, boundaries, cutoff and preparer. Missing scope or cutoff is a legal stop.

`P01-C02 Authority-aware source inventory`  
Inventory required and optional sources before reading content. Each source has one disposition at the cutoff: `authoritative_current`, `current_supplemental`, `stale`, `conflicting`, `missing`, `unknown` or `unreadable`.

`P01-C03 Source integrity and lineage`  
Every source has stable identity, authority class, observed time and lineage. Readable sources require checksum algorithm/value. Missing, unknown or unreadable sources use `checksum_status=not_observed` with a reason. Mismatch is failed, not legal stop.

`P01-C04 State classification`  
Items are classified exactly once as `current`, `decided`, `pending`, `blocked` or `superseded`. Each item has owner, source refs, decision ref or `not_decided`, cutoff validity, lineage and checksum.

`P01-C05 Staleness and conflict detection`  
Required stale/conflicting sources trigger legal stop. The protocol never silently selects a winner.

`P01-C06 Gap and limitation disclosure`  
`unknown`, `not_observed`, `not_attempted`, missing and unreadable remain distinct and are never serialized as zero or silently filled.

`P01-C07 Self-contained handoff`  
A01 contains enough scope, source, state, conflict, limitation and next-gate detail for an independent reviewer without hidden chat memory.

`P01-C08 Independent review and acceptance`  
The preparer cannot accept their own packet. A `partial_success` A01 becomes accepted only when the independent reviewer explicitly accepts the allowlisted optional limitations.

## 5. Ordered stages

| Order | Stage | Entry | Exit |
|---:|---|---|---|
| 1 | `scope_and_cutoff` | recovery request | scope/cutoff complete |
| 2 | `required_source_inventory` | stage 1 completed | required/optional inventory frozen |
| 3 | `source_integrity_verification` | inventory frozen | checksums/dispositions verified |
| 4 | `state_classification` | required sources readable | five classes assembled |
| 5 | `staleness_and_conflict_check` | state assembled | no unresolved required conflict |
| 6 | `packet_assembly` | required baseline passes | A01 draft complete |
| 7 | `independent_context_review` | A01 draft | lifecycle accepted/rejected |
| 8 | `supplemental_context_collection` | optional class declared/candidate exists | completed, failed or skipped with reason |
| 9 | `external_resolution` | never entered in M5-A | fixed `disabled` |

The supplemental stage may be skipped only when the optional class is undeclared, not applicable or has no candidate. A declared source ID that is missing, stale or unreadable is a limitation and may reach allowlisted partial success; it is not a skip.

## 6. State and outcome reduction

Stage status enum: `completed`, `skipped`, `disabled`, `not_attempted`, `legal_stop`, `failed`.

Top-level outcome enum: `success`, `partial_success`, `legal_stop`, `failed`.

Reduction priority:

```text
any invoked stage failed
  > any required-stage legal_stop
  > allowlisted partial_success
  > success
```

P01 is the only M5-A protocol that permits partial success. It requires all required sources/stages to pass, no failed/legal-stop stage, only declared optional evidence missing/stale/unreadable, complete limitations and explicit reviewer acceptance. Any invoked optional-stage failure yields `failed`.

Artifact lifecycle is separate: `draft`, `under_review`, `accepted`, `rejected`, `superseded`. A legal stop is not an artifact lifecycle value.

## 7. Legal stops and failures

Legal stop examples: missing cutoff, required source stale/conflicting without authoritative replacement, missing acceptance authority.  
Failed examples: checksum mismatch, schema invalidity, classification collision, secret/host payload leakage, invoked optional-stage contract failure.

Every non-success result carries a secret-safe failure envelope with code, public message, retryable, side-effect flag, last safe checkpoint, takeover requirement, owner role and evidence refs. No implicit retry is authorized.

## 8. Output acceptance

Output is one A01 candidate conforming to `COS_Context_Packet_v0.1.schema.json`. A01 can be accepted only when:

- required sources and integrity checks pass;
- state item IDs are unique across all five classes;
- conflicts, stale sources and limitations are explicit;
- accepted A03 or bounded bootstrap authority is verified;
- independent review assertions pass;
- artifact checksum and lineage are recorded.

Accepted A01 is an auditable context statement, not a Decision or ground truth.

## 9. Conformance and limitations

M5-A fixtures cover success, partial success, legal stop and failed; every stage status is reachable. Required scenarios include N01-N05, N13-N15, N17-N21 and N23.

Known limitations: manual/static execution only; freshness thresholds remain host-supplied; no automatic source discovery, external resolution, runtime validation or production connection; no cross-host validation claim.

## 10. Host adapter points

Host adapters may provide safe identity mapping, source register, freshness rules and redacted references. They may not redefine P01 status semantics, copy business schema/payload into A01, or treat A01 as host business authority.
