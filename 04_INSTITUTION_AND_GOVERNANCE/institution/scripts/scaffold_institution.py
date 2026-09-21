#!/usr/bin/env python3
"""Scaffold the canonical institutional repository.

This script is intentionally conservative and idempotent:
- it creates directories but never deletes existing content;
- it writes seed control files only when absent, unless --overwrite-control-files is used;
- it does not populate unresolved organizational facts;
- it does not create or backdate historical operational records.

Examples:
    python scaffold_institution.py --root ./institution
    python scaffold_institution.py --root ./institution --activation-pack ./activation-pack
    python scaffold_institution.py --root ./institution --overwrite-control-files
"""
from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path
from textwrap import dedent

DIRECTORIES = [
    "00-control/adoption-register",
    "00-control/manifests",
    "00-control/releases",
    "01-formation/charter",
    "01-formation/ein",
    "01-formation/organizational-actions",
    "01-formation/state-filings",
    "02-constitutional/REL-CON-001/0.1.0",
    "02-constitutional/ECC-CON-001/0.1.0",
    "02-constitutional/BYL-001/0.1.0",
    "02-constitutional/ECC-COUNCIL-001/0.1.0",
    "02-constitutional/CONST-GUARD-001/0.1.0",
    "02-constitutional/ACCOUNT-001/0.1.0",
    "02-constitutional/MEM-001/0.1.0",
    "02-constitutional/MIN-001/0.1.0",
    "02-constitutional/DISC-001/0.1.0",
    "02-constitutional/SUCC-001/0.1.0",
    "02-constitutional/SAFE-001/0.1.0",
    "02-constitutional/FIN-001/0.1.0",
    "02-constitutional/GOV-PROC-001/0.1.0",
    "02-constitutional/JUR-001/0.1.0",
    "02-constitutional/FOUND-TRANS-001/0.1.0",
    "02-constitutional/LOCAL-001/0.1.0",
    "02-constitutional/AFF-001/0.1.0",
    "02-constitutional/DOC-001/0.1.0",
    "03-doctrine-and-religious-life/beliefs",
    "03-doctrine-and-religious-life/doctrine",
    "03-doctrine-and-religious-life/worship",
    "03-doctrine-and-religious-life/rites",
    "03-doctrine-and-religious-life/history",
    "03-doctrine-and-religious-life/teaching",
    "04-governance/board/minutes",
    "04-governance/board/resolutions",
    "04-governance/ecclesiastical-council/founding",
    "04-governance/ecclesiastical-council/minutes",
    "04-governance/ecclesiastical-council/decisions",
    "04-governance/ccg",
    "04-governance/eac",
    "04-governance/cma/minutes",
    "04-governance/decisions",
    "05-operations/membership",
    "05-operations/ministry",
    "05-operations/safeguarding",
    "05-operations/discipline",
    "05-operations/finance",
    "05-operations/education",
    "05-operations/facilities",
    "05-operations/local-communities",
    "05-operations/affiliations",
    "06-templates/governance",
    "06-templates/safeguarding",
    "06-templates/finance",
    "06-templates/ministry",
    "06-templates/discipline",
    "06-templates/doctrine",
    "06-templates/succession",
    "06-templates/local-affiliation",
    "06-templates/manuals",
    "07-records/services",
    "07-records/attendance",
    "07-records/teaching",
    "07-records/rites",
    "07-records/membership",
    "07-records/credentials",
    "07-records/safeguarding",
    "07-records/discipline",
    "07-records/financial/reports",
    "07-records/financial/related-parties",
    "08-evidence/church-characteristics",
    "08-evidence/facilities",
    "08-evidence/worship",
    "08-evidence/publications",
    "08-evidence/exhibits",
    "09-tax-and-regulatory/form-1023",
    "09-tax-and-regulatory/schedule-a",
    "09-tax-and-regulatory/irs-correspondence",
    "09-tax-and-regulatory/state-compliance",
    "99-archive/superseded",
    "99-archive/withdrawn",
    "99-archive/historical-drafts",
    "scripts",
]

ORG_CONSTANTS = dedent("""\
# ORG-CONST-001 machine-readable seed.
# Status values: VERIFIED | PROVISIONAL | RESERVED | NOT_YET_EXISTENT | SUPERSEDED
# Do not replace unresolved values with guesses.
constants:
  ORG.LEGAL_NAME:
    value: "[[CORP_NAME]]"
    status: RESERVED
    evidence: "Filed charter / Tennessee Secretary of State"
  ORG.PUBLIC_NAME:
    value: "[[PUBLIC_NAME]]"
    status: RESERVED
    evidence: "Authorized naming decision"
  ORG.JURISDICTION:
    value: "Tennessee"
    status: VERIFIED
    evidence: "Founding design / charter"
  ORG.EIN:
    value: "[[EIN]]"
    status: NOT_YET_EXISTENT
    evidence: "IRS EIN confirmation"
  GOV.FOUNDER:
    value: "[[NAME]]"
    status: PROVISIONAL
    evidence: "EC-FOUND-001"
  GOV.CONSTITUTION_ADOPTION_DATE:
    value: "[[DATE]]"
    status: NOT_YET_EXISTENT
    evidence: "EC-FOUND-001"
  GOV.PSL:
    value: "[[NAME]]"
    status: NOT_YET_EXISTENT
    evidence: "EC-FOUND-001 or succession record"
  REC.REPOSITORY:
    value: "institution/"
    status: PROVISIONAL
    evidence: "REPO-001"
""")

RECORD_SERIES = dedent("""\
# REC-ID-001 machine-readable seed.
# Allocate IDs contemporaneously. Never recycle identifiers.
series:
  BOARD-MIN: {pattern: "BOARD-MIN-YYYY-NNNN", next: 1, custodian: "Secretary"}
  BOARD-RES: {pattern: "BOARD-RES-YYYY-NNNN", next: 1, custodian: "Secretary"}
  EC-MIN: {pattern: "EC-MIN-YYYY-NNNN", next: 1, custodian: "EC Recorder"}
  EC-DEC: {pattern: "EC-DEC-YYYY-NNNN", next: 1, custodian: "EC Recorder"}
  CMA-MIN: {pattern: "CMA-MIN-YYYY-NNNN", next: 1, custodian: "CMA Recorder"}
  GOV-DEC: {pattern: "GOV-DEC-YYYY-NNNN", next: 1, custodian: "Records Custodian"}
  SR: {pattern: "SR-YYYY-NNNN", next: 1, custodian: "Worship Records Custodian"}
  ATT: {pattern: "ATT-YYYY-NNNN", next: 1, custodian: "Attendance Custodian"}
  TA: {pattern: "TA-YYYY-NNNN", next: 1, custodian: "Teaching Archivist"}
  RR: {pattern: "RR-YYYY-NNNN", next: 1, custodian: "Religious Records Custodian"}
  MEM: {pattern: "MEM-YYYY-NNNN", next: 1, custodian: "Membership Registrar"}
  MIN-CRED: {pattern: "MIN-CRED-YYYY-NNNN", next: 1, custodian: "Credential Registrar"}
  SAFE: {pattern: "SAFE-YYYY-NNNN", next: 1, custodian: "Safeguarding Custodian"}
  DISC: {pattern: "DISC-YYYY-NNNN", next: 1, custodian: "Discipline Records Custodian"}
  FIN-TXN: {pattern: "FIN-TXN-YYYY-NNNN", next: 1, custodian: "Treasurer"}
  FIN-RPT: {pattern: "FIN-RPT-YYYY-NNNN", next: 1, custodian: "Treasurer"}
  EVD: {pattern: "EVD-YYYY-NNNN", next: 1, custodian: "Records Custodian"}
  CORR-IRS: {pattern: "CORR-IRS-YYYY-NNNN", next: 1, custodian: "Secretary/Treasurer"}
  ADOPT: {pattern: "ADOPT-YYYY-NNNN", next: 1, custodian: "Records Custodian"}
""")

README = dedent("""\
# Canonical Institutional Repository

This repository is controlled by REPO-001, REC-ID-001, ORG-CONST-001, and ADOPT-001.

## First use
1. Run `python scripts/scaffold_institution.py --root .` if the tree was not already generated.
2. Review `00-control/org_constants.yaml`; change a value to VERIFIED only when source evidence exists.
3. Open `00-control/Activation-Control-Workbook.xlsx` and use it as the human-operable activation register.
4. Preserve all existing drafts before producing adopted versions.
5. Record every adoption with exact instrument version, authority, decision ID, date, concurrence, and canonical path.

## Hard controls
- Do not fabricate or backdate operational records.
- Do not infer an EIN, filing date, officeholder, address, congregation count, attendance, credential, or financial history.
- Do not collapse Civil Board and ecclesiastical authority into one decision merely for convenience.
- Do not overwrite historical versions; supersede and archive them.
- Do not store completed safeguarding/discipline/personnel records in broad-access template folders.
""")

GITIGNORE = dedent("""\
# Local/editor noise
.DS_Store
Thumbs.db
~$*.docx
*.tmp

# Sensitive working exports should be added here as the institution chooses.
# Do NOT assume the whole repository is safe for a public Git remote.
""")

ACTIVATION_DESTINATIONS = {
    "ORG-CONST-001-Organization-Constants-and-Institutional-Identity-Register.docx": "00-control/",
    "REC-ID-001-Institutional-Identifier-and-Record-Numbering-Standard.docx": "00-control/",
    "REPO-001-Canonical-Institutional-Repository-Standard.docx": "00-control/",
    "ADOPT-001-Founding-Adoption-and-Activation-Register.docx": "00-control/",
    "ACT-RUN-001-Institutional-Activation-Runbook.docx": "00-control/",
    "Activation-Control-Workbook.xlsx": "00-control/",
    "BOARD-ACT-001-Initial-Board-Organizational-Actions-Packet.docx": "01-formation/organizational-actions/",
    "EC-FOUND-001-Founding-Ecclesiastical-Adoption-Instrument.docx": "04-governance/ecclesiastical-council/founding/",
}


def write_if_allowed(path: Path, content: str, overwrite: bool) -> None:
    if path.exists() and not overwrite:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def build_manifest(root: Path) -> dict:
    return {
        "schema_version": 1,
        "canonical_root": str(root),
        "directories": DIRECTORIES,
        "controls": [
            "00-control/org_constants.yaml",
            "00-control/record_series.yaml",
            "00-control/repository_manifest.json",
            "00-control/Activation-Control-Workbook.xlsx",
        ],
        "principles": {
            "one_canonical_current_copy": True,
            "preserve_superseded_versions": True,
            "no_backdating_or_fabrication": True,
            "record_identity_distinct_from_filename": True,
        },
    }


def copy_activation_pack(pack: Path, root: Path) -> None:
    if not pack.exists():
        raise SystemExit(f"Activation pack does not exist: {pack}")
    for filename, rel_dest in ACTIVATION_DESTINATIONS.items():
        src = pack / filename
        if not src.exists():
            print(f"warning: activation artifact missing, skipped: {src}")
            continue
        dest_dir = root / rel_dest
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest = dest_dir / filename
        if dest.exists():
            print(f"exists, skipped: {dest}")
        else:
            shutil.copy2(src, dest)
            print(f"seeded: {dest}")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", default="institution", help="Repository root to create (default: institution)")
    ap.add_argument("--activation-pack", help="Optional directory containing the downloadable activation artifacts")
    ap.add_argument("--overwrite-control-files", action="store_true", help="Rewrite seed YAML/README/control manifest files only; never deletes records")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    root.mkdir(parents=True, exist_ok=True)
    for rel in DIRECTORIES:
        (root / rel).mkdir(parents=True, exist_ok=True)

    write_if_allowed(root / "README.md", README, args.overwrite_control_files)
    write_if_allowed(root / ".gitignore", GITIGNORE, args.overwrite_control_files)
    write_if_allowed(root / "00-control/org_constants.yaml", ORG_CONSTANTS, args.overwrite_control_files)
    write_if_allowed(root / "00-control/record_series.yaml", RECORD_SERIES, args.overwrite_control_files)
    manifest = json.dumps(build_manifest(root), indent=2) + "\n"
    write_if_allowed(root / "00-control/repository_manifest.json", manifest, args.overwrite_control_files)

    # Make empty directories visible to Git without creating fake records.
    for rel in DIRECTORIES:
        d = root / rel
        if not any(d.iterdir()):
            (d / ".gitkeep").touch(exist_ok=True)

    if args.activation_pack:
        copy_activation_pack(Path(args.activation_pack).resolve(), root)

    print(f"Scaffold ready: {root}")
    print("No operational history or unresolved facts were generated.")


if __name__ == "__main__":
    main()
