#!/usr/bin/env python3
"""Verify public JSON, package-manifest, links, and sensitive-path boundaries."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "PACKAGE_MANIFEST.json"
MARKDOWN_LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
ABSOLUTE_PRIVATE = re.compile(
    re.escape("/" + "Users/")
    + "|"
    + re.escape("/" + "private/tmp")
    + "|"
    + re.escape("/" + "private/var")
    + r"|[A-Za-z]:\\\\"
    + "Users"
    + r"\\\\"
)


def reject_duplicates(pairs: list[tuple[str, object]]) -> dict[str, object]:
    output: dict[str, object] = {}
    for key, value in pairs:
        if key in output:
            raise ValueError(f"duplicate JSON key: {key}")
        output[key] = value
    return output


def tracked_files() -> list[Path]:
    completed = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    return sorted(
        (Path(raw.decode("utf-8")) for raw in completed.stdout.split(b"\0") if raw),
        key=lambda item: item.as_posix(),
    )


def verify_manifest(tracked: list[Path]) -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"), object_pairs_hook=reject_duplicates)
    expected_paths = [path for path in tracked if path != Path("PACKAGE_MANIFEST.json")]
    members = manifest["members"]
    if manifest["member_count"] != len(members):
        raise ValueError("package manifest member_count mismatch")
    if [row["path"] for row in members] != [path.as_posix() for path in expected_paths]:
        raise ValueError("package manifest path inventory mismatch")
    for path, row in zip(expected_paths, members, strict=True):
        data = (ROOT / path).read_bytes()
        if row["bytes"] != len(data) or row["sha256"] != hashlib.sha256(data).hexdigest():
            raise ValueError(f"package manifest mismatch: {path}")


def verify_json(tracked: list[Path]) -> int:
    count = 0
    for path in tracked:
        if path.suffix == ".json":
            json.loads((ROOT / path).read_text(encoding="utf-8"), object_pairs_hook=reject_duplicates)
            count += 1
    return count


def verify_links(tracked: list[Path]) -> int:
    checked = 0
    for path in tracked:
        if path.suffix != ".md":
            continue
        text = (ROOT / path).read_text(encoding="utf-8")
        for match in MARKDOWN_LINK.finditer(text):
            target = unquote(match.group(1).split("#", 1)[0])
            if not target or target.startswith(("http://", "https://", "mailto:")):
                continue
            resolved = (ROOT / path.parent / target).resolve()
            resolved.relative_to(ROOT)
            if not resolved.exists():
                raise ValueError(f"missing local Markdown link: {path} -> {target}")
            checked += 1
    return checked


def verify_private_paths(tracked: list[Path]) -> None:
    for path in tracked:
        if path.suffix.lower() not in {".md", ".json", ".py", ".yml", ".yaml"}:
            continue
        text = (ROOT / path).read_text(encoding="utf-8")
        if ABSOLUTE_PRIVATE.search(text):
            raise ValueError(f"private absolute path found: {path}")


def main() -> int:
    tracked = tracked_files()
    verify_manifest(tracked)
    json_count = verify_json(tracked)
    link_count = verify_links(tracked)
    verify_private_paths(tracked)
    print(
        json.dumps(
            {
                "tracked_files": len(tracked),
                "strict_json": json_count,
                "local_markdown_links": link_count,
                "package_manifest": "PASS",
                "private_absolute_paths": 0,
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
