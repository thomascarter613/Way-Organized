#!/usr/bin/env python3
"""Audit a local clone of Way-Organized without modifying it.

Outputs:
- tracked-like file counts by top-level zone
- exact SHA-256 duplicate groups
- duplicate group classification hints

This script intentionally does not delete or move anything.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from collections import defaultdict
from pathlib import Path

GENERATED_PARTS = {"node_modules", ".next", ".turbo", ".cache", "__pycache__", ".git"}


def is_generated(path: Path) -> bool:
    return any(part in GENERATED_PARTS for part in path.parts)


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def classify(paths: list[str]) -> str:
    joined = "\n".join(paths)
    if any("/node_modules/" in f"/{p}/" or "/.next/" in f"/{p}/" for p in paths):
        return "generated"
    if any(p.startswith("03_RELEASES_AND_BASELINES/") for p in paths):
        if any(p.startswith("01_FOUNDATIONAL_SOURCE/") for p in paths):
            return "source-release-snapshot"
        return "release-carry-forward"
    if any(p.startswith("80_HISTORICAL_AND_PREINTEGRATION_PACKAGES/") for p in paths):
        if any(p.startswith("04_INSTITUTION_AND_GOVERNANCE/") for p in paths):
            return "canonical-historical-mirror"
        return "historical-mirror"
    if "institutional_integrity_v0_" in joined:
        return "version-carry-forward"
    return "review-required"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("root", nargs="?", default=".", help="Repository root")
    ap.add_argument("--out", default="00_START_HERE/inventory/git_duplicate_audit.csv")
    ap.add_argument("--json", default="00_START_HERE/inventory/git_repository_audit.json")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    out_csv = root / args.out
    out_json = root / args.json

    files: list[Path] = []
    zone_counts: dict[str, int] = defaultdict(int)

    for p in root.rglob("*"):
        if not p.is_file():
            continue
        rel = p.relative_to(root)
        if is_generated(rel):
            continue
        files.append(p)
        zone = rel.parts[0] if rel.parts else "."
        zone_counts[zone] += 1

    groups: dict[tuple[int, str], list[str]] = defaultdict(list)
    for p in files:
        rel = p.relative_to(root).as_posix()
        try:
            size = p.stat().st_size
            digest = sha256(p)
        except OSError:
            continue
        groups[(size, digest)].append(rel)

    duplicates = [
        {
            "sha256": digest,
            "size_bytes": size,
            "copy_count": len(paths),
            "classification_hint": classify(paths),
            "paths": sorted(paths),
        }
        for (size, digest), paths in groups.items()
        if len(paths) > 1
    ]
    duplicates.sort(key=lambda x: (-x["copy_count"], -x["size_bytes"], x["sha256"]))

    out_csv.parent.mkdir(parents=True, exist_ok=True)
    with out_csv.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["sha256", "size_bytes", "copy_count", "classification_hint", "path"])
        for group in duplicates:
            for path in group["paths"]:
                w.writerow([
                    group["sha256"],
                    group["size_bytes"],
                    group["copy_count"],
                    group["classification_hint"],
                    path,
                ])

    summary = {
        "root": str(root),
        "files_scanned": len(files),
        "duplicate_groups": len(duplicates),
        "zone_counts": dict(sorted(zone_counts.items())),
        "classification_counts": dict(
            sorted(
                {
                    cls: sum(1 for g in duplicates if g["classification_hint"] == cls)
                    for cls in {g["classification_hint"] for g in duplicates}
                }.items()
            )
        ),
    }
    out_json.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")

    print(json.dumps(summary, indent=2))
    print(f"Wrote {out_csv}")
    print(f"Wrote {out_json}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
