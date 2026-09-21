# Historical ZIP Archive Reclassified

**Date:** 2026-09-21  
**Branch:** `curation/reclassify-archive-packages-v2`

The contents of `99_UNCLASSIFIED/.archive/` were reviewed and found to be classifiable historical package snapshots rather than genuinely unresolved material.

All 34 ZIP blobs were moved byte-for-byte into:

`80_HISTORICAL_AND_PREINTEGRATION_PACKAGES/archive-packages/`

with six domain groups:

- `research-hterp/`
- `religious-source-releases/`
- `organizational-releases/`
- `institutional-integrity/`
- `institutional-and-church/`
- `digital-platform/`

No ZIP was recompressed or altered; the move reused each existing Git blob SHA.

A new `ARCHIVE_PACKAGE_REGISTRY.csv` records filename, domain classification, package type, SHA, size, previous path, current path, and lifecycle note for every package.

`99_UNCLASSIFIED/` now contains only its README and is reserved as a future holding area for genuinely unresolved material.
