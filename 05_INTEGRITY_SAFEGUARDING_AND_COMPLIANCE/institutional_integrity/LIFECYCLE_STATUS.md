# Institutional Integrity — Lifecycle Status

**Repository lifecycle:** mixed version family  
**Status date:** 2026-09-21  
**Current working baseline:** `institutional_integrity_v0_4/`  
**Current release snapshot:** `institutional_integrity_v0_4_release/`

## Purpose

The `institutional_integrity/` directory contains several generations of the integrity, safeguarding, governance-readiness, and filing-readiness system. This wrapper records which generation is current without rewriting or deleting earlier versions.

## Current interpretation

### Unversioned root artifacts

Root-level files such as:

- `institutional_integrity_framework.md`
- `institutional_integrity_framework.docx`
- `institutional_integrity_framework.pdf`
- `institutional_integrity_dashboard_v0_2.xlsx`

are predecessor/general framework artifacts retained for provenance.

They should not be treated as the current execution baseline merely because they sit at the parent directory root.

### v0.2 and v0.3

The v0.2/v0.3 work trees and release packages are historical predecessors.

They remain useful for provenance, design evolution, comparison, and reconstruction of why later controls exist.

They should not be silently rewritten to match v0.4.

### v0.4 working tree

`institutional_integrity_v0_4/` is the **current working integrity/founding-readiness baseline**.

Its `70_V0_4_README.md` classifies it as:

> Pre-filing working package; board/counsel/CPA review required before filing or adoption.

Its `decision_records/94_human_input_boundary.md` records that the document/template architecture has reached a real-world input boundary involving:

- legal/public name;
- actual directors and Secretary;
- registered/principal addresses;
- concrete program facts;
- and good-faith financial assumptions.

Therefore v0.4 is current and operationally useful, but **not legally operative merely because the files exist**.

### v0.4 release

`institutional_integrity_v0_4_release/` is the packaged **immutable v0.4 reference snapshot**.

Its `README_v0_4.md` identifies the release as:

> Pre-filing; at genuine human-input boundary.

Use the release to preserve what v0.4 contained when packaged. Do not edit it to reflect later working changes.

## Authority boundaries

| Material | Lifecycle | Authority / role |
| --- | --- | --- |
| Root unversioned framework | historical/predecessor | provenance/reference |
| v0.2/v0.3 work trees | historical | predecessor working material |
| v0.2/v0.3 releases | released historical snapshots | reference/provenance |
| v0.4 work tree | current working | pre-filing integrity/founding-readiness |
| v0.4 release | released snapshot | immutable v0.4 reference |

None of these statuses by themselves prove legal adoption, board approval, filing, tax-exempt recognition, church classification, officer appointment, director acceptance, compensation approval, or policy implementation.

Those states require the real-world evidence and controlled institutional records specified by the canonical institution repository.

## Relationship to the canonical institution repository

The integrity system is a source/control package for safeguarding, anti-coercion, governance readiness, and filing preparation.

Explicitly statused TEMPLATE, WORKING, and READY-FOR-REVIEW materials may be maintained in their designated controlled institutional working/template paths where the canonical repository permits them.

ADOPTED, EXECUTED, FILED, and ACCEPTED/ISSUED status must remain evidence-backed.

Where an integrity instrument becomes formally adopted or operative, its institutional status and record should be controlled through:

`04_INSTITUTION_AND_GOVERNANCE/institution/`

according to that repository's control documents and adoption records.

Do not infer that a v0.4 model policy is already an adopted institutional policy merely because a corresponding canonical destination exists.

## Related repository controls

See:

- `../../00_START_HERE/AUTHORITY_LIFECYCLE_REGISTRY.csv`
- `../../00_START_HERE/CANONICAL_PATH_REGISTRY.csv`
- `../../00_START_HERE/ORGANIZATIONAL_RELEASE_INSTITUTION_CROSSWALK.md`

## Preservation rule

Do not collapse this family into a single folder merely to remove duplicate files.

Version carry-forward is part of the development record. Earlier generations and release snapshots remain provenance artifacts unless a future compaction process explicitly preserves their lineage and migration metadata.
