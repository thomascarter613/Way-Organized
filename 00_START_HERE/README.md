# Way — Organized Working Repository

This repository was generated non-destructively from `/home/oss/Way`.
The original source directory was not changed.

## Current curation layer

Start with:

- [Repository master README](../README.md)
- [Current state](CURRENT_STATE.md)
- [Curation policy](CURATION_POLICY.md)
- [Authority/lifecycle registry](AUTHORITY_LIFECYCLE_REGISTRY.csv)
- [Source/release crosswalk](SOURCE_RELEASE_CROSSWALK.csv)
- [Duplicate triage summary](DUPLICATE_TRIAGE_SUMMARY.md)
- [Epistemology / authority crosswalk](EPISTEMOLOGY_AUTHORITY_CROSSWALK.md)
- [Integration gaps](INTEGRATION_GAPS.md)
- [Original copy inventory](inventory/)

## Organization

- `00_START_HERE/` — navigation, manifests, original root metadata, routing records, and curation controls.
- `01_FOUNDATIONAL_SOURCE/` — authored/mixed-lifecycle source material used to build theological/community artifacts.
- `02_RESEARCH_AND_EVIDENCE/` — HTERP and associated research/evidence work.
- `03_RELEASES_AND_BASELINES/` — versioned reference and release packages (v0.8, v0.9, v1.0, v1.1, v1.2).
- `04_INSTITUTION_AND_GOVERNANCE/` — the structured canonical institutional repository.
- `05_INTEGRITY_SAFEGUARDING_AND_COMPLIANCE/` — integrity framework versions, safeguarding, compliance, and related releases.
- `06_DIGITAL_PLATFORM/` — application/web source code.
- `80_HISTORICAL_AND_PREINTEGRATION_PACKAGES/` — older, flattened, duplicate, or predecessor packages retained intact for provenance.
- `90_WORKING_NOTES_AND_SCRIPTS/` — notes and loose generation/build/audit scripts; not authoritative by placement.
- `99_UNCLASSIFIED/` — anything not recognized by the routing rules; nothing is discarded.

## Important design decisions

1. **No destructive source migration has occurred.**
2. **Mature subsystems stay intact.** HTERP, institution, institutional_integrity, source, releases, and the community platform retain their internal directory layout.
3. **Duplicate historical exports are preserved.** All 594 original SHA-256 duplicate groups have now been classified; none remain unexplained at the repository-lifecycle level.
4. **Authority and lifecycle are separated.** Working notes, research, release snapshots, templates, and current institutional material are not assumed to have equal status.
5. **Every copied file from the original organization run is traceable.** See `inventory/copy_manifest.csv`.
6. **The original copy inventory is a local-snapshot inventory, not necessarily the same as Git-tracked state.**

## Repository working rule

Before editing substantive content, identify the artifact's lifecycle in the [authority/lifecycle registry](AUTHORITY_LIFECYCLE_REGISTRY.csv). Historical releases should remain immutable; changes belong in current source/canonical homes or in new releases.
