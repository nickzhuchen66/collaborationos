# CollaborationOS Target Architecture

Version: `v0.1.0-public-draft`

## 1. Architecture objective

COS separates stable governance semantics from host-specific business systems.
The core owns protocols, artifact contracts, maturity rules, and conformance
examples. A host owns its business data, domain ontology, execution systems,
permissions, and final decisions.

## 2. Six planes

| Plane | COS-owned content |
|---|---|
| Governance | Constitution, public change and contribution rules |
| Core | Methodology and invariants |
| Protocol | P01-P07 ordered collaboration contracts |
| Artifact | A01-A09 schemas and human templates |
| Conformance | fixtures, matrices, and claim boundaries |
| Adoption | reference-based host integration guidance |

Host adapters and domain extensions are optional downstream surfaces. They do
not become part of the public core merely because a host uses them.

## 3. Authority flow

```text
Host source of truth
  -> A01 Context Packet
  -> A02 Evidence Record
  -> A03 Role/Authority Map
  -> A04 Decision Packet
  -> A05 Cost Decision Packet when triggered
  -> A06 Execution Handoff
  -> A07 Change Acceptance Packet
  -> A08 Failure/Manual Takeover Record when needed
  -> A09 Learning Candidate Record
```

Each transition validates the current upstream artifact and does not inherit
authority from a filename, actor identity, or later result.

## 4. Adoption boundary

A host adopts COS by reference:

- pin a COS version;
- map host roles to COS functional roles;
- map host artifacts to A01-A09 without copying business payload into COS;
- declare every permission explicitly;
- retain host-owned decisions and operational authority;
- submit only de-identified learning candidates when desired.

COS must not read, copy, or mutate a host merely because an adapter document
exists.

## 5. Conformance architecture

The public baseline provides strict JSON schemas and synthetic fixtures.
Conformance has three separate claims:

1. **artifact validity**: the instance satisfies its schema;
2. **protocol behavior**: stages, outcomes, stops, and failures follow the
   protocol contract;
3. **governance acceptance**: an authorized human accepts a bounded result.

No one claim substitutes for another.

## 6. Deferred executable surfaces

Executable Skills, Workflows, validators, CLIs, SDKs, host connectors,
schedulers, and production services are outside v0.1.0. If introduced later,
they must preserve the same authority flow and cannot self-authorize, self-
accept, or silently widen permissions.

