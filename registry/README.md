# Thalean structure registry - 24 September 2026

**225 named structure/view and notation records; 61 typed relationship decisions.**

This archive separates reused letter-number labels into source-defined objects before attempting consolidation. It is a companion to `qr_core_terms.md`, not a replacement of that file or a new mathematical audit.

## Start here

Open **[the offline searchable explorer](structure_explorer.html)** in a browser. It is self-contained: search and filtering do not need a server or Internet connection. The packaged source links work after extracting the complete ZIP.

The portable text edition is **[notes/qr_structure_registry.md](notes/qr_structure_registry.md)**. The [priority collision guide](notes/priority_collisions.md) gives the high-risk cases first. The [qualified-name table](notes/qualified_names.md) is the compact naming index.

## What the counts mean

The lexical sweep covers 228 retained text-file paths, reduced to 225 byte-distinct payloads, and records 6,679 occurrences under 354 lookup keys. A token is not a mathematical object. These totals include equation numbers, audit codes, indexed variables, dimensions, ordinary powers, and repeated discussion in earlier glossary versions.

The 225 registry records include mathematical structures, specific views, parameterized families, comparison targets, and explicit notation/metadata bins. They are not 225 distinct proven native objects. The matching number of byte-distinct source files is coincidental.

## Main files

| Path | Purpose |
|---|---|
| `notes/qr_structure_registry.md` | Full definitions, domains, type, action, typed sizes, evidence and boundaries. |
| `notes/label_collision_index.md` | Every lexical lookup key and its candidate named views. |
| `notes/consolidation_ledger.md` | Source-backed identities, descents, quotients, constructions, rejected mergers and open comparisons. |
| `notes/unresolved_label_queue.md` | Missing source payloads and unresolved/ambiguous local annotations. |
| `data/structure_registry.json` | Authoritative curated names, records, sources and typed relationships. |
| `data/structure_registry.csv` | Flat machine-readable record table. |
| `data/occurrences.jsonl` | Every match with its source path, original line/column, spelling and candidate views. |
| `data/label_index.json` | Complete key-to-occurrence and key-to-candidate index. |
| `provenance/coverage.md` | Full-text versus excerpt coverage and limitations. |
| `provenance/inputs/` | Preserved source files and current Draft 6 text/data. |
| `provenance/excerpts/` | Explicitly labeled passage digests and current-chat digest. |
| `data/validation_report.json` | Archive integrity and internal reference checks, not mathematical verification. |
| `SHA256SUMS` | File integrity hashes. |

## Naming and consolidation policy

The proper name identifies the view: for example **Native G60 rooted-neighborhood stabilizer**, **Native face realization kernel**, or **Real five-frame oriented difference operator**. The old label remains searchable.

Retain separate IDs when the carrier, embedding, selected root/face, coefficient field, basis, action, kernel/image role, or evidence boundary differs. Link proven relationships explicitly. Only a stated same-entity correspondence can support alias consolidation; a quotient or abstract group isomorphism does not.

This is not an automatic global rename. In particular, `D8`, `D5`, `T10`, `S1`, `r1`, `P0`, and `K120` cannot safely be replaced without reading the local context. The sources use mixed dihedral conventions: D8 has total order 8, historical D5 order 10, and registered-decagon D10 order 20. Store the order and presentation separately from the source spelling.

## Rebuild and validate

Python 3 with its standard library is sufficient:

```sh
python3 scripts/build_indexes.py
python3 scripts/validate_archive.py
sha256sum -c SHA256SUMS
```

`build_indexes.py` scans the frozen sources and renders the text indexes from the curated JSON. It does not discover semantic equivalences or run historical producers. Manual changes to names, classifications or source files change the published archive; regenerate its manifest and checksums for a new edition rather than treating this edition's hashes as current.

## Repository placement

Suggested main note: `notes/qr_structure_registry.md`. Keep the supporting index and ledger beside it. Preserve the archive folder for working relative source links and reproducibility. The actual local repository and existing `notes/qr_core_terms.md` have not been changed.

The next consolidation step is to choose a candidate pair in the relationship ledger and inspect its specific source map. No additional mathematical identification is being admitted merely by publishing these names.
