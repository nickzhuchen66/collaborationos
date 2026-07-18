# Security Policy

## Supported release

The current public release is a manual/static specification. It contains no
supported runtime service. Security reports may still concern schema bypass,
authority escalation, secret exposure, unsafe examples, dependency confusion,
or documentation that could cause dangerous execution.

## Reporting

Do not disclose a suspected vulnerability, credential, private host path, or
personal data in a public issue. Use GitHub private vulnerability reporting when
enabled. Until that channel is configured, do not publish sensitive details;
contact the repository owner through their GitHub profile and request a private
reporting channel.

Include:

- affected version and files;
- the violated authority or safety boundary;
- minimal synthetic reproduction;
- observed and expected behavior;
- whether any real data, access, write, cost, or external call occurred.

## Response boundary

Acknowledgment is best-effort and no SLA is promised. A documentation or schema
fix does not retroactively authorize host action. Security fixes should preserve
failure evidence, avoid implicit retry, and receive independent review before
release.
