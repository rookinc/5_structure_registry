# Program 5: Thalean structure registry and constraint mapping

Archive edition: 24 September 2026.

This program packages the core terminology consolidation, named structure/view
registry, and CP-SAT-ready alias-consistency model. It is an archival and indexing
program, not a new theorem seal or a continuation of Programs 1-4.

## Read

- [Verbose core terms: 160 canonical entries](glossary/notes/qr_core_terms.md)
- [Core-term names, aliases and sources](glossary/notes/qr_core_terms_index.md)
- [Core-term changes and deduplication](glossary/notes/qr_core_terms_changes_2026-09-24.md)
- [Structure registry: 225 named views](registry/notes/qr_structure_registry.md)
- [Qualified names](registry/notes/qualified_names.md)
- [Reused-label collision index](registry/notes/label_collision_index.md)
- [Consolidation relationship ledger](registry/notes/consolidation_ledger.md)
- [Offline explorer](registry/structure_explorer.html)
- [CP-SAT mapping report](cp_sat/reports/structure_cp_sat_report.md)
- [Archived CP-SAT engine status](cp_sat/reports/cp_sat_result.json)

The HTML explorer runs locally in a browser. The Markdown pages are the browsing
surface on GitHub; this bundle does not configure a GitHub Pages site.

## Preservation and status

The three delivered packages are extracted under `glossary/`, `registry/`, and
`cp_sat/`. Their source files and package-internal relative paths are unchanged.
Only the outer ZIP directory prefixes were removed. `SOURCE_ARCHIVES.json` records
the original archive hashes, destination roots, and checksum counts.

The glossary package includes the original uploaded core-terms note unchanged.
The root `notes/qr_core_terms.md` installed by the wrapper is a byte-identical
working copy of `glossary/notes/qr_core_terms.md` at this archive edition. It may
later evolve independently; this program preserves the dated source.

The archived CP-SAT engine status is NOT_RUN. Its source/encoding preflight is
recorded as executed, but is not CP-SAT execution. Publishing this package does not
promote a reported result, resolve an occurrence, or prove a native equivalence.
The newest full history/analyzer action claims retain the source's conversation-
reported boundary until their original producer/action tables are archived.

## Verify without changing the archive

Run from this directory:

    python3 verify_archive.py

This checks preserved bytes and the archived execution boundary. It does not run
historical mathematical producers, regenerate reports, install OR-Tools, or solve
the constraint model. To run or revise those programs, copy the frozen package to
a new working edition and preserve its input and output receipts separately.

## Repository boundary

No Git repository or remote is created by this package. Do not assume that the QR
parent and Programs 1-4 share a Git root. The top-level preparation helper reads
those local boundaries before any staging. Do not stage the entire QR tree merely
to publish these files; it may contain independent repositories.

## Publication content

The preserved provenance includes research notes, source excerpts, exact-data
snapshots and the Draft 6 source archive. Source-relative links remain intact.
Source prose can contain workstation paths and author metadata. No redaction,
license declaration, public visibility change, or remote selection is introduced.
