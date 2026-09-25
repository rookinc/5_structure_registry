# Thalean CP-SAT Mapping Report

Date: 2026-09-24  
Edition: v0.1 - frozen-registry mapping and independent preflight  
Source: the supplied Thalean Structure and Label Registry archive

## Executive result

Yes: the registry can be turned into a constraint report. The useful question is not
"how few names can we keep?" It is "which identifications are required, prohibited,
or still undecided by a specified body of evidence, and what actual map would settle
an undecided comparison?"

This package maps all **225 view records** and **61 recorded relationship decisions**.
It retains every view, its domain, its family parameters, its original standing and
its source anchors. Two existing source-identified alias decisions are retained.
No new mathematical identification is admitted.

**Execution boundary:** the standard-library archive/compiler preflight was run and
passed 174 assertions. The complete equality/disequality fragment was
checked independently. **OR-Tools CP-SAT was not available in this runtime, and an
attempt to install it was blocked by unavailable network resolution. CP-SAT itself
was not run; its own model validation was not run.** The included runner is
syntax-checked, not execution-tested against an installed OR-Tools engine here.
`reports/cp_sat_result.json` records `engine_status: NOT_RUN`.

This is therefore a **CP-SAT-ready mapping with an executed independent preflight**,
not a completed CP-SAT search and not a new native theorem.

## 1. What was actually mapped

| Item | Count | Interpretation |
|---|---:|---|
| Retained named view records | 225 | Includes families, operators, groups, sets and metadata views. |
| Original relationship decisions | 61 | All are translated explicitly; no unknown decision is silently defaulted. |
| Original source-supported alias decisions | 2 | Equality at the stated editorial referent level, retaining the views. |
| Original preserve-separate decisions | 47 | No alias substitution at the recorded view/domain level. |
| Original open comparisons | 12 | Both possibilities survive the present weak alias encoding; no promotion. |
| Additional reviewed type guards | 3 | Two group/operator separations and kernel-order 10 versus image-order 8. |
| Hard alias constraints | 52 | 2 equalities and 50 disequalities after the type guards. |
| Scoped pair probes | 64 | The 61 source relationship pairs and the 3 type-control pairs. |
| Other possible record pairs | 25,136 | Not tested. They are not declared distinct or equivalent. |
| Source-supported alias buckets | 223 | 225 views minus two alias joins; not 223 proved distinct mathematical objects. |
| Retained lexical occurrences | 6,679 | Candidate lists and original review statuses are retained unchanged. |
| Lookup keys | 354 | Lookup strings, not object identities. |
| Source anchors checked against archived bytes | 57 | Hash integrity only, not validation of the source's mathematics. |
| New semantic occurrence assignments | 0 | A candidate list is not accepted as an interpretation. |

The two source-supported alias joins are:

| View A | View B | Qualified names |
|---|---|---|
| `g-family-6` | `g60-native` | Sixty-vertex census-family child 6 / Thalion native graph carrier |
| `s12-phase-set` | `twelve-face-phases` | Twelve-state phase factor of the serialized line map / Twelve face/relative-orientation objects |

These joins were already in the supplied registry. They are not solver discoveries.
An explicitly source-identified graph may have multiple coordinate presentations;
the alias bucket does not erase their vertex-label crosswalk.

## 2. The identity question must be typed

A single `same_object` flag would recreate the ambiguity we are trying to remove.
At least five distinct comparisons are needed:

| Comparison | What must agree | What a positive result does not automatically establish |
|---|---|---|
| Editorial alias | A source identifies two names with one declared referent. | Equal stored coordinates or identical constructor histories. |
| Literal embedded subgroup or actor | Ambient carrier, actual elements/actions, and selected parameters. | A different embedding with the same abstract type. |
| Abstract group isomorphism | A bijection preserving multiplication. | Same action, same root, same physical role, or the same named generator. |
| Equivariant action equivalence | A group correspondence and a carrier bijection commuting with the actions. | A canonical or uniquely selected map unless separately proved. |
| Quotient, embedding or operator construction | The specified direction, kernel, fibers or algebraic operation. | Synonymy between its source and target. |

A linear intertwiner is a further typed comparison. Its coefficient field, whether
it is invertible/isometric, and its permitted map family must be declared.
A signed-permutation search is narrower than a search over all real linear maps.

The current executable model addresses the first row: **editorial alias consistency**.
The preserved relationship ledger and bridge request manifests retain the other rows
as separate mathematical obligations. An `INFEASIBLE` alias proposal is not a
refutation of abstract isomorphism. An `OPEN` alias proposal is not evidence that
a native intertwiner exists.

## 3. Model variables and constraints

### 3.1 Immutable views and editable alias buckets

Every original stable view ID remains immutable. For each view `v`, the model has an
integer variable `bucket[v]`. Equal bucket values mean a proposed editorial alias
join at the declared referent level; they do not delete the original view records.

```text
source-supported alias A,B:
    bucket[A] = bucket[B]

source-directed non-alias separation A,B:
    bucket[A] != bucket[B]

open comparison A,B:
    no equality or disequality is asserted by that relationship alone
```

Equality of integer bucket variables provides transitivity. It avoids the common
encoding error of separately asserting pairwise equivalences while forgetting that
A=B and B=C force A=C.

Each hard relation receives a stable constraint ID, its inherited relationship type,
its source IDs, and its evidence standing. `REL001` through `REL061` refer to the
original relationship ledger; `TYPE001` through `TYPE003` are explicit additional
encoding guards. None is extracted by guessing the meaning of a subscript.

The runner limits each variable's possible bucket labels to the connected component
of the **scoped comparison graph**. This is a computational scope restriction, not
a claim that different components could never be connected. Queries outside this
scope remain `NOT_TESTED`.

### 3.2 Occurrence variables do not manufacture semantic evidence

For an occurrence `o`, the optional occurrence layer has

```text
meaning[o] in {UNRESOLVED} union candidate_structure_ids[o]
```

The archive includes all original spellings, notation classes, source paths,
line/column locations, candidate IDs and review statuses. An unresolved value is
always permitted. A single candidate is still only a single candidate, not a
source-verified interpretation. The current model supplies no new contextual
annotation constraints and admits zero new semantic assignments.

In particular, the **1,951 ambiguous occurrences remain ambiguous**. There is no
objective rewarding the solver for making uncertainty disappear. The runner's
`--include-occurrences` option demonstrates the representation only; without more
source-grounded constraints, it cannot improve the interpretation.

### 3.3 Evidence eligibility is separate from logical possibility

An undecided pair may be merged or separated in different feasible assignments of
this limited model. That is a statement about missing constraints, not a discovered
mathematical equivalence. The exported record explicitly sets
`promotion_eligible_from_this_input: false` for every open comparison.

A solver cannot convert a conversation-reported advance into a replayed theorem.
Source-recorded, conditional, locator-only and conversation-reported standings remain
attached to their original statements.

## 4. Concrete D8 / D5 example

The registry distinguishes:

```text
face-stabilizer     : native face-family ambient stabilizer, order 80
    |
    +-- kernel     : d5-face-kernel, order 10
    |
    +-- image      : d8-face-blocks, order 8, acting on four signed blocks
```

The recorded orders satisfy

```text
80 = 10 * 8.
```

The independent preflight checks this arithmetic. It does not re-establish the
kernel or the group action. A later structural CP-SAT module can encode the actual
homomorphism once its action tables and kernel elements are supplied.

The two other `D5` views remain separate:

```text
d5-history       : historical order-ten rotation-reflection register
frame-difference : D5_frame = S - S^-1, a real linear operator
```

The frame operator is not a group. Both group/operator comparisons are therefore
explicit non-alias controls. The historical group and the face kernel have the same
abstract dihedral type, but their actual action crosswalk remains an open comparison.
Their shared order is not used to merge them.

Similarly, a faithful rooted descent connects the common-cover, G60 and positional
D8 views. It is stored as a bridge, not as permission to substitute arbitrary source
and target actions or their central elements.

Sources for this example are preserved in the original registry under `FACE`,
`D5_KERNEL`, `HISTORICAL_FIVEFOLD`, `CHAT`, `COVER` and `MM`.

## 5. How the report distinguishes forced, excluded and undecided

After establishing that the baseline constraints are consistent, the runner performs
two satisfiability probes for every scoped pair A,B:

```text
Probe M: add bucket[A] = bucket[B]
Probe S: add bucket[A] != bucket[B]
```

| Merge probe | Separate probe | Report meaning |
|---|---|---|
| Feasible | Infeasible | Alias is forced by the frozen input constraints. |
| Infeasible | Feasible | Alias conflicts with the frozen view-level constraints. |
| Feasible | Feasible | Open under the encoding; do not promote either choice. |
| Any inconclusive solver result | Any | Inconclusive unless the other evidence settles the exact requested question. |
| Baseline inconsistent | Any | Quarantine the report and inspect the encoding/source constraints. |

The current exact preflight obtains the first three classifications using a complete
independent checker for this equality/disequality fragment. It produces 2 forced
aliases, 50 view-level separations, and 12 open comparisons. **These are not claimed
CP-SAT engine results.** The future CP-SAT run is required to agree on every conclusive
probe; disagreement stops the script instead of being interpreted as a discovery.

There is **no minimization objective**. Minimizing the number of names would prefer
unsupported merges. Maximizing assignments would prefer unsupported interpretations.
Either could be useful later as an explicitly labeled editorial scenario, but neither
is a theorem or part of this report.

The official CP-SAT interface distinguishes `OPTIMAL`, `FEASIBLE`, `INFEASIBLE`,
`MODEL_INVALID` and `UNKNOWN`. An `OPTIMAL` response from a satisfaction problem is
not a uniqueness certificate. The opposition probes, not the word "optimal", test
whether a proposed relation is forced. [OR1]

## 6. Contradiction explanations and controls

Each hard constraint is guarded by its own positive assumption literal in the CP-SAT
runner. An infeasible probe can report a sufficient set of assumptions, mapped back
to named records and source anchors. The core returned by CP-SAT is not automatically
minimum-cardinality or even inclusion-minimal. [OR2, OR3]

The independent fragment checker separately reduces its own contradiction sets by
deletion. It verifies that each returned set is inconsistent and that deleting any
member removes that contradiction. Its claim is **deletion-minimal within the exact
fragment**, not a smallest possible explanation and not a CP-SAT core.

Executed controls include a three-view transitivity contradiction and a stress test
that proposes aliasing every D8 view merely because its spelling is D8. The latter
conflicts with the original registry's distinctions. This checks the encoding's
resistance to the exact error the registry was designed to prevent; it does not
establish new group theory.

The byte-integrity and compiler assertions total 174. That count includes
source hashes and conflict checks; it is not a count of new mathematical theorems.

## 7. Open comparison queue

These comparisons remain open in the limited model. Their native obligations are
in `data/native_bridge_requests.json`.

| ID | Source view | Target view |
|---|---|---|
| REL010 | Native face realization kernel | Historical fivefold rotation-reflection register |
| REL011 | Selected face complex/reflection operator group | Charge-center dihedral comparison target |
| REL012 | Selected face complex/reflection operator group | Four-signed-block face permutation group |
| REL018 | Native free normal Klein deck register | Klein-valued quotient voltage label group |
| REL019 | Native free normal Klein deck register | Rooted dihedral central quotient plane |
| REL028 | Twelve-section closure surface state set | Twelve-point normalized relational-kernel carrier |
| REL031 | Opposite-phase different-face crown orbital | Registered-pentagon conference support graph |
| REL032 | Five-frame golden contrast operator | Historical-register golden contrast operator |
| REL046 | Companion four-generator additive winding cochain | Primitive registered-history winding class |
| REL047 | Twelve-dimensional analyzer-frame candidate module | Registered-pentagon coefficient module |
| REL048 | 201EZ order-120 classification locator | Common AT4val-family bipartite cover graph |
| REL055 | Unoriented-axis stabilizer in rotations | Orthogonal winding-plane reference-transport envelope |

For each, begin by naming the requested map. Some rows ask for native identification;
others ask for a history or operator correspondence, while a locator-only target may
not yet provide enough data to define a comparison at all.

## 8. Next structural layer: solve for actual maps

Once both objects have a complete finite specification, CP-SAT can search for a
finite witness instead of merely checking names. The search contract must remain
separate from the input registry.

### Finite group isomorphism

Give explicit multiplication tables for G and H. For each g in G, use an integer
variable `phi[g]` naming its image in H. Impose a bijection, the identity constraint,
and the complete multiplication law:

```text
phi[g*h] = phi[g] * phi[h].
```

The products on the right must come from H's supplied table. Table/element constraints
can implement these finite lookups. A resulting witness is independently checked
against every product. Rooted stabilizers additionally retain their selected root
and ambient embedding; an abstract isomorphism does not remove those parameters.

### Action equivalence

Give generator actions on finite carriers X and Y and the correspondence between
those generators. Search for a bijection `pi` such that

```text
pi(g.x) = phi(g).pi(x).
```

This is the correct form for asking whether two named D8 views act in the same way
under the requested crosswalk. Exact validation must check the actual source arrays,
not two arrays both produced by the same possibly faulty compiler.

### Quotient and kernel

A quotient requires a surjection with declared fibers rather than `AllDifferent`.
Check the transported action and kernel explicitly. Unequal cardinalities can be
correct for a quotient even though they forbid a bijective carrier identification.

### Signed actions and cocycles

A supplied sign defect can be represented by Boolean variables and parity equations.
For a candidate sign rephasing `x[g]`, a typical equation is

```text
x[g] + x[h] + x[g*h] = omega[g,h]  (mod 2).
```

The actual cocycle table must be supplied. Do not insert the desired cancellation as
an axiom and then report its consistency as a native derivation.

### Linear intertwiners and algebraic coefficients

CP-SAT is an integer solver. [OR1] Keep irrational structure exact outside the solver,
or encode a declared finite coefficient representation and map family. For matrices
in Q(sqrt(5)), preserve rational and sqrt(5) coefficients separately; do not round
sqrt(5) into an integer surrogate and call the result exact.

A useful division is: CP-SAT proposes a permutation, signed permutation, bounded
integer map, or finite incidence assignment; exact algebra verifies
`T A_g = B_g T`, rank, invertibility, Gram relations and any required kernel.
Infeasibility in a bounded or signed-permutation family excludes only that family.
It cannot exclude an unrestricted real intertwiner.

## 9. Consolidation policy

Promote a result only at the level tested. Source aliases can share a referent key.
Explicit isomorphisms can share an abstract type while retaining their embeddings.
An equivariant crosswalk links two action views and includes its reference choices.
A quotient or kernel relation remains a directed relation, not an alias.

The resulting archive should be a constraint-backed map of structures, not one giant
bin of objects with coincident labels. Names lead to views; views lead to supplied
objects; proposed identifications lead to explicit map obligations.

The earlier G15 CP-SAT search concerned a different matrix-construction problem.
This registry encoding does not supersede, reconstruct or claim a dependency on that
historical matrix witness.

## 10. Reproduction

The input ZIP is retained byte-for-byte under `upstream/`. Run from the extracted
package root:

```bash
python3 scripts/preflight.py
python3 scripts/make_report.py
```

The preflight requires only Python's standard library. In a Python environment with
OR-Tools installed, run:

```bash
python3 scripts/run_cp_sat.py
```

The optional lexical-domain representation is enabled with:

```bash
python3 scripts/run_cp_sat.py --include-occurrences
```

All runs write only inside this extracted package. They do not edit the user's
research repository, rename source symbols, upload to Library, or mutate native
admission records. The solver writes its exact engine version, parameters, model,
search log, individual query statuses and a separately checked feasible witness.
That arbitrary witness is explicitly not an accepted consolidation plan.

## 11. Source and methodology references

The mathematical structure descriptions in this report are inherited from the
supplied registry, not supplemented with outside mathematical identifications.
Original record/source standings remain unchanged. The full source archive is at
`upstream/thalean_symbol_registry_2026-09-24.zip`; its SHA-256 is recorded in
`reports/preflight.json`.

OR1. Google OR-Tools, CP-SAT Solver: integer model requirements, status meanings,
model validation and solution enumeration. Retrieved 2026-09-24.
`https://developers.google.com/optimization/cp/cp_solver`

OR2. Google OR-Tools, CP-SAT troubleshooting: assumptions and diagnostic boundaries.
Retrieved 2026-09-24.
`https://github.com/google/or-tools/blob/stable/ortools/sat/docs/troubleshooting.md`

OR3. Google OR-Tools, assumptions sample: tagged constraints and sufficient
assumptions for infeasibility. Retrieved 2026-09-24.
`https://github.com/google/or-tools/blob/stable/ortools/sat/samples/assumptions_sample_sat.py`

## Appendix A. Complete scoped pair report

These are independent exact-fragment classifications of the compiled frozen input,
not CP-SAT statuses and not mathematical isomorphism verdicts.

| ID | Left view ID | Right view ID | Classification |
|---|---|---|---|
| REL001 | `d8-native-root` | `d8-position` | SEPARATE_AT_RECORDED_VIEW_LEVEL |
| REL002 | `d8-cover-root` | `d8-position` | SEPARATE_AT_RECORDED_VIEW_LEVEL |
| REL003 | `g-family-6` | `g60-native` | FORCED_ALIAS_BY_FROZEN_INPUT |
| REL004 | `k120-common-cover` | `g60-native` | SEPARATE_AT_RECORDED_VIEW_LEVEL |
| REL005 | `q30-family` | `g30-original` | SEPARATE_AT_RECORDED_VIEW_LEVEL |
| REL006 | `g1800-family` | `g900-associated` | SEPARATE_AT_RECORDED_VIEW_LEVEL |
| REL007 | `g9000-registered` | `g1800-family` | SEPARATE_AT_RECORDED_VIEW_LEVEL |
| REL008 | `d5-face-kernel` | `face-stabilizer` | SEPARATE_AT_RECORDED_VIEW_LEVEL |
| REL009 | `face-stabilizer` | `d8-face-blocks` | SEPARATE_AT_RECORDED_VIEW_LEVEL |
| REL010 | `d5-face-kernel` | `d5-history` | OPEN_UNDER_ENCODED_CONSTRAINTS |
| REL011 | `d8-selected-face-operators` | `d8-charge-center-locator` | OPEN_UNDER_ENCODED_CONSTRAINTS |
| REL012 | `d8-selected-face-operators` | `d8-face-blocks` | OPEN_UNDER_ENCODED_CONSTRAINTS |
| REL013 | `d8-surface-edges` | `d8-lifted-holonomy` | SEPARATE_AT_RECORDED_VIEW_LEVEL |
| REL014 | `d8-lifted-holonomy` | `d8-native-root` | SEPARATE_AT_RECORDED_VIEW_LEVEL |
| REL015 | `q8-lifted-holonomy` | `d8-lifted-holonomy` | SEPARATE_AT_RECORDED_VIEW_LEVEL |
| REL016 | `d8-history-factor` | `history-coset-image` | SEPARATE_AT_RECORDED_VIEW_LEVEL |
| REL017 | `v4-native` | `v4-fp-kernel` | SEPARATE_AT_RECORDED_VIEW_LEVEL |
| REL018 | `v4-native` | `v4-voltage` | OPEN_UNDER_ENCODED_CONSTRAINTS |
| REL019 | `v4-native` | `v4-root-projective` | OPEN_UNDER_ENCODED_CONSTRAINTS |
| REL020 | `c2-root-center` | `c2-native-double-deck` | SEPARATE_AT_RECORDED_VIEW_LEVEL |
| REL021 | `c2-history-extra` | `c2-history-kernel` | SEPARATE_AT_RECORDED_VIEW_LEVEL |
| REL022 | `c2-axis-central` | `c2-analyzer-sector` | SEPARATE_AT_RECORDED_VIEW_LEVEL |
| REL023 | `c2-threefold-deck` | `d8-native-root` | SEPARATE_AT_RECORDED_VIEW_LEVEL |
| REL024 | `s3-abstract-klein` | `c2-register-parity` | SEPARATE_AT_RECORDED_VIEW_LEVEL |
| REL025 | `s3-mode` | `c3-mode` | SEPARATE_AT_RECORDED_VIEW_LEVEL |
| REL026 | `s5-native-quotient` | `s5-six-axes` | SEPARATE_AT_RECORDED_VIEW_LEVEL |
| REL027 | `signed-axis-extension` | `s5-analyzer-sectors` | SEPARATE_AT_RECORDED_VIEW_LEVEL |
| REL028 | `x12-sections` | `x12-kernel` | OPEN_UNDER_ENCODED_CONSTRAINTS |
| REL029 | `x12-kernel` | `twelve-pair-descriptors` | SEPARATE_AT_RECORDED_VIEW_LEVEL |
| REL030 | `twelve-face-phases` | `history-pentagon-space` | SEPARATE_AT_RECORDED_VIEW_LEVEL |
| REL031 | `face-crown` | `history-crown` | OPEN_UNDER_ENCODED_CONSTRAINTS |
| REL032 | `frame-contrast` | `history-fivefold-contrast` | OPEN_UNDER_ENCODED_CONSTRAINTS |
| REL033 | `frame-difference` | `frame-hermitian-current` | SEPARATE_AT_RECORDED_VIEW_LEVEL |
| REL034 | `frame-multiplier` | `frame-sector-exchange` | SEPARATE_AT_RECORDED_VIEW_LEVEL |
| REL035 | `frame-multiplier` | `u2-face-envelope` | SEPARATE_AT_RECORDED_VIEW_LEVEL |
| REL036 | `s1-residual-reflection` | `circle-space` | SEPARATE_AT_RECORDED_VIEW_LEVEL |
| REL037 | `s1-residual-reflection` | `r1-native-residual` | SEPARATE_AT_RECORDED_VIEW_LEVEL |
| REL038 | `r1-native-residual` | `r1-history-class` | SEPARATE_AT_RECORDED_VIEW_LEVEL |
| REL039 | `frame-sector-exchange` | `residue-spaces` | SEPARATE_AT_RECORDED_VIEW_LEVEL |
| REL040 | `cochain-coboundaries` | `face-disagreement` | SEPARATE_AT_RECORDED_VIEW_LEVEL |
| REL041 | `history-incidence` | `history-gram` | SEPARATE_AT_RECORDED_VIEW_LEVEL |
| REL042 | `history-gram` | `history-contrast` | SEPARATE_AT_RECORDED_VIEW_LEVEL |
| REL043 | `history-sheet-grading` | `history-sheet-exchange` | SEPARATE_AT_RECORDED_VIEW_LEVEL |
| REL044 | `u1-anchor-first` | `u1-anchor-second` | SEPARATE_AT_RECORDED_VIEW_LEVEL |
| REL045 | `u1-anchor-first` | `u1-face-center` | SEPARATE_AT_RECORDED_VIEW_LEVEL |
| REL046 | `w4-winding` | `r1-history-class` | OPEN_UNDER_ENCODED_CONSTRAINTS |
| REL047 | `h12-history-candidate` | `history-pentagon-space` | OPEN_UNDER_ENCODED_CONSTRAINTS |
| REL048 | `k120-group-locator` | `k120-common-cover` | OPEN_UNDER_ENCODED_CONSTRAINTS |
| REL049 | `s12-phase-set` | `twelve-face-phases` | FORCED_ALIAS_BY_FROZEN_INPUT |
| REL050 | `t01-edge-connection` | `c10-native` | SEPARATE_AT_RECORDED_VIEW_LEVEL |
| REL051 | `p01-line-partitions` | `frame-common-projector` | SEPARATE_AT_RECORDED_VIEW_LEVEL |
| REL052 | `m4-mode-set` | `matrix-algebras` | SEPARATE_AT_RECORDED_VIEW_LEVEL |
| REL053 | `cochain-spaces` | `complex-spaces` | SEPARATE_AT_RECORDED_VIEW_LEVEL |
| REL054 | `inertia-moments` | `identity-matrices` | SEPARATE_AT_RECORDED_VIEW_LEVEL |
| REL055 | `rotor-o2` | `o2-surface-envelope` | OPEN_UNDER_ENCODED_CONSTRAINTS |
| REL056 | `history-primitive-family` | `r1-history-class` | SEPARATE_AT_RECORDED_VIEW_LEVEL |
| REL057 | `frame-sign-values` | `frame-current-sign` | SEPARATE_AT_RECORDED_VIEW_LEVEL |
| REL058 | `connection-doublet` | `c2-phase-residual` | SEPARATE_AT_RECORDED_VIEW_LEVEL |
| REL059 | `three-section-coordinate` | `x12-sections` | SEPARATE_AT_RECORDED_VIEW_LEVEL |
| REL060 | `t10-native-macro` | `c10-native` | SEPARATE_AT_RECORDED_VIEW_LEVEL |
| REL061 | `t10-native-macro` | `t01-edge-connection` | SEPARATE_AT_RECORDED_VIEW_LEVEL |
| TYPE001 | `d5-history` | `frame-difference` | SEPARATE_AT_RECORDED_VIEW_LEVEL |
| TYPE002 | `d5-face-kernel` | `frame-difference` | SEPARATE_AT_RECORDED_VIEW_LEVEL |
| TYPE003 | `d5-face-kernel` | `d8-face-blocks` | SEPARATE_AT_RECORDED_VIEW_LEVEL |
