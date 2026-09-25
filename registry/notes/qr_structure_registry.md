# Thalean Structure and Label Registry

Date: 2026-09-24  
Edition: archival view inventory v1  
Purpose: separate the actual source-defined structures before consolidating their names.

**225 named structure/view records; 61 typed relationship decisions.** The lexical scan found **354 lookup keys in 225 byte-distinct text payloads**. Those are not 354 mathematical objects. Counts include metadata, indexed variables, ordinary exponents and secondary glossary repetitions.

## Governing rule

A label is a lookup key. An object is identified by its domain, construction, action and evidence. An abstract group type is only one part of that identity.

For example, `D8` can label a root stabilizer, a presentation factor, a block permutation image, a selected operator group, an edge-transport group or a lifted loop group. Sharing an order-eight dihedral presentation does not erase those roles. Conversely, a source-derived descent may identify two views of the same rooted structure, and that relationship should be recorded rather than forbidden by blanket warnings.

The qualified names and semantic IDs in this edition are **editorial proposals**. Existing equations, source files, native generator labels, repository audits and `qr_core_terms.md` are not rewritten. A family record covers parameterized instances such as six faces or sixty roots; it does not assert that all embedded subgroup members are one literal subgroup.

## How the bins work

Every named record distinguishes the object type, carrier/domain, historical spellings, action or construction, numerical size with its meaning, source basis, and boundary. The relationship ledger then records one of: source-identified entity; faithful descent; quotient; subgroup/image; operator construction; abstract-type match only; incompatible structure; or unresolved comparison. No automatic identity closure is taken through quotient or same-type edges.

A `candidate_structure_ids` field in the occurrence index is a navigation aid, **not a completed semantic annotation**. Ambiguous and unmapped occurrences stay in the review queue. Superscripts are retained separately, so `C^2`, `C_2`, `C_2^3`, `U_2`, `U(2)`, `S_1`, and `S^1` are not normalized into one object.

## Evidence and coverage

The scan covers the four archived glossary/baseline texts, current Draft 6 TEX plus retained text/JSON sources, the recovered native analyzer/EPR/G9000 notes, selected source artifacts, and explicitly identified passage digests from earlier papers. It is not a complete export of the user's chat account or research repositories. The current conversation is represented by a clearly marked digest, not a claimed transcript dump.

No historical mathematical producer was executed for this inventory. A stored `audit_pass` flag is evidence about what its source reports, not a new verification performed here. In particular, the newest claimed full twelve-pentagon/action cocycle cancellation remains **conversation-reported pending its original action tables**. The previously recovered Gram and Clifford artifacts do not by themselves supply that later full-action verification.

Full lexical inventory: [label collision index](label_collision_index.md).  
Relations and consolidation decisions: [relationship ledger](consolidation_ledger.md).  
Cases requiring more evidence: [review queue](unresolved_label_queue.md).  
Source coverage and checksums: [coverage ledger](../provenance/coverage.md).

## Dihedral naming convention

The sources mix conventions. Their `D8` is the square dihedral group of total order eight; historical `D5` is the pentagonal dihedral group of total order ten; registered-decagon `D10` has total order twenty. This edition retains the original label and writes the order explicitly. Use the qualified view name first. If a compact neutral type is needed, write `Dih(rotation_order=4, total_order=8)` rather than changing a source subscript silently.

**A matched group order is not a domain map. A group, its matrix representation, the orbit it acts on, the stabilizer of a point, and a quotient image are separate records.**

## Section index

- [Dihedral and quaternionic views](#section-d8-native-root)
- [Klein and binary-register views](#section-v4-native)
- [Cyclic, alternating and symmetric actions](#section-c3-mode)
- [Graphs, finite state sets, and counting conventions](#section-g60-native)
- [Operators, indexed variables, and readouts](#section-frame-contrast)
- [Continuous envelopes, scalar spaces, and homology](#section-u2-face-envelope)
- [Source-code and metadata bins](#section-source-h-locators)
- [Companion objects needed for typed relationships](#section-face-stabilizer)
- [Additional collisions from the exact occurrence sweep](#section-adjacency-g15)

<a id="section-d8-native-root"></a>

# Dihedral and quaternionic views

<a id="d8-native-root"></a>

## Native G60 rooted-neighborhood stabilizer

**Stable ID:** `d8-native-root`  
**Historical labels / lookup forms:** `D8`, `D_8`, `D8_frame`  
**Kind:** finite subgroup family  
**Domain:** Aut(G60), with a selected vertex x and its neighbor set  
**Typed size:** Group order: 8  
**Family parameters:** x in V(G60); retain x and the actual embedding  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The automorphisms fixing the selected native vertex, with the faithful action on its four neighbors. The comparator audit places the odd-comparator square in the center of this rooted group. A root is part of the object.

```text
Stab_Aut(G60)(x); |Stab|=8; r^4=s^2=1, srs=r^-1
```

**Keep distinct:** Not the global fiber-product D8 factor, the free eight-point deck group, or the face-operator D8.

**Recorded relationships:** [d8-position](#d8-position) (faithful descent); [d8-lifted-holonomy](#d8-lifted-holonomy) (extension type compatibility); [c2-threefold-deck](#c2-threefold-deck) (nonisomorphic group types).

**Sources:** [MM](../provenance/inputs/C107.json#L1-L44), [COVER](../provenance/inputs/draft6/sections/01B_common_cover.tex#L1-L101).

---

<a id="d8-position"></a>

## Petersen-edge positional stabilizer

**Stable ID:** `d8-position`  
**Historical labels / lookup forms:** `D8`, `D_8`, `D8_pos`  
**Kind:** finite subgroup family  
**Domain:** S5 acting on the fifteen unordered Petersen edges / G15 vertices  
**Typed size:** Group order: 8  
**Family parameters:** one G15 vertex / one unordered Petersen edge  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The subgroup preserving one unordered pair of disjoint two-subsets. It permits the two internal swaps and interchange of the pair. The quotient notation here is a coset space, not a quotient group.

```text
V(G15) ~= S5 / D8_pos
```

**Keep distinct:** Keep the positional action distinct from the upstairs native action even though the specified descent identifies rooted stabilizers.

**Recorded relationships:** [d8-native-root](#d8-native-root) (faithful descent); [d8-cover-root](#d8-cover-root) (faithful descent).

**Sources:** [COVER](../provenance/inputs/draft6/sections/01B_common_cover.tex#L1-L101).

---

<a id="d8-cover-root"></a>

## Common-cover rooted stabilizer

**Stable ID:** `d8-cover-root`  
**Historical labels / lookup forms:** `D8`, `D_8`, `D8_frame`  
**Kind:** finite subgroup family  
**Domain:** Aut(K120), at one selected cover vertex  
**Typed size:** Group order: 8  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The order-eight stabilizer upstairs in the common census cover. The manuscript reports faithful descent to the corresponding G15 rooted stabilizer, and treats the associated rooted cover/G60/G15 actions together.

```text
Stab_Aut(K120)(x_tilde) -> Stab_Aut(G15)(q(x_tilde))
```

**Keep distinct:** This is an action-linked view of the rooted family, not the composite C2^3 deck action.

**Recorded relationships:** [d8-position](#d8-position) (faithful descent).

**Sources:** [COVER](../provenance/inputs/draft6/sections/01B_common_cover.tex#L1-L101), [CENSUS_REPORT](../provenance/inputs/draft6/data/generated/census_family_report.json#L1-L5852).

---

<a id="d8-fiber-product"></a>

## Global fiber-product dihedral coordinate factor

**Stable ID:** `d8-fiber-product`  
**Historical labels / lookup forms:** `D8`, `D_8`, `d8`  
**Kind:** abstract presentation factor  
**Domain:** S5 x D8 subject to parity compatibility  
**Typed size:** Group order: 8  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The dihedral factor used to present all 480 native automorphisms. Its coordinates are a rotation r mod 4 and a flip f mod 2; its character r mod 2 is matched with the S5 sign. This is a factor in a model, not by itself a chosen subgroup of native permutations.

```text
(r,f)(u,g)=(r+(-1)^f u mod4,f+g mod2); parity(sigma)=r mod2
```

**Keep distinct:** Do not identify the D8 projection of the full group with a root stabilizer or its specific center without an explicit map.

**Sources:** [FP](../provenance/inputs/native_g60_fiber_product_isomorphism_044.json#L37805-L37814).

---

<a id="d8-history-factor"></a>

## Registered phase-group dihedral factor

**Stable ID:** `d8-history-factor`  
**Historical labels / lookup forms:** `D8`, `D_8`, `D8_hist`  
**Kind:** embedded subgroup / direct factor  
**Domain:** Gamma_hist=<r,s,z> inside the supplied Aut(G60) cache  
**Typed size:** Group order: 8  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The factor generated by the declared r and s in the sixteen-element history-phase group. A central extra z supplies the additional C2. The source gives actual cache indices, but those numbers are not universal names.

```text
<r,s>; r=cache[3], s=cache[325], z=cache[324]; Gamma_hist ~= D8 x C2
```

**Keep distinct:** This is not the twelve-pentagon coefficient representation or the original history alphabet {2,3}. The exact chosen generators, not just the abstract D8 label, identify the factor.

**Recorded relationships:** [history-coset-image](#history-coset-image) (factor vs action image).

**Sources:** [HISTORY_PHASE](../provenance/inputs/draft6/sections/03F_history_phase_groupoid.tex#L1-L66).

---

<a id="history-coset-image"></a>

## Four-phase coset permutation image

**Stable ID:** `history-coset-image`  
**Historical labels / lookup forms:** `D8`, `D8_hist_image`  
**Kind:** finite permutation image  
**Domain:** Gamma_hist acting on X=Gamma_hist/H0  
**Typed size:** Group order: 8; Point/object count: 4  
**Standing:** Source-recorded four-coset action; the D8 type follows from its displayed presentation and kernel, not a newly run native census.

The faithful image of the history-phase action after its constant kernel is removed. Keep this image separate from the embedded <r,s> factor even where an isomorphism is available. The source explicitly records its four cosets and kernel.

```text
Gamma_hist -> Perm(X); kernel K=<a>; |Gamma_hist/K|=8
```

**Keep distinct:** The order-eight image and the full sixteen-element actor group are not interchangeable. The D8 classification is read in the supplied four-phase action, not a new independent audit.

**Recorded relationships:** [d8-history-factor](#d8-history-factor) (factor vs action image).

**Sources:** [HISTORY_PHASE](../provenance/inputs/draft6/sections/03F_history_phase_groupoid.tex#L1-L66), [NATIVE_REPORT](../provenance/inputs/draft6/data/generated/draft6_native_incidence_groupoid_report.json#L1-L16892).

---

<a id="d8-face-blocks"></a>

## Four-signed-block face permutation group

**Stable ID:** `d8-face-blocks`  
**Historical labels / lookup forms:** `D8`, `D_8`, `local_D8`  
**Kind:** finite permutation image family  
**Domain:** Four signed blocks in a selected native face family  
**Typed size:** Group order: 8; Point/object count: 4  
**Family parameters:** six native face families f  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The image of the order-eighty face stabilizer on its four signed blocks. Its order is eight, while the action kernel has order ten. This is the local block permutation group, not the entire face stabilizer.

```text
Stab(f) -> Perm(B_f); image ~= D8; kernel=D5_f
```

**Keep distinct:** Do not substitute the order-eight image for the order-ten kernel or the order-eighty ambient stabilizer.

**Recorded relationships:** [face-stabilizer](#face-stabilizer) (permutation image); [d8-selected-face-operators](#d8-selected-face-operators) (shared group type distinct action).

**Sources:** [FACE](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_face_field_higgs_bridge_checkpoint_receipt_201fk.v1.json#L1-L144), [D5_KERNEL](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_d5_kernel_naturality_201fqb.v1.json#L1-L70), [FACE_SCOPE](../provenance/inputs/draft6/appendices/O_reference_audit.tex#L1-L82).

---

<a id="d8-selected-face-operators"></a>

## Selected face complex/reflection operator group

**Stable ID:** `d8-selected-face-operators`  
**Historical labels / lookup forms:** `D8`, `D_8`  
**Kind:** finite operator group  
**Domain:** Native complex face fiber with J_F and the connection residual S1  
**Typed size:** Group order: 8; Real dimension: 4; Complex dimension: 2  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The source explicitly calls <J_F,S1> the selected face operator D8. J_F supplies the complex quarter-turn and S1 is the residual anti-complex involution. The selected transport itself is not S1.

```text
<J_F,S1>; J_F^2=-I, S1^2=I, S1 J_F S1=-J_F
```

**Keep distinct:** No Aut(G60)-to-Pin, charge-center identity, physical gauge identification, or equivalence to the block-permutation action is supplied.

**Recorded relationships:** [d8-charge-center-locator](#d8-charge-center-locator) (named comparison target); [d8-face-blocks](#d8-face-blocks) (shared group type distinct action).

**Sources:** [RESIDUAL](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_signed_event_s1_torsor_selector_201h65b.v1.json#L1-L42), [REFLECTION](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_selected_reflection_event_pauli_anatomy_201h67b.v1.json#L1-L41).

---

<a id="d8-charge-center-locator"></a>

## Charge-center dihedral comparison target

**Stable ID:** `d8-charge-center-locator`  
**Historical labels / lookup forms:** `D8`, `D8_charge_center`  
**Kind:** source-locator-only group view  
**Domain:** Charge-center construction referenced by the selected-face audit  
**Standing:** Referenced comparison target only; insufficient data for an action identification.

The source names a charge-center D8=<r,s> as the next comparison target. The defining charge-center action is not supplied by the retrieved packet. This entry prevents that target from being silently merged with the selected face group.

```text
Named target: charge-center D8=<r,s>
```

**Keep distinct:** Full domain, generator realization, kernel and comparison remain unresolved in this corpus.

**Recorded relationships:** [d8-selected-face-operators](#d8-selected-face-operators) (named comparison target).

**Sources:** [RESIDUAL](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_signed_event_s1_torsor_selector_201h65b.v1.json#L1-L42).

---

<a id="d8-section-square"></a>

## Closure-section square-factor symmetry

**Stable ID:** `d8-section-square`  
**Historical labels / lookup forms:** `D8`, `D_8`  
**Kind:** finite action factor  
**Domain:** Four-state coordinate X4 in X12_sections ~= X3 x X4  
**Typed size:** Group order: 8; Point/object count: 4  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The specified square symmetry acting on the four-state section coordinate. It is one factor of the source-given H ~= S3 x D8 action on twelve sections, not automatically the full symmetry of a graph on twelve vertices.

```text
(sigma,d)(s,q)=(sigma s,dq)
```

**Keep distinct:** No equality with a rooted stabilizer, selected face-operator group, or phase-history factor is established by the 3 x 4 count.

**Sources:** [OLDER_SECTION_SURFACE](../provenance/excerpts/older_section_surface.md#L1-L9).

---

<a id="d8-surface-edges"></a>

## Surface reference edge-transport group

**Stable ID:** `d8-surface-edges`  
**Historical labels / lookup forms:** `D8`, `D_8`  
**Kind:** finite matrix transport group  
**Domain:** Local primitive winding reference planes on the genus-21 surface  
**Typed size:** Group order: 8; Real dimension: 2  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The square rotation/reflection group containing the edge transports of the surface reference connection. Its loop holonomy is only a V4 subgroup before lifting. Edge-value group and loop group are different views.

```text
D8=<J,S | J^4=S^2=1, SJS=J^-1>
```

**Keep distinct:** Do not call every transport value an attained loop holonomy; unlifted loops do not supply an order-four return.

**Recorded relationships:** [d8-lifted-holonomy](#d8-lifted-holonomy) (distinct extension levels).

**Sources:** [SURFACE](../provenance/inputs/README(20260920-001150).md#L1-L300).

---

<a id="d8-lifted-holonomy"></a>

## Dihedral lifted surface loop holonomy

**Stable ID:** `d8-lifted-holonomy`  
**Historical labels / lookup forms:** `D8`, `D_8`, `Hol_plus`  
**Kind:** finite holonomy group  
**Domain:** Reflection-square +1 central lift of the surface connection  
**Typed size:** Group order: 8  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The attained loop group in the plus lift, of order eight with profile 1:1,2:5,4:2. It is a lift of the unlifted V4 loop group, not the unlifted D8 edge-value group under another name.

```text
q_tilde^2=z; Hol_plus ~= D8
```

**Keep distinct:** The comparator selects the extension type, not a particular one of the 2^42 gauge-inequivalent lifts or an elementwise native identification.

**Recorded relationships:** [d8-surface-edges](#d8-surface-edges) (distinct extension levels); [d8-native-root](#d8-native-root) (extension type compatibility); [q8-lifted-holonomy](#q8-lifted-holonomy) (nonisomorphic alternatives).

**Sources:** [SURFACE](../provenance/inputs/README(20260920-001150).md#L1-L300).

---

<a id="q8-lifted-holonomy"></a>

## Quaternionic alternative surface loop holonomy

**Stable ID:** `q8-lifted-holonomy`  
**Historical labels / lookup forms:** `Q8`, `Q_8`, `Hol_minus`  
**Kind:** finite holonomy group  
**Domain:** Reflection-square-central alternative lift  
**Typed size:** Group order: 8  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The other tested lift has loop group Q8, with profile 1:1,2:1,4:6. This is not another spelling of the dihedral branch and cannot represent its multiple reflection involutions.

```text
Hol_minus ~= Q8
```

**Keep distinct:** Retain as an alternative construction excluded from a direct comparator-type match, not as a failed existence construction.

**Recorded relationships:** [d8-lifted-holonomy](#d8-lifted-holonomy) (nonisomorphic alternatives).

**Sources:** [SURFACE](../provenance/inputs/README(20260920-001150).md#L1-L300).

---

<a id="surface-extension-plus"></a>

## Reflection-involutory ambient double-cover extension

**Stable ID:** `surface-extension-plus`  
**Historical labels / lookup forms:** `D16_candidate`, `central_cover_plus`  
**Kind:** group presentation  
**Domain:** Ambient cover of the surface D8 edge-transport group  
**Standing:** Source-given presentation; D16 is not asserted as the source label.

The source specifies this group by generators and relations. Its attained loop subgroup is separately D8. The proposed name describes the presentation; a D16 spelling is only a search aid, not imported source terminology.

```text
R^8=1, S^2=1, SRS=R^-1; projection kernel={1,R^4}
```

**Keep distinct:** Do not confuse the ambient extension with its order-eight attained holonomy. No source-selected lift is unique.

**Sources:** [SURFACE](../provenance/inputs/README(20260920-001150).md#L1-L300).

---

<a id="surface-extension-minus"></a>

## Reflection-square-central ambient double-cover extension

**Stable ID:** `surface-extension-minus`  
**Historical labels / lookup forms:** `Q16_candidate`, `central_cover_minus`  
**Kind:** group presentation  
**Domain:** Alternative ambient cover of surface edge transports  
**Standing:** Source-given presentation; Q16 is not asserted as the source label.

The reflection squares to the central kernel element. The source tests this presentation separately; its attained holonomy is Q8. A Q16 lookup is editorial only.

```text
R^8=1, S^2=R^4, SRS=R^-1; kernel={1,R^4}
```

**Keep distinct:** Do not collapse it with the involutory-reflection extension or either loop subgroup.

**Sources:** [SURFACE](../provenance/inputs/README(20260920-001150).md#L1-L300).

---

<a id="d5-history"></a>

## Historical fivefold rotation-reflection register

**Stable ID:** `d5-history`  
**Historical labels / lookup forms:** `D5`, `D_5`  
**Kind:** finite group presentation on a historical register  
**Domain:** The historical fivefold object described in the integrated draft  
**Typed size:** Group order: 10  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

Two involutions generate a rotation of order five. Its role is fivefold history and harmonic structure. Here a and b are noncommuting reflection generators and must not be read as the commuting native deck involutions.

```text
a^2=b^2=1; s=ab; s^5=1; ba=s^-1
```

**Keep distinct:** Order-ten historical D5 is not rooted order-eight D8, nor automatically the face realization kernel.

**Recorded relationships:** [d5-face-kernel](#d5-face-kernel) (same abstract type only).

**Sources:** [HISTORICAL_FIVEFOLD](../provenance/excerpts/historical_fivefold.md#L1-L9).

---

<a id="d5-face-kernel"></a>

## Native face realization kernel

**Stable ID:** `d5-face-kernel`  
**Historical labels / lookup forms:** `D5`, `D_5`, `D5_f`  
**Kind:** kernel subgroup family  
**Domain:** Order-eighty stabilizer of a selected four-block native face  
**Typed size:** Group order: 10  
**Family parameters:** f ranges over six faces  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The automorphisms fixing every signed block of that face. Its order is ten and it is generated by a fivefold rotation and an inverting involution. The source makes this kernel family natural under face transport.

```text
D5_f=ker(Stab(f)->Perm(B_f)); g D5_f g^-1=D5_(gf)
```

**Keep distinct:** Not the four-block D8 image. The order-four kernel tested in failed Audit018C is a different layer, not this kernel.

**Recorded relationships:** [face-stabilizer](#face-stabilizer) (kernel embedding); [d5-history](#d5-history) (same abstract type only).

**Sources:** [D5_KERNEL](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_d5_kernel_naturality_201fqb.v1.json#L1-L70), [FACE_SCOPE](../provenance/inputs/draft6/appendices/O_reference_audit.tex#L1-L82).

---

<a id="face-kernel-wrong-layer"></a>

## Earlier order-four face action-kernel candidate

**Stable ID:** `face-kernel-wrong-layer`  
**Historical labels / lookup forms:** `D5_candidate`, `Audit018C_kernel`  
**Kind:** rejected-identification view  
**Domain:** The distinct action layer tested in Audit018C  
**Typed size:** Group order: 4  
**Standing:** Source-recorded rejected identification; exact earlier action not fully recovered.

The archive says an order-four kernel was tested against the intended order-ten realization gauge and failed. Preserve the actual layer as an unresolved source-specific kernel rather than changing its label to D5.

```text
Order reported: 4; intended D5 target order:10
```

**Keep distinct:** Original failed test remains failed; do not infer a V4 or C4 group law merely from order four.

**Sources:** [FACE_SCOPE](../provenance/inputs/draft6/appendices/O_reference_audit.tex#L1-L82).

---

<a id="d10-decagon"></a>

## Registered decagon setwise stabilizer

**Stable ID:** `d10-decagon`  
**Historical labels / lookup forms:** `D10`, `D_10`  
**Kind:** finite subgroup family  
**Domain:** Aut(G60) acting on one of the 24 registered ten-cycles  
**Typed size:** Group order: 20  
**Family parameters:** one registered ten-cycle C  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The source uses D10 for the full dihedral symmetry of a ten-cycle, explicitly order twenty. It acts faithfully on the ten cycle vertices and has trivial pointwise stabilizer.

```text
Stab(C) ~= D10; ten rotations plus ten reflections
```

**Keep distinct:** D10 uses rotation-count notation here, while D8 elsewhere uses total-order notation. Always state order twenty.

**Sources:** [DECAGON_STABILIZERS](../provenance/excerpts/decagon_stabilizers.md#L1-L9).

---

<a id="answering-pair-stabilizer"></a>

## Lifted-decagon answering-pair stabilizer

**Stable ID:** `answering-pair-stabilizer`  
**Historical labels / lookup forms:** `D10 x C2`, `D_10 x C_2`  
**Kind:** finite subgroup family  
**Domain:** Two lifted registered decagons above one quotient pentagon  
**Typed size:** Group order: 40  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The order-forty setwise stabilizer includes the decagon symmetry and a commuting involution exchanging the two cycles. This C2 has an actual pair-exchange domain.

```text
Stab(P_C) ~= D10 x C2
```

**Keep distinct:** Not Gamma_hist ~= D8 x C2; their orders, domains and generators differ.

**Sources:** [DECAGON_STABILIZERS](../provenance/excerpts/decagon_stabilizers.md#L1-L9).

---

<a id="section-v4-native"></a>

# Klein and binary-register views

<a id="v4-native"></a>

## Native free normal Klein deck register

**Stable ID:** `v4-native`  
**Historical labels / lookup forms:** `V4`, `V_4`, `V4_nat`  
**Kind:** embedded finite group  
**Domain:** The 60-vertex native carrier  
**Typed size:** Group order: 4  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The native free normal action {1,a,b,ab} whose orbits are fifteen four-state chambers. Its three nonidentity elements are involutions. Native conjugation fixes a and exchanges b with ab through an index-two character.

```text
a^2=b^2=1; ab=ba; V4={1,a,b,ab}
```

**Keep distinct:** Not every group of four, not the noncommuting D5 reflections, and not a cyclic quarter-turn group.

**Recorded relationships:** [v4-fp-kernel](#v4-fp-kernel) (explicit model isomorphism); [v4-voltage](#v4-voltage) (coefficient to deck identification); [v4-root-projective](#v4-root-projective) (same abstract type only).

**Sources:** [ANALYZER](../provenance/inputs/native_analyzer_constraints.md#L1-L450), [CORE](../provenance/inputs/qr_core_terms_consolidated.md#L1-L3141), [FP](../provenance/inputs/native_g60_fiber_product_isomorphism_044.json#L37805-L37814).

---

<a id="v4-voltage"></a>

## Klein-valued quotient voltage label group

**Stable ID:** `v4-voltage`  
**Historical labels / lookup forms:** `V4`, `V_4`  
**Kind:** coefficient group with voltage assignment  
**Domain:** Oriented edges of the G15 quotient and their G60 lift  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The four-element group used to label quotient edges and accumulate deck holonomy. It can be explicitly identified with native deck elements in a supplied voltage chart, but the edge labeling is gauge dependent.

```text
hol(gamma)=product of native V4 edge voltages
```

**Keep distinct:** Keep coefficient group, gauge-chosen voltage cochain, and actual deck permutation action as separate objects.

**Recorded relationships:** [v4-native](#v4-native) (coefficient to deck identification).

**Sources:** [CORE](../provenance/inputs/qr_core_terms_consolidated.md#L1-L3141), [BASE](../provenance/inputs/qr_core_terms_original.md#L1-L1982).

---

<a id="v4-root-projective"></a>

## Rooted dihedral central quotient plane

**Stable ID:** `v4-root-projective`  
**Historical labels / lookup forms:** `V4`, `V_4`  
**Kind:** quotient group / projective comparison plane  
**Domain:** D8_root/Z(D8_root)  
**Typed size:** Group order: 4  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The commuting four-element quotient of a specified dihedral central extension. Its lifts retain nontrivial central commutators and square refinements, so the projective data are not encoded by the abstract V4 alone.

```text
[U,V]=z^beta(u,v); U^2=z^q(u)
```

**Keep distinct:** An abstract V4 isomorphism does not identify this quotient with native deck V4.

**Recorded relationships:** [v4-native](#v4-native) (same abstract type only).

**Sources:** [HISTORICAL_FIVEFOLD](../provenance/excerpts/historical_fivefold.md#L1-L9).

---

<a id="v4-fp-kernel"></a>

## Fiber-product parity-character Klein kernel

**Stable ID:** `v4-fp-kernel`  
**Historical labels / lookup forms:** `V4`, `V_4`  
**Kind:** kernel of a presentation character  
**Domain:** D8 coordinate factor of the global fiber product  
**Typed size:** Group order: 4  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The kernel of chi(r,f)=r mod2 in the D8 model. Via the full explicit group isomorphism, this participates in the native kernel over S5; that map, not the number four, licenses comparison.

```text
ker(chi)={(r,f): r is even}
```

**Keep distinct:** Preserve the model-to-native isomorphism rather than treating literal r,f coordinates as native vertex labels.

**Recorded relationships:** [v4-native](#v4-native) (explicit model isomorphism).

**Sources:** [FP](../provenance/inputs/native_g60_fiber_product_isomorphism_044.json#L37805-L37814).

---

<a id="v4-cover-center"></a>

## Central Klein group of the common 120-cover

**Stable ID:** `v4-cover-center`  
**Historical labels / lookup forms:** `V4`, `V_4`  
**Kind:** center of graph automorphism group  
**Domain:** Aut(K120) for the census common cover  
**Typed size:** Group order: 4  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The center {1,tau4,tau5,tau6} controls three central two-fold quotients. It is a different embedded Klein group from the named deck register downstairs.

```text
Z(Aut(K120))={1,tau4,tau5,tau6}
```

**Keep distinct:** All central elements remain fixed under conjugation in this ambient group; equal child size does not merge the quotient involutions.

**Sources:** [COVER](../provenance/inputs/draft6/sections/01B_common_cover.tex#L1-L101).

---

<a id="v4-section-coordinate"></a>

## Four-point square section coordinate

**Stable ID:** `v4-section-coordinate`  
**Historical labels / lookup forms:** `V4`, `V_4`, `X4`  
**Kind:** structured finite set  
**Domain:** The X4 factor in an explicitly chosen 3 x 4 closure-section presentation  
**Typed size:** Point/object count: 4  
**Standing:** Source-recorded four-point factor; particular Klein identification unresolved.

The retrieved section source specifies a four-point square coordinate X4 and a D8 action. It does not, in that passage, select a particular regular Klein translation subgroup on the four points. Preserve the coordinate as a set with square structure until the original coordinate registry supplies more.

```text
Four-point factor X4; retain its section-coordinate bijection
```

**Keep distinct:** The identification of this coordinate with the native Klein deck labels, or with a particular V4 subgroup of the square symmetry, is not recovered here.

**Sources:** [OLDER_SECTION_SURFACE](../provenance/excerpts/older_section_surface.md#L1-L9), [BASE](../provenance/inputs/qr_core_terms_original.md#L1-L1982).

---

<a id="v4-kernel-coordinate"></a>

## Binary translation coordinate of the rank-eight relational kernel

**Stable ID:** `v4-kernel-coordinate`  
**Historical labels / lookup forms:** `V4`, `V_4`  
**Kind:** finite additive coordinate group  
**Domain:** X12_kernel=Z3 x F2^2  
**Typed size:** Group order: 4  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The normalized two-bit coordinate with named directions u=(1,0),v=(0,1). The source expressly says these are not new names for historical native deck permutations.

```text
x -> x+t; t in F2^2
```

**Keep distinct:** Do not relabel u,v as a,b without a source-derived correspondence.

**Sources:** [KERNEL](../provenance/inputs/draft6/sections/01C_relational_kernel.tex#L1-L68).

---

<a id="v4-surface-holonomy"></a>

## Unlifted surface winding-plane loop group

**Stable ID:** `v4-surface-holonomy`  
**Historical labels / lookup forms:** `V4`, `V_4`  
**Kind:** finite matrix holonomy subgroup  
**Domain:** The surface reference O(2) connection  
**Typed size:** Group order: 4  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The loop group {I,-I,Sprime,-Sprime} inside the edge-transport D8. It has no order-four element and must be distinguished from the lifted dihedral holonomy.

```text
Hol={I,-I,Sprime,-Sprime}
```

**Keep distinct:** Not the entire edge transport group or a chosen central lift.

**Sources:** [SURFACE](../provenance/inputs/README(20260920-001150).md#L1-L300).

---

<a id="v4-face-compatibility"></a>

## Face semilinearity compatibility subgroup

**Stable ID:** `v4-face-compatibility`  
**Historical labels / lookup forms:** `V4`, `V_4`  
**Kind:** index-two operator subgroup  
**Domain:** Local D8 face block representation 1+chi_face+E2  
**Typed size:** Group order: 4  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The kernel of the mismatch character delta=chi_face*det_E2. Restricting to it reconciles scalar-plane and E2 conjugation behavior and supports the selected complex doublet structure.

```text
ker(delta) <= D8; order4; preimage in Stab(face) has order40
```

**Keep distinct:** Not the full face D8 image; the reduction and its preimage have different orders and roles.

**Sources:** [FACE](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_face_field_higgs_bridge_checkpoint_receipt_201fk.v1.json#L1-L144).

---

<a id="v4-connection-gauge"></a>

## Connection local gauge/transport ambiguity group

**Stable ID:** `v4-connection-gauge`  
**Historical labels / lookup forms:** `V4`, `V_4`  
**Kind:** local gauge action family  
**Domain:** Four-state transports between declared face-phase objects  
**Typed size:** Group order: 4  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The connection checkpoint reports four local transports per edge forming a source/target V4 torsor. Pair and signed-event data reduce this ambiguity. The gauge group acts on transport choices, not as a new four-point history set.

```text
Four transports -> pair-level residual C2 -> one selected local transport
```

**Keep distinct:** Equal group type to the compatibility subgroup alone is not enough; use the source connection action to relate them.

**Sources:** [CONNECTION](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_u2_gauge_bridge_connection_frontier_checkpoint_201fp7.v1.json#L1-L190), [RESIDUAL](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_signed_event_s1_torsor_selector_201h65b.v1.json#L1-L42).

---

<a id="v4-history-isotropy"></a>

## Four-element registered-phase isotropy

**Stable ID:** `v4-history-isotropy`  
**Historical labels / lookup forms:** `V4`, `H0`, `H1`, `H2`, `H3`, `H_0`, `H_1`, `H_2`, `H_3`  
**Kind:** isotropy subgroup family  
**Domain:** Gamma_hist acting on its four cosets  
**Typed size:** Group order: 4  
**Family parameters:** k mod4; embedded isotropy repeats at k+2  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

H_k=<a,w_k> is the stabilizer of S_k. The family has period two despite the four-state phase period. Keep each embedded H_k and its quotient by K typed.

```text
H_k=r^k H0 r^-k; w_k=r^(2(k mod2)) s z
```

**Keep distinct:** Not homology H1; not the ordinary twelve-pentagon history space. The source identifies H_k/K as a group of order two.

**Sources:** [HISTORY_PHASE](../provenance/inputs/draft6/sections/03F_history_phase_groupoid.tex#L1-L66).

---

<a id="v4-relational-subgroup"></a>

## Five-address relational Klein subgroup

**Stable ID:** `v4-relational-subgroup`  
**Historical labels / lookup forms:** `V4`, `Vrel`  
**Kind:** finite subgroup reference  
**Domain:** Double transpositions on four selected five-address points  
**Standing:** Retained source-context distinction; full original subgroup specification outside this scan.

The wider source notation distinguishes a five-address relational Klein register Vrel from the native deck register. This view is retained as a reference target, not identified with the local four-state deck merely because both are called V4.

```text
Vrel is a separately named relation register; original embedding required.
```

**Keep distinct:** The complete Vrel generator/domain source is not included in the fully scanned current packet. Recover it before promoting an embedded-subgroup identity.

**Sources:** [CORE](../provenance/inputs/qr_core_terms_consolidated.md#L1-L3141).

---

<a id="binary-field"></a>

## Two-element scalar field

**Stable ID:** `binary-field`  
**Historical labels / lookup forms:** `F2`, `F_2`, `\mathbb F_2`  
**Kind:** coefficient field  
**Domain:** Binary cochains, signs and normalized coordinates  
**Typed size:** Point/object count: 2  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

F2 is a scalar field, not the forward relation F_2, a frame action or a signed outcome. Its additive group has order two, but changing codomain type still matters.

```text
0+1=1; 1+1=0 in F2
```

**Keep distinct:** Identifying additive scalar groups does not identify their native actions.

**Sources:** [KERNEL](../provenance/inputs/draft6/sections/01C_relational_kernel.tex#L1-L68), [WINDING](../provenance/inputs/PHASE_RELATION_CELLULAR_PROOF.md#L1-L392).

---

<a id="c2-register-parity"></a>

## Native register-orientation quotient action

**Stable ID:** `c2-register-parity`  
**Historical labels / lookup forms:** `C2`, `C_2`  
**Kind:** quotient group/action  
**Domain:** Conjugation of Aut(G60) on {b,ab}  
**Typed size:** Group order: 2  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The two-element image fixes a and either fixes or exchanges b and ab. The map has a kernel of order 240. It is not the central sign in every double cover.

```text
epsilon:Aut(G60)->C2
```

**Keep distinct:** Do not infer a one-leg correlation sign change from this parity alone.

**Recorded relationships:** [s3-abstract-klein](#s3-abstract-klein) (full abstract vs native image).

**Sources:** [ANALYZER](../provenance/inputs/native_analyzer_constraints.md#L1-L450), [CORE](../provenance/inputs/qr_core_terms_consolidated.md#L1-L3141).

---

<a id="c2-root-center"></a>

## Rooted-comparator central subgroup

**Stable ID:** `c2-root-center`  
**Historical labels / lookup forms:** `C2`, `C_2`, `z_F`  
**Kind:** central subgroup family  
**Domain:** The selected G60 root stabilizer  
**Typed size:** Group order: 2  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The center generated by the square of an odd rooted comparator. Its nontrivial native permutation fixes the four vertices of one Klein fiber, unlike the fixed-point-free global deck center.

```text
<z_F>; z_F^2=I; Fix(z_F) has four native vertices
```

**Keep distinct:** This is not the global a-deck involution, nor the BR exchange fixing six vertices.

**Recorded relationships:** [c2-native-double-deck](#c2-native-double-deck) (distinct native permutations).

**Sources:** [MM](../provenance/inputs/C107.json#L1-L44).

---

<a id="c2-native-double-deck"></a>

## Native G60-to-G30 central deck subgroup

**Stable ID:** `c2-native-double-deck`  
**Historical labels / lookup forms:** `C2`, `C_2`, `a_deck`  
**Kind:** embedded deck subgroup  
**Domain:** G60 -> original G30  
**Typed size:** Group order: 2  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The order-two group generated by the named fixed-point-free central a. It is the kernel of the original two-fold covering, not a root stabilizer center.

```text
G30=G60/<a>
```

**Keep distinct:** Native a fixes no G60 vertices; rooted z_F fixes four.

**Recorded relationships:** [c2-root-center](#c2-root-center) (distinct native permutations).

**Sources:** [ANALYZER](../provenance/inputs/native_analyzer_constraints.md#L1-L450), [CORE](../provenance/inputs/qr_core_terms_consolidated.md#L1-L3141).

---

<a id="c2-cover-extra"></a>

## Canonical-double extra sheet deck

**Stable ID:** `c2-cover-extra`  
**Historical labels / lookup forms:** `C2`, `C_2`, `kappa`  
**Kind:** deck subgroup  
**Domain:** K120 -> G60 in the chosen common-cover chart  
**Typed size:** Group order: 2  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The extra two-sheet flip in K120 represented as (x,e)->(x,e+1). It enters the composite free C2^3 deck but is not automatically the lower native a.

```text
kappa(x,e)=(x,e+1)
```

**Keep distinct:** Its role is the extra canonical-double cover coordinate, not a fresh branch choice at each event.

**Sources:** [COVER](../provenance/inputs/draft6/sections/01B_common_cover.tex#L1-L101).

---

<a id="c2-history-kernel"></a>

## Constant kernel of the four-phase history action

**Stable ID:** `c2-history-kernel`  
**Historical labels / lookup forms:** `C2`, `C_2`, `K_hist_action`  
**Kind:** central kernel subgroup  
**Domain:** Gamma_hist -> Perm(Gamma_hist/H0)  
**Typed size:** Group order: 2  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

K=<a>, with a=r^2 z and supplied cache indices {0,326}. This K is a group, not the golden history matrix K_hist or local G1800 operator K.

```text
K=<a>; a=r^2 z; |K|=2
```

**Keep distinct:** Retain the ambient group and map; the subscripted matrix K_hist is a different object.

**Recorded relationships:** [c2-history-extra](#c2-history-extra) (distinct embedded subgroups).

**Sources:** [HISTORY_PHASE](../provenance/inputs/draft6/sections/03F_history_phase_groupoid.tex#L1-L66).

---

<a id="c2-history-extra"></a>

## Extra central factor of Gamma_hist

**Stable ID:** `c2-history-extra`  
**Historical labels / lookup forms:** `C2`, `C_2`, `z_hist`  
**Kind:** direct-product factor  
**Domain:** Gamma_hist=<r,s> x <z>  
**Typed size:** Group order: 2  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The factor generated by z=cache[324] in the supplied phase presentation. It is not automatically K=<r^2z>, even though both are central involutory subgroups.

```text
<z>; z^2=I; [z,r]=[z,s]=I
```

**Keep distinct:** Same order and centrality do not identify distinct subgroups.

**Recorded relationships:** [c2-history-kernel](#c2-history-kernel) (distinct embedded subgroups).

**Sources:** [HISTORY_PHASE](../provenance/inputs/draft6/sections/03F_history_phase_groupoid.tex#L1-L66).

---

<a id="c2-history-word"></a>

## Phase-isotropy word-exchange quotient

**Stable ID:** `c2-history-word`  
**Historical labels / lookup forms:** `C2`, `C_2`, `H_k/K`  
**Kind:** quotient group family  
**Domain:** H_k/K at each declared phase coset  
**Typed size:** Group order: 2  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The source gives an order-two quotient whose nonidentity element is interpreted as a word exchange. This quotient has a distinguished identity; it is not just an unmarked two-element torsor.

```text
H_k / K
```

**Keep distinct:** An actual map to original history states {2,3} is still required.

**Sources:** [HISTORY_PHASE](../provenance/inputs/draft6/sections/03F_history_phase_groupoid.tex#L1-L66).

---

<a id="c2-axis-central"></a>

## Central global sign in the signed-axis extension

**Stable ID:** `c2-axis-central`  
**Historical labels / lookup forms:** `C2`, `C_2`, `I6`, `-I6`  
**Kind:** central operator subgroup  
**Domain:** A_e={+/-M_g} within one conference sector  
**Typed size:** Group order: 2  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The central pair {I6,-I6} of the order-120 split signed extension. It reverses every vector in a chosen three-dimensional conference eigenspace, unlike central spinor -I2 whose conjugation on observables is trivial.

```text
1->C2->A_e->A5->1
```

**Keep distinct:** Not the analyzer-sector flip or automatic physical axis inversion.

**Recorded relationships:** [c2-analyzer-sector](#c2-analyzer-sector) (central sign vs sector character).

**Sources:** [SIGNED_AXIS](../provenance/inputs/draft6/sections/05A_signed_axis_reference.tex#L1-L86).

---

<a id="c2-analyzer-sector"></a>

## Analyzer-sector exchange quotient

**Stable ID:** `c2-analyzer-sector`  
**Historical labels / lookup forms:** `C2`, `C_2`  
**Kind:** quotient action  
**Domain:** G_sec ~= S5 with sector-preserving subgroup A5  
**Typed size:** Group order: 2  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

This C2 records preserving versus exchanging the two conference sectors. The total sector group has trivial center; this character is not the central sign in A_e.

```text
1->A5->G_sec->C2->1
```

**Keep distinct:** A_e and G_sec both have order120 but are nonisomorphic.

**Recorded relationships:** [c2-axis-central](#c2-axis-central) (central sign vs sector character).

**Sources:** [SIGNED_AXIS](../provenance/inputs/draft6/sections/05A_signed_axis_reference.tex#L1-L86).

---

<a id="c2-phase-residual"></a>

## Pair-registration connection residual

**Stable ID:** `c2-phase-residual`  
**Historical labels / lookup forms:** `C2`, `C_2`  
**Kind:** residual action on a transport torsor  
**Domain:** {T,S1 T} before signed-event selection  
**Typed size:** Group order: 2  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The last two-fold ambiguity after pair-level event registration. Its generator is S1; the signed event picks a member. The group, torsor, generator and selected member are distinct records.

```text
{T,S1*T}; residual generator S1
```

**Keep distinct:** Not the actual selected transport, and not the global history2/3 alphabet.

**Recorded relationships:** [connection-doublet](#connection-doublet) (companion action).

**Sources:** [RESIDUAL](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_signed_event_s1_torsor_selector_201h65b.v1.json#L1-L42), [CONNECTION](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_u2_gauge_bridge_connection_frontier_checkpoint_201fp7.v1.json#L1-L190).

---

<a id="c2-threefold-deck"></a>

## Composite elementary-abelian eight-fold deck group

**Stable ID:** `c2-threefold-deck`  
**Historical labels / lookup forms:** `C2^3`, `C_2^3`  
**Kind:** deck group  
**Domain:** K120 -> G15 composite covering  
**Typed size:** Group order: 8  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The free order-eight action generated by the native four-fold deck lifts and the canonical-double sheet flip. All nonidentity elements are involutions.

```text
<a_tilde,b_tilde,kappa> ~= C2 x C2 x C2
```

**Keep distinct:** Not cyclic C8, rooted D8, history D8, or a three-element C3 group.

**Recorded relationships:** [d8-native-root](#d8-native-root) (nonisomorphic group types).

**Sources:** [COVER](../provenance/inputs/draft6/sections/01B_common_cover.tex#L1-L101).

---

<a id="section-c3-mode"></a>

# Cyclic, alternating and symmetric actions

<a id="c3-mode"></a>

## Registered event-frame cyclic phase action

**Stable ID:** `c3-mode`  
**Historical labels / lookup forms:** `C3`, `C_3`, `C_evt`  
**Kind:** cyclic action  
**Domain:** Six registered event frames with Mode reversal  
**Typed size:** Group order: 3  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The phase operator of order three in the specified event-frame model. Together with the involutory Mode action it realizes S3 on that domain.

```text
C_evt^3=M_evt^2=I; M_evt C_evt M_evt=C_evt^-1
```

**Keep distinct:** Not automatically the three-cell shift in X12_kernel or a clock winding.

**Recorded relationships:** [s3-mode](#s3-mode) (generated subgroup).

**Sources:** [MODE](../provenance/inputs/draft6/sections/03A_mode.tex#L1-L69).

---

<a id="c3-kernel"></a>

## Three-cell cyclic shift in the relational kernel

**Stable ID:** `c3-kernel`  
**Historical labels / lookup forms:** `C3`, `C_3`, `Z3`, `Z_3`  
**Kind:** cyclic coordinate/action  
**Domain:** The i coordinate of X12_kernel=Z3 x F2^2  
**Typed size:** Group order: 3  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The cyclic order of the three cells. It preserves forward/reverse relation naming in the color automorphism group; the position coordinate is a residue, not a historical event.

```text
i -> i+1 mod3
```

**Keep distinct:** Same C3 type as event phase is not an event-Mode intertwiner.

**Sources:** [KERNEL](../provenance/inputs/draft6/sections/01C_relational_kernel.tex#L1-L68).

---

<a id="c3-section"></a>

## Closure three-section rotation subgroup

**Stable ID:** `c3-section`  
**Historical labels / lookup forms:** `C3`, `C_3`  
**Kind:** cyclic subgroup  
**Domain:** S3 acting on the three-state closure factor X3  
**Typed size:** Group order: 3  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The order-three rotations of the section-coordinate action. The full factor also contains reversals. A cyclic order is a presentation choice, not an absolute time direction.

```text
C3 <= Sym(X3) ~= S3
```

**Keep distinct:** No equality with event C_evt or companion monodromy rotation has been supplied.

**Sources:** [OLDER_SECTION_SURFACE](../provenance/excerpts/older_section_surface.md#L1-L9).

---

<a id="c4-native-exchange"></a>

## Selected native exchange cyclic subgroup

**Stable ID:** `c4-native-exchange`  
**Historical labels / lookup forms:** `C4`, `C_4`  
**Kind:** cyclic subgroup  
**Domain:** <g> in the supplied Aut(G60) cache  
**Typed size:** Group order: 4  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The selected order-four native action with g=cache[3], g^2=cache[2] and inverse cache[5]. This same selected element occurs in the declared phase-group construction, but its other representations remain separate views.

```text
g^4=I; g^2=r1_native; powers indices [0,3,2,5]
```

**Keep distinct:** Not G1800 K without a carrier map; r1_native is not primitive homology class r1.

**Sources:** [HISTORY_PHASE](../provenance/inputs/draft6/sections/03F_history_phase_groupoid.tex#L1-L66), [CARTAN](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_order4_square_cartan_orientation_201h35b.v1.json#L1-L99), [BUNDLE](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_r1_face_bundle_cocycle_triviality_201h69g.v1.json#L1-L50).

---

<a id="c4-g1800"></a>

## Registered G1800 quarter-turn subgroup

**Stable ID:** `c4-g1800`  
**Historical labels / lookup forms:** `C4`, `C_4`, `K_1800`  
**Kind:** cyclic permutation group  
**Domain:** One ordered registration of a native G1800 product quotient  
**Typed size:** Group order: 4  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The group generated by the specific K_1800 action. Its square is Delta_1800, and each free orbit contains four native states.

```text
K_1800^4=I; K_1800^2=Delta_1800
```

**Keep distinct:** Not the native Klein register or a C4 graph-census code.

**Sources:** [FRAMES](../provenance/inputs/native_g9000_map_test.md#L1-L295).

---

<a id="c4-face-complex"></a>

## Face complex-quarter-turn subgroup

**Stable ID:** `c4-face-complex`  
**Historical labels / lookup forms:** `C4`, `C_4`, `J_F`  
**Kind:** cyclic operator group  
**Domain:** Chosen face complex structure on a four-real-dimensional fiber  
**Typed size:** Group order: 4; Real dimension: 4  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The powers of the selected orthogonal complex structure J_F, for which J_F^2=-I. Its inclusion in <J_F,S1> is an operator-group statement.

```text
<J_F>; J_F^2=-I4
```

**Keep distinct:** Not the selected cache element g unless an admitted representation identifies their actions.

**Sources:** [FACE](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_face_field_higgs_bridge_checkpoint_receipt_201fk.v1.json#L1-L144), [RESIDUAL](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_signed_event_s1_torsor_selector_201h65b.v1.json#L1-L42).

---

<a id="c4-history-companion"></a>

## Registered-decagon companion cyclic action

**Stable ID:** `c4-history-companion`  
**Historical labels / lookup forms:** `C4`, `C_4`, `history24`  
**Kind:** cyclic subgroup family  
**Domain:** Companion actions generated using BR-related involutions  
**Typed size:** Group order: 4  
**Standing:** Source-reported companion family; original action tables not replayed.

The integrated draft distinguishes order-four companions built from BR-related involutions from rooted comparators. The displayed companion square is the global native a, whereas the rooted comparator square fixes four vertices. This archive preserves that contrast without identifying all members of the companion family.

```text
(b j)^2=(ab j)^2=a; (b j)^-1=ab j
```

**Keep distinct:** The original companion action table is not rerun or fully reproduced. A matching order-four presentation is insufficient for a rooted-comparator identification.

**Sources:** [MACRO_EXCERPT](../provenance/excerpts/macro_and_support.md#L1-L10), [MM](../provenance/inputs/C107.json#L1-L44).

---

<a id="c5-history"></a>

## Fivefold rotation subgroup of the historical D5 register

**Stable ID:** `c5-history`  
**Historical labels / lookup forms:** `C5`, `C_5`  
**Kind:** cyclic subgroup  
**Domain:** Historical D5=<a,b> with s=ab  
**Typed size:** Group order: 5  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The rotation subgroup carrying the historical fivefold contrast polynomial. It is not obtained by simply taking ab of the native commuting Klein pair.

```text
<s>; s=ab; s^5=I
```

**Keep distinct:** Same polynomial as a frame contrast does not identify native state actions.

**Sources:** [HISTORICAL_FIVEFOLD](../provenance/excerpts/historical_fivefold.md#L1-L9).

---

<a id="c5-analyzer"></a>

## Analyzer Sylow-five subgroup family

**Stable ID:** `c5-analyzer`  
**Historical labels / lookup forms:** `C5`, `C_5`  
**Kind:** subgroup family / axis index  
**Domain:** Six Sylow-5 subgroups in the S5 quotient action  
**Typed size:** Group order: 5  
**Family parameters:** six subgroup objects C5_i  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The six subgroup objects provide analyzer axes via order-five averaging on specified native modes. Each cyclic subgroup is a group; their six-member family is a different set.

```text
Pi_i=(1/5) sum_(g in C5_i) U_g P
```

**Keep distinct:** Do not identify the six-axis index set with five frame labels.

**Sources:** [ANALYZER](../provenance/inputs/native_analyzer_constraints.md#L1-L450), [CONF_ACTION](../provenance/inputs/thalean_transport_conference_bridge_audit.json#L1-L123).

---

<a id="c5-frame"></a>

## Pure five-frame shift action

**Stable ID:** `c5-frame`  
**Historical labels / lookup forms:** `C5`, `C_5`, `S_frame`  
**Kind:** cyclic permutation action  
**Domain:** Five registered frame copies of G1800  
**Typed size:** Group order: 5  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The pure frame-coordinate shift separated from the combined registered step. The historical reconstructed coordinate chart supports the definition; physical or unrestricted native-dynamics admission remains separate.

```text
S_frame(f,x)=(f+1,x); S_frame^5=I; F_reg=S_frame K_1800
```

**Keep distinct:** Preserve conditional native/admissibility status from the archive. Not the analyzer-axis C5.

**Sources:** [FRAMES](../provenance/inputs/native_g9000_map_test.md#L1-L295), [CHAT](../provenance/excerpts/current_chat_archive.md#L1-L21).

---

<a id="c10-native"></a>

## Native decagonal macro-transport subgroup

**Stable ID:** `c10-native`  
**Historical labels / lookup forms:** `C10`, `C_10`  
**Kind:** cyclic subgroup  
**Domain:** Native G60 macro-history transport T10  
**Typed size:** Group order: 10  
**Standing:** Source/context-reported macro action; five-axis quotient data available, full original actor not replayed.

The cyclic subgroup generated by the independently named native T10 macro transport. The inherited law T10^5=b and the nontrivial involution b give the reported decagonal action. The subgroup is not the generating element and is not the C20 frame group.

```text
<T10> ~= C10; T10^5=b; T10^10=I
```

**Keep distinct:** The T10 full-permutation law is retained from earlier source context; this sweep does not reconstruct it. T10 is a selected actor name, not group order notation by itself.

**Recorded relationships:** [t01-edge-connection](#t01-edge-connection) (endpoint indices vs actor name); [t10-native-macro](#t10-native-macro) (generates).

**Sources:** [MACRO_EXCERPT](../provenance/excerpts/macro_and_support.md#L1-L10), [CONF_ACTION](../provenance/inputs/thalean_transport_conference_bridge_audit.json#L1-L123), [CORE](../provenance/inputs/qr_core_terms_consolidated.md#L1-L3141).

---

<a id="c20-registered"></a>

## Registered twenty-step frame-history action

**Stable ID:** `c20-registered`  
**Historical labels / lookup forms:** `C20`, `C_20`, `F_reg`  
**Kind:** cyclic action  
**Domain:** Each free orbit of the registered G9000 action  
**Typed size:** Group order: 20  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The full registered action has order twenty, combining mod5 frame and mod4 internal residue. This does not make it an automorphism of one bare G1800 graph.

```text
F_reg^5=K_1800; F_reg^20=I; 450 free20-cycles
```

**Keep distinct:** Retain the registered groupoid and its frame maps; not an SI clock.

**Sources:** [FRAMES](../provenance/inputs/native_g9000_map_test.md#L1-L295).

---

<a id="s3-abstract-klein"></a>

## Abstract Klein automorphism triality

**Stable ID:** `s3-abstract-klein`  
**Historical labels / lookup forms:** `S3`, `S_3`  
**Kind:** abstract automorphism group  
**Domain:** Aut(V4_abstract)  
**Typed size:** Group order: 6  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The permutations of three nonidentity elements of an abstract Klein group. This full type is not realized by native G60 conjugation on its named deck triple, whose image is only C2.

```text
Aut(V4_abstract) ~= S3
```

**Keep distinct:** Do not upgrade abstract automorphisms to native admitted symmetries.

**Recorded relationships:** [c2-register-parity](#c2-register-parity) (full abstract vs native image).

**Sources:** [CORE](../provenance/inputs/qr_core_terms_consolidated.md#L1-L3141), [ANALYZER](../provenance/inputs/native_analyzer_constraints.md#L1-L450).

---

<a id="s3-mode"></a>

## Event phase-Mode permutation action

**Stable ID:** `s3-mode`  
**Historical labels / lookup forms:** `S3`, `S_3`  
**Kind:** finite action  
**Domain:** The six registered event frames  
**Typed size:** Group order: 6  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The specified order-three phase and reversal give the six-element action described in the Mode section. It remains a finite action on event frames, not a universal physical time symmetry.

```text
<C_evt,M_evt>; M_evt C_evt M_evt=C_evt^-1
```

**Keep distinct:** Distinct from companion three-cover monodromy and abstract Klein triality.

**Recorded relationships:** [c3-mode](#c3-mode) (generated subgroup).

**Sources:** [MODE](../provenance/inputs/draft6/sections/03A_mode.tex#L1-L69).

---

<a id="s3-section"></a>

## Three-section factor permutation symmetry

**Stable ID:** `s3-section`  
**Historical labels / lookup forms:** `S3`, `S_3`  
**Kind:** action factor  
**Domain:** X3 in the twelve-section closure surface  
**Typed size:** Group order: 6; Point/object count: 3  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The full three-point factor symmetry supplied in the X3 x X4 presentation. It permutes closure-section coordinates and participates in the S3 x D8 product action.

```text
Sym(X3) ~= S3
```

**Keep distinct:** An isomorphic event-phase action does not imply identical section objects.

**Sources:** [OLDER_SECTION_SURFACE](../provenance/excerpts/older_section_surface.md#L1-L9).

---

<a id="s3-monodromy"></a>

## Companion three-cover monodromy action

**Stable ID:** `s3-monodromy`  
**Historical labels / lookup forms:** `S3`, `S_3`  
**Kind:** quotient/monodromy action  
**Domain:** Three-cover companion construction in the infrared manuscript  
**Typed size:** Group order: 6  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The six-element monodromy giving a real regular representation and protected real-rank4 E-isotypic sector. The source places this below a 720-element companion group, not the native order480 group.

```text
R[S3]=1+1prime+E+E; E-isotypic real rank4
```

**Keep distinct:** No arbitrary microscopic G60/G1800 transport factoring through it is claimed.

**Sources:** [COMPANION_TRIALITY](../provenance/excerpts/companion_triality.md#L1-L9).

---

<a id="s5-native-quotient"></a>

## Native five-address quotient symmetry

**Stable ID:** `s5-native-quotient`  
**Historical labels / lookup forms:** `S5`, `S_5`, `s5`  
**Kind:** quotient group/action  
**Domain:** Aut(G60)/V4_nat on the canonical five-address register  
**Typed size:** Group order: 120; Point/object count: 5  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The faithful quotient factor used throughout the native symmetry architecture. Its induced actions on five addresses, six Sylow-five axes and other domains must be named independently.

```text
1->V4_nat->Aut(G60)->S5->1
```

**Keep distinct:** The abstract group is shared; action spaces of sizes5,6,12,15 are not thereby identical.

**Recorded relationships:** [s5-six-axes](#s5-six-axes) (same group different representation).

**Sources:** [FP](../provenance/inputs/native_g60_fiber_product_isomorphism_044.json#L37805-L37814), [CONF_ACTION](../provenance/inputs/thalean_transport_conference_bridge_audit.json#L1-L123), [COVER](../provenance/inputs/draft6/sections/01B_common_cover.tex#L1-L101).

---

<a id="s5-six-axes"></a>

## Six-Sylow-axis quotient permutation action

**Stable ID:** `s5-six-axes`  
**Historical labels / lookup forms:** `S5`, `S_5`  
**Kind:** permutation representation  
**Domain:** Six intrinsic Sylow-five subgroup objects  
**Typed size:** Group order: 120; Point/object count: 6  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The quotient acts by subgroup conjugation, giving the six-axis permutation action used in the conference comparison. It is the same quotient group with a different domain.

```text
g:C5_i -> g C5_i g^-1
```

**Keep distinct:** Preserve the specific axis relabeling and signed lift separately.

**Recorded relationships:** [s5-native-quotient](#s5-native-quotient) (same group different representation).

**Sources:** [CONF_ACTION](../provenance/inputs/thalean_transport_conference_bridge_audit.json#L1-L123).

---

<a id="s5-analyzer-sectors"></a>

## Two-sector projective analyzer symmetry

**Stable ID:** `s5-analyzer-sectors`  
**Historical labels / lookup forms:** `S5`, `S_5`, `G_sec`  
**Kind:** finite projective symmetry group  
**Domain:** Two conference sectors with signed switchings  
**Typed size:** Group order: 120  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The sector group of order120 with an index-two A5 sector-preserving subgroup. Its center is trivial; source comparison to native face actions is not a selected operator binding.

```text
G_sec ~= S5; M C M^T=+/-C
```

**Keep distinct:** Not the order120 signed within-sector extension A5 x C2.

**Recorded relationships:** [signed-axis-extension](#signed-axis-extension) (nonisomorphic groups of equal order).

**Sources:** [SIGNED_AXIS](../provenance/inputs/draft6/sections/05A_signed_axis_reference.tex#L1-L86).

---

<a id="a5-axis-base"></a>

## Within-sector projective analyzer base group

**Stable ID:** `a5-axis-base`  
**Historical labels / lookup forms:** `A5`, `A_5`  
**Kind:** finite projective action  
**Domain:** One six-axis conference sector  
**Typed size:** Group order: 60  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The sixty within-sector switchings form the source base group A5. A section into signed matrices may initially have a global sign factor set; the source rephases that section.

```text
60 switchings; signed extension A_e ~= A5 x C2
```

**Keep distinct:** This A5 action is not a 60-vertex G60 carrier.

**Sources:** [SIGNED_AXIS](../provenance/inputs/draft6/sections/05A_signed_axis_reference.tex#L1-L86).

---

<a id="signed-axis-extension"></a>

## Split within-sector signed-axis extension

**Stable ID:** `signed-axis-extension`  
**Historical labels / lookup forms:** `A5 x C2`, `A_e`, `A_tilde`  
**Kind:** finite matrix group  
**Domain:** Six signed analyzer coordinates / either rank-three eigenspace  
**Typed size:** Group order: 120  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The doubled group of signed matrices {+/-M_g}; source rephasing shows a split extension with central global reversal.

```text
1->C2->A_e->A5->1; A_e ~= A5 x C2
```

**Keep distinct:** Not G_sec, the common-cover graph, or the 120 bare face incidences.

**Recorded relationships:** [s5-analyzer-sectors](#s5-analyzer-sectors) (nonisomorphic groups of equal order).

**Sources:** [SIGNED_AXIS](../provenance/inputs/draft6/sections/05A_signed_axis_reference.tex#L1-L86).

---

<a id="a4-kernel-color"></a>

## Tetrahedral factor in kernel color symmetry

**Stable ID:** `a4-kernel-color`  
**Historical labels / lookup forms:** `A4`, `A_4`  
**Kind:** semidirect-product action factor  
**Domain:** Even-parity binary translations and three-cell rotation in X12_kernel  
**Typed size:** Group order: 12  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The normalized kernel calculation splits the shift kernel into a diagonal line and a two-dimensional even-parity plane. The plane plus rotation gives V4 semidirect C3, identified as A4.

```text
V4_even semidirect C3 ~= A4
```

**Keep distinct:** Not a raw adjacency A4 move operator or generic fourth indexed observable.

**Sources:** [KERNEL](../provenance/inputs/draft6/sections/01C_relational_kernel.tex#L1-L68).

---

<a id="kernel-color-group"></a>

## Rank-eight kernel color-preserving group

**Stable ID:** `kernel-color-group`  
**Historical labels / lookup forms:** `C2 x A4`, `C2`, `A4`  
**Kind:** finite automorphism group  
**Domain:** The eight colored relations on X12_kernel  
**Typed size:** Group order: 24; Point/object count: 12  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The order24 color group, acting transitively on12points with point stabilizer2. It is smaller than the full fused graph group, because it retains relation colors.

```text
(i,x)->(i+r,x+(b_(i+1),b_i)); r in Z3,b in F2^3
```

**Keep distinct:** Do not identify the full fused symmetry with the color group.

**Sources:** [KERNEL](../provenance/inputs/draft6/sections/01C_relational_kernel.tex#L1-L68).

---

<a id="a3-mode-subgroup"></a>

## Alternating three-frame phase subgroup

**Stable ID:** `a3-mode-subgroup`  
**Historical labels / lookup forms:** `A3`, `A_3`  
**Kind:** cyclic subgroup view  
**Domain:** Even permutations in the specified event S3 action  
**Typed size:** Group order: 3  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

A3 is the alternating subgroup of the event-frame S3; where the phase generator is specified, it is that order-three cyclic subgroup.

```text
A3=<C_evt> within the declared event action
```

**Keep distinct:** Not the A3 root-system comparison target or fused distance-three adjacency.

**Sources:** [MODE](../provenance/inputs/draft6/sections/03A_mode.tex#L1-L69).

---

<a id="a3-root-target"></a>

## A3 outer-root-reversal comparison target

**Stable ID:** `a3-root-target`  
**Historical labels / lookup forms:** `A3`, `A_3`  
**Kind:** referenced root-system operation  
**Domain:** Higher four-complex-dimensional/Weyl comparison mentioned in the reflection audit  
**Standing:** Unresolved comparison target, not a certified operator.

The selected antiunitary audit explicitly lists an A3 outer root reversal as a separate target not derived there. The spelling does not mean the order-three alternating group.

```text
No full C^4 A3 outer operator derived in 201H67B
```

**Keep distinct:** Keep as a named target; no matrix, root embedding or identification is supplied.

**Sources:** [REFLECTION](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_selected_reflection_event_pauli_anatomy_201h67b.v1.json#L1-L41).

---

<a id="section-g60-native"></a>

# Graphs, finite state sets, and counting conventions

<a id="g60-native"></a>

## Thalion native graph carrier

**Stable ID:** `g60-native`  
**Historical labels / lookup forms:** `G60`, `G_60`, `AT4val[60,6]`  
**Kind:** finite graph  
**Domain:** Native60vertex graph  
**Typed size:** Point/object count: 60  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The quartic carrier at the center of the inherited work. The label G60 names its vertices and edges, not its automorphism group, vector space dimension in every representation, or a general arbitrary60state model.

```text
G60=AT4val[60,6]; 60 vertices,120 edges
```

**Keep distinct:** The 480-element symmetry group and the 60-element analyzer base group are different objects.

**Recorded relationships:** [g-family-6](#g-family-6) (source identified graph); [k120-common-cover](#k120-common-cover) (canonical double cover).

**Sources:** [EPR](../provenance/inputs/native_epr_history_control.md#L1-L74), [COVER](../provenance/inputs/draft6/sections/01B_common_cover.tex#L1-L101), [ANALYZER](../provenance/inputs/native_analyzer_constraints.md#L1-L450).

---

<a id="g30-original"></a>

## Original native central-deck quotient graph

**Stable ID:** `g30-original`  
**Historical labels / lookup forms:** `G30`, `G_30`  
**Kind:** finite quotient graph  
**Domain:** G60/<a> in the inherited native tower  
**Typed size:** Point/object count: 30  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The named two-fold quotient in the original tower, identified in the manuscript as L(Dodecahedron). The cover-family intermediate Q30 is not this graph.

```text
G30=G60/<a>; original G30=L(Dodecahedron)
```

**Keep distinct:** Same thirty-vertex count as Q30 is not identity.

**Recorded relationships:** [q30-family](#q30-family) (distinct graphs).

**Sources:** [COVER](../provenance/inputs/draft6/sections/01B_common_cover.tex#L1-L101), [CORE](../provenance/inputs/qr_core_terms_consolidated.md#L1-L3141).

---

<a id="g15-native"></a>

## Native Klein quotient / Petersen line graph

**Stable ID:** `g15-native`  
**Historical labels / lookup forms:** `G15`, `G_15`  
**Kind:** finite quotient graph  
**Domain:** G60/V4_nat  
**Typed size:** Point/object count: 15  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The fifteen-chamber quotient with thirty edges, identified as the Petersen line graph. Its vertices can be represented as Petersen edges using the declared isomorphism.

```text
G15 ~= L(Petersen)
```

**Keep distinct:** Quotient-visible relations need not retain all native lifted signs.

**Sources:** [EPR](../provenance/inputs/native_epr_history_control.md#L1-L74), [COVER](../provenance/inputs/draft6/sections/01B_common_cover.tex#L1-L101).

---

<a id="q30-family"></a>

## Common cover-family thirty-vertex intermediate

**Stable ID:** `q30-family`  
**Historical labels / lookup forms:** `Q30`, `Q_30`  
**Kind:** finite graph  
**Domain:** Common AT4val-family cover diagram  
**Typed size:** Point/object count: 30  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The family intermediate identified as L(CDC(Petersen)). The source expressly distinguishes it from original G30.

```text
Q30=L(CDC(Petersen))
```

**Keep distinct:** No consolidation with G30 merely through shared size or tetravalency.

**Recorded relationships:** [g30-original](#g30-original) (distinct graphs).

**Sources:** [COVER](../provenance/inputs/draft6/sections/01B_common_cover.tex#L1-L101).

---

<a id="k120-common-cover"></a>

## Common AT4val-family bipartite cover graph

**Stable ID:** `k120-common-cover`  
**Historical labels / lookup forms:** `K120`, `K_120`, `mathsfK120`, `C4[120,38]`  
**Kind:** finite graph  
**Domain:** Census family comparison of the three sixty-vertex children  
**Typed size:** Point/object count: 120  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The custom named common cover K120 has120vertices240edges and is represented by census C4[120,38]. It is not the complete graph on120vertices.

```text
K120=CDC(G60) in the stated chart; census C4[120,38]
```

**Keep distinct:** Never expand this custom K120 to complete-graph notation K_n. Also distinguish the unresolved 201EZ K120 group-locator label.

**Recorded relationships:** [g60-native](#g60-native) (canonical double cover); [k120-group-locator](#k120-group-locator) (unresolved name collision).

**Sources:** [COVER](../provenance/inputs/draft6/sections/01B_common_cover.tex#L1-L101), [CENSUS_REPORT](../provenance/inputs/draft6/data/generated/census_family_report.json#L1-L5852).

---

<a id="g-family-4"></a>

## Sixty-vertex census-family child 4

**Stable ID:** `g-family-4`  
**Historical labels / lookup forms:** `G4`, `G_4`, `AT4val[60,4]`  
**Kind:** finite graph  
**Domain:** Quotient K120/<tau_4>  
**Typed size:** Point/object count: 60  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The subscript 4 identifies a census-family child, not the number of vertices. All three children here have sixty vertices. Its quotient involution and census identity are retained separately.

```text
G_4=K120/<tau_4>
```

**Keep distinct:** Distinct central quotient involutions are not conjugated into each other by the same cover automorphism group.

**Sources:** [COVER](../provenance/inputs/draft6/sections/01B_common_cover.tex#L1-L101), [CENSUS_REPORT](../provenance/inputs/draft6/data/generated/census_family_report.json#L1-L5852).

---

<a id="g-family-5"></a>

## Sixty-vertex census-family child 5

**Stable ID:** `g-family-5`  
**Historical labels / lookup forms:** `G5`, `G_5`, `AT4val[60,5]`  
**Kind:** finite graph  
**Domain:** Quotient K120/<tau_5>  
**Typed size:** Point/object count: 60  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The subscript 5 identifies a census-family child, not the number of vertices. All three children here have sixty vertices. Its quotient involution and census identity are retained separately.

```text
G_5=K120/<tau_5>
```

**Keep distinct:** Distinct central quotient involutions are not conjugated into each other by the same cover automorphism group.

**Sources:** [COVER](../provenance/inputs/draft6/sections/01B_common_cover.tex#L1-L101), [CENSUS_REPORT](../provenance/inputs/draft6/data/generated/census_family_report.json#L1-L5852).

---

<a id="g-family-6"></a>

## Sixty-vertex census-family child 6

**Stable ID:** `g-family-6`  
**Historical labels / lookup forms:** `G6`, `G_6`, `AT4val[60,6]`  
**Kind:** finite graph  
**Domain:** Quotient K120/<tau_6>  
**Typed size:** Point/object count: 60  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The subscript 6 identifies a census-family child, not the number of vertices. All three children here have sixty vertices. The source identifies child6 with the native G60 graph.

```text
G_6=K120/<tau_6>
```

**Keep distinct:** Distinct central quotient involutions are not conjugated into each other by the same cover automorphism group.

**Recorded relationships:** [g60-native](#g60-native) (source identified graph).

**Sources:** [COVER](../provenance/inputs/draft6/sections/01B_common_cover.tex#L1-L101), [CENSUS_REPORT](../provenance/inputs/draft6/data/generated/census_family_report.json#L1-L5852).

---

<a id="g1800-family"></a>

## Registered two-factor native product quotient family

**Stable ID:** `g1800-family`  
**Historical labels / lookup forms:** `G1800`, `G_1800`, `Y1800`  
**Kind:** finite graph family  
**Domain:** (G60 square G60)/diag<d>, with d and ordered registration declared  
**Typed size:** Point/object count: 1800  
**Family parameters:** d; ordered pair of native deck axes; chosen labeling  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

There are three native quotient kernels and six ordered axis registrations in the retained construction. The label names a family unless the kernel and register are supplied. It is not an operator K or its900state shadow.

```text
Y_d=(G60 square G60)/diag<d>; d in {a,b,ab}
```

**Keep distinct:** Record the quotient fibers, kernel, native labeling and ordered registration for every selected instance.

**Recorded relationships:** [g900-associated](#g900-associated) (quotient); [g9000-registered](#g9000-registered) (five registered frames).

**Sources:** [FRAMES](../provenance/inputs/native_g9000_map_test.md#L1-L295), [EPR](../provenance/inputs/native_epr_history_control.md#L1-L74).

---

<a id="g900-associated"></a>

## Associated Delta quotient of a registered G1800 carrier

**Stable ID:** `g900-associated`  
**Historical labels / lookup forms:** `G900`, `G_900`  
**Kind:** finite quotient graph family  
**Domain:** G1800/<Delta_1800> for the declared registration  
**Typed size:** Point/object count: 900  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The associated900state graph obtained from the free involution. Its relationship to other historical G900 registry/viewer objects requires their exact body/source mapping; the count is not enough.

```text
q(x)=q(Delta_1800 x)
```

**Keep distinct:** Not the sending receipt delta_e or an automatically universal G900 across all project versions.

**Recorded relationships:** [g1800-family](#g1800-family) (quotient).

**Sources:** [FRAMES](../provenance/inputs/native_g9000_map_test.md#L1-L295), [CORE](../provenance/inputs/qr_core_terms_consolidated.md#L1-L3141).

---

<a id="g9000-registered"></a>

## Registered five-frame native groupoid carrier

**Stable ID:** `g9000-registered`  
**Historical labels / lookup forms:** `G9000`, `G_9000`  
**Kind:** registered finite groupoid state set  
**Domain:** Five transported G1800 frames  
**Typed size:** Point/object count: 9000  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The9000states consist of five1800state frames. Four transport choices and six axis registrations give24raw arrays, not24timesmore state capacity. Native coordinate trivialization makes inter-frame comparisons explicit.

```text
F_reg(f,x)=(f+1,K_1800 x)
```

**Keep distinct:** Not one canonical unlabeled9000vertex graph, nor five of the six analyzer axes.

**Recorded relationships:** [g1800-family](#g1800-family) (five registered frames).

**Sources:** [FRAMES](../provenance/inputs/native_g9000_map_test.md#L1-L295).

---

<a id="x12-sections"></a>

## Twelve-section closure surface state set

**Stable ID:** `x12-sections`  
**Historical labels / lookup forms:** `X12`, `X_12`, `X3 x X4`  
**Kind:** structured finite set  
**Domain:** Original registered closure-section construction  
**Typed size:** Point/object count: 12  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

A source-supplied3by4set with a specified S3 x D8 action and a K12-minus-matching section graph. Its incidence/cochain structure is part of its view.

```text
X12_sections ~= X3 x X4
```

**Keep distinct:** Not automatically the normalized relational-kernel points, twelve pentagon generators, twelve phase pairs or a twelve-dimensional module.

**Recorded relationships:** [x12-kernel](#x12-kernel) (similar count and product shape); [three-section-coordinate](#three-section-coordinate) (coordinate factor).

**Sources:** [OLDER_SECTION_SURFACE](../provenance/excerpts/older_section_surface.md#L1-L9).

---

<a id="x12-kernel"></a>

## Twelve-point normalized relational-kernel carrier

**Stable ID:** `x12-kernel`  
**Historical labels / lookup forms:** `X12`, `X_12`, `Z3 x V4`  
**Kind:** structured finite set  
**Domain:** Normalized rank-eight coherent configuration  
**Typed size:** Point/object count: 12  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The12points(i,x1,x2) carry eight specified relations. Its normalized coordinate description is the source for the noncommuting adjacency algebra and the icosahedral fusion.

```text
X12_kernel=Z3 x F2^2
```

**Keep distinct:** A common size and3x4factorization do not by themselves identify the earlier closure surface.

**Recorded relationships:** [x12-sections](#x12-sections) (similar count and product shape); [twelve-pair-descriptors](#twelve-pair-descriptors) (points vs pair partition).

**Sources:** [KERNEL](../provenance/inputs/draft6/sections/01C_relational_kernel.tex#L1-L68).

---

<a id="twelve-pair-descriptors"></a>

## Twelve directed-pair descriptor bins

**Stable ID:** `twelve-pair-descriptors`  
**Historical labels / lookup forms:** `X12_descriptor`, `3x2x2`  
**Kind:** partition of pairs  
**Domain:** Cross-cell ordered pairs of X12_kernel  
**Typed size:** Pair-bin count: 12; Ordered-pair count: 96  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

Each descriptor(i,forward/reverse,c) bins eight ordered pairs. There are12bins and96cross-cellpairs. These are not12additional point states.

```text
12 bins x8 pairs=96 cross-cellpairs; plus48within-cellpairs=144
```

**Keep distinct:** Keep pair bins distinct from point sets and spectral dimensions.

**Recorded relationships:** [x12-kernel](#x12-kernel) (points vs pair partition).

**Sources:** [KERNEL](../provenance/inputs/draft6/sections/01C_relational_kernel.tex#L1-L68).

---

<a id="twelve-face-phases"></a>

## Twelve face/relative-orientation objects

**Stable ID:** `twelve-face-phases`  
**Historical labels / lookup forms:** `phase_state_count_12`, `12_phase_objects`, `6K2_domain`, `S12`  
**Kind:** structured finite set  
**Domain:** Six native faces times two relative-complex-orientation states  
**Typed size:** Point/object count: 12  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The face gauge-envelope construction has12objects, with a native action and stabilizer40. The same-face phase-flip relation is6K2; other orbitals are twoK6 and a crown.

```text
6 faces x2phasechoices; suborbit profile[1,1,5,5]
```

**Keep distinct:** This is not the four cosets of Gamma_hist or the twelve-pentagon cycle space.

**Recorded relationships:** [history-pentagon-space](#history-pentagon-space) (finite set vs vector space); [s12-phase-set](#s12-phase-set) (same source phase objects).

**Sources:** [CONNECTION](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_u2_gauge_bridge_connection_frontier_checkpoint_201fp7.v1.json#L1-L190), [FACE](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_face_field_higgs_bridge_checkpoint_receipt_201fk.v1.json#L1-L144).

---

<a id="six-k2"></a>

## Six same-face phase-flip edges

**Stable ID:** `six-k2`  
**Historical labels / lookup forms:** `6K2`, `6K_2`  
**Kind:** finite orbital graph  
**Domain:** The twelve face/relative-orientation objects  
**Typed size:** Point/object count: 12  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

Six disjoint two-vertex complete graphs, one for each same-face phase flip. This is the connection domain selected in the source, not a group named6K2.

```text
6K2 = disjoint union of six K2
```

**Keep distinct:** Source selects local transports here; crown and same-phase connection choices remain separately open.

**Sources:** [CONNECTION](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_u2_gauge_bridge_connection_frontier_checkpoint_201fp7.v1.json#L1-L190).

---

<a id="two-k6"></a>

## Same-phase complete-component orbital

**Stable ID:** `two-k6`  
**Historical labels / lookup forms:** `2K6`, `2K_6`  
**Kind:** finite orbital graph  
**Domain:** Twelve face/phase objects, grouped by phase  
**Typed size:** Point/object count: 12  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The union of two complete six-vertex components representing same-phase adjacency. It is not the same-face6K2relation and does not inherit its selected connection automatically.

```text
2K6
```

**Keep distinct:** The source explicitly leaves the twoK6connection unselected.

**Sources:** [CONNECTION](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_u2_gauge_bridge_connection_frontier_checkpoint_201fp7.v1.json#L1-L190).

---

<a id="face-crown"></a>

## Opposite-phase different-face crown orbital

**Stable ID:** `face-crown`  
**Historical labels / lookup forms:** `K6,6-M6`, `K_{6,6}-M_6`, `M6`  
**Kind:** finite orbital graph  
**Domain:** Twelve face/phase objects  
**Typed size:** Point/object count: 12  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The opposite-phase crown: complete bipartite six-by-six with the same-face matching removed. M6 means the matching in this expression, not a six-dimensional matrix algebra.

```text
K6,6 minus a six-edge perfect matching
```

**Keep distinct:** An isomorphic crown appears as support of the history operator; no domain map follows from graph isomorphism alone.

**Recorded relationships:** [history-crown](#history-crown) (same graph type only).

**Sources:** [CONNECTION](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_u2_gauge_bridge_connection_frontier_checkpoint_201fp7.v1.json#L1-L190).

---

<a id="history-crown"></a>

## Registered-pentagon conference support graph

**Stable ID:** `history-crown`  
**Historical labels / lookup forms:** `crown12`, `K6,6-M6`  
**Kind:** support graph of a matrix  
**Domain:** Twelve registered pentagon coefficient generators  
**Typed size:** Point/object count: 12  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The nonzero pattern of K_hist is a connected crown graph. Its bipartition is the six b versus six ab generators. Signs and Gram values add information beyond this graph.

```text
Support(K_hist);12vertices30edgesdegree5
```

**Keep distinct:** Not identical to the face-phase crown orbital absent a map between its vertices.

**Recorded relationships:** [face-crown](#face-crown) (same graph type only).

**Sources:** [HIST](../provenance/inputs/thalean_registered_history_conference_operator_audit.json#L1-L564).

---

<a id="k4-matching"></a>

## Four-point complete graph used for local pairings

**Stable ID:** `k4-matching`  
**Historical labels / lookup forms:** `K4`, `K_4`  
**Kind:** comparison graph  
**Domain:** Four elements of a local Klein cell  
**Typed size:** Point/object count: 4  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The three nonidentity Klein translations correspond to the three perfect matchings of K4. The complete graph is a representation of pairings, not itself the V4 action group.

```text
Three perfect matchings of K4
```

**Keep distinct:** Not quaternionic generator K4 or a census catalogue code.

**Sources:** [BASE](../provenance/inputs/qr_core_terms_original.md#L1-L1982), [CORE](../provenance/inputs/qr_core_terms_consolidated.md#L1-L3141).

---

<a id="k12-complete-parent"></a>

## Complete twelve-point graph used as a section-graph parent

**Stable ID:** `k12-complete-parent`  
**Historical labels / lookup forms:** `K12`, `K_12`  
**Kind:** graph notation  
**Domain:** Parent in K12 minus perfect matching  
**Typed size:** Point/object count: 12  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The section source uses complete-graph notation here, unlike custom K120. The actual section graph removes a matching, so the complete parent and the section graph are distinct objects.

```text
Section graph = K12 - perfect matching
```

**Keep distinct:** Do not parse every K followed by a number as this family; K120 is custom.

**Sources:** [OLDER_SECTION_SURFACE](../provenance/excerpts/older_section_surface.md#L1-L9).

---

<a id="prism-support"></a>

## Minimal binary-support hexagonal prism graph

**Stable ID:** `prism-support`  
**Historical labels / lookup forms:** `C6 square K2`, `C_6 square K_2`  
**Kind:** finite graph  
**Domain:** Weight-eighteen binary support in the section closure discussion  
**Typed size:** Point/object count: 12  
**Standing:** Source-referenced support graph; exact original support source not reproduced.

The integrated draft refers to two minimum-weight binary supports, each isomorphic to a hexagonal prism. In this graph expression C6 is the six-cycle graph and K2 the two-vertex complete graph, not selected cyclic group actions.

```text
C6 square K2, twelve vertices and eighteen edges
```

**Keep distinct:** The original support certificate is not rerun. Preserve the graph/encoding map rather than merging this C6 with a phase group.

**Sources:** [MACRO_EXCERPT](../provenance/excerpts/macro_and_support.md#L1-L10).

---

<a id="census-c4"></a>

## C4 tetravalent census catalogue prefix

**Stable ID:** `census-c4`  
**Historical labels / lookup forms:** `C4[120,38]`, `C4[60,4]`, `C4`  
**Kind:** catalogue namespace  
**Domain:** Census identifiers for graphs  
**Standing:** Naming/type convention from source catalogue usage.

C4 in a bracketed census identifier is part of the catalogue name. The bracket arguments and linked graph determine the object. It is not a four-element cyclic group.

```text
C4[n,index]
```

**Keep distinct:** Never normalize catalogue C4[n,i] into group C_4.

**Sources:** [COVER](../provenance/inputs/draft6/sections/01B_common_cover.tex#L1-L101).

---

<a id="k120-group-locator"></a>

## 201EZ order-120 classification locator

**Stable ID:** `k120-group-locator`  
**Historical labels / lookup forms:** `K120`  
**Kind:** unresolved source-linked label  
**Domain:** Referenced project41_K120_C2xA5_classification_receipt_201ez  
**Standing:** Source-locator-only; no object identity assigned.

The face-field checkpoint refers to a K120 classification with C2xA5 in its filename. The full 201EZ payload is not in the recovered source corpus. Retain a separate locator bin rather than silently identify it with the common-cover graph or signed-axis group.

```text
Source key K120_classification -> ...201ez.v1.json
```

**Keep distinct:** Exact referent, action and identity with any120element group require the missing source.

**Recorded relationships:** [k120-common-cover](#k120-common-cover) (unresolved name collision).

**Sources:** [FACE](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_face_field_higgs_bridge_checkpoint_receipt_201fk.v1.json#L1-L144).

---

<a id="section-frame-contrast"></a>

# Operators, indexed variables, and readouts

<a id="frame-contrast"></a>

## Five-frame golden contrast operator

**Stable ID:** `frame-contrast`  
**Historical labels / lookup forms:** `K5`, `K_5`  
**Kind:** linear operator  
**Domain:** Nontrivial frame harmonics of the registered G9000 carrier  
**Standing:** Exact algebra conditional on declared S; native/current-to-history binding open.

The contrast polynomial in the pure frame shift. Its square is5times the event projector, not5I on the whole9000space.

```text
K5_frame=S+S^-1-S^2-S^-2; K5_frame^2=5P_evt
```

**Keep distinct:** Candidate native bridge remains open; not the historical-register contrast by state identity.

**Recorded relationships:** [history-fivefold-contrast](#history-fivefold-contrast) (same formal group ring polynomial).

**Sources:** [CHAT](../provenance/excerpts/current_chat_archive.md#L1-L21), [CORE](../provenance/inputs/qr_core_terms_consolidated.md#L1-L3141).

---

<a id="history-fivefold-contrast"></a>

## Historical-register golden contrast operator

**Stable ID:** `history-fivefold-contrast`  
**Historical labels / lookup forms:** `K5`, `K_5`  
**Kind:** linear operator  
**Domain:** Representation of the historical D5 rotation s  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The same formal group-ring expression evaluated in the historical fivefold representation. Sharing the polynomial with the frame operator yields an algebraic template, not a native carrier identification.

```text
K5_history=s+s^-1-s^2-s^-2
```

**Keep distinct:** Keep distinct until the historical s and frame S have an explicit compatible action map.

**Recorded relationships:** [frame-contrast](#frame-contrast) (same formal group ring polynomial).

**Sources:** [HISTORICAL_FIVEFOLD](../provenance/excerpts/historical_fivefold.md#L1-L9).

---

<a id="frame-difference"></a>

## Real five-frame oriented difference operator

**Stable ID:** `frame-difference`  
**Historical labels / lookup forms:** `D5`, `D_5`  
**Kind:** real linear operator  
**Domain:** R^1800 tensor R[C5] in the frame proposal  
**Standing:** Conditional frame-algebra construction.

The skew-symmetric difference of forward and inverse pure frame shifts. Its kernel is the common frame mode; it is not a dihedral group.

```text
D5_frame=S-S^-1; D5_frame^T=-D5_frame
```

**Keep distinct:** Not operational information current merely because the archive calls it a current. A norm-square readout still needs its own measure/instrument justification.

**Recorded relationships:** [frame-hermitian-current](#frame-hermitian-current) (scalar complexification relation).

**Sources:** [CHAT](../provenance/excerpts/current_chat_archive.md#L1-L21), [CORE](../provenance/inputs/qr_core_terms_consolidated.md#L1-L3141).

---

<a id="frame-hermitian-current"></a>

## Hermitian five-frame current operator

**Stable ID:** `frame-hermitian-current`  
**Historical labels / lookup forms:** `H5`, `H_5`  
**Kind:** complex linear operator  
**Domain:** Complexification of the five-frame carrier  
**Standing:** Conditional frame-algebra construction.

The operator iD5, self-adjoint in the declared complexification. Complexification resolves current-sign character modes without changing the real Gram norm.

```text
H5_frame=i(S-S^-1); H5_frame^2=D5_frame^T D5_frame
```

**Keep distinct:** Not H5 as a fifth isotropy subgroup or a five-dimensional history.

**Recorded relationships:** [frame-difference](#frame-difference) (scalar complexification relation).

**Sources:** [CHAT](../provenance/excerpts/current_chat_archive.md#L1-L21), [CORE](../provenance/inputs/qr_core_terms_consolidated.md#L1-L3141).

---

<a id="frame-golden-involution"></a>

## Normalized five-frame golden involution

**Stable ID:** `frame-golden-involution`  
**Historical labels / lookup forms:** `J5`, `J_5`  
**Kind:** linear operator  
**Domain:** Event subspace only  
**Standing:** Conditional frame-algebra construction.

The contrast divided by sqrt5. It squares to the event projector on the full carrier and to identity only after restriction.

```text
J5=K5/sqrt5; J5^2=P_evt
```

**Keep distinct:** Not the skew complex structure J_F, whose square is -I.

**Sources:** [CHAT](../provenance/excerpts/current_chat_archive.md#L1-L21), [CORE](../provenance/inputs/qr_core_terms_consolidated.md#L1-L3141).

---

<a id="frame-current-sign"></a>

## Five-frame conjugate-mode sign observable

**Stable ID:** `frame-current-sign`  
**Historical labels / lookup forms:** `R5`, `R_5`  
**Kind:** spectral sign operator  
**Domain:** Complex event harmonics  
**Standing:** Conditional spectral construction; native outcome readout open.

The sign of H5 distinguishes the two complex-conjugate modes within each golden sector. It commutes with J5. Defining it on the zero mode requires a separate convention, so its stated domain is the event sector.

```text
R5=sgn(H5); R5^2=P_evt
```

**Keep distinct:** Not real5space R^5; not the reverse relation family R_c.

**Recorded relationships:** [frame-sign-values](#frame-sign-values) (eigenvalue readout).

**Sources:** [CHAT](../provenance/excerpts/current_chat_archive.md#L1-L21), [CORE](../provenance/inputs/qr_core_terms_consolidated.md#L1-L3141).

---

<a id="frame-multiplier"></a>

## Five-frame index-doubling permutation

**Stable ID:** `frame-multiplier`  
**Historical labels / lookup forms:** `U2`, `U_2`  
**Kind:** coordinate permutation  
**Domain:** The frame residue f in Z5, with internal x retained  
**Standing:** Candidate coordinate action; native admission open.

The multiplier f->2f is a permutation of frame coordinates and conjugates S to S^2. It is not U(2), and native admissibility as a groupoid operation has not been certified here.

```text
U2(f,x)=(2f mod5,x)
```

**Keep distinct:** Not the derived involution Z5 or a selected registered step F.

**Recorded relationships:** [frame-sector-exchange](#frame-sector-exchange) (piecewise operator construction); [u2-face-envelope](#u2-face-envelope) (permutation vs continuous group).

**Sources:** [CHAT](../provenance/excerpts/current_chat_archive.md#L1-L21), [CORE](../provenance/inputs/qr_core_terms_consolidated.md#L1-L3141).

---

<a id="frame-sector-exchange"></a>

## Piecewise five-frame golden-sector exchange

**Stable ID:** `frame-sector-exchange`  
**Historical labels / lookup forms:** `Z5`, `Z_5`  
**Kind:** linear involution construction  
**Domain:** The frame event subspace with P+ and P-  
**Standing:** Conditional operator construction; native provenance open.

The piecewise use of U2 in one direction and U2 inverse in the other creates an involution exchanging golden sectors. It is neither the raw multiplier nor the residue group Z_5.

```text
Z5=P- U2 P+ + P+ U2^-1 P-; Z5 J5=-J5 Z5
```

**Keep distinct:** Matching history Clifford relations is not the native history intertwiner.

**Recorded relationships:** [frame-multiplier](#frame-multiplier) (piecewise operator construction); [residue-spaces](#residue-spaces) (operator vs residue group).

**Sources:** [CHAT](../provenance/excerpts/current_chat_archive.md#L1-L21), [CORE](../provenance/inputs/qr_core_terms_consolidated.md#L1-L3141).

---

<a id="frame-common-projector"></a>

## Frame-common zero-current projector

**Stable ID:** `frame-common-projector`  
**Historical labels / lookup forms:** `P0`, `P_0`  
**Kind:** orthogonal projector  
**Domain:** Full9000dimensional frame representation  
**Typed size:** Projector rank: 1800; Ambient real carrier dimension: 9000  
**Standing:** Conditional frame representation.

The average of the five pure shifts projects onto vectors constant in the frame coordinate. Its rank is1800 in the proposed full carrier.

```text
P0=(I+S+S^2+S^3+S^4)/5
```

**Keep distinct:** P0 is an operator, not an1800element subset or a physical observer.

**Recorded relationships:** [p01-line-partitions](#p01-line-partitions) (partition vs projector).

**Sources:** [CHAT](../provenance/excerpts/current_chat_archive.md#L1-L21), [CORE](../provenance/inputs/qr_core_terms_consolidated.md#L1-L3141).

---

<a id="frame-harmonic-72"></a>

## Seventy-two-degree real frame harmonic

**Stable ID:** `frame-harmonic-72`  
**Historical labels / lookup forms:** `V72`, `V_72`  
**Kind:** real representation plane  
**Domain:** Real regular C5 module before internal multiplicity  
**Typed size:** Real dimension: 2  
**Standing:** Conditional C5 harmonic notation.

The conjugate character pair {1,4} forms a real2plane. The72label is an angle; after tensoring withR1800 its real dimension is3600.

```text
V72: k=1,4
```

**Keep distinct:** The subscript is not the dimension72 or an axis index.

**Sources:** [CHAT](../provenance/excerpts/current_chat_archive.md#L1-L21).

---

<a id="frame-harmonic-144"></a>

## One-hundred-forty-four-degree real frame harmonic

**Stable ID:** `frame-harmonic-144`  
**Historical labels / lookup forms:** `V144`, `V_144`  
**Kind:** real representation plane  
**Domain:** Real regular C5 module before internal multiplicity  
**Typed size:** Real dimension: 2  
**Standing:** Conditional C5 harmonic notation.

The conjugate pair{2,3} forms the other real2plane, with full-carrier multiplicity1800.

```text
V144: k=2,3
```

**Keep distinct:** Not a144state set or144dimensional independent carrier.

**Sources:** [CHAT](../provenance/excerpts/current_chat_archive.md#L1-L21).

---

<a id="frame-character-blocks"></a>

## Complex five-frame character block family

**Stable ID:** `frame-character-blocks`  
**Historical labels / lookup forms:** `E1`, `E2`, `E3`, `E4`, `E_1`, `E_2`, `E_3`, `E_4`  
**Kind:** complex invariant subspaces  
**Domain:** Complexified C5 frame representation  
**Typed size:** Complex dimension: 1800  
**Family parameters:** k=1,2,3,4; stated dimension on full frame carrier  
**Standing:** Conditional frame representation.

The four nontrivial characters are distinct complex one-dimensional modules before internal multiplicity and complex 1,800-dimensional blocks afterward. Conjugate pairs form the two real harmonic sectors. These subspaces are not automatically four real outcome-state sets.

```text
E_k: S eigenvalue exp(2*pi*i*k/5); k=1,2,3,4
```

**Keep distinct:** Do not merge E2 with the native face E2 real representation plane, with a generic event E_2, or with the equation file E02.

**Sources:** [CHAT](../provenance/excerpts/current_chat_archive.md#L1-L21).

---

<a id="history-clifford-j2"></a>

## Two-by-two signed history-sheet phase matrix

**Stable ID:** `history-clifford-j2`  
**Historical labels / lookup forms:** `J2`, `J_2`  
**Kind:** real matrix  
**Domain:** Sheet factor in the reported full history/analyzer chart  
**Typed size:** Real dimension: 2  
**Standing:** Explicit matrix; full native-action placement is conversation-reported.

The explicit square-minus-identity matrix used in the reported history-sheet factor. Its formula is unambiguous. Its placement in the newest full native action and the associated cocycle cancellation remains conversation-reported pending the original producer/action tables.

```text
J2=[[0,1],[-1,0]]; J2^2=-I2
```

**Keep distinct:** Not the two-state history alphabet, the normalized frame J5, or a canonical identification of every real complex structure.

**Sources:** [CHAT](../provenance/excerpts/current_chat_archive.md#L1-L21), [CORE](../provenance/inputs/qr_core_terms_consolidated.md#L1-L3141).

---

<a id="g1800-operator"></a>

## Registered native product quarter-turn operator

**Stable ID:** `g1800-operator`  
**Historical labels / lookup forms:** `K1800`, `K_1800`, `K`  
**Kind:** permutation / induced linear operator  
**Domain:** One G1800 ordered deck registration  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The actual map descending from(u,v)->(ab(v),b(u)) in the source registration. An operator, its generated C4 group and its orbits are separate views.

```text
K^2=Delta_1800; K^4=I
```

**Keep distinct:** Do not treat K and G1800 as aliases; one acts on the other.

**Sources:** [FRAMES](../provenance/inputs/native_g9000_map_test.md#L1-L295).

---

<a id="fusion-adjacencies"></a>

## Icosahedral fused distance adjacency matrices

**Stable ID:** `fusion-adjacencies`  
**Historical labels / lookup forms:** `A0`, `A1`, `A2`, `A3`, `A_0`, `A_1`, `A_2`, `A_3`  
**Kind:** matrix family  
**Domain:** The twelve-point relational-kernel carrier  
**Family parameters:** distance index0..3  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The four graph-distance matrices formed by the specified fusion of the eight colored relations. Index zero denotes the identity relation; indices one to three denote graph distance. These are actual matrices on the twelve-point kernel carrier.

```text
A0=A_T0; A1=A_Tu+A_F0+A_R0; A2=A_Tv+A_F1+A_R1; A3=A_Tu+v
```

**Keep distinct:** A3 here is a distance-three matrix, not the alternating group A3 or the A3 root-system target.

**Sources:** [KERNEL](../provenance/inputs/draft6/sections/01C_relational_kernel.tex#L1-L68).

---

<a id="binary-analyzer-local"></a>

## Local binary analyzer observable families

**Stable ID:** `binary-analyzer-local`  
**Historical labels / lookup forms:** `A0`, `A1`, `B0`, `B1`, `A_0`, `A_1`, `B_0`, `B_1`  
**Kind:** observable / response family  
**Domain:** Alice and Bob settings in their explicitly represented experiment  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The setting-indexed local observable or classical response families in a CHSH comparison. Classical functions of hidden history and quantum operators are different implementations; keep that representation qualification.

```text
A_i; B_j; CHSH=A0(B0+B1)+A1(B0-B1)
```

**Keep distinct:** Do not identify A0,A1 with fusion matrices or face-circle generators. A local operator is not an admitted physical instrument by notation.

**Sources:** [EPR](../provenance/inputs/native_epr_history_control.md#L1-L74), [MEASURE](../provenance/inputs/draft6/sections/05_measure_registration.tex#L1-L57).

---

<a id="anchor-circle-generators"></a>

## Event-anchor circle Lie generators

**Stable ID:** `anchor-circle-generators`  
**Historical labels / lookup forms:** `A0`, `A1`, `A_0`, `A_1`  
**Kind:** Lie-algebra operator pair  
**Domain:** Two positive event vectors in the complex face doublet  
**Typed size:** Real dimension: 2  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The two point-stabilizer circles have generators A0 and A1. Their sum is centralJ and difference is the event-defined neutralSU2axisT. These are not the two EPR settings.

```text
A0=(J-T)/2; A1=(J+T)/2
```

**Keep distinct:** The source has no physical coupling metric or hypercharge identification.

**Sources:** [CIRCLES](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_positive_pair_hermitian_geometry_201fv.v1.json#L1-L116), [NEUTRAL](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_neutral_generator_anatomy_201fw.v1.json#L1-L152), [REFLECTION](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_selected_reflection_event_pauli_anatomy_201h67b.v1.json#L1-L41).

---

<a id="quaternionic-face-axes"></a>

## Derived quaternionic face-axis generators

**Stable ID:** `quaternionic-face-axes`  
**Historical labels / lookup forms:** `K1`, `K2`, `K3`, `K_1`, `K_2`, `K_3`  
**Kind:** operator-frame family  
**Domain:** Derived su(2)-type part of the face U(2) envelope  
**Family parameters:** i=1,2,3  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

Three native derived axes in the face-envelope calculation, normalized as T_i=K_i/2. Their labels are not complete graphs or equation tags.

```text
K1,K2,K3; T_i=K_i/2; Casimir=3/4
```

**Keep distinct:** No identification with physical weak isospin or a measured spatial frame follows.

**Sources:** [CONNECTION](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_u2_gauge_bridge_connection_frontier_checkpoint_201fp7.v1.json#L1-L190), [NEUTRAL](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_neutral_generator_anatomy_201fw.v1.json#L1-L152).

---

<a id="quaternionic-normalized-generators"></a>

## Normalized derived face Lie generators

**Stable ID:** `quaternionic-normalized-generators`  
**Historical labels / lookup forms:** `T1`, `T2`, `T3`, `T_1`, `T_2`, `T_3`  
**Kind:** Lie-generator family  
**Domain:** Same face-derived su(2) module  
**Family parameters:** i=1,2,3  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The half-scaled generators associated with the K_i operator frame. Scaling is an explicit relation, not an alias that can be used interchangeably in formulas.

```text
T_i=K_i/2
```

**Keep distinct:** Not macro T10/T12 or kernel translation T0.

**Sources:** [CONNECTION](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_u2_gauge_bridge_connection_frontier_checkpoint_201fp7.v1.json#L1-L190), [NEUTRAL](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_neutral_generator_anatomy_201fw.v1.json#L1-L152).

---

<a id="kernel-forward"></a>

## Forward binary relations of the normalized kernel

**Stable ID:** `kernel-forward`  
**Historical labels / lookup forms:** `F0`, `F1`, `F_0`, `F_1`  
**Kind:** binary relation / adjacency family  
**Domain:** Ordered cross-cell pairs of X12_kernel  
**Family parameters:** c=0,1  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The binary index c records a constraint between a source first bit and target second bit while the cell index advances. Each source retains multiple allowed targets. This is a relation and its adjacency matrix, not a uniquely chosen execution.

```text
F_c: i->i+1 and x1+y2=c
```

**Keep distinct:** Not a power of F_reg, a chronological event, or the F1/F2 equation-tag family.

**Sources:** [KERNEL](../provenance/inputs/draft6/sections/01C_relational_kernel.tex#L1-L68).

---

<a id="kernel-reverse"></a>

## Reverse binary relations of the normalized kernel

**Stable ID:** `kernel-reverse`  
**Historical labels / lookup forms:** `R0`, `R1`, `R_0`, `R_1`  
**Kind:** binary relation / adjacency family  
**Domain:** Ordered cross-cell pairs of X12_kernel  
**Family parameters:** c=0,1  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The reverse direction uses the source second bit and target first bit. Its adjacency matrix is the transpose of the corresponding forward matrix. Relation reversal has not been identified with the separate point action called Mode.

```text
R_c=F_c^T
```

**Keep distinct:** R1 is not primitive winding class r1, the native exchange-square residual, or a real one-dimensional space.

**Sources:** [KERNEL](../provenance/inputs/draft6/sections/01C_relational_kernel.tex#L1-L68).

---

<a id="kernel-identity-relation"></a>

## Within-cell identity translation relation

**Stable ID:** `kernel-identity-relation`  
**Historical labels / lookup forms:** `T0`, `T_0`  
**Kind:** binary relation / identity matrix  
**Domain:** Diagonal pairs of X12_kernel  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The identity member of the four within-cell translation relations. Every point is related to itself, and the corresponding adjacency matrix is identity on the twelve-point function space.

```text
T0={((i,x),(i,x))}
```

**Keep distinct:** Not the T10 macro transport, an initial event, or a time origin.

**Sources:** [KERNEL](../provenance/inputs/draft6/sections/01C_relational_kernel.tex#L1-L68).

---

<a id="cochain-coboundaries"></a>

## Discrete cochain incidence/coboundary operators

**Stable ID:** `cochain-coboundaries`  
**Historical labels / lookup forms:** `D0`, `D1`, `D2`, `D_0`, `D_1`, `D_2`  
**Kind:** linear map family  
**Domain:** A specified cell complex in the discrete Maxwell comparison  
**Family parameters:** k and the actual cochain complex  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The incidence or coboundary maps connecting successive cochain degrees in the separately declared discrete Maxwell comparison. Their composition vanishes on the specified chain complex. Matrix conventions, dimensions and the cell complex are part of each instance.

```text
D_(k+1) D_k = 0 for composable cochain degrees
```

**Keep distinct:** Not dihedral groups, the frame D5 current, or the scalar face disagreement D2.

**Recorded relationships:** [face-disagreement](#face-disagreement) (linear map vs scalar functional).

**Sources:** [MAXWELL](../provenance/inputs/draft6/sections/09C_maxwell.tex#L1-L93).

---

<a id="face-disagreement"></a>

## Six-face quadratic disagreement scalar

**Stable ID:** `face-disagreement`  
**Historical labels / lookup forms:** `D2`  
**Kind:** scalar functional  
**Domain:** Binary six-face field and continuous R^6 lift  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The six-face alignment measure defined from the native phase pair. On binary fields it counts pairwise disagreements; the source gives its transverse quadratic rendering in a continuous real six-dimensional lift. Here the digit two is associated with quadratic degree.

```text
D2(x) = sum_(i<j) (1-s_i s_j x_i x_j)/2 = (3/2) x^T P_perp x
```

**Keep distinct:** Not the Maxwell degree-two incidence map. The continuous potential does not by itself supply physical energy.

**Recorded relationships:** [cochain-coboundaries](#cochain-coboundaries) (linear map vs scalar functional).

**Sources:** [FACE](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_face_field_higgs_bridge_checkpoint_receipt_201fk.v1.json#L1-L144).

---

<a id="analyzer-z3"></a>

## Three-dimensional canonical analyzer Z reflection

**Stable ID:** `analyzer-z3`  
**Historical labels / lookup forms:** `Z3`, `Z_3`  
**Kind:** real 3-by-3 matrix  
**Domain:** A native analyzer character mode  
**Typed size:** Real dimension: 3  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The canonical real three-by-three binary analyzer reflection with one positive and two negative eigenvalues. It acts on a chosen three-dimensional native character mode and is one member of a fixed distinct-axis pair normal form.

```text
Z3=diag(1,-1,-1)
```

**Keep distinct:** Not the residue group Z_3. Its matrix size does not imply a three-element action.

**Sources:** [EPR](../provenance/inputs/native_epr_history_control.md#L1-L74), [HISTORICAL_FIVEFOLD](../provenance/excerpts/historical_fivefold.md#L1-L9).

---

<a id="analyzer-r3"></a>

## Three-dimensional canonical analyzer R reflection

**Stable ID:** `analyzer-r3`  
**Historical labels / lookup forms:** `R3`, `R_3`  
**Kind:** real 3-by-3 matrix  
**Domain:** The second analyzer in a canonical distinct-axis pair  
**Typed size:** Real dimension: 3  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The second rational reflection in the canonical distinct-axis pair. Its noncommutation with Z3 is part of the represented analyzer calculation. The operator and its real three-dimensional domain require separate names.

```text
R3=[[-3/5,4/5,0],[4/5,3/5,0],[0,0,-1]]
```

**Keep distinct:** Not the scalar vector space R^3 or the reverse relation R_c.

**Sources:** [EPR](../provenance/inputs/native_epr_history_control.md#L1-L74), [HISTORICAL_FIVEFOLD](../provenance/excerpts/historical_fivefold.md#L1-L9).

---

<a id="causal-golden-b"></a>

## Integral causal-current square-five operator pair

**Stable ID:** `causal-golden-b`  
**Historical labels / lookup forms:** `B1`, `B2`, `B_1`, `B_2`  
**Kind:** integral operator pair  
**Domain:** Causal-current lattice with S5 action  
**Standing:** Source-reported operator pair with original matrix recovery pending.

The integrated draft reports two integral operators in the causal-current commutant, both squaring to five times identity. A rational S5-module crosswalk does not identify their integral lattice with the golden-period lattice; the source reports an index-32 integral embedding instead.

```text
B1^2=B2^2=5I
```

**Keep distinct:** The original operator matrices and producer are not included in the retrieved excerpt. No fresh lattice calculation is claimed.

**Sources:** [GOLDEN_LATTICE](../provenance/excerpts/golden_lattice.md#L1-L9).

---

<a id="s1-residual-reflection"></a>

## Connection-selected anti-complex face reflection

**Stable ID:** `s1-residual-reflection`  
**Historical labels / lookup forms:** `S1`, `S_1`  
**Kind:** involutory operator  
**Domain:** Four-state face basis / event-adapted complex doublet  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The explicitly selected permutation (1,0,3,2) generating the last connection-residual ambiguity. In the event-adapted complex doublet it is sigma_x followed by complex conjugation. A signed event selects one transport in the torsor; it does not make the residual generator equal that transport.

```text
S1=(1,0,3,2); S1=sigma_x K_conj; S1^2=I
```

**Keep distinct:** Not the circle S^1, the phase coset S_1, the bundle residual r1, or the selected transport T.

**Recorded relationships:** [circle-space](#circle-space) (operator vs circle); [r1-native-residual](#r1-native-residual) (fiber actor vs base bundle action).

**Sources:** [RESIDUAL](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_signed_event_s1_torsor_selector_201h65b.v1.json#L1-L42), [REFLECTION](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_selected_reflection_event_pauli_anatomy_201h67b.v1.json#L1-L41).

---

<a id="s2-twin-reflection"></a>

## L-twisted companion face reflection

**Stable ID:** `s2-twin-reflection`  
**Historical labels / lookup forms:** `S2`, `S_2`  
**Kind:** involutory operator  
**Domain:** Same four-state face basis asS1  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The companion permutation (2,3,0,1), obtained as L S1 with L=(3,2,1,0). The source distinguishes it from S1 and says it does not occur as the actual residual in the tested connection selector.

```text
S2=L S1
```

**Keep distinct:** Do not merge it with S1 because both are involutory or anti-complex.

**Sources:** [RESIDUAL](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_signed_event_s1_torsor_selector_201h65b.v1.json#L1-L42).

---

<a id="phase-cosets"></a>

## Four registered history-phase coset objects

**Stable ID:** `phase-cosets`  
**Historical labels / lookup forms:** `S0`, `S1`, `S2`, `S3`, `S_0`, `S_1`, `S_2`, `S_3`  
**Kind:** coset object family  
**Domain:** X=Gamma_hist/H0  
**Typed size:** Point/object count: 4  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The four phase objects r^k H0 in the specified left-coset space. Their phase cycle has period four, while the listed embedded isotropy and word-generator family has period two. Each coset is an object, not a reflection matrix.

```text
S_k=r^kH0; k=0..3
```

**Keep distinct:** S_1 and S_2 here are cosets, not the face operators. Selecting S_0 marks an origin but does not make that marking invariant.

**Sources:** [HISTORY_PHASE](../provenance/inputs/draft6/sections/03F_history_phase_groupoid.tex#L1-L66).

---

<a id="r1-native-residual"></a>

## Selected native exchange-square residual

**Stable ID:** `r1-native-residual`  
**Historical labels / lookup forms:** `r1`, `r_1`, `rho1`, `rho_1`  
**Kind:** native permutation  
**Domain:** Aut(G60) cache index2 in the supplied exchange source  
**Typed size:** Group order: 2  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The selected native order-two permutation at cache index 2, equal to the square of cache[3]. Its face-bundle action has a nontrivial base permutation and a chart-dependent local compatibility cocycle. The source explicitly distinguishes it from a purely vertical S1.

```text
r1_native=g^2; g=cache[3]; r1=cache[2]
```

**Keep distinct:** Not the primitive homology class r1 or the first event receipt. The source records r1_equals_vertical_S1=false.

**Recorded relationships:** [s1-residual-reflection](#s1-residual-reflection) (fiber actor vs base bundle action); [r1-history-class](#r1-history-class) (permutation vs homology class).

**Sources:** [BUNDLE](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_r1_face_bundle_cocycle_triviality_201h69g.v1.json#L1-L50), [CARTAN](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_order4_square_cartan_orientation_201h35b.v1.json#L1-L99).

---

<a id="r1-history-class"></a>

## Primitive registered-history winding class

**Stable ID:** `r1-history-class`  
**Historical labels / lookup forms:** `r1`, `r_1`  
**Kind:** homology generator/class  
**Domain:** The declared registered-history domain  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The distinguished primitive class in the declared registered-history construction. Thalean time is its additive oriented winding. A homology generator and a native permutation with the same display name are not the same type of object.

```text
tau_Th(gamma)=wind_(r1_history)(gamma)
```

**Keep distinct:** Not automatically W4/2 on a different presentation. Do not assign a native permutation-cache index to the homology class.

**Recorded relationships:** [r1-native-residual](#r1-native-residual) (permutation vs homology class); [w4-winding](#w4-winding) (different winding domains); [history-primitive-family](#history-primitive-family) (selected family member).

**Sources:** [CORE](../provenance/inputs/qr_core_terms_consolidated.md#L1-L3141), [BASE](../provenance/inputs/qr_core_terms_original.md#L1-L1982).

---

<a id="r-indexed-receipts"></a>

## Indexed event receipt variables

**Stable ID:** `r-indexed-receipts`  
**Historical labels / lookup forms:** `r1`, `r2`, `r_1`, `r_2`  
**Kind:** indexed data family  
**Domain:** Ordered transduction history  
**Family parameters:** i = event position  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The baseline uses r_i or rho_i for successive individual receipts in an event history. These are chronology-indexed data, not group orders or names of a universal primitive class.

```text
(e1,r1) o (e2,r2) ...
```

**Keep distinct:** Do not compare r1_receipt with r1_native or r1_history solely through their spelling.

**Sources:** [BASE](../provenance/inputs/qr_core_terms_original.md#L1-L1982).

---

<a id="w4-winding"></a>

## Companion four-generator additive winding cochain

**Stable ID:** `w4-winding`  
**Historical labels / lookup forms:** `W4`, `W_4`  
**Kind:** integral 1-cochain  
**Domain:** Four-generator cellular history presentation  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The primitive integral cochain (1,1,1,1) on the specified four-generator companion presentation. It annihilates its defining relations. On the even-history cover it equals twice a primitive integer cochain plus an exact endpoint term.

```text
W4 = 2 N + d h; on closed histories W4(gamma) = 2 N(gamma)
```

**Keep distinct:** The source explicitly does not identify N with original Project 41 tau_T on arbitrary histories.

**Recorded relationships:** [r1-history-class](#r1-history-class) (different winding domains).

**Sources:** [WINDING](../provenance/inputs/PHASE_RELATION_CELLULAR_PROOF.md#L1-L392).

---

<a id="w5-transverse"></a>

## Transverse five-dimensional six-face field sector

**Stable ID:** `w5-transverse`  
**Historical labels / lookup forms:** `W5`, `W_5`  
**Kind:** real invariant subspace  
**Domain:** Continuous R^6 lift of the six-face order field  
**Typed size:** Real dimension: 5  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The real five-dimensional complement to the one-dimensional phase line in the continuous lift of the six-face order field. Its label records a representation dimension, not five frame states or a fivefold cyclic action.

```text
R^6 = L_phase direct_sum W5
```

**Keep distinct:** No physical Higgs, Goldstone-mode, or energy interpretation is promoted.

**Sources:** [FACE](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_face_field_higgs_bridge_checkpoint_receipt_201fk.v1.json#L1-L144).

---

<a id="e2-face-plane"></a>

## Real irreducible face plane

**Stable ID:** `e2-face-plane`  
**Historical labels / lookup forms:** `E2`, `E_2`  
**Kind:** real representation component  
**Domain:** Four-mode face representation 1 + chi_face + E2  
**Typed size:** Real dimension: 2; Complex dimension: 1  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The real two-dimensional irreducible component in the four-mode face representation 1 + chi_face + E2. After a complex-orientation choice it is a complex line. Under full local D8 its conjugation character differs from that of the scalar plane.

```text
V_face = 1 direct_sum chi_face direct_sum E2
```

**Keep distinct:** Not the complex frame character block E_2 or equation E02. The full D8 action does not yield the claimed common semilinear doublet without the specified restriction.

**Sources:** [FACE](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_face_field_higgs_bridge_checkpoint_receipt_201fk.v1.json#L1-L144).

---

<a id="reference-lines"></a>

## Reference-gauge projective analyzer line labels

**Stable ID:** `reference-lines`  
**Historical labels / lookup forms:** `L0`, `L1`, `L_0`, `L_1`  
**Kind:** projective-line pair  
**Domain:** Selected reference gauge in CP^1  
**Typed size:** Point/object count: 2  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The two projective analyzer lines named L0 and L1 after choosing a reference gauge. The original Program 2 source describes the codomain as a two-line subset of CP1. These labels identify lines, not oriented vector representatives.

```text
{L0,L1} subset CP1
```

**Keep distinct:** No automatic identification with the two inert complex lines L1,L2 in the separate charge-Cartan construction. A line alone is not a signed observable.

**Sources:** [LINES](../provenance/inputs/draft6/provenance/draft6/native_snapshot/program02/artifacts/json/epr_reference_gauge_projective_line_map_018.v1.json#L1-L775), [PARTITIONS](../provenance/inputs/draft6/provenance/draft6/native_snapshot/program02/artifacts/json/epr_native_face_projective_line_partition_017.v1.json#L1-L566).

---

<a id="cartan-inert-lines"></a>

## Ordered inert complex lines in the charge-Cartan sector

**Stable ID:** `cartan-inert-lines`  
**Historical labels / lookup forms:** `L1`, `L2`, `L_1`, `L_2`  
**Kind:** complex subspace pair  
**Domain:** Q_tau complement in the specified C^4 comparison  
**Typed size:** Complex dimension: 1  
**Family parameters:** two separate lines in Q_tau  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The two ordered inert complex lines in the Q_tau complement of the specified four-complex-dimensional representation. The selected square orders them in that construction. This is a different pair from the reference-gauge analyzer lines L0,L1.

```text
Y=q_D P_tau+q1 Pi1+q2 Pi2
```

**Keep distinct:** The coefficients q1,q2 remain unassigned. No Standard Model charge or face-to-spin axis identification follows.

**Sources:** [CARTAN](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_order4_square_cartan_orientation_201h35b.v1.json#L1-L99).

---

<a id="cartan-charge-coefficients"></a>

## Unassigned inert-line charge coefficients

**Stable ID:** `cartan-charge-coefficients`  
**Historical labels / lookup forms:** `q1`, `q2`, `q_1`, `q_2`  
**Kind:** scalar parameter pair  
**Domain:** Three-parameter charge algebra in theC^4comparison  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The two free scalar coefficients multiplying the inert singlet-line projectors in the displayed charge algebra. They are parameters rather than vertex addresses, history bits, or already determined physical charges.

```text
Y=q_D P_tau+q1 Pi1+q2 Pi2
```

**Keep distinct:** Do not supply numerical hypercharges that the source leaves unassigned.

**Sources:** [CARTAN](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_order4_square_cartan_orientation_201h35b.v1.json#L1-L99).

---

<a id="correlation-entries"></a>

## Setting-pair correlation table entries

**Stable ID:** `correlation-entries`  
**Historical labels / lookup forms:** `E00`, `E01`, `E10`, `E11`, `E_00`, `E_01`, `E_10`, `E_11`  
**Kind:** indexed scalar readout  
**Domain:** Two-wing measurement context (i,j)  
**Family parameters:** ordered setting pair(i,j)  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The correlation expectation indexed by an ordered pair of settings. The two digits carry separate local-setting information. Leading zeros must be preserved: E01 is not automatically the same label as E1.

```text
E_ij = expectation[a b | i,j]
```

**Keep distinct:** Distinguish the mathematical correlation E_01 from the equation-file locator E01 using the occurrence context.

**Sources:** [EPR](../provenance/inputs/native_epr_history_control.md#L1-L74), [MEASURE](../provenance/inputs/draft6/sections/05_measure_registration.tex#L1-L57).

---

<a id="identity-matrices"></a>

## Identity operator family with domain size

**Stable ID:** `identity-matrices`  
**Historical labels / lookup forms:** `I1`, `I2`, `I3`, `I4`, `I6`, `I12`, `I20`, `I30`, `I60`, `I600`, `I_2`, `I_6`, `I_12`  
**Kind:** parametric matrix family  
**Domain:** Declared vector space of dimension n  
**Family parameters:** dimension n; scalar field; carrier  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The identity operator on a declared vector space. Its numeric suffix specifies matrix size, not an independent native object. An identity acting on a sheet factor and one acting on a spinor factor can have the same matrix while retaining different roles.

```text
I_(n,domain) v=v
```

**Keep distinct:** Annotate field and carrier, particularly for I2. Equal-size identities do not provide a map between the underlying native domains.

**Recorded relationships:** [inertia-moments](#inertia-moments) (physical parameter vs identity matrix).

**Sources:** [CHAT](../provenance/excerpts/current_chat_archive.md#L1-L21), [MEASURE](../provenance/inputs/draft6/sections/05_measure_registration.tex#L1-L57), [CARTAN](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_order4_square_cartan_orientation_201h35b.v1.json#L1-L99).

---

<a id="section-u2-face-envelope"></a>

# Continuous envelopes, scalar spaces, and homology

<a id="u2-face-envelope"></a>

## Continuous unitary envelope of a selected face complex fiber

**Stable ID:** `u2-face-envelope`  
**Historical labels / lookup forms:** `U2`, `U(2)`, `U_2_envelope`  
**Kind:** continuous matrix group  
**Domain:** Selected face complex fiber: real dimension 4, complex dimension 2  
**Typed size:** Real dimension: 4; Complex dimension: 2  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The continuous group of unitary transformations for the selected face complex structure, with a real four-dimensional / complex two-dimensional fiber. Its Lie algebra has dimension four, one-dimensional center, and three-dimensional derived part. The digit two is complex matrix size.

```text
U(2) ~= (SU(2) x U(1))/C2
```

**Keep distinct:** Not the finite coordinate permutation U_2. The envelope does not establish physical gauge fields or hypercharge.

**Recorded relationships:** [frame-multiplier](#frame-multiplier) (permutation vs continuous group).

**Sources:** [U2](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_event_vector_u2_u1_stabilizer_201ft.v1.json#L1-L71), [CONNECTION](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_u2_gauge_bridge_connection_frontier_checkpoint_201fp7.v1.json#L1-L190), [NEUTRAL](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_neutral_generator_anatomy_201fw.v1.json#L1-L152).

---

<a id="u1-face-center"></a>

## Central face phase circle

**Stable ID:** `u1-face-center`  
**Historical labels / lookup forms:** `U1`, `U(1)`, `U_1_center`  
**Kind:** continuous central subgroup  
**Domain:** Center of faceU(2)  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The common complex-phase circle in the center of the face U(2) envelope. Its primitive Lie direction is J=A0+A1. This embedded circle is not either anchor stabilizer, although all three have abstract circle type.

```text
exp(theta J); J = A0 + A1
```

**Keep distinct:** Keep the continuous circle, Lie generator, and finite quarter-turn subgroup distinct.

**Recorded relationships:** [u1-anchor-first](#u1-anchor-first) (distinct circle subgroups).

**Sources:** [NEUTRAL](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_neutral_generator_anatomy_201fw.v1.json#L1-L152), [CIRCLES](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_positive_pair_hermitian_geometry_201fv.v1.json#L1-L116).

---

<a id="u1-anchor-first"></a>

## First positive-event anchor circle

**Stable ID:** `u1-anchor-first`  
**Historical labels / lookup forms:** `U1`, `U(1)`, `U_1_anchor0`  
**Kind:** continuous point stabilizer  
**Domain:** Face U(2), fixing the first positive event vector  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The point stabilizer fixing the first positive event vector. Its generator A0 is one half of the difference between central J and neutral T. Naming the anchor is necessary to specify the embedded subgroup.

```text
A0=(J-T)/2
```

**Keep distinct:** Not the central U(1) or the second anchor circle. The source reports trivial intersection of the two anchor circles.

**Recorded relationships:** [u1-anchor-second](#u1-anchor-second) (complementary subgroups); [u1-face-center](#u1-face-center) (distinct circle subgroups).

**Sources:** [CIRCLES](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_positive_pair_hermitian_geometry_201fv.v1.json#L1-L116), [NEUTRAL](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_neutral_generator_anatomy_201fw.v1.json#L1-L152).

---

<a id="u1-anchor-second"></a>

## Second positive-event anchor circle

**Stable ID:** `u1-anchor-second`  
**Historical labels / lookup forms:** `U1`, `U(1)`, `U_1_anchor1`  
**Kind:** continuous point stabilizer  
**Domain:** Face U(2), fixing the second positive event vector  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The point stabilizer fixing the second positive event vector. Its generator A1 is one half of the sum of central J and neutral T. Together the two anchor circles generate a maximal U(1) x U(1) torus, not the full U(2).

```text
A1=(J+T)/2
```

**Keep distinct:** Same abstract circle type does not merge the two embedded stabilizers.

**Recorded relationships:** [u1-anchor-first](#u1-anchor-first) (complementary subgroups).

**Sources:** [CIRCLES](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_positive_pair_hermitian_geometry_201fv.v1.json#L1-L116), [NEUTRAL](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_neutral_generator_anatomy_201fw.v1.json#L1-L152).

---

<a id="su2-face-derived"></a>

## Derived face unitary special-unitary envelope

**Stable ID:** `su2-face-derived`  
**Historical labels / lookup forms:** `SU2`, `SU(2)`  
**Kind:** continuous matrix group / Lie algebra view  
**Domain:** Derived part of the face U(2) envelope  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The special-unitary / derived three-generator structure in the chosen face complex-doublet envelope. The source computes quaternionic generator anatomy and normalization. Its Lie algebra, group, and represented operators remain separate views.

```text
T_i = K_i/2; quadratic Casimir = 3/4
```

**Keep distinct:** Not yet physical weak isospin or a unique native Weyl-to-face identification.

**Sources:** [CONNECTION](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_u2_gauge_bridge_connection_frontier_checkpoint_201fp7.v1.json#L1-L190), [NEUTRAL](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_neutral_generator_anatomy_201fw.v1.json#L1-L152).

---

<a id="o2-surface-envelope"></a>

## Orthogonal winding-plane reference-transport envelope

**Stable ID:** `o2-surface-envelope`  
**Historical labels / lookup forms:** `O2`, `O(2)`  
**Kind:** continuous matrix group  
**Domain:** Real local primitive winding planes  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The orthogonal two-plane envelope of the surface reference connection. The tested edge transports lie in a finite D8 subgroup, while the unlifted loop holonomy lies in a V4 subgroup. Ambient envelope, edge-value group, and loop group are distinct.

```text
D8_edge <= O(2); Hol_reference ~= V4
```

**Keep distinct:** No equality of an ambient group with its attained loop holonomy is inferred.

**Recorded relationships:** [rotor-o2](#rotor-o2) (same abstract envelope distinct action).

**Sources:** [SURFACE](../provenance/inputs/README(20260920-001150).md#L1-L300).

---

<a id="circle-space"></a>

## Unit-circle phase space

**Stable ID:** `circle-space`  
**Historical labels / lookup forms:** `S1`, `S^1`  
**Kind:** topological space / group model  
**Domain:** Continuous phase/orientation coordinate when explicitly selected  
**Standing:** Notation convention for the source phase-circle/envelope usage.

The unit-circle model of a continuous phase coordinate when such a coordinate is declared. Its superscript distinguishes it from the finite reflection operator S_1. A chosen phase circle can model U(1), but this is not the same as identifying every object called S1.

```text
S^1={z in C:|z|=1}
```

**Keep distinct:** The fully scanned sources contain phase-circle/envelope usage; no equality to a permutation S1 is intended.

**Recorded relationships:** [s1-residual-reflection](#s1-residual-reflection) (operator vs circle).

**Sources:** [U2](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_event_vector_u2_u1_stabilizer_201ft.v1.json#L1-L71), [CORE](../provenance/inputs/qr_core_terms_consolidated.md#L1-L3141).

---

<a id="real-spaces"></a>

## Real scalar vector-space family

**Stable ID:** `real-spaces`  
**Historical labels / lookup forms:** `R2`, `R3`, `R4`, `R5`, `R6`, `R12`, `R1800`, `R9000`, `R^2`, `R^3`, `R^6`  
**Kind:** scalar-space family  
**Domain:** Declared realcoordinate spaces  
**Family parameters:** n; native or constructed module  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

R^n records scalar field and real dimension. Compressed JSON prose may write R6, but an operator R3 or relation R_1 uses a different convention. Each actual native or constructed vector-space domain still needs its own qualified name.

```text
R^n; dimensionn overR
```

**Keep distinct:** Do not turn a superscript into a subscript. Equal dimensions do not supply a native vector-space identification.

**Sources:** [FACE](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_face_field_higgs_bridge_checkpoint_receipt_201fk.v1.json#L1-L144), [CORE](../provenance/inputs/qr_core_terms_consolidated.md#L1-L3141), [CHAT](../provenance/excerpts/current_chat_archive.md#L1-L21).

---

<a id="complex-spaces"></a>

## Complex scalar vector-space family

**Stable ID:** `complex-spaces`  
**Historical labels / lookup forms:** `C2`, `C4`, `C6`, `C12`, `C^2`, `C^4`, `C^6`  
**Kind:** scalar-space family  
**Domain:** Declared complexification/complexfiber  
**Family parameters:** n; chosen complex structure or complexification  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

C^n is a complex vector space, not the cyclic group C_n. A complex doublet has two complex dimensions and four real dimensions; it is not a two-element state set. A chosen complex structure is additional data on its real carrier.

```text
dim_R C^n=2n
```

**Keep distinct:** Preserve exponent, field, and domain. Complexification does not by itself turn spectral modes into registered physical outcomes.

**Recorded relationships:** [cochain-spaces](#cochain-spaces) (cochain degree vs complex dimension).

**Sources:** [CARTAN](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_order4_square_cartan_orientation_201h35b.v1.json#L1-L99), [U2](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_event_vector_u2_u1_stabilizer_201ft.v1.json#L1-L71), [COMPANION_TRIALITY](../provenance/excerpts/companion_triality.md#L1-L9).

---

<a id="residue-spaces"></a>

## Cyclic residue coordinate family

**Stable ID:** `residue-spaces`  
**Historical labels / lookup forms:** `Z2`, `Z3`, `Z4`, `Z5`, `Z6`, `Z20`, `Z_2`, `Z_3`, `Z_4`, `Z_5`, `Z_20`  
**Kind:** residue-coordinate group family  
**Domain:** Declared finite cyclic coordinates  
**Family parameters:** n; chosen origin and generator  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The integers modulo n used as coordinates on a declared finite cyclic register. Such coordinates may model a C_n action after an origin and generator are selected. They do not identify all native actions of that abstract type.

```text
Z/nZ
```

**Keep distinct:** Z_5 as a residue group is not Z5 the frame-sector exchange operator; Z_3 is not the analyzer Z3 reflection.

**Recorded relationships:** [frame-sector-exchange](#frame-sector-exchange) (operator vs residue group).

**Sources:** [KERNEL](../provenance/inputs/draft6/sections/01C_relational_kernel.tex#L1-L68), [FRAMES](../provenance/inputs/native_g9000_map_test.md#L1-L295), [CHAT](../provenance/excerpts/current_chat_archive.md#L1-L21).

---

<a id="matrix-algebras"></a>

## Full matrix algebra size notation

**Stable ID:** `matrix-algebras`  
**Historical labels / lookup forms:** `M2`, `M_2`, `M2(R)`, `M2(C)`  
**Kind:** associative algebra family  
**Domain:** Endomorphisms of the specified two-dimensional spaces  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The full two-by-two matrix algebra over the stated field. In the projective binary comparison, the complex lifts generate M2(C). A matrix algebra is not an individual indexed matrix M_2 or a return-count operator with the same compressed spelling.

```text
M_2(C), or M_2(R) where specified
```

**Keep distinct:** Keep the field and represented carrier explicit; matching matrix size is not native identity.

**Recorded relationships:** [m4-mode-set](#m4-mode-set) (finite mode set vs algebra).

**Sources:** [HISTORICAL_FIVEFOLD](../provenance/excerpts/historical_fivefold.md#L1-L9), [CORE](../provenance/inputs/qr_core_terms_consolidated.md#L1-L3141).

---

<a id="h1-homology"></a>

## First homology group on a declared complex

**Stable ID:** `h1-homology`  
**Historical labels / lookup forms:** `H1`, `H_1`  
**Kind:** homology group functor  
**Domain:** Declared complex and coefficient ring  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The first homology group of a specified complex with specified coefficients. Its cycles-modulo-boundaries definition and winding interpretation depend on that domain. It is not the isotropy subgroup H_1 at phase coset S_1.

```text
H1(K;Z)=ker(boundary1)/im(boundary2)
```

**Keep distinct:** Always include the complex and coefficient ring. Do not merge distinct winding constructions on their common abstract integer group.

**Sources:** [WINDING](../provenance/inputs/PHASE_RELATION_CELLULAR_PROOF.md#L1-L392), [CORE](../provenance/inputs/qr_core_terms_consolidated.md#L1-L3141).

---

<a id="h2-history-variable"></a>

## Indexed retained history states

**Stable ID:** `h2-history-variable`  
**Historical labels / lookup forms:** `H1`, `H2`, `H_1`, `H_2`  
**Kind:** indexed record family  
**Domain:** Two histories compared for future response  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

In the core definitions H1 and H2 also name two retained histories being compared by future admissibility and response. These numeric indices are variable labels, not homological degree or group order.

```text
H1 ~ H2 under the declared predictive-history equivalence
```

**Keep distinct:** The local formula must determine the type; a bare H1 match remains ambiguous.

**Sources:** [BASE](../provenance/inputs/qr_core_terms_original.md#L1-L1982), [CORE](../provenance/inputs/qr_core_terms_consolidated.md#L1-L3141).

---

<a id="h12-history-candidate"></a>

## Twelve-dimensional analyzer-frame candidate module

**Stable ID:** `h12-history-candidate`  
**Historical labels / lookup forms:** `H12`, `H_12`, `H12_cand`  
**Kind:** representation candidate  
**Domain:** Exchange-odd analyzer sector tensor nontrivial frame harmonics  
**Typed size:** Real dimension: 12  
**Standing:** Conversation-derived candidate; final native intertwiner open.

The proposed tensor product of a three-dimensional exchange-odd analyzer sector with the four-dimensional nontrivial frame module. It matches the dimension and abstract Clifford relations of registered pentagon history. It is not yet the construction-derived history module identification.

```text
H12_cand = wedge^2(V_chi) tensor E_C5_nontriv
```

**Keep distinct:** Not a set of twelve history events, section states, or phase objects. The final native intertwiner remains open.

**Recorded relationships:** [history-pentagon-space](#history-pentagon-space) (candidate module match).

**Sources:** [CHAT](../provenance/excerpts/current_chat_archive.md#L1-L21), [CORE](../provenance/inputs/qr_core_terms_consolidated.md#L1-L3141).

---

<a id="section-source-h-locators"></a>

# Source-code and metadata bins

<a id="source-h-locators"></a>

## H-prefixed audit/frontier source locators

**Stable ID:** `source-h-locators`  
**Historical labels / lookup forms:** `H8`, `H10`, `H35`, `H40`, `H41`, `H58`, `H61`, `H65`, `H67`, `H69`, `H71`  
**Kind:** metadata / locator family  
**Domain:** Project 41 audit and frontier names  
**Standing:** Metadata where explicit; H8/H10 standalone referents unresolved.

H35, H58, H61 and related strings in provenance refer to audits or frontiers. They are not automatically homology groups, group orders, or Hilbert-space dimensions. H8 and H10 were not resolved as standalone mathematical objects in the fully scanned current packet.

```text
H35: selected square; H58: face-to-Weyl comparison; H61: pairing; H67: reflection audit
```

**Keep distinct:** Recover the original referenced payload before assigning a structure to an unresolved locator. No H8/H10 group is invented from the spelling.

**Sources:** [CARTAN](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_order4_square_cartan_orientation_201h35b.v1.json#L1-L99), [REFLECTION](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_selected_reflection_event_pauli_anatomy_201h67b.v1.json#L1-L41), [BUNDLE](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_r1_face_bundle_cocycle_triviality_201h69g.v1.json#L1-L50).

---

<a id="source-draft-codes"></a>

## Draft-number source citation codes

**Stable ID:** `source-draft-codes`  
**Historical labels / lookup forms:** `D6`, `d6`, `D5_draft`, `D3_draft`  
**Kind:** source identifier  
**Domain:** Glossary source keys and filenames  
**Standing:** Lexical metadata.

D6 in the glossary source keys generally means Draft 6. Draft identifiers and filenames can share a letter-number spelling with dihedral notation. The enclosing source reference and the complete filename disambiguate them.

```text
[D6] identifies the Draft 6 manuscript source
```

**Keep distinct:** Citation metadata is not a mathematical group. Preserve the whole source token.

**Sources:** [CORE](../provenance/inputs/qr_core_terms_consolidated.md#L1-L3141), [GLOSS](../provenance/inputs/thalean_glossary_previous.md#L1-L4227).

---

<a id="source-equation-codes"></a>

## Equation and statement identifier families

**Stable ID:** `source-equation-codes`  
**Historical labels / lookup forms:** `E01..E52`, `F1..F8`, `K1..K4`, `M1..M4`, `S10_1`, `E02..E52`, `W1`, `W2`  
**Kind:** metadata / locator family  
**Domain:** TEX equation tags, statement filenames and input commands  
**Standing:** Lexical metadata.

Equation tags and statement filenames are locators. For example, K1 is the tag of the kernel point definition, while K_1 elsewhere is a quaternionic generator. E01 can name an equation file, whereas E_01 can denote a correlation entry.

```text
\tag{K1}; \input{equations/E01}; statements/S10_1.tex
```

**Keep distinct:** A regular-expression match is not a mathematical object. Keep leading zeros, suffixes and enclosing tag or path syntax.

**Sources:** [KERNEL](../provenance/inputs/draft6/sections/01C_relational_kernel.tex#L1-L68), [COVER](../provenance/inputs/draft6/sections/01B_common_cover.tex#L1-L101), [MODE](../provenance/inputs/draft6/sections/03A_mode.tex#L1-L69), [CORE](../provenance/inputs/qr_core_terms_consolidated.md#L1-L3141).

---

<a id="source-census-codes"></a>

## Census path and source transport code families

**Stable ID:** `source-census-codes`  
**Historical labels / lookup forms:** `N015`, `N030`, `N060`, `N120`, `x012`, `x210`  
**Kind:** catalogue / transport-code identifier  
**Domain:** Census paths and complete source transport labels  
**Standing:** Lexical metadata.

N015, N030, N060 and N120 are census path components. The strings x012 and x210 occur inside complete source transport codes. Their meaning comes from the full path or transport label rather than the isolated letter-number substring.

```text
Catalogue example N120/N120i038; complete transport codes 02_x_012 and 021_x_210
```

**Keep distinct:** Do not create an N-dimensional space or an X012 state carrier from these substrings.

**Sources:** [COVER](../provenance/inputs/draft6/sections/01B_common_cover.tex#L1-L101), [FRAMES](../provenance/inputs/native_g9000_map_test.md#L1-L295).

---

<a id="source-audit-codes"></a>

## Numeric audit/version labels

**Stable ID:** `source-audit-codes`  
**Historical labels / lookup forms:** `C107`, `v0`, `v1`, `G21`, `O48`, `FP7`  
**Kind:** audit / schema / source-locator family  
**Domain:** Audit IDs, schema versions and upstream frontier references  
**Standing:** Metadata; full G21/O48 payloads not recovered.

C107 names the comparator-center audit rather than a cyclic group of order 107. v1 usually labels a schema version. G21, O48 and FP7 are references to particular upstream artifacts or label sets; not every full referent is included in this packet.

```text
Audit C107; schema suffix .v1.json; source references G21, O48, FP7
```

**Keep distinct:** v1 may also be a variable in a different context. No unseen O48 group is inferred from the number 48.

**Sources:** [MM](../provenance/inputs/C107.json#L1-L44), [CONNECTION](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_u2_gauge_bridge_connection_frontier_checkpoint_201fp7.v1.json#L1-L190), [BUNDLE](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_r1_face_bundle_cocycle_triviality_201h69g.v1.json#L1-L50).

---

<a id="section-face-stabilizer"></a>

# Companion objects needed for typed relationships

<a id="face-stabilizer"></a>

## Native face-family ambient stabilizer

**Stable ID:** `face-stabilizer`  
**Historical labels / lookup forms:** `Stab_f`, `H_face80`  
**Kind:** finite subgroup family  
**Domain:** Aut(G60), fixing one native face family  
**Typed size:** Group order: 80  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The order-eighty subgroup fixing one native face family setwise. It maps to the order-eight block permutation image and has the order-ten realization kernel. These three objects belong in one exact sequence, not one alias list.

```text
1 -> D5_f -> Stab(f) -> D8_blocks(f) -> 1
```

**Keep distinct:** Never list ambient stabilizer, image and kernel as interchangeable names for D8.

**Recorded relationships:** [d5-face-kernel](#d5-face-kernel) (kernel embedding); [d8-face-blocks](#d8-face-blocks) (permutation image).

**Sources:** [D5_KERNEL](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_d5_kernel_naturality_201fqb.v1.json#L1-L70), [FACE_SCOPE](../provenance/inputs/draft6/appendices/O_reference_audit.tex#L1-L82).

---

<a id="history-pentagon-space"></a>

## Registered-pentagon coefficient module

**Stable ID:** `history-pentagon-space`  
**Historical labels / lookup forms:** `H_hist`, `H12_history`  
**Kind:** real vector space  
**Domain:** Coefficient space of twelve oriented quotient pentagon generators  
**Typed size:** Real dimension: 12  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The twelve-dimensional coefficient domain generated by the twelve oriented quotient pentagons. Its basis labels are finite cycles, but its possible vectors are not limited to twelve point states. The signed cycle-incidence map acts from this space.

```text
B_hist: R^12 -> R^30
```

**Keep distinct:** Not the phase actor Gamma_hist, the twelve-section set, the twelve face-phase objects, or the candidate analyzer-frame module.

**Recorded relationships:** [twelve-face-phases](#twelve-face-phases) (finite set vs vector space); [h12-history-candidate](#h12-history-candidate) (candidate module match).

**Sources:** [HIST](../provenance/inputs/thalean_registered_history_conference_operator_audit.json#L1-L564), [MEASURE](../provenance/inputs/draft6/sections/05_measure_registration.tex#L1-L57).

---

<a id="history-incidence"></a>

## Signed registered-pentagon incidence map

**Stable ID:** `history-incidence`  
**Historical labels / lookup forms:** `B_hist`, `M_cycle`  
**Kind:** linear map  
**Domain:** R^12 cycle coefficients -> R^30 oriented G15 edge coordinates  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The signed thirty-by-twelve edge-cycle incidence map. Its columns are oriented registered pentagons in the thirty-edge quotient. Older source notation uses M for this map; later manuscript notation uses B_hist.

```text
G_hist=B_hist^T B_hist
```

**Keep distinct:** M_sec is a different fifteen-by-thirty map. Only merge the M/B_hist spellings when they refer to this same edge-cycle map.

**Recorded relationships:** [history-gram](#history-gram) (gram construction).

**Sources:** [HIST](../provenance/inputs/thalean_registered_history_conference_operator_audit.json#L1-L564), [MEASURE](../provenance/inputs/draft6/sections/05_measure_registration.tex#L1-L57).

---

<a id="history-gram"></a>

## Registered-pentagon Gram operator

**Stable ID:** `history-gram`  
**Historical labels / lookup forms:** `G_hist`, `M_hist`  
**Kind:** positive operator  
**Domain:** R^12 history coefficient module  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The positive twelve-by-twelve Gram operator of the cycle-incidence map. Its trace is sixty because each of the twelve cycle generators has squared norm five. It acts on coefficients rather than sending them to edges.

```text
G_hist=B_hist^T B_hist=5I12+K_hist
```

**Keep distinct:** Not the incidence map B_hist, its coefficient carrier H_hist, or its centered contrast K_hist.

**Recorded relationships:** [history-incidence](#history-incidence) (gram construction); [history-contrast](#history-contrast) (centering relation).

**Sources:** [HIST](../provenance/inputs/thalean_registered_history_conference_operator_audit.json#L1-L564), [CLIFF](../provenance/inputs/thalean_registered_history_clifford_measure_audit.json#L1-L54).

---

<a id="history-contrast"></a>

## Registered-history centered conference operator

**Stable ID:** `history-contrast`  
**Historical labels / lookup forms:** `K_hist`  
**Kind:** real symmetric operator  
**Domain:** R^12 history coefficient module  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The integer symmetric centered Gram operator. Its square is five times identity. The stored signed row/column chart identifies its off-diagonal conference block, while native action equivariance requires its separate source evidence.

```text
K_hist=G_hist-5I12; K_hist^2=5I12
```

**Keep distinct:** The normalized J_hist=K_hist/sqrt(5) is related by scaling, not literally the same operator.

**Recorded relationships:** [history-gram](#history-gram) (centering relation).

**Sources:** [HIST](../provenance/inputs/thalean_registered_history_conference_operator_audit.json#L1-L564).

---

<a id="history-sheet-grading"></a>

## Receipt-family diagonal grading

**Stable ID:** `history-sheet-grading`  
**Historical labels / lookup forms:** `Z_hist`  
**Kind:** linear involution  
**Domain:** Six b and six ab pentagon coefficients  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The diagonal sign operator distinguishing the six b-receipt cycles from the six ab-receipt cycles. It anticommutes with the centered history operator. This raw family grading is not the sheet-exchange observable used in the spectral refinement.

```text
Z_hist = +1 on b, -1 on ab; Z_hist K_hist = -K_hist Z_hist
```

**Keep distinct:** Not the frame Z5, a universal physical parity, or the sheet-exchange eigenvalue q.

**Recorded relationships:** [history-sheet-exchange](#history-sheet-exchange) (grading vs exchange).

**Sources:** [CLIFF](../provenance/inputs/thalean_registered_history_clifford_measure_audit.json#L1-L54).

---

<a id="history-sheet-exchange"></a>

## Signed-chart history sheet-exchange operator

**Stable ID:** `history-sheet-exchange`  
**Historical labels / lookup forms:** `Q_H`, `Q_hist`  
**Kind:** linear involution  
**Domain:** Two-sheet by six-axis signed normal form  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The exchange operator on the sheet factor in the signed conference chart. It commutes with the normalized conference factor T_H. It differs from the diagonal receipt-family grading Z_hist.

```text
Q_H=X_sheet tensor I6
```

**Keep distinct:** A chart-derived operator is not a raw two-sheet record or the sector overlap Gram Q_sec.

**Recorded relationships:** [history-sheet-grading](#history-sheet-grading) (grading vs exchange).

**Sources:** [CHAT](../provenance/excerpts/current_chat_archive.md#L1-L21), [CORE](../provenance/inputs/qr_core_terms_consolidated.md#L1-L3141), [HIST](../provenance/inputs/thalean_registered_history_conference_operator_audit.json#L1-L564).

---

<a id="history-axis-involution"></a>

## History-chart normalized conference factor

**Stable ID:** `history-axis-involution`  
**Historical labels / lookup forms:** `T_H`, `T_hist`  
**Kind:** linear involution  
**Domain:** Axis factor of the signed history normal form  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The normalized six-axis conference operator acting on the axis factor of the two-sheet history chart. Together with Q_H it factorizes J_hist and yields four joint rank-three spectral cells.

```text
T_H=I2 tensor C_conf/sqrt5; J_hist=Q_H T_H
```

**Keep distinct:** Not a macro-history transport T10/T12, Thalean time, or a local scalar relay.

**Sources:** [CHAT](../provenance/excerpts/current_chat_archive.md#L1-L21), [CORE](../provenance/inputs/qr_core_terms_consolidated.md#L1-L3141), [HIST](../provenance/inputs/thalean_registered_history_conference_operator_audit.json#L1-L564).

---

<a id="conference-matrix"></a>

## Six-axis symmetric conference matrix

**Stable ID:** `conference-matrix`  
**Historical labels / lookup forms:** `C_conf`, `C6_conf`  
**Kind:** real 6-by-6 matrix  
**Domain:** Signed presentation of six projective analyzer axes  
**Typed size:** Real dimension: 6  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The six-by-six signed symmetric conference representative with zero diagonal, off-diagonal entries +/-1, and square five times identity. Its rank-three Gram realization describes the six projective analyzer lines up to the appropriate sign and coordinate choices.

```text
C_conf^2=5I6
```

**Keep distinct:** Line-sign changes alter its presentation by switching. The matrix is not the symmetry group or a physical analyzer instrument.

**Sources:** [HIST](../provenance/inputs/thalean_registered_history_conference_operator_audit.json#L1-L564), [CONF_ACTION](../provenance/inputs/thalean_transport_conference_bridge_audit.json#L1-L123).

---

<a id="sector-incidence"></a>

## Fifteen-by-thirty sector incidence map

**Stable ID:** `sector-incidence`  
**Historical labels / lookup forms:** `M_sec`  
**Kind:** linear map  
**Domain:** Inherited sector/edge-coordinate construction on G15  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The fifteen-by-thirty incidence map in the inherited sector/edge construction. It supplies the quadratic sector shadow on G15. Its shape and domain distinguish it from the thirty-by-twelve history-cycle map.

```text
Q_sec=M_sec M_sec^T
```

**Keep distinct:** Historical reuse of M must not erase which domain and codomain are being used.

**Sources:** [CORE](../provenance/inputs/qr_core_terms_consolidated.md#L1-L3141), [BASE](../provenance/inputs/qr_core_terms_original.md#L1-L1982).

---

<a id="sector-overlap"></a>

## Sector overlap quadratic shadow

**Stable ID:** `sector-overlap`  
**Historical labels / lookup forms:** `Q_sec`  
**Kind:** symmetric 15-by-15 operator  
**Domain:** G15sectorregister  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The fifteen-by-fifteen Gram shadow of the sector-incidence map, with the retained source identity involving G15 adjacency. It is a quadratic overlap/readout object rather than automatically the primitive transport generator.

```text
Q_sec=A15^3+2A15^2+2I15
```

**Keep distinct:** Not the history sheet exchange Q_H or a universal event law.

**Sources:** [CORE](../provenance/inputs/qr_core_terms_consolidated.md#L1-L3141).

---

<a id="g1800-delta"></a>

## Registered G1800 midpoint involution

**Stable ID:** `g1800-delta`  
**Historical labels / lookup forms:** `Delta_1800`  
**Kind:** permutation  
**Domain:** Declared registered G1800 carrier  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The free midpoint involution equal to the square of the declared registered G1800 quarter-turn. The associated quotient forgets its two-state lift coordinate.

```text
Delta_1800=K_1800^2; Delta_1800^2=I
```

**Keep distinct:** Not an event receipt delta_e, accumulated Delta[Gamma], global native deck a, or rooted comparator center by a matching sign alone.

**Sources:** [FRAMES](../provenance/inputs/native_g9000_map_test.md#L1-L295).

---

<a id="t12-macro"></a>

## Native T12 macro-history transport

**Stable ID:** `t12-macro`  
**Historical labels / lookup forms:** `T12`, `T_12`  
**Kind:** native actor / quotient-view  
**Domain:** Native macro-history alphabet and conference quotient action  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The named macro-history transport whose conference comparison has odd orientation and an order-six quotient action. The retained artifact gives its six-axis permutation and switching signs. The digits in the name do not establish its full native permutation order.

```text
Conference orientation -1; quotient order 6; six-axis cycle type 6
```

**Keep distinct:** Keep native actor order separate from quotient order. No order-twelve conclusion is inferred from T12.

**Sources:** [CONF_ACTION](../provenance/inputs/thalean_transport_conference_bridge_audit.json#L1-L123).

---

<a id="h-history-group"></a>

## Literal sixteen-element phase-history actor group

**Stable ID:** `h-history-group`  
**Historical labels / lookup forms:** `Gamma_hist`  
**Kind:** finite subgroup  
**Domain:** Supplied Aut(G60) cache and four phase cosets  
**Typed size:** Group order: 16  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The declared sixteen-element group generated by r,s,z in the native cache. Its four-object action groupoid is constructed explicitly in the source. It is not the scalar correlation Gamma or an arbitrary history word using that letter.

```text
Gamma_hist=<r,s,z> ~= D8 x C2
```

**Keep distinct:** The later twelve-pentagon coefficient action has its own domain and evidence; it is not this group by identity.

**Sources:** [HISTORY_PHASE](../provenance/inputs/draft6/sections/03F_history_phase_groupoid.tex#L1-L66).

---

<a id="history-alphabet"></a>

## Original two-member continuation-history alphabet

**Stable ID:** `history-alphabet`  
**Historical labels / lookup forms:** `h23`, `{2,3}`  
**Kind:** two-state indexed set  
**Domain:** Original Program 03 continuation interface  
**Typed size:** Point/object count: 2  
**Standing:** Source-recorded; original producer not re-executed in this sweep.

The original two continuation-history labels, with the source preserve-roles and swap-roles semantics. Equivariant sign naming leaves a global reversal choice. The actual projection from the decorated phase carrier remains an independent requirement.

```text
h in {2,3}; preserve roles: h -> 5-h
```

**Keep distinct:** Not the b/ab pentagon family, the q,t spectral signs, or the frame character index.

**Sources:** [HISTORY_PHASE](../provenance/inputs/draft6/sections/03F_history_phase_groupoid.tex#L1-L66), [CORE](../provenance/inputs/qr_core_terms_consolidated.md#L1-L3141).

---

<a id="section-adjacency-g15"></a>

# Additional collisions from the exact occurrence sweep

<a id="adjacency-g15"></a>

## Native quotient adjacency operator

**Stable ID:** `adjacency-g15`  
**Historical labels / lookup forms:** `A15`, `A_15`  
**Kind:** graph adjacency matrix  
**Domain:** G15 vertex function space  
**Typed size:** Real dimension: 15  
**Standing:** Source-recorded; no original mathematical producer re-executed here.

The fifteen-by-fifteen adjacency appearing in the sector Gram identity. The graph and its matrix are related but not interchangeable objects; the chosen vertex order matters for literal matrix identity.

```text
A15 = adjacency(G15)
```

**Keep distinct:** Not the alternating group A15 or the distance-fusion matrices A_0 through A_3.

**Sources:** [CORE](../provenance/inputs/qr_core_terms_consolidated.md#L1-L3141), [CENSUS](../provenance/inputs/draft6/sections/01A_census_family.tex#L1-L59).

---

<a id="adjacency-g60"></a>

## Native carrier adjacency operator

**Stable ID:** `adjacency-g60`  
**Historical labels / lookup forms:** `A60`, `A_60`  
**Kind:** graph adjacency matrix  
**Domain:** G60 vertex function space  
**Typed size:** Real dimension: 60  
**Standing:** Source-recorded; no original mathematical producer re-executed here.

The sixty-by-sixty adjacency whose product-space lift is A60 tensor I + I tensor A60 before the diagonal deck quotient. Its spectral sectors are not the graph vertices themselves.

```text
A_product=A60 tensor I+I tensor A60
```

**Keep distinct:** Not the graph G60, its full automorphism group, or a sixty-element alternating group.

**Sources:** [ANALYZER](../provenance/inputs/native_analyzer_constraints.md#L1-L450), [EPR](../provenance/inputs/native_epr_history_control.md#L1-L74).

---

<a id="petersen-f10"></a>

## Petersen graph in the F10 construction label

**Stable ID:** `petersen-f10`  
**Historical labels / lookup forms:** `F10`, `F_10`, `Petersen`  
**Kind:** finite graph  
**Domain:** Census construction expression L(B(F10))  
**Typed size:** Point/object count: 10  
**Standing:** Source-recorded; no original mathematical producer re-executed here.

The census-family section explicitly writes F10=P, the Petersen graph, and B=CDC. Here F10 names a ten-vertex source graph, not a tenth power of the registered F action.

```text
F10=P; Q30=L(B(F10)), B=CDC
```

**Keep distinct:** Only the explicit source construction licenses this alias.

**Sources:** [CENSUS](../provenance/inputs/draft6/sections/01A_census_family.tex#L1-L59).

---

<a id="chain-groups"></a>

## Cellular integral chain group family

**Stable ID:** `chain-groups`  
**Historical labels / lookup forms:** `C0`, `C1`, `C2`, `C_0`, `C_1`, `C_2`  
**Kind:** free abelian chain groups  
**Domain:** The stated four-generator relation complex K  
**Family parameters:** degree k and declared complex/coefficient ring  
**Standing:** Source-recorded; no original mathematical producer re-executed here.

C0,C1,C2 here record cellular chain degree. The particular complex has one vertex, four loop edges and nine relation cells. C2(K;Z)=Z^9 is not a cyclic group of order two or a complex two-dimensional space.

```text
C0(K;Z)=Z; C1(K;Z)=Z^4; C2(K;Z)=Z^9
```

**Keep distinct:** Preserve the complex and coefficient ring. Do not strip the arguments or the degree role.

**Sources:** [WINDING](../provenance/inputs/PHASE_RELATION_CELLULAR_PROOF.md#L1-L392).

---

<a id="cochain-spaces"></a>

## Discrete Maxwell cochain-degree spaces

**Stable ID:** `cochain-spaces`  
**Historical labels / lookup forms:** `C^0`, `C^1`, `C^2`, `C^3`, `C^2_cochain`  
**Kind:** cochain space family  
**Domain:** A specified discrete cell complex  
**Family parameters:** cochain degree and actual cell complex  
**Standing:** Source-recorded; no original mathematical producer re-executed here.

In C^0 -> C^1 -> C^2 -> C^3, the superscript denotes cochain degree. It does not state complex vector-space dimension. This is a superscript collision that subscript-only normalization would miss.

```text
C^0 --D0--> C^1 --D1--> C^2 --D2--> C^3
```

**Keep distinct:** C^2 can also mean complex two-space in a fonted scalar context. Preserve notation, chain complex and arguments.

**Recorded relationships:** [complex-spaces](#complex-spaces) (cochain degree vs complex dimension).

**Sources:** [DYN_TARGETS](../provenance/inputs/draft6/appendices/L2_dynamical_targets.tex#L1-L25), [MAXWELL](../provenance/inputs/draft6/sections/09C_maxwell.tex#L1-L93).

---

<a id="binary-vector-spaces"></a>

## Binary vector-space dimension family

**Stable ID:** `binary-vector-spaces`  
**Historical labels / lookup forms:** `F2^2`, `F2^3`, `F2^4`, `F_2^2`, `F_2^3`, `F_2^4`  
**Kind:** finite vector-space family  
**Domain:** Binary coordinate, cochain or reference-fiber domains  
**Family parameters:** n and the specified coordinate domain  
**Standing:** Source-recorded; no original mathematical producer re-executed here.

The exponent is vector dimension over the two-element field. F2^2 has four elements, F2^3 eight and F2^4 sixteen; that count does not select a native deck embedding or a symplectic/Pauli structure.

```text
dim_(F2)(F2^n)=n; cardinality=2^n
```

**Keep distinct:** The space, a bilinear form on it, and a group acting on it are distinct records.

**Sources:** [KERNEL](../provenance/inputs/draft6/sections/01C_relational_kernel.tex#L1-L68), [CORE](../provenance/inputs/qr_core_terms_consolidated.md#L1-L3141).

---

<a id="cp1-line-space"></a>

## Projective complex line space in the reference gauge

**Stable ID:** `cp1-line-space`  
**Historical labels / lookup forms:** `CP1`, `CP^1`  
**Kind:** projective space  
**Domain:** Lines in the specified complex doublet  
**Standing:** Source-recorded; no original mathematical producer re-executed here.

The Program 2 line map has a two-point image {L0,L1} within a common reference CP1 gauge. The full projective space is not that two-element image.

```text
ell: S_12 x M_4 -> {L0,L1} subset CP1
```

**Keep distinct:** No absolute Pauli axis, raw Hilbert transport, probability law or physical instrument is selected merely by this codomain.

**Sources:** [LINES](../provenance/inputs/draft6/provenance/draft6/native_snapshot/program02/artifacts/json/epr_reference_gauge_projective_line_map_018.v1.json#L1-L775).

---

<a id="s12-phase-set"></a>

## Twelve-state phase factor of the serialized line map

**Stable ID:** `s12-phase-set`  
**Historical labels / lookup forms:** `S12`, `S_12`  
**Kind:** finite structured set  
**Domain:** Phase factor in ell:S_12 x M_4 -> CP1  
**Typed size:** Point/object count: 12  
**Standing:** Source-recorded; no original mathematical producer re-executed here.

The source gives twelve phase states, each with four local modes. Here S_12 is a set of twelve phase objects, not the symmetric group on twelve letters. The source connects these objects to the six face carriers and two relative orientations.

```text
S_12: six faces x two phase states
```

**Keep distinct:** Keep this view linked to the face-phase objects; do not identify it with twelve pentagons.

**Recorded relationships:** [twelve-face-phases](#twelve-face-phases) (same source phase objects).

**Sources:** [LINES](../provenance/inputs/draft6/provenance/draft6/native_snapshot/program02/artifacts/json/epr_reference_gauge_projective_line_map_018.v1.json#L1-L775), [CONNECTION](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_u2_gauge_bridge_connection_frontier_checkpoint_201fp7.v1.json#L1-L190).

---

<a id="m4-mode-set"></a>

## Four local signed modes of the line-map domain

**Stable ID:** `m4-mode-set`  
**Historical labels / lookup forms:** `M4`, `M_4`  
**Kind:** finite indexed mode set  
**Domain:** Local mode factor in S_12 x M_4  
**Typed size:** Point/object count: 4  
**Standing:** Source-recorded; no original mathematical producer re-executed here.

The four local signed event modes consist of two positive and two negative modes. This four-element factor in the serialized map is not a four-by-four matrix algebra and not the equation tag M4.

```text
ell domain has 12 x 4 = 48 phase-mode pairs
```

**Keep distinct:** The point-mode labels and the linear representation they index remain separate.

**Recorded relationships:** [matrix-algebras](#matrix-algebras) (finite mode set vs algebra).

**Sources:** [LINES](../provenance/inputs/draft6/provenance/draft6/native_snapshot/program02/artifacts/json/epr_reference_gauge_projective_line_map_018.v1.json#L1-L775), [PARTITIONS](../provenance/inputs/draft6/provenance/draft6/native_snapshot/program02/artifacts/json/epr_native_face_projective_line_partition_017.v1.json#L1-L566).

---

<a id="p01-line-partitions"></a>

## Two relative-complex-line partitions

**Stable ID:** `p01-line-partitions`  
**Historical labels / lookup forms:** `P0`, `P1`, `P_0`, `P_1`  
**Kind:** partition pair  
**Domain:** Four local signed event modes on a native face  
**Typed size:** Point/object count: 2  
**Standing:** Source-recorded; no original mathematical producer re-executed here.

The two distinct partitions each pair a positive and a negative mode into projective lines. The selected same-face phase-flip transport exchanges these partitions. Here P0 is not the frame-common projector.

```text
P0 <-> P1 under the selected phase flip
```

**Keep distinct:** A partition of four modes is not an orthogonal projector unless the corresponding operator is separately constructed.

**Recorded relationships:** [frame-common-projector](#frame-common-projector) (partition vs projector).

**Sources:** [LINES](../provenance/inputs/draft6/provenance/draft6/native_snapshot/program02/artifacts/json/epr_reference_gauge_projective_line_map_018.v1.json#L1-L775), [PARTITIONS](../provenance/inputs/draft6/provenance/draft6/native_snapshot/program02/artifacts/json/epr_native_face_projective_line_partition_017.v1.json#L1-L566).

---

<a id="t01-edge-connection"></a>

## Same-face forward and reverse connection maps

**Stable ID:** `t01-edge-connection`  
**Historical labels / lookup forms:** `T01`, `T10`, `T_01`, `T_10`  
**Kind:** oriented-edge transport pair  
**Domain:** A selected 6K2 phase-flip edge  
**Standing:** Source-recorded; no original mathematical producer re-executed here.

The numeric indices are ordered endpoints 0 and 1. The source gives T_10=T_01^-1=T_01 for this local involutory transport. That T_10 is not the macro-history actor T10.

```text
T_10=T_01^-1=T_01
```

**Keep distinct:** Do not infer an order-ten transport from the two endpoint indices. Preserve the edge and its local representation.

**Recorded relationships:** [c10-native](#c10-native) (endpoint indices vs actor name); [t10-native-macro](#t10-native-macro) (notation collision).

**Sources:** [TWISTED](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_6k2_twisted_selector_covariance_201fqd.v1.json#L1-L91).

---

<a id="connection-doublet"></a>

## Twisted-covariant two-sheet connection object

**Stable ID:** `connection-doublet`  
**Historical labels / lookup forms:** `C2_connection`, `connection_doublet`  
**Kind:** unordered transport doublet  
**Domain:** The six same-face phase-flip edges  
**Typed size:** Point/object count: 2  
**Standing:** Source-recorded; no original mathematical producer re-executed here.

The source distinguishes a selected sheet T_f from its residual companion R_f T_f. The unordered pair is covariant, whereas strict covariance of one selected sheet fails under the full tested sign-reversing sector.

```text
{T_f,R_f T_f}; h{T_f,R_f T_f}h^-1={T_hf,R_hf T_hf}
```

**Keep distinct:** The twisting C2 is explicitly not identified with physical parity, charge conjugation or time reversal.

**Recorded relationships:** [c2-phase-residual](#c2-phase-residual) (companion action).

**Sources:** [TWISTED](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_6k2_twisted_selector_covariance_201fqd.v1.json#L1-L91).

---

<a id="c4-crown-loop"></a>

## Four-cycle loop in the crown orbital

**Stable ID:** `c4-crown-loop`  
**Historical labels / lookup forms:** `C4`, `C_4`  
**Kind:** graph-cycle target  
**Domain:** Opposite-phase crown connection frontier  
**Typed size:** Point/object count: 4  
**Standing:** Named graph-loop target; a source-selected holonomy is not yet given.

The source proposes a genuine induced C4 loop as the next connection/holonomy target. Here C4 means a four-vertex graph cycle, not an asserted cyclic action or an already selected connection.

```text
Induced four-cycle in the crown orbital
```

**Keep distinct:** The source leaves the crown connection and its curvature unselected.

**Sources:** [TWISTED](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_6k2_twisted_selector_covariance_201fqd.v1.json#L1-L91).

---

<a id="rotor-so3"></a>

## Conventional full-frame rotation group

**Stable ID:** `rotor-so3`  
**Historical labels / lookup forms:** `SO3`, `SO(3)`  
**Kind:** continuous rotation group  
**Domain:** Separately declared mechanical orientation model  
**Standing:** Source-recorded; no original mathematical producer re-executed here.

The full-frame rotation Q acts on an oriented axis n=Q e3. The stabilizer geometry and precession formulas are conventional correspondence calculations, not a derived finite native symmetry.

```text
SO(3) -> S^2, Q -> Q e3
```

**Keep distinct:** The axis map is not a group homomorphism or a normal-kernel quotient.

**Sources:** [CONSERVATIVE](../provenance/inputs/draft6/appendices/N_conservative_calculations.tex#L1-L128).

---

<a id="rotor-so2"></a>

## Oriented-axis rotation stabilizer

**Stable ID:** `rotor-so2`  
**Historical labels / lookup forms:** `SO2`, `SO(2)`  
**Kind:** embedded stabilizer subgroup  
**Domain:** SO(3) fixing the selected oriented axis  
**Standing:** Source-recorded; no original mathematical producer re-executed here.

The rotations h_theta about e3 form the stabilizer of that oriented axis. Each different axis has a conjugate stabilizer. This is not automatically every QR U1 or C_n phase.

```text
Stab_SO3(e3) ~= SO(2)
```

**Keep distinct:** An embedded stabilizer and an invisible normal subgroup are different roles.

**Sources:** [CONSERVATIVE](../provenance/inputs/draft6/appendices/N_conservative_calculations.tex#L1-L128).

---

<a id="rotor-o2"></a>

## Unoriented-axis stabilizer in rotations

**Stable ID:** `rotor-o2`  
**Historical labels / lookup forms:** `O2`, `O(2)`  
**Kind:** embedded two-component stabilizer  
**Domain:** SO(3) preserving the line R e3  
**Standing:** Source-recorded; no original mathematical producer re-executed here.

The source constructs the two components {h_theta} and {s h_theta}, with s e3=-e3 and det(s)=1. This embedded O(2) differs from the surface winding-plane reference envelope by its ambient group and action.

```text
s h_theta s=h_-theta; stabilizer of an unoriented axis
```

**Keep distinct:** Not an identification with the surface O(2) connection or a native finite D8.

**Recorded relationships:** [o2-surface-envelope](#o2-surface-envelope) (same abstract envelope distinct action).

**Sources:** [CONSERVATIVE](../provenance/inputs/draft6/appendices/N_conservative_calculations.tex#L1-L128).

---

<a id="rotor-sphere"></a>

## Oriented-axis sphere base

**Stable ID:** `rotor-sphere`  
**Historical labels / lookup forms:** `S^2`  
**Kind:** homogeneous space  
**Domain:** SO(3)/SO(2) in the conventional rotor model  
**Standing:** Source-recorded; no original mathematical producer re-executed here.

The sphere of oriented axes is the base of the full-frame map. Its local transverse phase chart is not a global product decomposition. This S^2 is not the square of an operator S.

```text
SO(2) -> SO(3) -> S^2
```

**Keep distinct:** No universal native spacetime sphere or global independent phase coordinate is inferred.

**Sources:** [CONSERVATIVE](../provenance/inputs/draft6/appendices/N_conservative_calculations.tex#L1-L128).

---

<a id="rotor-projective-base"></a>

## Unoriented-axis projective base

**Stable ID:** `rotor-projective-base`  
**Historical labels / lookup forms:** `RP2`, `RP^2`  
**Kind:** homogeneous/projective space  
**Domain:** Axes without an orientation in the rotor comparison  
**Standing:** Source-recorded; no original mathematical producer re-executed here.

The unoriented line base corresponding to the embedded two-component stabilizer. It differs from the oriented sphere because n and -n represent the same line.

```text
SO(3)/O(2) ~= RP^2 in the specified stabilizer model
```

**Keep distinct:** Not the complex line space CP1 or the native phase quotient by a matching number.

**Sources:** [CONSERVATIVE](../provenance/inputs/draft6/appendices/N_conservative_calculations.tex#L1-L128).

---

<a id="inertia-moments"></a>

## Transverse and axial heavy-top moments

**Stable ID:** `inertia-moments`  
**Historical labels / lookup forms:** `I1`, `I3`, `I_1`, `I_3`  
**Kind:** physical-model scalar parameters  
**Domain:** Conventional symmetric heavy top about a fixed pivot  
**Standing:** Source-recorded; no original mathematical producer re-executed here.

I1 is the transverse moment about the pivot and I3 the axial moment. These are not identity matrices of size one or three, despite identical subscript spelling.

```text
L3=I3 omega3; regular balance I1 Omega^2 cos(theta)-L3 Omega+Mgr=0
```

**Keep distinct:** These inertia inputs are imported mechanical assumptions, not finite QR outputs.

**Recorded relationships:** [identity-matrices](#identity-matrices) (physical parameter vs identity matrix).

**Sources:** [CONSERVATIVE](../provenance/inputs/draft6/appendices/N_conservative_calculations.tex#L1-L128).

---

<a id="top-l3"></a>

## Axial angular momentum of the heavy-top example

**Stable ID:** `top-l3`  
**Historical labels / lookup forms:** `L3`, `L_3`  
**Kind:** physical-model scalar  
**Domain:** The fixed-pivot symmetric-top comparison  
**Standing:** Source-recorded; no original mathematical producer re-executed here.

The axial component L3=I3 omega3 entering regular-precession balance. It is not a third complex line or an audit priority label.

```text
L3=I3 omega3
```

**Keep distinct:** No native angular momentum calibration is inferred.

**Sources:** [CONSERVATIVE](../provenance/inputs/draft6/appendices/N_conservative_calculations.tex#L1-L128).

---

<a id="wxyz-m-controls"></a>

## Binary-coordinate Mode lookalike control maps

**Stable ID:** `wxyz-m-controls`  
**Historical labels / lookup forms:** `M0`, `M1`, `M_0`, `M_1`  
**Kind:** declared comparison maps  
**Domain:** Toy coordinates (p,mu,r) in the WXYZTI nonidentification test  
**Standing:** Source-recorded; no original mathematical producer re-executed here.

Both maps flip p and mu while either retaining or flipping the role bit. The source uses their commutation with R to show that flipping an extra bit does not by itself establish the required noncommuting Mode law.

```text
M_k(p,mu,r)=(-p,1-mu,r+k), k in F2
```

**Keep distinct:** These are counterexample/control maps, not admitted native Mode actors.

**Sources:** [WXYZ_SECTION](../provenance/inputs/draft6/sections/03B_wxyzti.tex#L1-L54).

---

<a id="wxyz-six-position"></a>

## Six-position realized circuit coordinate

**Stable ID:** `wxyz-six-position`  
**Historical labels / lookup forms:** `Z6`, `Z_6`, `C6`  
**Kind:** finite cyclic index set/action  
**Domain:** Occurrence positions j in each retained WXYZTI circuit  
**Typed size:** Point/object count: 6  
**Standing:** Source-recorded; no original mathematical producer re-executed here.

The channel shift j->j+2 and reciprocal-role exchange j->j+3 commute on the six-position register. This commuting action is not the modal reflection that inverts phase.

```text
C_W:j->j+2; R_W:j->j+3 mod6
```

**Keep distinct:** The six-cycle index does not establish a D5 history or a noncommuting event S3.

**Sources:** [WXYZ_SECTION](../provenance/inputs/draft6/sections/03B_wxyzti.tex#L1-L54).

---

<a id="cellular-generators"></a>

## Four companion-history presentation generators

**Stable ID:** `cellular-generators`  
**Historical labels / lookup forms:** `x1`, `x2`, `x3`, `x4`, `x_1`, `x_2`, `x_3`, `x_4`  
**Kind:** group-presentation generator family  
**Domain:** The declared integral companion history group  
**Standing:** Source-recorded; no original mathematical producer re-executed here.

The x_i are four positive generators represented by oriented loop edges. Their equal-square relations and other relators define the presentation. They are not coordinates of a generic state or binary kernel bits.

```text
x_j^2=x_1^2 for j=2,3,4; W4(x_i)=1
```

**Keep distinct:** Preserve complete word order and presentation relations; do not substitute endpoint values for words.

**Sources:** [WINDING](../provenance/inputs/PHASE_RELATION_CELLULAR_PROOF.md#L1-L392).

---

<a id="cellular-r3-word"></a>

## Six-increment companion word representative

**Stable ID:** `cellular-r3-word`  
**Historical labels / lookup forms:** `r3`, `r_3`  
**Kind:** group word  
**Domain:** The specified cellular companion presentation  
**Standing:** Source-recorded; no original mathematical producer re-executed here.

The source names r3=(x1 x2 x3)^2, with the same reported finite endpoint as another word but different integer winding. This r3 is a word name, not the third power of a generator in compressed notation.

```text
r3=(x1 x2 x3)^2; W4(r3)=6; N(r3)=3
```

**Keep distinct:** Not an analyzer R3 matrix or an abstract rank-three space.

**Sources:** [WINDING](../provenance/inputs/PHASE_RELATION_CELLULAR_PROOF.md#L1-L392).

---

<a id="history-primitive-family"></a>

## Three primitive registered homology species

**Stable ID:** `history-primitive-family`  
**Historical labels / lookup forms:** `r0`, `r1`, `r2`, `r_0`, `r_1`, `r_2`  
**Kind:** homology class family  
**Domain:** Inherited rank-three registered-history homology register  
**Standing:** Source-recorded; no original mathematical producer re-executed here.

The manuscript retains three primitive species r0,r1,r2 and a visibility test selecting r1 for its temporal readout. This is a family of classes, not a three-state finite phase.

```text
phi1(r0)=0; phi1(r1)=1; phi1(r2)=0
```

**Keep distinct:** The family is inherited from its own original history domain, not automatically the cellular W4 presentation.

**Recorded relationships:** [r1-history-class](#r1-history-class) (selected family member).

**Sources:** [HISTORY_CLASSES](../provenance/inputs/draft6/appendices/E_history.tex#L1-L26).

---

<a id="frame-sign-values"></a>

## Golden-sector and conjugate-current eigenvalue signs

**Stable ID:** `frame-sign-values`  
**Historical labels / lookup forms:** `s5`, `r5`  
**Kind:** spectral scalar labels  
**Domain:** Joint eigenmodes of J5 and R5 in the event subspace  
**Standing:** Source-recorded; no original mathematical producer re-executed here.

The lower-case signs s5,r5 are eigenvalues +/-1, not the upper-case involutions J5,R5. Listing all four as aliases would collapse an operator with its readout.

```text
(s5,r5) = (eigenvalue of J5, eigenvalue of R5)
```

**Keep distinct:** Not the primitive history r1 or a cyclic group C5.

**Recorded relationships:** [frame-current-sign](#frame-current-sign) (eigenvalue readout).

**Sources:** [CORE](../provenance/inputs/qr_core_terms_consolidated.md#L1-L3141), [CHAT](../provenance/excerpts/current_chat_archive.md#L1-L21).

---

<a id="g2-word-spelling"></a>

## Compressed square-of-g source key

**Stable ID:** `g2-word-spelling`  
**Historical labels / lookup forms:** `g2`  
**Kind:** source-key / operation spelling  
**Domain:** Source checks referring to the square of selected g  
**Standing:** Source-recorded; no original mathematical producer re-executed here.

The key g2_equals_r1_on_all_signed_blocks records g squared. It does not introduce a new generator called g2 or the exceptional Lie group G2.

```text
g2 in this check means g^2
```

**Keep distinct:** Use the underlying action equation before naming an object; no Lie-group G2 is inferred.

**Sources:** [CARTAN](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_order4_square_cartan_orientation_201h35b.v1.json#L1-L99), [HISTORY_PHASE](../provenance/inputs/draft6/sections/03F_history_phase_groupoid.tex#L1-L66).

---

<a id="quotient-q30"></a>

## Original native double-cover projection

**Stable ID:** `quotient-q30`  
**Historical labels / lookup forms:** `q30`, `q_30`  
**Kind:** quotient map  
**Domain:** G60 -> original G30  
**Standing:** Source-recorded; no original mathematical producer re-executed here.

The map to the orbit under the central deck involution a. The map is not the quotient graph, its matrix, or an additional thirty-state carrier.

```text
q30(v)=[v]_<a>
```

**Keep distinct:** Keep map, domain and codomain separately named.

**Sources:** [QUOTIENTS](../provenance/inputs/draft6/appendices/C_quotient_tower.tex#L1-L20).

---

<a id="quotient-q15"></a>

## Native Klein-orbit projection

**Stable ID:** `quotient-q15`  
**Historical labels / lookup forms:** `q15`, `q_15`  
**Kind:** quotient map  
**Domain:** G60 -> G15  
**Standing:** Source-recorded; no original mathematical producer re-executed here.

The map assigning a native vertex its V4 orbit. The original thirty-state quotient refines these fibers, but that relation does not identify the two maps.

```text
q15(v)=[v]_V4
```

**Keep distinct:** Not the G15 adjacency or a fifteen-dimensional scalar functional.

**Sources:** [QUOTIENTS](../provenance/inputs/draft6/appendices/C_quotient_tower.tex#L1-L20).

---

<a id="n0-count-domain"></a>

## Nonnegative integer iteration domain

**Stable ID:** `n0-count-domain`  
**Historical labels / lookup forms:** `N0`, `N_0`  
**Kind:** scalar set  
**Domain:** Counts of repeated histories  
**Standing:** Source-recorded; no original mathematical producer re-executed here.

The nonnegative integers indexing allowed repetition counts. This is not a group called N0 or the initial value of a separately specified sequence.

```text
n in N0={0,1,2,...}
```

**Keep distinct:** The domain alone is not a native source law.

**Sources:** [SCALAR](../provenance/inputs/draft6/sections/03C_scalar_relay.tex#L1-L88).

---

<a id="n1-registration-count"></a>

## Registered binary outcome-one count

**Stable ID:** `n1-registration-count`  
**Historical labels / lookup forms:** `N1`, `N_1`  
**Kind:** scalar count function  
**Domain:** Supplied-weight mechanical registration sequence  
**Standing:** Source-recorded; no original mathematical producer re-executed here.

The count of ones in the defined binary sequence. Its telescoping formula proves realization once alpha and the update are supplied, not native selection of the weight or chronology.

```text
N1(N)=floor(N alpha+theta)-floor(theta)
```

**Keep distinct:** Not the nonnegative integer set N0 or a native state-space cardinality.

**Sources:** [MEASURE](../provenance/inputs/draft6/sections/05_measure_registration.tex#L1-L57).

---

<a id="b1-betti"></a>

## First Betti number of the reference surface

**Stable ID:** `b1-betti`  
**Historical labels / lookup forms:** `b1`, `b_1`  
**Kind:** topological rank  
**Domain:** The closed orientable surface used in the phase-lift example  
**Standing:** Source-recorded; no original mathematical producer re-executed here.

The source gives b1=2g=42 for genus21. The subscript denotes homological degree, not a receipt bit b_1 or Bob setting B1.

```text
b1=42
```

**Keep distinct:** This rank is not a new four-dimensional or forty-two-point carrier.

**Sources:** [SURFACE](../provenance/inputs/README(20260920-001150).md#L1-L300).

---

<a id="d0-section-sign"></a>

## Initial signed-switching section convention

**Stable ID:** `d0-section-sign`  
**Historical labels / lookup forms:** `d0`, `d_0`  
**Kind:** scalar sign convention  
**Domain:** Projective signed analyzer section  
**Standing:** Source-recorded; no original mathematical producer re-executed here.

The convention d(g,0)=+1 selects representatives of the signed switching class. The source shows that this section need not multiply exactly before rephasing.

```text
d(g,0)=+1
```

**Keep distinct:** Not the cochain map D0 or a canonical absolute axis orientation.

**Sources:** [SIGNED_AXIS](../provenance/inputs/draft6/sections/05A_signed_axis_reference.tex#L1-L86).

---

<a id="d1-tick-depth"></a>

## Event depth of one declared winding traversal

**Stable ID:** `d1-tick-depth`  
**Historical labels / lookup forms:** `d1`, `d_1`  
**Kind:** scalar execution cost  
**Domain:** A selected primitive registered-history traversal  
**Standing:** Source-recorded; no original mathematical producer re-executed here.

The number of event steps required by that declared traversal. The corresponding tick-per-event rate is 1/d1. Its local index does not define a universal one-event tick.

```text
tick rate = 1/d1
```

**Keep distinct:** Event depth and signed winding remain different quantities.

**Sources:** [HISTORY_TIME](../provenance/inputs/draft6/sections/03_information_history_time.tex#L1-L87).

---

<a id="d34-move-labels"></a>

## Balanced-release d3/d4 move-class labels

**Stable ID:** `d34-move-labels`  
**Historical labels / lookup forms:** `d3`, `d4`  
**Kind:** native move-class references  
**Domain:** Balanced-release execution grammar referenced by the winding extraction  
**Standing:** Source-referenced move classes; full region reconstruction outside this scan.

The companion-word source distinguishes d4 connectors from the extracted positive companion factors. In that particular receipt extraction they contribute no companion factor. That does not mean no physical or causal cost, or that the complete move grammar is reconstructed here.

```text
Ordinary d4 connectors contribute no factor to this extracted companion word
```

**Keep distinct:** The fully scanned packet does not contain the complete region move definition; preserve the original d3/d4 grammar source.

**Sources:** [WINDING](../provenance/inputs/PHASE_RELATION_CELLULAR_PROOF.md#L1-L392).

---

<a id="coordinate-variables"></a>

## Indexed endpoint and state-coordinate variables

**Stable ID:** `coordinate-variables`  
**Historical labels / lookup forms:** `x0`, `x1`, `x2`, `x_0`, `x_1`, `x_2`, `y1`, `y2`, `y_1`, `y_2`, `z0`, `z_0`  
**Kind:** indexed variable families  
**Domain:** The local context in which a state or bit is written  
**Standing:** Source-recorded; no original mathematical producer re-executed here.

The same x1 can be a state at event one or the first bit of a kernel point. These are local variable uses, not global reusable mathematical objects. The occurrence index retains the defining sentence.

```text
History states x_n; kernel points (i,x1,x2); target bits y1,y2
```

**Keep distinct:** Do not merge chronology indices with coordinate slots or the cellular presentation generators x_i.

**Sources:** [BASE](../provenance/inputs/qr_core_terms_original.md#L1-L1982), [KERNEL](../provenance/inputs/draft6/sections/01C_relational_kernel.tex#L1-L68).

---

<a id="basis-vector-family"></a>

## Coordinate basis-vector family

**Stable ID:** `basis-vector-family`  
**Historical labels / lookup forms:** `e1`, `e2`, `e3`, `e_1`, `e_2`, `e_3`  
**Kind:** basis vectors  
**Domain:** Declared conservative/rotor comparison space  
**Standing:** Source-recorded; no original mathematical producer re-executed here.

The vectors e1,e2,e3 are coordinate basis vectors in the explicit comparison calculations. They are not completed events e_i merely because the same letter and index occur in event histories.

```text
e_i = ith coordinate basis vector in the specified space
```

**Keep distinct:** Basis choice and event registration require separate domains.

**Sources:** [CONSERVATIVE](../provenance/inputs/draft6/appendices/N_conservative_calculations.tex#L1-L128).

---

<a id="event-index-family"></a>

## Chronologically indexed events

**Stable ID:** `event-index-family`  
**Historical labels / lookup forms:** `e1`, `e2`, `e3`, `E1`, `E2`, `E3`, `e_1`, `e_2`, `e_3`  
**Kind:** event-record variable family  
**Domain:** Ordered QR event histories  
**Standing:** Source-recorded; no original mathematical producer re-executed here.

The event index specifies chronological position. It does not identify a frame character E_k, a face representation E2, or a coordinate vector e_k.

```text
(e1,r1) o (e2,r2) ...
```

**Keep distinct:** The variables are local to the declared history; no global equivalence is created by the index.

**Sources:** [BASE](../provenance/inputs/qr_core_terms_original.md#L1-L1982).

---

<a id="torsor-t-variables"></a>

## Selected-reference torsor elements

**Stable ID:** `torsor-t-variables`  
**Historical labels / lookup forms:** `t1`, `t2`, `t_1`, `t_2`  
**Kind:** torsor element variables  
**Domain:** Two-member orientation torsor in the reconciliation theorem  
**Standing:** Source-recorded; no original mathematical producer re-executed here.

The compared elements t1,t2 are points of a supplied orientation torsor. They are not times, a macro transport, or the Lie generators T_i.

```text
sigma_ref(t1) sigma_ref(t2)
```

**Keep distinct:** The comparison needs a declared torsor and action; naming its elements does not construct a cross-register map.

**Sources:** [INCIDENCE](../provenance/inputs/draft6/sections/03E_incidence_reconciliation.tex#L1-L126).

---

<a id="wxyz-a-variables"></a>

## Intermediate WXYZTI register entries

**Stable ID:** `wxyz-a-variables`  
**Historical labels / lookup forms:** `a1`, `a2`, `a_1`, `a_2`  
**Kind:** state-coordinate variables  
**Domain:** The source six-step closure argument  
**Standing:** Source-recorded; no original mathematical producer re-executed here.

The changed first-slot values in the displayed shared-output sequence. They are intermediate register values, not independent generators of an alternating group or new native graph vertices by convention.

```text
(a,b,c) -> (a1,b,t) -> ... -> (a2,t,c)
```

**Keep distinct:** The occurrence-dependent native endpoint/path assignment remains its own open crosswalk.

**Sources:** [WXYZ_CHOOSER](../provenance/inputs/draft6/provenance/draft3/wxyzti_chooser_exploration.md#L1-L71), [WXYZ_SECTION](../provenance/inputs/draft6/sections/03B_wxyzti.tex#L1-L54).

---

<a id="paired-coordinate-flags"></a>

## Paired u/v local relation indices

**Stable ID:** `paired-coordinate-flags`  
**Historical labels / lookup forms:** `u0`, `u1`, `u2`, `v0`, `v1`  
**Kind:** source-local coordinate/flag family  
**Domain:** Native input bundle Boolean relation fields  
**Standing:** Source-field names resolved as local index syntax; underlying relation meaning requires the enclosing record.

The input bundle contains flags such as u0_v0 and u0_v1. These are source-local paired indices, not continuous U(1)/U(2), and v1 in that context is not a schema version.

```text
Read the complete field name, e.g. u0_v1
```

**Keep distinct:** The registry does not assign unseen physical or group meaning to these Boolean field indices.

**Sources:** [BUNDLE_INPUT](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/sources/upstream/g60_native_generator_input_bundle_001.v1.json#L1-L2567).

---

<a id="su3-target"></a>

## SU(3) completion target

**Stable ID:** `su3-target`  
**Historical labels / lookup forms:** `SU3`, `SU(3)`  
**Kind:** unestablished continuous-group target  
**Domain:** Charge-Cartan source next-frontier list  
**Standing:** Explicitly uncompleted target.

The source lists SU3 completion among possible additional constraints on the charge algebra. It does not derive that completion or numerical Standard Model charges.

```text
Referenced next target: SU3 completion
```

**Keep distinct:** Not an admitted gauge group or a proved identification.

**Sources:** [CARTAN](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_order4_square_cartan_orientation_201h35b.v1.json#L1-L99).

---

<a id="su4-target"></a>

## Excluded physical SU(4) gauge identification

**Stable ID:** `su4-target`  
**Historical labels / lookup forms:** `SU4`, `SU(4)`  
**Kind:** unestablished interpretation target  
**Domain:** Boundary of the selected face-reflection audit  
**Standing:** Boundary-only occurrence; no admitted physical group.

The source expressly says no physical SU4 gauge claim is derived by its finite reflection selector. The label must therefore stay in the boundary/target bin, not the proved-structure column.

```text
physical SU4 gauge claim: not derived
```

**Keep distinct:** A C^4 representation is not proof of a physical SU4 gauge symmetry.

**Sources:** [RESIDUAL](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_signed_event_s1_torsor_selector_201h65b.v1.json#L1-L42).

---

<a id="periodic-t3"></a>

## Periodic three-torus Maxwell domain

**Stable ID:** `periodic-t3`  
**Historical labels / lookup forms:** `T^3`  
**Kind:** topological domain  
**Domain:** The conventional periodic Maxwell operator example  
**Standing:** Source-recorded; no original mathematical producer re-executed here.

The torus supplies the periodic function domain for the curl operator. The superscript denotes a threefold product, not the third power of an event transport T.

```text
T^3=(R/2pi Z)^3
```

**Keep distinct:** Not a finite C3 event-phase action or a native spatial derivation.

**Sources:** [CONSERVATIVE](../provenance/inputs/draft6/appendices/N_conservative_calculations.tex#L1-L128).

---

<a id="l2-field-space"></a>

## Square-integrable field space

**Stable ID:** `l2-field-space`  
**Historical labels / lookup forms:** `L2`, `L^2`  
**Kind:** function-space family  
**Domain:** Periodic Maxwell fields on the stated domain  
**Standing:** Source-recorded; no original mathematical producer re-executed here.

L^2 denotes a function-space integrability class. It is not the second inert complex line L2 or an appendix source identifier. Boundary and curl-domain conditions remain part of the operator specification.

```text
L^2(T^3; C^3)
```

**Keep distinct:** Do not infer a two-dimensional finite space from the exponent two.

**Sources:** [CONSERVATIVE](../provenance/inputs/draft6/appendices/N_conservative_calculations.tex#L1-L128).

---

<a id="k2-edge"></a>

## Two-vertex complete edge graph

**Stable ID:** `k2-edge`  
**Historical labels / lookup forms:** `K2`, `K_2`  
**Kind:** finite graph  
**Domain:** An individual edge component or Cartesian-product factor  
**Typed size:** Point/object count: 2  
**Standing:** Source notation and structure as recorded; no native producer rerun.

K2 is a complete graph on two vertices in 6K2 and C6 square K2. It is a component/factor, not the full six-edge orbital or the prism. A different K_2 in the face-envelope calculation is a Lie generator.

```text
K2: two vertices, one edge
```

**Keep distinct:** Keep graph component, disjoint union, Cartesian product, and operator-generator meanings separate.

**Sources:** [CONNECTION](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_u2_gauge_bridge_connection_frontier_checkpoint_201fp7.v1.json#L1-L190), [MACRO_EXCERPT](../provenance/excerpts/macro_and_support.md#L1-L10).

---

<a id="k6-component"></a>

## Complete six-vertex orbital component

**Stable ID:** `k6-component`  
**Historical labels / lookup forms:** `K6`, `K_6`  
**Kind:** finite graph  
**Domain:** A component of the same-phase 2K6 orbital  
**Typed size:** Point/object count: 6  
**Standing:** Source notation and structure as recorded; no native producer rerun.

The individual complete six-vertex graph in the disjoint union of two same-phase components. The source explicitly leaves the corresponding connection selection open.

```text
2K6 is two disjoint copies of K6
```

**Keep distinct:** A component is not the whole twelve-point orbital.

**Sources:** [CONNECTION](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_u2_gauge_bridge_connection_frontier_checkpoint_201fp7.v1.json#L1-L190).

---

<a id="c6-cycle-graph"></a>

## Six-cycle graph factor

**Stable ID:** `c6-cycle-graph`  
**Historical labels / lookup forms:** `C6`, `C_6`  
**Kind:** finite graph  
**Domain:** Hexagonal factor of the binary-support prism  
**Typed size:** Point/object count: 6  
**Standing:** Source notation and structure as recorded; no native producer rerun.

The six-vertex cycle appearing in C6 square K2. Its graph automorphism group and any selected cyclic transport would be additional objects, not consequences of using the graph name.

```text
C6: hexagonal cycle
```

**Keep distinct:** Not the six-position WXYZTI action without a domain map.

**Sources:** [MACRO_EXCERPT](../provenance/excerpts/macro_and_support.md#L1-L10).

---

<a id="integer-lattices"></a>

## Integral coordinate lattice family

**Stable ID:** `integer-lattices`  
**Historical labels / lookup forms:** `Z^3`, `Z^4`, `Z^9`  
**Kind:** free abelian group family  
**Domain:** Declared chain groups or Fourier-index lattices  
**Family parameters:** rank n and specified realization  
**Standing:** Source notation and structure as recorded; no native producer rerun.

Z^n denotes a rank-n free abelian group or integer lattice. For example, the four-generator cellular C1 group is Z^4, while periodic Maxwell Fourier indices lie in Z^3. These are not cyclic residues modulo n.

```text
Z^n with coordinatewise addition
```

**Keep distinct:** Preserve the coefficient ring and the actual chain/Fourier domain.

**Sources:** [WINDING](../provenance/inputs/PHASE_RELATION_CELLULAR_PROOF.md#L1-L392), [CONSERVATIVE](../provenance/inputs/draft6/appendices/N_conservative_calculations.tex#L1-L128).

---

<a id="power-expression"></a>

## Powers and repeated-composition notation

**Stable ID:** `power-expression`  
**Historical labels / lookup forms:** `F^5`, `S^5`, `a^2`, `b^2`, `r^4`, `J5^2`, `K5^2`  
**Kind:** syntax layer  
**Domain:** A previously defined operator, scalar, group element or set  
**Standing:** Explicit notation triage; local semantic context still required.

An exponent usually constructs a power of an already named object. It does not create a fresh letter-number label. Some superscripts instead indicate scalar-space dimension, cochain degree or a sphere; those meanings are named separately in this register.

```text
F^5 is the fifth power of F, not a new object called F5
```

**Keep distinct:** Read the base object and mathematical syntax. This bin is not a theorem that every superscript is an operator power.

**Sources:** [FRAMES](../provenance/inputs/native_g9000_map_test.md#L1-L295), [CHAT](../provenance/excerpts/current_chat_archive.md#L1-L21).

---

<a id="source-path-fragments"></a>

## Letter-number fragments inside source paths and schemas

**Stable ID:** `source-path-fragments`  
**Historical labels / lookup forms:** `g60`, `g30`, `g15`, `g900`, `g1800`, `g9000`, `c4`, `a5`, `v4`, `k22`, `p1`, `p3`, `d5`, `s1`, `s3`, `c3`, `c5`  
**Kind:** source-path reference family  
**Domain:** Filenames, URLs, schema keys and proof-check identifiers  
**Standing:** Metadata triage; source file identifies any referenced object.

Lower-case fragments in a path can refer to a named structure, but the whole source identifier is the object being indexed in that occurrence. No automatic case-folding equates arbitrary lower-case variables with upper-case group labels. Lowercase c3/c5 here occur in source filenames and HTML anchors; they are retained as locators rather than case-folded into mathematical C3/C5.

```text
Example: native_g60_...json is a source path mentioning G60
```

**Keep distinct:** A source-path reference is not another independent mathematical occurrence or a new native group.

**Sources:** [CENSUS](../provenance/inputs/draft6/sections/01A_census_family.tex#L1-L59), [CORE](../provenance/inputs/qr_core_terms_consolidated.md#L1-L3141), [BUNDLE_INPUT](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/sources/upstream/g60_native_generator_input_bundle_001.v1.json#L1-L2567).

---

<a id="three-section-coordinate"></a>

## Three-section coordinate set

**Stable ID:** `three-section-coordinate`  
**Historical labels / lookup forms:** `X3`, `X_3`  
**Kind:** finite coordinate set  
**Domain:** Three-state factor of the earlier twelve-section closure surface  
**Typed size:** Point/object count: 3  
**Standing:** Source-defined notation; no new mathematical producer run.

The source writes the section set as X12 ~= X3 x X4. X3 is the three-element coordinate set carrying the stated S3 permutation action. It is not the acting group itself and is not a three-dimensional vector space.

```text
|X3|=3; (sigma,d).(s,q)=(sigma(s),d(q))
```

**Keep distinct:** Keep separate from the C3 rotation subgroup, full S3 action, and the normalized Z3 coordinate in the relational-kernel model until the specific coordinate comparison is supplied.

**Recorded relationships:** [x12-sections](#x12-sections) (coordinate factor).

**Sources:** [OLDER_SECTION_SURFACE](../provenance/excerpts/older_section_surface.md#L1-L9).

---

<a id="initial-history-prefix"></a>

## Initial history prefix for a freedom comparison

**Stable ID:** `initial-history-prefix`  
**Historical labels / lookup forms:** `h0`, `h_0`  
**Kind:** history-variable role  
**Domain:** Specified initial prefix in the finite-frame freedom comparison  
**Standing:** Source-defined notation; no new mathematical producer run.

h0 marks the reference prefix from which resolved freedom is measured. Its zero subscript identifies its role in the comparison, not a zero-degree homology group or a fixed native state number.

```text
R_W(h)=F_W(h0)-F_W(h)
```

**Keep distinct:** The choice of initial history and the fixed completion universe are part of the comparison. Do not confuse h0 with H_0 homology.

**Sources:** [CORE](../provenance/inputs/qr_core_terms_consolidated.md#L1-L3141).

---

<a id="predictive-history-test-pair"></a>

## Histories compared for predictive equivalence

**Stable ID:** `predictive-history-test-pair`  
**Historical labels / lookup forms:** `h1`, `h2`, `h_1`, `h_2`  
**Kind:** indexed history variables  
**Domain:** Two histories evaluated against the same future-language and response criterion  
**Standing:** Source-defined notation; no new mathematical producer run.

The indices distinguish the two arguments of predictive equivalence. They do not designate the native two-state alphabet {2,3}, homology groups H1/H2, or an ordered generator list.

```text
h1 ~_pred h2 iff L(h1)=L(h2) and O(h1,w)=O(h2,w) for all w in the common admitted language
```

**Keep distinct:** Agreement on only some intersecting tests is weaker than this definition. The labels are variables, not newly defined carriers.

**Sources:** [CORE](../provenance/inputs/qr_core_terms_consolidated.md#L1-L3141).

---

<a id="t10-native-macro"></a>

## Native decagonal macro-history actor

**Stable ID:** `t10-native-macro`  
**Historical labels / lookup forms:** `T10`, `T_10`  
**Kind:** native permutation / named actor  
**Domain:** Selected native G60 macro transport, with separately reported six-axis image  
**Standing:** Source-recorded; no historical producer re-executed in this sweep.

T10 is the named actor used by the macro-history alphabet. The inherited source records T10^5=b and T10^10=I. Its conference image has even orientation and a five-cycle plus a fixed analyzer axis. The complete native action and its quotient image have different orders.

```text
Native: T10^5=b, T10^10=I; conference quotient: order 5, cycle type 5+1
```

**Keep distinct:** Not the generated subgroup <T10> itself. Not the same-face reverse-edge connection T_10=T_01^-1, and not F_reg^2. Full actor provenance is inherited, not replayed here.

**Recorded relationships:** [c10-native](#c10-native) (generates); [t01-edge-connection](#t01-edge-connection) (notation collision).

**Sources:** [MACRO_EXCERPT](../provenance/excerpts/macro_and_support.md#L1-L10), [CONF_ACTION](../provenance/inputs/thalean_transport_conference_bridge_audit.json#L1-L123), [CORE](../provenance/inputs/qr_core_terms_consolidated.md#L1-L3141).

---

<a id="h40-dart-incidence"></a>

## Two-dodecahedral dart-incidence graph reference

**Stable ID:** `h40-dart-incidence`  
**Historical labels / lookup forms:** `H40`, `h40`  
**Kind:** source-referenced finite graph  
**Domain:** Graph pairing dart descriptions of the native sixty states  
**Typed size:** Point/object count: 40  
**Standing:** Source-recorded; no historical producer re-executed in this sweep.

An upstream verdict preserved in the signed-face audit names h40 as the graph whose sixty edges pair the sixty dart descriptions from two complementary dodecahedral graphs. It associates the forty native G60 triangles with the twenty plus twenty vertex stars. This supplies a graph role for the label, but not the full original edge table in this sweep.

```text
Reported correspondence: 60 G60 states <-> 60 h40 edges; 40 G60 triangles <-> 20+20 vertex stars
```

**Keep distinct:** Do not confuse this graph reference with frontier H40, homology, or an abstract group of order forty. Original audit024 adjacency and exact maps remain to be recovered.

**Sources:** [H40_REFERENCE](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/json/signed_24_face_block_closure_audit_025.json#L3751-L3755).

---

<a id="escaped-string-fragment"></a>

## Serialized escape-sequence false matches

**Stable ID:** `escaped-string-fragment`  
**Historical labels / lookup forms:** `n0`, `n1`  
**Kind:** lexical false-positive bin  
**Domain:** JSON strings containing escaped newline followed by a digit  
**Standing:** Scanner artifact, not a mathematical object.

The raw text pattern can match n0 inside a JSON escape such as backslash-n followed by 0. That is not an indexed variable n0. The occurrence inventory preserves it and flags the escape context.

```text
JSON raw text: \n0
```

**Keep distinct:** Do not create a mathematical structure from a serialization artifact.

**Sources:** [CORE](../provenance/inputs/qr_core_terms_consolidated.md#L1-L3141).

---

## Source anchor index

- **ANALYZER**: [provenance/inputs/native_analyzer_constraints.md](../provenance/inputs/native_analyzer_constraints.md), lines 1-450; source-recorded.
- **BASE**: [provenance/inputs/qr_core_terms_original.md](../provenance/inputs/qr_core_terms_original.md), lines 1-1982; superseded-baseline.
- **BUNDLE**: [provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_r1_face_bundle_cocycle_triviality_201h69g.v1.json](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_r1_face_bundle_cocycle_triviality_201h69g.v1.json), lines 1-50; source-recorded.
- **BUNDLE_INPUT**: [provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/sources/upstream/g60_native_generator_input_bundle_001.v1.json](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/sources/upstream/g60_native_generator_input_bundle_001.v1.json), lines 1-2567; source-recorded.
- **CARTAN**: [provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_order4_square_cartan_orientation_201h35b.v1.json](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_order4_square_cartan_orientation_201h35b.v1.json), lines 1-99; source-recorded.
- **CENSUS**: [provenance/inputs/draft6/sections/01A_census_family.tex](../provenance/inputs/draft6/sections/01A_census_family.tex), lines 1-59; source-recorded.
- **CENSUS_REPORT**: [provenance/inputs/draft6/data/generated/census_family_report.json](../provenance/inputs/draft6/data/generated/census_family_report.json), lines 1-5852; source-recorded.
- **CHAT**: [provenance/excerpts/current_chat_archive.md](../provenance/excerpts/current_chat_archive.md), lines 1-21; conversation-reported.
- **CIRCLES**: [provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_positive_pair_hermitian_geometry_201fv.v1.json](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_positive_pair_hermitian_geometry_201fv.v1.json), lines 1-116; source-recorded.
- **CLIFF**: [provenance/inputs/thalean_registered_history_clifford_measure_audit.json](../provenance/inputs/thalean_registered_history_clifford_measure_audit.json), lines 1-54; source-recorded.
- **COMPANION_TRIALITY**: [provenance/excerpts/companion_triality.md](../provenance/excerpts/companion_triality.md), lines 1-9; selected-source-digest.
- **CONF_ACTION**: [provenance/inputs/thalean_transport_conference_bridge_audit.json](../provenance/inputs/thalean_transport_conference_bridge_audit.json), lines 1-123; source-recorded.
- **CONNECTION**: [provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_u2_gauge_bridge_connection_frontier_checkpoint_201fp7.v1.json](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_u2_gauge_bridge_connection_frontier_checkpoint_201fp7.v1.json), lines 1-190; source-recorded.
- **CONSERVATIVE**: [provenance/inputs/draft6/appendices/N_conservative_calculations.tex](../provenance/inputs/draft6/appendices/N_conservative_calculations.tex), lines 1-128; source-recorded.
- **CORE**: [provenance/inputs/qr_core_terms_consolidated.md](../provenance/inputs/qr_core_terms_consolidated.md), lines 1-3141; secondary-glossary.
- **COVER**: [provenance/inputs/draft6/sections/01B_common_cover.tex](../provenance/inputs/draft6/sections/01B_common_cover.tex), lines 1-101; source-recorded.
- **D5_KERNEL**: [provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_d5_kernel_naturality_201fqb.v1.json](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_d5_kernel_naturality_201fqb.v1.json), lines 1-70; source-recorded.
- **DECAGON_STABILIZERS**: [provenance/excerpts/decagon_stabilizers.md](../provenance/excerpts/decagon_stabilizers.md), lines 1-9; selected-source-digest.
- **DYN_TARGETS**: [provenance/inputs/draft6/appendices/L2_dynamical_targets.tex](../provenance/inputs/draft6/appendices/L2_dynamical_targets.tex), lines 1-25; source-recorded.
- **EPR**: [provenance/inputs/native_epr_history_control.md](../provenance/inputs/native_epr_history_control.md), lines 1-74; source-recorded.
- **FACE**: [provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_face_field_higgs_bridge_checkpoint_receipt_201fk.v1.json](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_face_field_higgs_bridge_checkpoint_receipt_201fk.v1.json), lines 1-144; source-recorded.
- **FACE_SCOPE**: [provenance/inputs/draft6/appendices/O_reference_audit.tex](../provenance/inputs/draft6/appendices/O_reference_audit.tex), lines 1-82; source-recorded.
- **FP**: [provenance/inputs/native_g60_fiber_product_isomorphism_044.json](../provenance/inputs/native_g60_fiber_product_isomorphism_044.json), lines 37805-37814; source-recorded.
- **FRAMES**: [provenance/inputs/native_g9000_map_test.md](../provenance/inputs/native_g9000_map_test.md), lines 1-295; source-recorded.
- **GLOSS**: [provenance/inputs/thalean_glossary_previous.md](../provenance/inputs/thalean_glossary_previous.md), lines 1-4227; secondary-glossary.
- **GOLDEN_LATTICE**: [provenance/excerpts/golden_lattice.md](../provenance/excerpts/golden_lattice.md), lines 1-9; selected-source-digest.
- **H40_REFERENCE**: [provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/json/signed_24_face_block_closure_audit_025.json](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/json/signed_24_face_block_closure_audit_025.json), lines 3751-3755; quoted-upstream-verdict-in-retained-audit.
- **HIST**: [provenance/inputs/thalean_registered_history_conference_operator_audit.json](../provenance/inputs/thalean_registered_history_conference_operator_audit.json), lines 1-564; source-recorded.
- **HISTORICAL_FIVEFOLD**: [provenance/excerpts/historical_fivefold.md](../provenance/excerpts/historical_fivefold.md), lines 1-9; selected-source-digest.
- **HISTORY_CLASSES**: [provenance/inputs/draft6/appendices/E_history.tex](../provenance/inputs/draft6/appendices/E_history.tex), lines 1-26; source-recorded.
- **HISTORY_PHASE**: [provenance/inputs/draft6/sections/03F_history_phase_groupoid.tex](../provenance/inputs/draft6/sections/03F_history_phase_groupoid.tex), lines 1-66; source-recorded.
- **HISTORY_TIME**: [provenance/inputs/draft6/sections/03_information_history_time.tex](../provenance/inputs/draft6/sections/03_information_history_time.tex), lines 1-87; source-recorded.
- **INCIDENCE**: [provenance/inputs/draft6/sections/03E_incidence_reconciliation.tex](../provenance/inputs/draft6/sections/03E_incidence_reconciliation.tex), lines 1-126; source-recorded.
- **KERNEL**: [provenance/inputs/draft6/sections/01C_relational_kernel.tex](../provenance/inputs/draft6/sections/01C_relational_kernel.tex), lines 1-68; source-recorded.
- **LINES**: [provenance/inputs/draft6/provenance/draft6/native_snapshot/program02/artifacts/json/epr_reference_gauge_projective_line_map_018.v1.json](../provenance/inputs/draft6/provenance/draft6/native_snapshot/program02/artifacts/json/epr_reference_gauge_projective_line_map_018.v1.json), lines 1-775; source-recorded.
- **MACRO_EXCERPT**: [provenance/excerpts/macro_and_support.md](../provenance/excerpts/macro_and_support.md), lines 1-10; selected-source-digest.
- **MAXWELL**: [provenance/inputs/draft6/sections/09C_maxwell.tex](../provenance/inputs/draft6/sections/09C_maxwell.tex), lines 1-93; source-recorded.
- **MEASURE**: [provenance/inputs/draft6/sections/05_measure_registration.tex](../provenance/inputs/draft6/sections/05_measure_registration.tex), lines 1-57; source-recorded.
- **MM**: [provenance/inputs/C107.json](../provenance/inputs/C107.json), lines 1-44; source-recorded.
- **MODE**: [provenance/inputs/draft6/sections/03A_mode.tex](../provenance/inputs/draft6/sections/03A_mode.tex), lines 1-69; source-recorded.
- **NATIVE_REPORT**: [provenance/inputs/draft6/data/generated/draft6_native_incidence_groupoid_report.json](../provenance/inputs/draft6/data/generated/draft6_native_incidence_groupoid_report.json), lines 1-16892; source-recorded.
- **NEUTRAL**: [provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_neutral_generator_anatomy_201fw.v1.json](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_neutral_generator_anatomy_201fw.v1.json), lines 1-152; source-recorded.
- **OLDER_SECTION_SURFACE**: [provenance/excerpts/older_section_surface.md](../provenance/excerpts/older_section_surface.md), lines 1-9; selected-source-digest.
- **PARTITIONS**: [provenance/inputs/draft6/provenance/draft6/native_snapshot/program02/artifacts/json/epr_native_face_projective_line_partition_017.v1.json](../provenance/inputs/draft6/provenance/draft6/native_snapshot/program02/artifacts/json/epr_native_face_projective_line_partition_017.v1.json), lines 1-566; source-recorded.
- **QUOTIENTS**: [provenance/inputs/draft6/appendices/C_quotient_tower.tex](../provenance/inputs/draft6/appendices/C_quotient_tower.tex), lines 1-20; source-recorded.
- **REFLECTION**: [provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_selected_reflection_event_pauli_anatomy_201h67b.v1.json](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_selected_reflection_event_pauli_anatomy_201h67b.v1.json), lines 1-41; source-recorded.
- **RESIDUAL**: [provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_signed_event_s1_torsor_selector_201h65b.v1.json](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_signed_event_s1_torsor_selector_201h65b.v1.json), lines 1-42; source-recorded.
- **SCALAR**: [provenance/inputs/draft6/sections/03C_scalar_relay.tex](../provenance/inputs/draft6/sections/03C_scalar_relay.tex), lines 1-88; source-recorded.
- **SEAM**: [provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_registered_seam_world_address_crosswalk_201bd.v1.json](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_registered_seam_world_address_crosswalk_201bd.v1.json), lines 1-1844; source-recorded.
- **SIGNED_AXIS**: [provenance/inputs/draft6/sections/05A_signed_axis_reference.tex](../provenance/inputs/draft6/sections/05A_signed_axis_reference.tex), lines 1-86; source-recorded.
- **SURFACE**: [provenance/inputs/README(20260920-001150).md](../provenance/inputs/README(20260920-001150).md), lines 1-300; source-recorded.
- **TWISTED**: [provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_6k2_twisted_selector_covariance_201fqd.v1.json](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_6k2_twisted_selector_covariance_201fqd.v1.json), lines 1-91; source-recorded.
- **U2**: [provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_event_vector_u2_u1_stabilizer_201ft.v1.json](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_event_vector_u2_u1_stabilizer_201ft.v1.json), lines 1-71; source-recorded.
- **WINDING**: [provenance/inputs/PHASE_RELATION_CELLULAR_PROOF.md](../provenance/inputs/PHASE_RELATION_CELLULAR_PROOF.md), lines 1-392; source-recorded.
- **WXYZ**: [provenance/inputs/draft6/provenance/draft3/wxyzti_contract_reconciliation.md](../provenance/inputs/draft6/provenance/draft3/wxyzti_contract_reconciliation.md), lines 1-68; source-recorded.
- **WXYZ_CHOOSER**: [provenance/inputs/draft6/provenance/draft3/wxyzti_chooser_exploration.md](../provenance/inputs/draft6/provenance/draft3/wxyzti_chooser_exploration.md), lines 1-71; source-recorded.
- **WXYZ_SECTION**: [provenance/inputs/draft6/sections/03B_wxyzti.tex](../provenance/inputs/draft6/sections/03B_wxyzti.tex), lines 1-54; source-recorded.
