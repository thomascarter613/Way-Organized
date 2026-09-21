# Way-Organized

This repository is the organized, provenance-preserving working corpus for **The Way**. It was created from an unorganized source directory without deleting the original material.

## Start here

- [Repository current state](00_START_HERE/CURRENT_STATE.md)
- [Curation policy](00_START_HERE/CURATION_POLICY.md)
- [Authority and lifecycle registry](00_START_HERE/AUTHORITY_LIFECYCLE_REGISTRY.csv)
- [Canonical path registry](00_START_HERE/CANONICAL_PATH_REGISTRY.csv)
- [Source/release crosswalk](00_START_HERE/SOURCE_RELEASE_CROSSWALK.csv)
- [Organizational release → canonical institution crosswalk](00_START_HERE/ORGANIZATIONAL_RELEASE_INSTITUTION_CROSSWALK.md)
- [Duplicate triage summary](00_START_HERE/DUPLICATE_TRIAGE_SUMMARY.md)
- [Epistemology / authority crosswalk](00_START_HERE/EPISTEMOLOGY_AUTHORITY_CROSSWALK.md)
- [Authority and canon terminology](00_START_HERE/AUTHORITY_TERMINOLOGY.md)
- [Integration gaps](00_START_HERE/INTEGRATION_GAPS.md)
- [Original organization notes](00_START_HERE/README.md)
- [Original copy inventory](00_START_HERE/inventory/)

## Current baseline map

| Domain | Current working baseline | Notes |
| --- | --- | --- |
| Foundational religious synthesis | `03_RELEASES_AND_BASELINES/release_v1_0/` | v1.0 identifies itself as the first coherent public-facing religious/founding synthesis. |
| Organizational adoption | `03_RELEASES_AND_BASELINES/release_v1_1/` | Converts v1.0 into pre-incorporation/future-board adoption materials; preserved as predecessor to v1.2 execution. |
| Incorporation/execution package | `03_RELEASES_AND_BASELINES/release_v1_2/` | Current filing/board/EIN/banking/federal-exemption execution release; builds on v1.0 and v1.1 rather than replacing their religious content. |
| Pilot operations / evidence framework | `03_RELEASES_AND_BASELINES/release_v1_4/` | 90-day Founding Gathering Circle operating framework and evidence/review tooling; explicitly pre-incorporation and not a new theological or filing baseline. |
| Pilot curriculum | `03_RELEASES_AND_BASELINES/release_v1_5/` | Current 13-week print-and-run curriculum layer built on v1.4. The repo stores the release record and limited tracked source lineage; its README says binary deliverables remain in the ChatGPT project deliverable. |
| Research / evidence | `02_RESEARCH_AND_EVIDENCE/HTERP/HTERP_v1.4/` | Current HTERP research baseline; project status says WP-001 through WP-013 are complete as documents/protocols. |
| Canonical institutional repository | `04_INSTITUTION_AND_GOVERNANCE/institution/` | Its own README identifies it as the canonical institutional repository. |
| Integrity / safeguarding / filing readiness | `05_INTEGRITY_SAFEGUARDING_AND_COMPLIANCE/institutional_integrity/institutional_integrity_v0_4/` | Current pre-filing working package; not legally operative until appropriately adopted/filed. |
| Digital platform | `06_DIGITAL_PLATFORM/community-platform/` | Application source. It has no doctrinal or institutional authority merely by placement. |

## Important lifecycle rules

1. **Folder placement is not authority by itself.**
2. `01_FOUNDATIONAL_SOURCE/source/` is preserved mixed-lifecycle authoring provenance. New unrelated foundational drafting should begin in `01_FOUNDATIONAL_SOURCE/current/`; active series already established under the legacy tree (currently EPC/FWSD) may remain together there until a deliberate series migration.
3. `03_RELEASES_AND_BASELINES/` preserves released snapshots. Do not edit historical release contents merely to make them look current.
4. `80_HISTORICAL_AND_PREINTEGRATION_PACKAGES/` is retained for provenance and comparison, not as a current authority source.
5. `90_WORKING_NOTES_AND_SCRIPTS/` is working material.
6. `99_UNCLASSIFIED/` is now an empty holding area for future material that cannot yet be classified safely; historical ZIP packages have been moved to `80_HISTORICAL_AND_PREINTEGRATION_PACKAGES/archive-packages/` with a migration registry.
7. Exact duplicates are not automatically errors. The original 594 SHA-256 groups are now lifecycle-classified; most are generated artifacts, version carry-forwards, release snapshots, or provenance mirrors.

## Working rule for contributors

Before changing a substantive file, identify whether it is:

- **current source**
- **current canonical/institutional material**
- **released snapshot**
- **historical/pre-integration material**
- **working material**
- **unclassified**

When in doubt, preserve the original and make the change through a branch/PR with an explicit lifecycle decision.
