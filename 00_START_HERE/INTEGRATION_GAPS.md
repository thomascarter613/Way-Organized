# Integration Gaps and Next Curation Work

This register records structural inconsistencies or unresolved integration work. It is not a list of theological defects.

## IG-001 — Foundational source tree has mixed version identity

**Observed**

`01_FOUNDATIONAL_SOURCE/source/00_README.md` identifies the source pack as v0.8, while the same directory contains v1.0 and v1.2 material.

**Status: partially addressed**

The repository now contains:

- `SOURCE_RELEASE_CROSSWALK.csv`
- `01_FOUNDATIONAL_SOURCE/SOURCE_TREE_LIFECYCLE_MAP.md`

All eight files in `release_v1_0/source/` are exact matches to same-path foundational-source files, and five v1.2 execution-source files are exact matches to their v1.2 release copies.

**Remaining decision**

Choose whether the mixed source tree should eventually remain as historical authoring provenance or be migrated into a clean current-source layout.

## IG-002 — HTERP v1.4 contains older embedded version headings

**Observed**

`HTERP_v1.4/README.md` begins with "HTERP v0.7 Status Note" and "Working Baseline v0.1", while `PROJECT-STATUS.md` identifies the folder/project state as v1.4.

**Status: contained**

Repository wrapper navigation now identifies v1.4 as the current HTERP lifecycle baseline.

**Remaining decision**

Whether to add an HTERP-local version metadata file or leave the internal README untouched as historical provenance.

## IG-003 — Proto-canon terminology vs Library of Witnesses posture

**Observed**

HTERP v1.4 has a proto-canon architecture and status file. The foundational-source canon dossier says the Way presently maintains a Library of Witnesses rather than a closed canon and reserves any future canon for a separate process.

**Status: analytically reconciled, governance decision still open**

`EPISTEMOLOGY_AUTHORITY_CROSSWALK.md` records that HTERP itself says the proto-canon is a chosen constructive center/source-priority architecture and that "included" does not mean infallible or normatively binding.

**Remaining decision**

Harmonize "proto-canon", "Library of Witnesses", "foundational witness", "liturgical source", and "binding doctrine" in a future adopted authority document.

## IG-004 — Epistemology/canon governance exists in multiple layers

Relevant material appears in foundational source, HTERP constructive work, and institutional integrity policy.

**Status: crosswalk completed**

See `EPISTEMOLOGY_AUTHORITY_CROSSWALK.md`.

**Remaining decision**

Choose one authoritative home and adoption/status process for a consolidated epistemic/revelation/canon governance instrument.

## IG-005 — Organizational release and canonical institution trees overlap

v1.1/v1.2 release packets and the canonical `institution/` tree contain overlapping organizational material.

**Status: open**

**Next action**

Build a migration/crosswalk showing:
- which released instruments are immutable reference snapshots;
- which canonical institutional paths are the editable/current homes;
- which require future board adoption;
- which remain model/pre-filing documents.

Do not copy filing-ready templates into executed-record locations before real-world actions occur.

## IG-006 — Duplicate inventory lifecycle classification

**Status: addressed**

All 594 original SHA-256 duplicate groups are now classified in `DUPLICATE_TRIAGE_SUMMARY.md`.

No group remains unexplained at the repository-lifecycle level.

The dominant classes are generated app artifacts, canonical/historical mirrors, version carry-forwards, and source/release snapshots.

**Remaining optional work**

Run the included audit helper from a clean clone if a Git-tracked-only duplicate report is desired. No mass deletion is recommended.

## IG-007 — Local copy inventory differs from Git tracking state

**Status: understood**

The original inventory was generated before Git filtering and includes local/generated paths such as `node_modules/`, `.next/`, nested `.git/` metadata, and `.env.local`.

Treat it as provenance for the local copy operation, not as a definitive Git-tracked-file list.

## IG-008 — Repository root previously lacked a master index

**Status: addressed**

The root README and domain wrapper READMEs now provide current navigation and lifecycle context.
