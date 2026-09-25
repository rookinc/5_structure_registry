# Thalean registry to CP-SAT mapping

Date: 2026-09-24

**225 views retained. 61 source relationship decisions mapped.**
Two source-supported alias joins; 47 original non-alias relations; 12 open comparisons.
Three explicit type guards bring the scoped pair report to 64 probes.

Start with [the report](reports/structure_cp_sat_report.md).

## Actual execution status

- Standard-library source/compiler preflight: PASS, 174 assertions.
- Independent exact equality/disequality fragment: consistent.
- OR-Tools CP-SAT execution and CP-SAT model validation: NOT RUN here.
- CP-SAT runner: Python syntax checked; engine integration not executed here.
- Original mathematical producers: not replayed.
- New native equivalences, probability laws or semantic annotations: none admitted.

OR-Tools is not installed in the available runtime; the installation attempt could
not resolve its package host. This limitation is recorded rather than replaced by a
fabricated solver receipt.

## Contents

- `reports/structure_cp_sat_report.md`: full mapping, interpretation and pair ledger.
- `inputs/model.json`: constraint-ready records, policies, relationships and queries.
- `inputs/source_registry.json`: the unaltered source registry content.
- `reports/preflight.json`: executed checks and input hashes.
- `reports/pair_queries.json` and `.csv`: all 64 scoped relation probes.
- `reports/constraint_ledger.csv`: 52 hard alias constraints with source IDs.
- `reports/supported_alias_classes.json`: editorial alias classes, all views retained.
- `reports/cp_sat_result.json`: explicit engine execution status.
- `data/occurrence_domains.jsonl`: 6,679 untouched candidate lists plus an unresolved option.
- `data/native_bridge_requests.json`: the 12 open comparison contracts.
- `scripts/registry_model.py`: conservative compiler and independent exact fragment checker.
- `scripts/preflight.py`: source and encoding verification.
- `scripts/run_cp_sat.py`: actual OR-Tools runner, opposite probes and assumption cores.
- `scripts/make_report.py`: report renderer.
- `upstream/thalean_symbol_registry_2026-09-24.zip`: preserved source archive.
- `MANIFEST.json` and `SHA256SUMS`: package integrity.

## Run

```bash
python3 scripts/preflight.py
```

In a supported Python environment with OR-Tools:

```bash
python3 -m pip install -r requirements.txt
python3 scripts/run_cp_sat.py
```

The current executable scope is registry alias consistency. It is not a solver for
all abstract isomorphisms or all native intertwiners in the registry. The report
specifies what source data is required to build those next modules.

No optimization objective rewards fewer names. Feasibility does not promote a
candidate. Infeasibility applies only to the supplied encoding and map family.
