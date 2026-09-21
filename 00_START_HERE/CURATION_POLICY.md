# Way Repository Curation Policy

## 1. Preserve first

Curation begins by preserving provenance.

Do not delete, overwrite, or silently rewrite an artifact merely because a newer copy exists.

## 2. Separate lifecycle from subject

Every artifact should eventually have a lifecycle classification independent of its topic:

- `current-source`
- `current-canonical`
- `current-working`
- `released-snapshot`
- `predecessor`
- `historical`
- `working-note`
- `generated`
- `unclassified`

## 3. Released snapshots are immutable

Files inside a named historical release should normally remain byte-stable.

Corrections belong in a later release or an explicit errata/addendum file.

## 4. Canonical/current repositories may supersede without erasing

Where a canonical/current tree supersedes a predecessor:

- keep the predecessor;
- record the relationship;
- do not backdate;
- do not make the predecessor appear to have contained later decisions.

## 5. Duplicate handling

An exact duplicate is not automatically removable.

Classify each duplicate group before deduplication:

### A. Intentional release duplication
A current/source artifact copied into a versioned release.

**Default:** preserve both.

### B. Canonical + historical mirror
A current canonical copy and an older flattened/pre-integration copy.

**Default:** preserve canonical copy; historical copy may remain for provenance until archive consolidation is verified.

### C. Version carry-forward
The same unchanged artifact appears in successive version directories.

**Default:** preserve inside immutable releases; consider reducing duplication only in non-release working trees.

### D. Generated dependency/build duplication
Examples: `node_modules`, `.next`, caches.

**Default:** do not track; reconstruct from lockfiles/build tooling.

### E. Accidental loose duplicate
No lifecycle or provenance reason exists for multiple live copies.

**Default:** select a source of truth, preserve migration history, then remove redundant live copy through a reviewed PR.

## 6. Authority is explicit, not inferred

Do not infer that a document is adopted because:

- it is polished;
- it is a PDF/DOCX;
- it appears in a folder named `source`;
- it has a version number;
- it contains "constitution", "policy", "canon", or "final" in the title.

Authority must come from the relevant adoption/status record.

## 7. Research is not doctrine

HTERP findings, hypothesis ledgers, proto-canon structures, and constructive-theology drafts remain research/constructive material unless a separate adopted Way instrument gives them doctrinal status.

## 8. Legal drafts are not operative records

Pre-filing and model legal/governance instruments remain drafts until actual authorized persons adopt/file them.

Executed records must never be fabricated from templates.

## 9. Binary + source relationship

Where a DOCX/PDF is compiled from Markdown/CSV/JSON source:

- preserve the source;
- preserve release binaries where they are part of a release;
- identify the authoritative editable source where known;
- do not edit release binaries in place to create a new version.

## 10. Branch and PR discipline

Substantive curation should occur on a branch.

PR descriptions should state:

- lifecycle changes;
- files selected as source of truth;
- files archived/removed;
- duplicate groups affected;
- whether any released snapshot changed;
- unresolved questions.

## 11. No mass deduplication without a map

The original inventory reports hundreds of SHA-256 duplicate groups. Many are expected.

Do not execute a blanket duplicate deletion.

Deduplication should proceed domain by domain after a source-of-truth map exists.

## 12. Current curation objective

The immediate objective is not to minimize file count.

It is to make the corpus **legible, traceable, and safe to evolve**.
