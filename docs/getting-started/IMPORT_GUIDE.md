# CollaborationOS Import Guide

## What “Import” Means

COS is not a package that gains authority when installed. Importing COS means:

1. pinning an immutable public baseline;
2. recording that baseline in host-owned governance files;
3. mapping host roles and artifacts to COS by reference;
4. keeping COS read-only from the host;
5. making every live permission and decision separately in the host project.

Do not fork COS Core into a private editable copy and treat local edits as
canonical COS.

## Stable Baseline

Use the stable public release, not `main`, for a governed adoption.

| Item | Pinned value |
|---|---|
| Release | `v0.1.0` |
| Release page | `https://github.com/nickzhuchen66/collaborationos/releases/tag/v0.1.0` |
| Commit | `b08db73c244be57807d99c9960ecf167496ebc65` |
| Root manifest SHA-256 | `0c726b28dc14edaaf40cf8996b73cfa9ebf24069ae832846c9312fdf87a2c018` |
| Gate Pack manifest SHA-256 | `c850471d4045678c0cda48dfea6f8cd7f15df65eec2618dfb5c2300564531a54` |

Later releases require a separate host upgrade decision. Never silently repoint
historical artifacts to `main` or a newer tag.

## Method A: Reference the GitHub Release

**Recommended for:** public projects and teams that can reach GitHub.

No COS files need to be copied into the host repository. Record the release
URL, commit, root manifest hash, Gate Pack path, and adopted level in the Host
Entry Pointer.

Optional local integrity check:

```bash
curl -L \
  https://raw.githubusercontent.com/nickzhuchen66/collaborationos/v0.1.0/PACKAGE_MANIFEST.json \
  -o COS_PACKAGE_MANIFEST_v0.1.0.json

shasum -a 256 COS_PACKAGE_MANIFEST_v0.1.0.json
```

Expected SHA-256:

```text
0c726b28dc14edaaf40cf8996b73cfa9ebf24069ae832846c9312fdf87a2c018
```

The downloaded manifest is integrity evidence, not a host decision or runtime
dependency.

## Method B: Use a Read-Only Sibling Checkout

**Recommended for:** local AI development workspaces containing multiple
projects.

```bash
git clone --branch v0.1.0 --depth 1 \
  https://github.com/nickzhuchen66/collaborationos.git \
  ../CollaborationOS

git -C ../CollaborationOS rev-parse HEAD
shasum -a 256 ../CollaborationOS/PACKAGE_MANIFEST.json
```

Expected commit and manifest values are listed above. Record the sibling path
in the Host Entry Pointer, but keep the path configurable across machines.

Rules:

- do not edit the checkout from the host project;
- do not place host payloads, evidence, or adapters inside it;
- do not infer host access from filesystem proximity;
- upgrade only through a separate human-owned host decision.

## Method C: Use an Approved Read-Only Snapshot

**Recommended for:** offline, restricted, or internally mirrored environments.

1. obtain the exact `v0.1.0` source archive through an approved channel;
2. extract it outside the host’s business-data directories;
3. verify `PACKAGE_MANIFEST.json` against the pinned root SHA-256;
4. verify required member hashes against the manifest;
5. record snapshot owner, location, source, and acquisition date;
6. make the snapshot read-only under the host’s normal controls;
7. reference it in the Host Entry Pointer and Adoption Record.

An internal mirror or snapshot is a dependency copy. It is not a new COS
authority and must not contain local changes presented as upstream COS.

## Create the Host Entry Files

Whichever import method you choose, create these host-owned files:

```text
<host-project>/
  governance/
    cos/
      COS_HOST_ENTRY_POINTER.md
      COS_HOST_ADOPTION_RECORD.md
      COS_HOST_ADAPTER.md
```

Use the canonical templates in
[`docs/adoption-kit-v0.1/templates/`](../adoption-kit-v0.1/templates/) or adapt
the [synthetic starter host](../../examples/starter-host/README.md).

## Minimum Binding to Record

The host must record:

- stable COS release, commit, and manifest SHA-256;
- adopted level and included/excluded surfaces;
- host source-of-truth locations and precedence;
- human decision, cost, independent acceptance, and takeover roles;
- host-local locations for A01-A09 instances and evidence;
- every applicable permission, defaulting to false;
- pause, exit, and version-upgrade ownership;
- the exact claim ceiling.

## Fail-Closed Import Checks

Stop before adoption if:

- the release, commit, or manifest hash cannot be verified;
- final human ownership is unknown;
- host source-of-truth precedence is unresolved;
- an adapter would require copying secrets or business payloads into COS;
- the first use requires execution, spending, external calls, or production;
- an AI or runtime would become its own decision owner or acceptor;
- the team expects installation alone to authorize a live action.

Continue with the [10-Minute Quickstart](10_MINUTE_QUICKSTART.md) after selecting
and verifying one import method.

