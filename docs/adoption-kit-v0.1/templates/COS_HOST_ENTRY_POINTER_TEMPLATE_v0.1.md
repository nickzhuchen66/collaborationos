# <Host Project> CollaborationOS Entry Pointer

Status: `<ACTIVE / PAUSED / RETIRED>`

Host project: `<name>`

Adopted COS level: `<L0 / L1 / L2 / L3>`

Adoption owner: `<human name or stable role>`

## Canonical dependency

- COS release URL, commit, or approved local snapshot: `<reference>`
- Gate Pack path: `<path>`
- Gate Pack manifest SHA-256: `<64 lowercase hex>`
- Adopted baseline: `<version / Decision / date>`

CollaborationOS is read-only from this host. Host business truth and final Decisions remain host-owned.

## Host-local routing

- Adoption Record: `<host path>`
- Host Adapter: `<host path>`
- COS artifact root: `<host path>`
- Host source of truth: `<host path(s)>`
- Failure/takeover records: `<host path>`
- Learning submissions: `<host path or not adopted>`

## Permission boundary

This pointer does not authorize execution, external calls, cost, retry, acceptance, promotion, canonical write, host access, runtime or production.

## Operator start

1. Read the Adoption Record.
2. Read the Host Adapter.
3. Confirm current A01 Context and A03 Authority.
4. Stop if authority, evidence, cost, version or scope is unknown.
