# Controlled-Draft Exception Added to Organizational Crosswalk

**Date:** 2026-09-21  
**Context:** Follow-up to merged PR #4 and its post-merge Codex review

A post-merge review correctly identified that the organizational-release crosswalk was too restrictive. It said release-derived material should enter the canonical institution tree only after adoption/execution/filing, while the canonical institution architecture itself permits controlled drafts, templates, and working regulatory materials.

The crosswalk has been corrected so that:

- immutable releases remain unchanged;
- explicitly statused **TEMPLATE**, **WORKING**, and **READY-FOR-REVIEW** derivatives may live in their designated canonical working/template paths;
- controlled drafts must not be represented as operative merely because they are in the canonical institution tree;
- **ADOPTED**, **EXECUTED**, **FILED**, **ACCEPTED/ISSUED**, or equivalent status still requires the appropriate real-world event and evidence;
- executed-record locations must not be populated with hypothetical future actions as though they occurred.

This aligns the crosswalk with the existing Canonical Path Registry and the institution repository's own draft-preservation controls.
