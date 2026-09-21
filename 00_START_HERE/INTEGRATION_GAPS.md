# Integration Gaps and Next Curation Work

This register records structural inconsistencies or unresolved integration work. It is not a list of theological defects.

## IG-001 — Foundational source tree has mixed version identity

**Observed**

`01_FOUNDATIONAL_SOURCE/source/00_README.md` identifies the source pack as v0.8, while the same directory contains v1.0 and v1.2 material.

**Status: structurally addressed**

The repository now contains:

- `SOURCE_RELEASE_CROSSWALK.csv`
- `01_FOUNDATIONAL_SOURCE/SOURCE_TREE_LIFECYCLE_MAP.md`
- `01_FOUNDATIONAL_SOURCE/current/README.md`

All eight files in `release_v1_0/source/` are exact matches to same-path foundational-source files, and five v1.2 execution-source files are exact matches to their v1.2 release copies.

**Curation decision**

Preserve `source/` in place as mixed-lifecycle authoring provenance.

Do not mass-migrate or rename it.

Use `01_FOUNDATIONAL_SOURCE/current/` for new foundational drafting going forward. This creates a clean forward source path without breaking historical references or release provenance.

## IG-002 — HTERP v1.4 contains older embedded version headings

**Observed**

`HTERP_v1.4/README.md` begins with "HTERP v0.7 Status Note" and "Working Baseline v0.1", while `PROJECT-STATUS.md` identifies the folder/project state as v1.4.

**Status: addressed**

`HTERP_v1.4/LIFECYCLE_STATUS.md` now records the repository lifecycle explicitly:

- the enclosing working baseline is v1.4;
- `PROJECT-STATUS.md` controls current project status;
- older README headings are preserved as embedded historical provenance;
- HTERP research maturity does not by itself create doctrine, canon, or institutional authority.

The inherited README remains unchanged.

## IG-003 — Proto-canon terminology vs Library of Witnesses posture

**Observed**

HTERP v1.4 has a proto-canon architecture and status file. The foundational-source canon dossier says the Way presently maintains a Library of Witnesses rather than a closed canon and reserves any future canon for a separate process.

**Status: repository terminology addressed; formal religious adoption still open**

`EPISTEMOLOGY_AUTHORITY_CROSSWALK.md` records that HTERP itself says the proto-canon is a chosen constructive center/source-priority architecture and that "included" does not mean infallible or normatively binding.

`AUTHORITY_TERMINOLOGY.md` now standardizes repository usage, including the qualified phrase:

> **HTERP proto-canon / research source-priority architecture**

and distinguishes Library of Witnesses, foundational witness, liturgical source, binding doctrine, canonical institutional repository, and canonical path.

**Remaining substantive decision**

A future adopted authority instrument may retain, revise, or replace this terminology. Repository curation no longer needs to guess in the meantime.

## IG-004 — Epistemology/canon governance exists in multiple layers

Relevant material appears in foundational source, HTERP constructive work, and institutional integrity policy.

**Status: repository architecture addressed; substantive consolidation/adoption still open**

See:

- `EPISTEMOLOGY_AUTHORITY_CROSSWALK.md`
- `01_FOUNDATIONAL_SOURCE/current/epistemology/README.md`

The designated forward drafting home for any consolidated epistemology/revelation/canon instrument is:

`01_FOUNDATIONAL_SOURCE/current/epistemology/`

Existing source documents remain in place for provenance.

**Remaining substantive work**

Draft, review, and if appropriate release/adopt a consolidated instrument. Storage in the drafting home does not itself create doctrine, canon, constitutional force, or institutional policy.

## IG-005 — Organizational release and canonical institution trees overlap

v1.1/v1.2 release packets and the canonical `institution/` tree contain overlapping organizational material.

**Status: structurally addressed**

See `ORGANIZATIONAL_RELEASE_INSTITUTION_CROSSWALK.md`.

The crosswalk establishes that:

- v1.1/v1.2 release packages remain immutable historical/reference snapshots;
- the canonical `institution/` tree is the home for current/adopted/executed institutional records;
- filing-ready or future-board templates must not be copied into executed-record locations as though the real-world action occurred;
- migration is event-by-event and must be supported by adoption, execution, filing, acceptance, issuance, or equivalent evidence.

**Remaining real-world work**

The structural mapping is complete. Actual migration into operative record locations can occur only as real organizational events take place. This is an execution boundary, not a repository-curation defect.

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
