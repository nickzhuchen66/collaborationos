# CollaborationOS Host Adoption Kit v0.1

Status: `PUBLIC_ADOPTION_GUIDE / MANUAL_STATIC / NO_EXECUTION_AUTHORITY`

## Purpose

This kit explains how another project can reference COS without copying or
overriding COS core authority. The adopting project remains the owner of its
business data, decisions, permissions, execution, acceptance, and risk.

New adopters should begin with the shorter
[Getting Started hub](../getting-started/README.md), then return here for the
formal manual and canonical templates.

## Documents

- [New Host Project Adoption Manual](COS_NEW_HOST_PROJECT_ADOPTION_MANUAL_v0.1.md)
- [Host Entry Pointer](templates/COS_HOST_ENTRY_POINTER_TEMPLATE_v0.1.md)
- [Host Adoption Record](templates/COS_HOST_ADOPTION_RECORD_TEMPLATE_v0.1.md)
- [Host Adapter](templates/COS_HOST_ADAPTER_TEMPLATE_v0.1.md)
- [`PACKAGE_MANIFEST.json`](PACKAGE_MANIFEST.json)

Dependencies:

- [Gate Pack](../gate-pack-v0.1/README.md)
- [Manual Operator Flow](../gate-pack-v0.1/MANUAL_OPERATOR_FLOW.md)
- [Artifact Selection and Ownership](../gate-pack-v0.1/ARTIFACT_SELECTION_AND_OWNERSHIP.md)
- [Evidence Maturity Model](../../05_Conformance/COS_Evidence_Maturity_Model.md)

## Deferred packages

Executable Skills and Workflows are not included in v0.1.0. Inventory or design
documents do not constitute executable packages.

## Authority boundary

This kit cannot make a business decision, authorize access or execution,
accept its own implementation, authorize retry or promotion, or modify a host
source of truth. Adoption by reference does not make ordinary host activity
cross-host COS validation.
