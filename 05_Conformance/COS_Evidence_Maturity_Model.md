# COS Evidence Maturity Model

Version: `v0.1.0-public-draft`

Evidence maturity describes where a governance claim has actually been
observed and accepted. It is not a quality score and must not be inferred from
document count, agreement, or project naming.

## States

| State | Meaning |
|---|---|
| `OBSERVED_SINGLE_HOST` | observed in one host or one bounded event |
| `VALIDATED_SAME_HOST` | positive and failure behavior validated within one host |
| `SUPPORTED_CROSS_HOST` | the exact clause/version/common scope is independently supported in structurally different hosts |
| `PROMOTED_CORE` | separately reviewed and human-authorized as canonical core material |
| `DOMAIN_EXTENSION_ONLY` | useful but intentionally limited to a host or domain extension |
| `REJECTED_OR_SUPERSEDED` | rejected or replaced while lineage is preserved |

## Promotion rules

1. A second mention is not cross-host support.
2. Planned scope is not exercised scope.
3. A successful result without failure-path evidence cannot establish robust
   same-host validation.
4. Cross-host support binds exact clause, version, common exercised scope,
   evidence, independent review, and final-human acceptance.
5. `SUPPORTED_CROSS_HOST` never automatically becomes `PROMOTED_CORE`.
6. Promotion must preserve the review head, human decision, canonical change,
   release identity, and final append-only learning event without circular
   self-reference.
7. Domain-specific ontology and host business outcomes do not become core
   governance rules merely because they were useful once.

## Claim ceiling

The v0.1.0 public repository contains a manual/static baseline and synthetic
conformance fixtures. It does not claim completed heterogeneous-host validation
or `PROMOTED_CORE` status for every clause.

