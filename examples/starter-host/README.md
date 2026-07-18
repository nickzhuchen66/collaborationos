# Synthetic Starter Host

This directory provides a copy-and-adapt scaffold for a fictional project,
`ASTER_DOCS`. It demonstrates the three host-owned files needed before formal
L1 adoption work begins.

It is **not** an accepted host, real evidence, a completed adoption, or an
execution package.

## Contents

```text
governance/
  cos/
    COS_HOST_ENTRY_POINTER.md
    COS_HOST_ADOPTION_RECORD.md
    COS_HOST_ADAPTER.md
```

## Use

From a CollaborationOS checkout:

```bash
mkdir -p <host-project>/governance/cos
cp examples/starter-host/governance/cos/*.md <host-project>/governance/cos/
```

Then, inside the host project:

```bash
rg -n 'ASTER_DOCS|REPLACE_BEFORE_USE' governance/cos
```

Replace every result before human review. Keep all files in draft/proposed
state until the host's named human owner makes an adoption decision.

## What Must Change

- host name and stable ID;
- release/snapshot location if not using the public GitHub release;
- host source-of-truth and governance paths;
- human owner, decision owner, reviewer, and takeover owner;
- included and excluded surfaces;
- evidence, failure, and learning routes;
- effective time and human decision reference.

The v0.1.0 release, commit, and manifest hashes may remain when that exact
baseline is adopted and independently verified.

## Next

1. Complete the [10-Minute Quickstart](../../docs/getting-started/10_MINUTE_QUICKSTART.md).
2. Use the [Host Adoption Checklist](../../docs/getting-started/HOST_ADOPTION_CHECKLIST.md).
3. Follow the [full Adoption Manual](../../docs/adoption-kit-v0.1/COS_NEW_HOST_PROJECT_ADOPTION_MANUAL_v0.1.md).
4. Prepare host-owned A01 and A03 only after the routing and authority facts are
   known.

