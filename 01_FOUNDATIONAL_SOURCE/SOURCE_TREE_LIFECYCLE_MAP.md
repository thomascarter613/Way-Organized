# Foundational Source Tree Lifecycle Map

The `source/` directory is **not one version**. It currently contains at least four distinct lifecycle groups.

## 1. Pre-v1.0 research/architecture material

Examples include:

- numbered theological/practice/community architecture documents
- `dossiers/tq_001...` through `tq_007...`
- v0.6/v0.7/v0.8 JSON/CSV/Markdown registers
- Library of Witnesses and provisional theological research materials

These remain valuable source/research material. Their presence does not mean they supersede the released v1.0 synthesis.

## 2. v1.0 release source — exact snapshot relationship

All eight files under:

`03_RELEASES_AND_BASELINES/release_v1_0/source/`

have identical Git blob hashes to the same-path files in:

`01_FOUNDATIONAL_SOURCE/source/`

Therefore the v1.0 release source is a true byte-for-byte snapshot of those eight source files.

**Working rule**

- release copy: immutable historical/released snapshot
- foundational-source copy: current editable/source provenance copy until a cleaner source-of-truth migration is adopted

Do not delete either merely because the bytes match.

## 3. v1.2 execution source — partial exact snapshot relationship

Five v1.2 source/working artifacts in this tree are byte-for-byte identical to files in `release_v1_2/v1_2/`:

- `director_candidate_tracker_v1_2.csv`
- `execution_sequence_v1_2.md`
- `filing_readiness_register_v1_2.csv`
- `name_clearance_record_v1_2.md`
- `organizational_instantiation_v1_2.json`

The v1.2 release additionally contains DOCX/PDF publications that have no same-path editable source file in this directory.

`build_v12.py` is also present in the foundational source tree and should be treated as build/helper tooling rather than religious source authority.

## 4. Unversioned/ambiguous numbered material

A set of numbered Markdown documents has no single directory-level version identity. These should not be mass-renamed or moved until their relationships to v0.6-v0.9 and v1.0 publications are mapped.

## Current curation decision

Do **not** split or delete the mixed source tree in this PR.

The first safe step is the explicit crosswalk in:

`../00_START_HERE/SOURCE_RELEASE_CROSSWALK.csv`

A later PR can create a cleaner editable-source architecture once all source/release relationships are known.
