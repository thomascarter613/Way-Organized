# Repository Current State

**Status date:** 2026-09-21  
**Purpose:** Record which parts of the organized corpus are current, historical, working, released, or unresolved without rewriting the underlying artifacts.

## Current-state findings

### Foundational/religious system

- `03_RELEASES_AND_BASELINES/release_v1_0/` is the **founding religious synthesis**. Its release README states that it reconciles v0.5-v0.9 into the first coherent public-facing religious baseline.
- `release_v1_1/` is an **organizational adoption/instantiation layer** built on v1.0.
- `release_v1_2/` is the **current execution/filing release** for incorporation, board, EIN/banking, federal-exemption, and compliance work. It should not be described as a new theological baseline unless a future release explicitly says so.
- `release_v1_4/` is the **pilot-operations/evidence framework** for the 90-day adult pre-incorporation Founding Gathering Circle. Its own README says it does not create a corporation, recognized House of Prayer, statutory membership body, or tax-exempt status. It does not replace v1.0's founding religious synthesis or v1.2's filing/execution role.
- `release_v1_5/` is the **current pilot-curriculum layer**. Its release record expands the v1.4 framework into a 13-week print-and-run adult curriculum while retaining the v1.4 evidence/review workbook. The v1.5 README says binary binders/workbooks/weekly packets remain in the ChatGPT project deliverable; Git currently preserves the release record plus limited tracked source lineage (`source/session_matrix_v1_5.csv`). Therefore v1.5 should not be described as a complete binary release stored in the repository.

### Foundational authoring tree

`01_FOUNDATIONAL_SOURCE/source/` is valuable but mixed-lifecycle.

Its `00_README.md` calls the pack **Theological Research & Library of Witnesses v0.8**, while the same directory contains:

- `teaching_and_practice_baseline_v1_0.md`
- `teaching_status_register_v1_0.csv`
- other v1.0 synthesis artifacts

The v1.0 teaching status register is byte-identical to the copy preserved in `release_v1_0/source/` according to the original SHA-256 duplicate inventory.

**Curation decision:** do not treat the source directory as one version. Treat each file by its explicit version/status.

The repository now preserves `source/` as mixed-lifecycle authoring provenance and uses `01_FOUNDATIONAL_SOURCE/current/` as the clean forward home for new unrelated foundational work.

Two active series were added concurrently under the legacy tree and should remain together there until deliberately migrated:

- `source/epistemology/` — EPC protocol series;
- `source/foundational-witness-dossiers/` — FWSD candidate evaluations.

The FWSD README explicitly states that dossier status is evaluative and does not constitute canonical admission.

### HTERP research

`02_RESEARCH_AND_EVIDENCE/HTERP/HTERP_v1.4/` is the current research baseline.

Its `PROJECT-STATUS.md` states:

- WP-001 through WP-013 are complete as documents/protocols;
- further HTERP-AI/PRED work requires real participants, preregistration, ethics/safety implementation, and data collection;
- the 30-day religious pilot requires an actual practitioner/community feedback loop.

The folder's `README.md` still begins with older internal headings ("HTERP v0.7 Status Note" / "Working Baseline v0.1"). Those headings should be treated as embedded historical metadata, not as the folder's current lifecycle label.

### Canon / source posture

Two current strands must be kept distinct:

1. HTERP v1.4 includes a **proto-canon / authority architecture** for research and constructive-theology purposes.
2. The foundational-source dossier `tq_006_scripture_canon_authority.md` says the Way presently maintains a **Library of Witnesses rather than a closed canon**, and reserves any future canon for a separate entrenched process.

The HTERP proto-canon itself says that "included" means **must be read and confronted**, not that every statement is infallible or normatively binding.

**Curation decision:** treat "proto-canon" as a research/constructive source-priority architecture unless and until an adopted Way instrument gives it stronger constitutional status.

### Institution

`04_INSTITUTION_AND_GOVERNANCE/institution/` identifies itself as the **Canonical Institutional Repository**.

Its controls explicitly require preservation of historical drafts and exact adoption records. This tree should therefore be treated as the primary institutional home for future adopted organizational instruments, subject to its own controls.

### Institutional integrity

`05_INTEGRITY_SAFEGUARDING_AND_COMPLIANCE/institutional_integrity/institutional_integrity_v0_4/` is the latest integrity/founding-readiness working package presently visible.

It explicitly remains **pre-filing** and says board/counsel/CPA review is required before filing or adoption.

Earlier v0.2 and v0.3 trees/releases are historical predecessors and should not be silently rewritten.

### Digital platform

`06_DIGITAL_PLATFORM/community-platform/` contains reconstructible application source including `package.json` and `bun.lock`.

The original local duplicate inventory includes paths under `node_modules/` and `.next/`, but these generated trees are not shown in the GitHub directory listing. The application already contains its own `.gitignore`.

**Curation decision:** generated dependencies/build output are not repository authority artifacts and should remain untracked.

## Authority/lifecycle principle

Repository path answers **where an artifact lives**.

It does not by itself answer:

- whether the artifact is adopted;
- whether it is current;
- whether it is a release snapshot;
- whether it is historically superseded;
- whether it is research rather than doctrine;
- whether it is a template rather than an executed record.

Use `AUTHORITY_LIFECYCLE_REGISTRY.csv` as the repository-level routing map.
