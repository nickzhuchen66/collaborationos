# CollaborationOS 10-Minute L1 Setup

## Scope

This quickstart prepares a **draft L1 Decision Governance scaffold**. It does
not complete host adoption, validate a real project, or authorize execution.

Use synthetic or low-sensitivity metadata while learning the structure. Keep
host secrets and business payloads outside COS and outside public issues.

## Before the Timer Starts

You need:

- one named human project owner;
- one known host source-of-truth location;
- one place for host-local governance files;
- one selected import method from the [Import Guide](IMPORT_GUIDE.md);
- permission to create documentation in the host project.

If any item is unavailable, stop and resolve it rather than inventing a value.

## Minute 0-2: Choose L1 and Create the Folder

Create a host-owned location:

```bash
mkdir -p governance/cos
```

Choose `L1 Decision Governance`. Initial scope is A01-A05 only. Execution
handoff, acceptance claims, retry, promotion, runtime, and production remain
outside scope.

## Minute 2-4: Copy the Three Starter Files

From a local COS checkout:

```bash
cp examples/starter-host/governance/cos/COS_HOST_ENTRY_POINTER.md governance/cos/
cp examples/starter-host/governance/cos/COS_HOST_ADOPTION_RECORD.md governance/cos/
cp examples/starter-host/governance/cos/COS_HOST_ADAPTER.md governance/cos/
```

These are synthetic examples. Change every `ASTER_DOCS` value and every
`REPLACE_BEFORE_USE` marker before review. Do not mark them accepted yet.

Without a local checkout, copy the canonical templates from
[`docs/adoption-kit-v0.1/templates/`](../adoption-kit-v0.1/templates/).

## Minute 4-6: Pin the Stable Baseline

In the Entry Pointer and Adoption Record, record:

```text
release=v0.1.0
commit=b08db73c244be57807d99c9960ecf167496ebc65
root_manifest_sha256=0c726b28dc14edaaf40cf8996b73cfa9ebf24069ae832846c9312fdf87a2c018
gate_pack_manifest_sha256=c850471d4045678c0cda48dfea6f8cd7f15df65eec2618dfb5c2300564531a54
```

Record the chosen release URL, sibling checkout, or approved snapshot path.

## Minute 6-8: Replace the Host Facts

Replace the synthetic values with:

- host project name and stable ID;
- human project and decision owner;
- source-of-truth paths and precedence;
- evidence and governance locations;
- independent reviewer and takeover owner, or `not_yet_assigned`;
- included and excluded project surfaces;
- known pause and upgrade owner.

Use `unknown`, `not_yet_assigned`, or `not_observed` honestly. Never coerce a
missing fact to false, zero, or approval.

## Minute 8-10: Freeze the Safe Draft Boundary

Confirm the draft contains these defaults:

```text
execution_authorized=false
host_access_authorized=false
external_call_authorized=false
cost_authorized=false
automatic_retry=false
automatic_acceptance=false
automatic_promotion=false
automatic_canonical_write=false
runtime_authorized=false
production_authorized=false
```

Set all three documents to `PROPOSED` or `DRAFT`, then record the next allowed
step:

```text
Prepare A01 and A03, perform one historical Decision-Only rehearsal, and route
the complete adoption record to a named human decision owner.
```

## What You Have After 10 Minutes

You have:

- a pinned COS dependency;
- three host-owned draft governance files;
- an explicit L1 scope and permission boundary;
- a clear next human decision gate.

You do **not** yet have:

- accepted host adoption;
- authority to access or modify a host;
- A06 execution handoff or A07 acceptance;
- permission to retry, promote, call an API, spend, deploy, or produce;
- cross-host validation or runtime capability.

## Finish the Adoption

1. Complete the [Host Adoption Checklist](HOST_ADOPTION_CHECKLIST.md).
2. Follow the [full Adoption Manual](../adoption-kit-v0.1/COS_NEW_HOST_PROJECT_ADOPTION_MANUAL_v0.1.md).
3. Prepare A01 and A03 for the adopted scope.
4. Review one historical Decision-Only rehearsal.
5. Obtain a separate final-human adoption decision.

