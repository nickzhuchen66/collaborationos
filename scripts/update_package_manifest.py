#!/usr/bin/env python3
"""Regenerate the non-self public package manifest from the Git index."""

from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "PACKAGE_MANIFEST.json"


def tracked_files() -> list[Path]:
    completed = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    paths = []
    for raw in completed.stdout.split(b"\0"):
        if not raw:
            continue
        path = Path(raw.decode("utf-8"))
        if path != Path("PACKAGE_MANIFEST.json"):
            paths.append(path)
    return sorted(paths, key=lambda item: item.as_posix())


def main() -> int:
    current = json.loads(MANIFEST.read_text(encoding="utf-8"))
    members = []
    for relative in tracked_files():
        data = (ROOT / relative).read_bytes()
        members.append(
            {
                "path": relative.as_posix(),
                "bytes": len(data),
                "sha256": hashlib.sha256(data).hexdigest(),
            }
        )
    current["member_count"] = len(members)
    current["members"] = members
    MANIFEST.write_text(json.dumps(current, indent=2, ensure_ascii=True) + "\n", encoding="utf-8")
    print(f"updated {MANIFEST.relative_to(ROOT)} with {len(members)} members")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
