# Integration Gaps and Next Curation Work

This register records structural inconsistencies or unresolved integration work. It is not a list of theological defects.

## IG-001 — Foundational source tree has mixed version identity

**Observed**

`01_FOUNDATIONAL_SOURCE/source/00_README.md` identifies the source pack as v0.8, while the same directory contains v1.0 teaching/baseline artifacts.

**Risk**

A contributor may treat the whole directory as one coherent version or edit a release-derived file without knowing its lifecycle.

**Next action**

Build a file-level source-of-truth registry for `01_FOUNDATIONAL_SOURCE/source/`, then decide whether to:
- retain it as a historical mixed authoring tree;
- split it by lifecycle;
- or promote a clean current source tree in a later curation PR.

## IG-002 — HTERP v1.4 contains older embedded version headings

**Observed**

`HTERP_v1.4/README.md` begins with "HTERP v0.7 Status Note" and "Working Baseline v0.1", while `PROJECT-STATUS.md` identifies the folder/project state as v1.4.

**Risk**

Version discovery from the README alone is misleading.

**Next action**

Do not rewrite historical content yet. Add/retain repository wrappers that identify v1.4 as the current HTERP lifecycle baseline.

## IG-003 — Proto-canon terminology vs Library of Witnesses posture

**Observed**

HTERP v1.4 has a proto-canon architecture and status file. The foundational-source canon dossier says the Way presently maintains a Library of Witnesses rather than a closed canon and reserves any future canon for a separate process.

**Current interpretation**

These can coexist if "proto-canon" means a research/constructive priority structure rather than an adopted closed canon.

**Next action**

Harmonize terminology in a later authoritative source document so that "proto-canon", "Library of Witnesses", "foundational witness", and "binding doctrine" cannot be confused.

## IG-004 — Epistemology/canon governance exists in multiple layers

Relevant material currently appears in:

- `01_FOUNDATIONAL_SOURCE/source/09_epistemic_integrity_encounter_to_doctrine.md`
- `01_FOUNDATIONAL_SOURCE/source/dossiers/tq_006_scripture_canon_authority.md`
- `HTERP_v1.4/constructive/epistemological-constitution.md`
- `HTERP_v1.4/constructive/authority-canon-architecture.md`
- institutional doctrine/revelation protocols

**Risk**

A later reader may treat multiple related drafts as equally adopted.

**Next action**

Create a crosswalk and choose one authoritative home for epistemic governance before any canon/authority model is declared adopted.

## IG-005 — Organizational release and canonical institution trees overlap

v1.1/v1.2 release packets and the canonical `institution/` tree contain overlapping organizational material.

**Next action**

Build a migration/crosswalk showing:
- which released instruments are reference snapshots;
- which canonical institutional paths are the editable/current homes;
- which require future board adoption;
- which remain model/pre-filing documents.

Do not copy filing-ready templates into executed-record locations before real-world actions occur.

## IG-006 — Duplicate inventory needs lifecycle-aware classification

The original local organization run reported 594 SHA-256 duplicate groups.

The sample contains several different classes:
- canonical institutional files duplicated in historical operations exports;
- unchanged files carried through integrity versions;
- source files duplicated inside releases;
- generated application dependencies/build artifacts;
- archived release source packs.

**Next action**

Recompute duplicates from a clean Git clone and classify by lifecycle before deleting anything.

## IG-007 — Local copy inventory is not identical to Git tracking state

The original inventory was generated from the local organized directory before Git filtering. It includes generated paths such as `node_modules/` and `.next/` that are not visible in the GitHub app root listing.

**Next action**

Treat the original inventory as provenance for the local copy operation, not as a definitive list of Git-tracked files.

## IG-008 — Repository root previously lacked a master index

**Status**

Addressed by this curation branch with the root `README.md`, current-state file, lifecycle registry, and curation policy.
