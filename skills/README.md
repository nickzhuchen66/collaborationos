# CollaborationOS Skills

This directory contains the public Wave 1 COS Skills for Codex-compatible
agents. Each Skill is a bounded preparation or inspection capability. A Skill
does not accept its own output, make a business decision, authorize execution,
or continue into another protocol automatically.

| Skill | COS artifact or control | Typical use |
|---|---|---|
| [`cos-context-recovery`](cos-context-recovery/SKILL.md) | A01 | Recover a bounded, source-aware project context |
| [`cos-role-authority-binding`](cos-role-authority-binding/SKILL.md) | A03 | Make actors, roles, permissions, and takeover explicit |
| [`cos-decision-packet-preparation`](cos-decision-packet-preparation/SKILL.md) | A04 | Prepare a human-owned decision before instruction |
| [`cos-review-circuit-breaker`](cos-review-circuit-breaker/SKILL.md) | Review control | Stop open-ended candidate and review loops |

## Install

Install Skills only into absent targets:

```bash
for skill in cos-context-recovery cos-role-authority-binding \
  cos-decision-packet-preparation cos-review-circuit-breaker
do
  target="$HOME/.codex/skills/$skill"
  test ! -e "$target" || { echo "Refusing to overwrite: $target" >&2; exit 1; }
  cp -R "skills/$skill" "$target"
done
```

Start a new Codex task so the registry is reloaded. The source checkout remains
the canonical protocol/schema source; do not copy private Host evidence into
the Skill directory.

Validate the public bindings before use:

```bash
python3 tools/cos_wave1.py verify-bindings --cos-root .
```

## Contribution rule

Keep Skills small and authority-neutral. Contract changes must update the
corresponding public protocol, schema or review profile, source bindings, tests,
and package manifest in the same pull request.
