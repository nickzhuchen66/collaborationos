# Getting Started with CollaborationOS

This directory is the shortest public path from discovering COS to preparing a
safe host-local adoption draft.

> CollaborationOS is adopted by reference, not installed as an authority. The
> host keeps its business truth, permissions, execution systems, and final
> decisions.

## Choose Your Path

| Goal | Time | Start here | Result |
|---|---:|---|---|
| Understand how COS enters another project | 5 minutes | [Import Guide](IMPORT_GUIDE.md) | Select a pinned reference method |
| Prepare an L1 host scaffold | 10 minutes | [10-Minute Quickstart](10_MINUTE_QUICKSTART.md) | Three draft host governance files |
| Review adoption readiness | 10-20 minutes | [Host Adoption Checklist](HOST_ADOPTION_CHECKLIST.md) | Explicit pass, limitation, or stop |
| Complete formal host adoption | Project-dependent | [Full Adoption Manual](../adoption-kit-v0.1/COS_NEW_HOST_PROJECT_ADOPTION_MANUAL_v0.1.md) | Human-accepted host adoption record |
| See a safe worked structure | 5 minutes | [Starter Host](../../examples/starter-host/README.md) | Synthetic files to adapt, never adopt unchanged |

## Recommended First Adoption

For a new project, use `L1 Decision Governance`:

1. pin the stable COS release;
2. create a Host Entry Pointer, Adoption Record, and Host Adapter;
3. keep execution, access, external calls, cost, retry, acceptance, promotion,
   runtime, and production permissions false;
4. perform one historical Decision-Only rehearsal;
5. have a human owner accept, adapt, defer, or reject the adoption;
6. consider `L2 Governed Change` only through a separate later decision.

## Adoption Levels

| Level | Name | Practical meaning |
|---|---|---|
| `L0` | Reference | Use COS principles and link the canonical baseline |
| `L1` | Decision Governance | Use A01-A05; no execution handoff or acceptance claim |
| `L2` | Governed Change | Add bounded A06-A08 with independent acceptance |
| `L3` | Learning Bridge | Add redacted A09 learning return; no automatic promotion |

The quickstart prepares an `L1` draft. It does not complete adoption or grant
permission to access, execute, spend, retry, accept, promote, or publish.

## After Adoption: Use COS on One Decision

At `L1`, the operating sequence ends after the human decision:

```text
A01 Context
  -> A02 Evidence + A03 Authority
  -> human A04 Decision
  -> optional A05 Cost Decision
  -> stop
```

Do not create A06 or begin implementation as part of an L1 Decision-Only flow.
Use the [Manual Operator Flow](../gate-pack-v0.1/MANUAL_OPERATOR_FLOW.md) for the
full stage checklist.

Only after a separate human decision adopts `L2` may a host add:

```text
A06 bounded execution handoff
  -> host-owned implementation mechanism
  -> A07 independent acceptance
  -> or A08 failure / manual takeover
  -> optional A09 learning candidate through a separate route
```

Execution evidence does not accept itself. Failure never grants retry, and A09
never promotes itself.

## Public Support Paths

- Ask adoption questions in
  [GitHub Discussions](https://github.com/nickzhuchen66/collaborationos/discussions).
- Report a bounded documentation or contract defect through
  [GitHub Issues](https://github.com/nickzhuchen66/collaborationos/issues).
- Never include host secrets, credentials, private paths, personal data, or
  proprietary evidence in a public discussion or issue.
