# COS A01 Context Packet Template v0.1

Repository role: `FORMAL M5-A IMPLEMENTATION ARTIFACT`  
Conformance mode: `MANUAL / STATIC ONLY`  
Release status: `PUBLIC_MANUAL_STATIC_BASELINE`  
Schema: `COS_Context_Packet_v0.1.schema.json`  
Owner protocol: `COS-P01`

> This is a human preparation/review view. The JSON artifact is canonical for field conformance. Do not place secrets, credentials, personal sensitive data or host business payload here.

## Identity

- Artifact ID:
- Created at:
- Source authority:
- Host/project safe refs:
- Lifecycle: `draft / under_review / accepted / rejected / superseded`

## Recovery Scope

- Purpose:
- In scope:
- Out of scope:
- As-of cutoff:
- Host-provided freshness rule:

## Participants

- Preparer actor fact:
- Independent reviewer actor fact:
- Confirm both are run participation facts only: `true`

## Source Register

For every source record:

- Source ID / safe ref / authority class:
- Required or optional:
- Checksum status, algorithm, value and not-observed reason:
- Observed time / freshness:
- Lineage ref:
- One disposition only: `authoritative_current / current_supplemental / stale / conflicting / missing / unknown / unreadable`

## State at Cutoff

Record each item exactly once under `current`, `decided`, `pending`, `blocked` or `superseded` with item ID, safe summary, owner, source IDs, Decision ref or `not_decided`, validity, lineage and checksum.

## Conflicts, Staleness and Gaps

- Formal conflicts and resolution owner:
- Stale required/optional sources:
- Unknowns:
- Not observed:
- Not attempted:
- Known limitations with source ID/disposition/reason:

## Authority for A01 Acceptance

Choose exactly one:

- Accepted A03 artifact ID/checksum/cutoff; or
- Bootstrap authority source/checksum/human actor/scope/effective/expiry/supersede/grant basis, with allowed action fixed to `accept_COS-A01_only`.

## Protocol Run

Record all nine P01 stages in order, each with status, invoked flag and reason. Apply failure > legal stop > allowlisted partial success > success. Include a stable failure envelope whenever outcome is not success.

## Review and Acceptance

- Reviewer and review time:
- Assertion results and evidence refs:
- Accepted limitation IDs:
- Result:
- Confirm accepted A01 does not create a Decision or grant role/permission:

## Lineage

- Supersedes / superseded by, or explicit `not_applicable`:
