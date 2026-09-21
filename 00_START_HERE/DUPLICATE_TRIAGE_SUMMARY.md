# Duplicate Triage Summary

**Source:** original local SHA-256 inventory created during the non-destructive organization pass  
**Total duplicate groups:** 594  
**Total duplicate file rows:** 1,657

## Classification

| Class | Groups | Interpretation | Default action |
| --- | ---: | --- | --- |
| Generated app artifacts | 321 | Duplicate files inside the original local `node_modules/` / `.next/` snapshot | Do not track; reconstruct from lock/build metadata |
| Canonical institutional ↔ historical mirror | 136 | Same operational/template files in `institution/` and older flattened/pre-integration packages | Preserve canonical copy; retain historical mirror for provenance until optional archive compaction |
| Integrity ↔ historical mirror | 45 | Integrity material also preserved in older root/pre-integration packages | Preserve current/versioned integrity history |
| Integrity version carry-forward | 38 | Unchanged files carried from one integrity version to another | Preserve inside version history/releases |
| HTERP version carry-forward | 25 | Unchanged research files carried from v0.1/v0.2 into later HTERP versions | Preserve as version snapshots; current working copy is v1.4 |
| Source ↔ release snapshot | 13 | Exact source files mirrored into v1.0/v1.2 releases | Preserve both source provenance and immutable release snapshots |
| Historical mirror — other | 6 | Historical top-level exports identical to reference/release artifacts | Preserve reference/release copy; historical copy optional only after provenance review |
| Release carry-forward | 5 | v1.0/v1.1 reference publications copied into later release packages | Preserve immutable release packages |
| Archive ↔ current release mirror | 2 | Source-pack ZIP duplicated in `99_UNCLASSIFIED/.archive` and versioned release | Release copy is the meaningful packaged copy; archive copy may be reviewed later |
| Original-root metadata ↔ release README | 1 | Original root `README_RELEASE.md` equals v1.2 release README | Preserve original metadata snapshot and release copy |
| Nested local Git-log artifact | 1 | Duplicate `.git/logs` files from the original local app directory | Not repository content; exclude from Git |
| Local env example/local copy | 1 | `.env.local` was identical to `.env.example` in the local snapshot | Keep example; keep local env untracked |

**Total:** 594 groups.

## Key conclusion

There are **no unexplained duplicate groups remaining at this classification level**.

The original count of 594 should therefore not be interpreted as 594 cleanup defects. Most duplication is intentional provenance/versioning or generated local application state.

## What should actually be removed?

### From Git tracking

Generated or local-only material should stay untracked:

- `node_modules/`
- `.next/`
- nested `.git/` metadata
- `.env.local`
- caches

The repository-level and app-level ignore rules cover these classes for future work.

### Do not mass-delete

Do not mass-delete:

- versioned releases;
- HTERP historical versions;
- integrity version snapshots;
- historical/pre-integration mirrors;
- current source ↔ released source duplicates.

Those duplicates carry lifecycle/provenance meaning.

## Future optional compaction

If repository size later becomes a problem, the safest optional compaction target is **historical loose mirrors that have a verified canonical/current or immutable release counterpart**.

Any such compaction should:

1. identify the retained source of truth;
2. record the old path;
3. preserve release immutability;
4. preserve a migration manifest;
5. avoid rewriting historical version directories.

At present, clarity is more valuable than reducing file count.
