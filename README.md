# CollaborationOS

CollaborationOS (COS) is a manual/static governance framework for consequential
human-AI collaboration. It helps teams manage evidence, authority, decisions,
controlled execution, independent acceptance, failure takeover, and learning
without transferring final accountability to an AI system.

## Release status

Version: `v0.1.0-public-draft`

This repository provides:

- seven governance protocols, P01-P07;
- nine strict artifact schema/template pairs, A01-A09;
- 126 conformance fixtures and four manual matrices;
- a manual/static Gate Pack;
- a guide for adopting COS in another project.

This repository does **not** provide an automated validator, executable Skill,
Workflow runtime, CLI, SDK, agent framework, SaaS product, host connector, or
production authority. It does not claim completed cross-host validation.

## Start here

1. Read the [Constitution](00_Governance/COS_Constitution.md).
2. Review the [Methodology](01_Core/COS_Methodology.md) and
   [Target Architecture](01_Core/COS_Target_Architecture.md).
3. Follow the [Protocol System Map](02_Protocols/COS_Protocol_System_Map_v0.1.md).
4. Select artifacts from the
   [Gate Pack Artifact Register](03_Schemas_and_Templates/COS_Gate_Pack_Artifact_Register_v0.1.md).
5. Use the [Manual Operator Flow](docs/gate-pack-v0.1/MANUAL_OPERATOR_FLOW.md).
6. For a new project, follow the
   [Host Adoption Manual](docs/adoption-kit-v0.1/COS_NEW_HOST_PROJECT_ADOPTION_MANUAL_v0.1.md).

## Core rules

- Human final authority is explicit and cannot be inferred from participation.
- Evidence admission is separate from evidence submission.
- Decision precedes executable instruction.
- Permissions default to false and are scoped to a specific action.
- Execution success is separate from independent acceptance.
- Failure evidence is preserved; retry is never implicit.
- Learning candidates do not automatically modify the COS core.
- A host project retains its own business source of truth.

## Repository map

| Path | Purpose |
|---|---|
| `00_Governance/` | Public Constitution only |
| `01_Core/` | Public methodology and architecture |
| `02_Protocols/` | P01-P07 and their dependency map |
| `03_Schemas_and_Templates/` | A01-A09 strict schemas and human templates |
| `05_Conformance/` | Manual matrices and synthetic fixtures |
| `docs/gate-pack-v0.1/` | Operator-facing manual/static package |
| `docs/adoption-kit-v0.1/` | New-host adoption guide and templates |
| `examples/synthetic/` | Non-authoritative synthetic walkthrough |

## License and brand

The public draft is prepared for release under the
[Apache License 2.0](LICENSE). See [NOTICE](NOTICE) for attribution.

The non-self [public package manifest](PACKAGE_MANIFEST.json) binds every other
file in this draft after final validation.

The license does not grant a right to imply endorsement by the upstream
CollaborationOS project. `CollaborationOS` is used here as the project name; no
registered trademark claim is made.

## Contributing and security

See [CONTRIBUTING.md](CONTRIBUTING.md),
[CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md), and [SECURITY.md](SECURITY.md).

Do not submit host secrets, personal data, proprietary evidence, credentials,
or confidential project records in issues or pull requests.
