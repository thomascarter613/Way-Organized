# Organizational Release → Canonical Institution Crosswalk

**Status:** second-pass curation record  
**Date:** 2026-09-21  
**Scope:** v1.1 organizational-instantiation release, v1.2 execution release, and the canonical institutional repository

## Governing distinction

The release packages are **immutable historical/reference snapshots**.  
The `04_INSTITUTION_AND_GOVERNANCE/institution/` tree is the **canonical institutional home** for current/adopted organizational instruments and records.

A released template or filing-ready packet is **not** an executed corporate record merely because it exists in a release.

The migration rule is therefore:

> preserve releases unchanged; use them as source/reference material; create or place only actually adopted, filed, signed, accepted, or otherwise operative records in the canonical institution tree, with the required adoption/evidence trail.

## v1.1 mapping

| v1.1 artifact | Function | Canonical institution relationship | Curation disposition |
| --- | --- | --- | --- |
| `adoption_and_organizational_instantiation_packet_v1_1.*` | pre-incorporation/future-board adoption packet | feeds formation/governance controls | Preserve as immutable release publication; do not copy as an executed record |
| `founding_gathering_90_day_pilot_field_guide_v1_1.*` | pilot/launch operational guide | relates to operations/program launch rather than corporate execution | Preserve as release reference; integrate specific adopted procedures only through controlled institution instruments |
| `source/corporate_interface_schedule_v1_1.md` | maps religious/community and future corporate domains | informs `02-constitutional/`, `04-governance/`, and control architecture | Reference source; do not treat as adopted governing instrument unless adopted through institution controls |
| `source/decision_register_v1_1.md` | records v1.1 design/adoption decisions | analogous to `04-governance/decisions/` but predates actual corporate action | Preserve in release; future actual decisions belong in canonical decision records |
| `source/founder_stewardship_declaration_v1_1.md` | personal pre-corporate stewardship commitment | may inform constitutional/ethics controls | Preserve as historical/personal commitment; not a board-adopted instrument by itself |
| `source/future_board_ratification_resolution_v1_1.md` | template for future board action | `01-formation/organizational-actions/` or `04-governance/board/resolutions/` after actual action | Keep release template immutable; create executed/adopted record only after real board action |
| `source/organizational_instantiation_v1_1.json` | machine-readable organizational model | control/reference metadata | Historical/reference; superseded operationally by later execution work, not an adopted record |
| `source/organizational_readiness_matrix_v1_1.csv` | readiness tracking | planning/control evidence | Preserve release snapshot; current readiness should live in a controlled current register |
| `source/pilot_launch_checklist_v1_1.md` | launch checklist | operations | Preserve release snapshot; adopted current checklist should be a controlled operational instrument |

## v1.2 mapping

| v1.2 artifact | Function | Canonical institution relationship | Curation disposition |
| --- | --- | --- | --- |
| `director_candidate_tracker_v1_2.csv` | pre-formation recruitment tracker | supports board formation; not itself a board record | Keep source/release copy; do not populate canonical executed-record folders until real candidates/acceptances exist |
| `founding_director_recruitment_and_acceptance_kit_v1_2.*` | recruitment/acceptance templates | feeds formation and governance | Preserve release; signed acceptances, when real, belong in controlled formation/personnel records |
| `filing_ready_incorporation_and_board_execution_packet_v1_2.*` | charter/board execution package | `01-formation/charter/`, `01-formation/organizational-actions/`, board resolutions/minutes | Release is reference/template; filed charter and executed actions move to canonical homes only after actual events |
| `ein_banking_federal_exemption_and_compliance_execution_packet_v1_2.*` | EIN, banking, exemption/compliance execution | `01-formation/ein/`, `07-records/financial/`, `09-tax-and-regulatory/` | Preserve release; only real confirmations, filings, bank records, and submitted applications become canonical evidence/records |
| `execution_sequence_v1_2.md` | ordered execution plan | cross-domain control aid | Preserve as execution-reference snapshot; actual completed actions must be evidenced separately |
| `filing_readiness_register_v1_2.csv` | pre-filing status register | repository/control planning | Preserve source/release snapshot; status entries do not prove completion without evidence |
| `name_clearance_record_v1_2.md` | name-clearance work record | supports formation/state filing | Preserve as pre-filing evidence; final accepted corporate name is established by actual filing/acceptance evidence |
| `organizational_instantiation_v1_2.json` | execution-state model | control/reference metadata | Preserve as release/source snapshot; does not itself create legal status |

## Canonical destination semantics

### `01-formation/charter/`

Use for the actual filed/accepted charter and controlled derivatives.  
Do **not** place a merely draft or "filing-ready" charter here as if filing occurred.

### `01-formation/organizational-actions/`

Use for actual incorporator/organizational actions and controlled board-organization records.  
The existing `BOARD-ACT-001-Initial-Board-Organizational-Actions-Packet.docx` is a canonical institutional packet/template; execution status still depends on completed records/evidence.

### `04-governance/board/minutes/` and `resolutions/`

Use for actual board minutes/resolutions after the board legally exists and acts.  
Do not populate these folders with hypothetical future-board resolutions.

### `01-formation/ein/`

Use for actual IRS EIN issuance/confirmation and controlled application records.

### `07-records/financial/`

Use for actual financial/banking records subject to the repository's access controls.

### `09-tax-and-regulatory/form-1023/`

Use for controlled working/submitted Form 1023 materials and supporting exhibits.  
Existing files explicitly labeled "Working Copy" or "DRAFT" remain non-filed until submission evidence exists.

### `09-tax-and-regulatory/schedule-a/`

Use for the controlled Schedule A working/submitted materials.  
The existing `CH-050-Form-1023-Schedule-A-Churches-Working-Copy.docx` is a working copy, not evidence of filing.

## Status model for release-derived institutional material

Use these lifecycle states when migrating or deriving a canonical institutional instrument:

- **REFERENCE** — historical/release source only.
- **TEMPLATE** — prepared for future use; no operative effect.
- **WORKING** — actively being completed/reviewed.
- **READY-FOR-REVIEW** — substantively prepared but not approved/filed.
- **ADOPTED** — validly approved by the proper authority.
- **EXECUTED** — signed/completed action where execution is required.
- **FILED** — submitted to the relevant governmental/third-party body.
- **ACCEPTED/ISSUED** — filing/application accepted or official evidence issued.
- **SUPERSEDED** — replaced by a later controlled instrument while retained historically.

No artifact should skip directly from RELEASE/REFERENCE to ADOPTED, EXECUTED, FILED, or ACCEPTED without evidence.

## Curation conclusion

The v1.1 and v1.2 releases should **not be migrated wholesale** into the canonical institution tree. Their proper role is to remain frozen source/reference packages.

The canonical institution tree already supplies the correct destination architecture. Migration should occur **event-by-event** as real-world actions occur, with each adopted/executed/filed artifact accompanied by its evidence and adoption metadata.

This resolves the structural ambiguity identified as IG-005 while preserving the substantive real-world execution work for the appropriate future moment.
