# Way — Organized Working Repository

This directory was generated non-destructively from `/home/oss/Way`.
The original source directory was not changed.

## Organization

- `00_START_HERE/` — navigation, manifests, original root metadata, and routing records.
- `01_FOUNDATIONAL_SOURCE/` — the authored source tree used to build theological/community artifacts.
- `02_RESEARCH_AND_EVIDENCE/` — HTERP and associated research/evidence work.
- `03_RELEASES_AND_BASELINES/` — versioned reference and release packages (v0.8, v0.9, v1.0, v1.1, v1.2).
- `04_INSTITUTION_AND_GOVERNANCE/` — the structured institutional repository.
- `05_INTEGRITY_SAFEGUARDING_AND_COMPLIANCE/` — integrity framework versions, safeguarding, compliance, and related releases.
- `06_DIGITAL_PLATFORM/` — application/web source code.
- `80_HISTORICAL_AND_PREINTEGRATION_PACKAGES/` — older, flattened, duplicate, or predecessor packages retained intact for provenance.
- `90_WORKING_NOTES_AND_SCRIPTS/` — notes and loose generation/build scripts; not authoritative by placement.
- `99_UNCLASSIFIED/` — anything not recognized by the routing rules; nothing is discarded.

## Important design decisions

1. **No destructive moves.** Everything is copied from the source tree.
2. **Mature subsystems stay intact.** HTERP, institution, institutional_integrity,
   source, releases, and the community platform keep their internal directory layout.
3. **Duplicate historical exports are preserved.** They are moved into the historical/pre-integration area instead of being silently deleted.
4. **Authority and lifecycle are separated.** Working notes are not mixed with releases or current repositories.
5. **Every copied file is traceable.** See `inventory/copy_manifest.csv`.
6. **Exact duplicates are reported, not removed.** See `inventory/duplicate_files_by_sha256.csv`.

## Suggested next step

Once this organized copy is reviewed, initialize Git **here**, not in the original unorganized directory:

```bash
cd /home/oss/Way-Organized
git init
git add .
git commit -m "Establish organized Way repository baseline"
```

Then create a private GitHub repository if you want remote history, backup, and collaborative curation.
