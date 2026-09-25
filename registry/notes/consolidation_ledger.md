# Consolidation and relationship ledger

Date: 2026-09-24

These are archival decisions about source evidence, not newly executed mathematical theorems. A relationship never silently overwrites either endpoint's domain. In particular, quotient, subgroup, representation, normalization, common type, and common numeric size are not synonym relations.

**Consolidation now** means that a source identifies an entity or supplies the stated map. Keep separate view IDs when the domain, ambient group, representation, coefficient field or marking differs. **Hold** means a specific original producer or action-level crosswalk is still needed. No new native identification is admitted in this file merely by assigning a name.

## 01. Native G60 rooted-neighborhood stabilizer / Petersen-edge positional stabilizer

**Relation:** faithful descent  
**Decision:** link views keep domains

The manuscript supplies the rooted descent. Different ambient groups and selected roots remain part of each view.

Views: [d8-native-root](qr_structure_registry.md#d8-native-root); [d8-position](qr_structure_registry.md#d8-position).  
Sources: [COVER](../provenance/inputs/draft6/sections/01B_common_cover.tex#L1-L101), [MM](../provenance/inputs/C107.json#L1-L44).

## 02. Common-cover rooted stabilizer / Petersen-edge positional stabilizer

**Relation:** faithful descent  
**Decision:** link views keep domains

The source reports an injective and onto rooted-stabilizer map, not identity of upstairs and downstairs points.

Views: [d8-cover-root](qr_structure_registry.md#d8-cover-root); [d8-position](qr_structure_registry.md#d8-position).  
Sources: [COVER](../provenance/inputs/draft6/sections/01B_common_cover.tex#L1-L101), [CENSUS_REPORT](../provenance/inputs/draft6/data/generated/census_family_report.json#L1-L5852).

## 03. Sixty-vertex census-family child 6 / Thalion native graph carrier

**Relation:** source identified graph  
**Decision:** consolidate entity keep census view

Child G6 is source-identified with native G60. Preserve the explicit vertex-label crosswalk and the census view.

Views: [g-family-6](qr_structure_registry.md#g-family-6); [g60-native](qr_structure_registry.md#g60-native).  
Sources: [COVER](../provenance/inputs/draft6/sections/01B_common_cover.tex#L1-L101).

## 04. Common AT4val-family bipartite cover graph / Thalion native graph carrier

**Relation:** canonical double cover  
**Decision:** link not alias

The common cover has an extra sheet and a projection to the native graph; these are not aliases.

Views: [k120-common-cover](qr_structure_registry.md#k120-common-cover); [g60-native](qr_structure_registry.md#g60-native).  
Sources: [COVER](../provenance/inputs/draft6/sections/01B_common_cover.tex#L1-L101).

## 05. Common cover-family thirty-vertex intermediate / Original native central-deck quotient graph

**Relation:** distinct graphs  
**Decision:** do not merge

The source explicitly identifies two different thirty-vertex line graphs.

Views: [q30-family](qr_structure_registry.md#q30-family); [g30-original](qr_structure_registry.md#g30-original).  
Sources: [COVER](../provenance/inputs/draft6/sections/01B_common_cover.tex#L1-L101).

## 06. Registered two-factor native product quotient family / Associated Delta quotient of a registered G1800 carrier

**Relation:** quotient  
**Decision:** link not alias

The midpoint involution has two-point fibers. G900 is the associated quotient, not another name for G1800.

Views: [g1800-family](qr_structure_registry.md#g1800-family); [g900-associated](qr_structure_registry.md#g900-associated).  
Sources: [FRAMES](../provenance/inputs/native_g9000_map_test.md#L1-L295).

## 07. Registered five-frame native groupoid carrier / Registered two-factor native product quotient family

**Relation:** five registered frames  
**Decision:** link not alias

Five registered frames and their transport maps are additional structure over a local G1800 carrier.

Views: [g9000-registered](qr_structure_registry.md#g9000-registered); [g1800-family](qr_structure_registry.md#g1800-family).  
Sources: [FRAMES](../provenance/inputs/native_g9000_map_test.md#L1-L295).

## 08. Native face realization kernel / Native face-family ambient stabilizer

**Relation:** kernel embedding  
**Decision:** link not alias

The order-ten kernel is embedded in the order-eighty face stabilizer.

Views: [d5-face-kernel](qr_structure_registry.md#d5-face-kernel); [face-stabilizer](qr_structure_registry.md#face-stabilizer).  
Sources: [D5_KERNEL](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_d5_kernel_naturality_201fqb.v1.json#L1-L70).

## 09. Native face-family ambient stabilizer / Four-signed-block face permutation group

**Relation:** permutation image  
**Decision:** link not alias

The order-eighty stabilizer and order-eight image differ by the order-ten realization kernel.

Views: [face-stabilizer](qr_structure_registry.md#face-stabilizer); [d8-face-blocks](qr_structure_registry.md#d8-face-blocks).  
Sources: [FACE](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_face_field_higgs_bridge_checkpoint_receipt_201fk.v1.json#L1-L144).

## 10. Native face realization kernel / Historical fivefold rotation-reflection register

**Relation:** same abstract type only  
**Decision:** hold for action crosswalk

An order-ten dihedral presentation alone does not identify these two native roles.

Views: [d5-face-kernel](qr_structure_registry.md#d5-face-kernel); [d5-history](qr_structure_registry.md#d5-history).  
Sources: [D5_KERNEL](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_d5_kernel_naturality_201fqb.v1.json#L1-L70), [HISTORICAL_FIVEFOLD](../provenance/excerpts/historical_fivefold.md#L1-L9).

## 11. Selected face complex/reflection operator group / Charge-center dihedral comparison target

**Relation:** named comparison target  
**Decision:** unresolved

The source lists this comparison as a next target, not a completed identity.

Views: [d8-selected-face-operators](qr_structure_registry.md#d8-selected-face-operators); [d8-charge-center-locator](qr_structure_registry.md#d8-charge-center-locator).  
Sources: [RESIDUAL](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_signed_event_s1_torsor_selector_201h65b.v1.json#L1-L42).

## 12. Selected face complex/reflection operator group / Four-signed-block face permutation group

**Relation:** shared group type distinct action  
**Decision:** hold for action crosswalk

One action is by complex/reflection operators, the other by signed-block permutations. No intertwiner is assumed.

Views: [d8-selected-face-operators](qr_structure_registry.md#d8-selected-face-operators); [d8-face-blocks](qr_structure_registry.md#d8-face-blocks).  
Sources: [RESIDUAL](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_signed_event_s1_torsor_selector_201h65b.v1.json#L1-L42), [FACE](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_face_field_higgs_bridge_checkpoint_receipt_201fk.v1.json#L1-L144).

## 13. Surface reference edge-transport group / Dihedral lifted surface loop holonomy

**Relation:** distinct extension levels  
**Decision:** do not merge

Before lifting, D8 contains edge values and V4 is the loop group. The lifted loop D8 is an upstairs object.

Views: [d8-surface-edges](qr_structure_registry.md#d8-surface-edges); [d8-lifted-holonomy](qr_structure_registry.md#d8-lifted-holonomy).  
Sources: [SURFACE](../provenance/inputs/README(20260920-001150).md#L1-L300).

## 14. Dihedral lifted surface loop holonomy / Native G60 rooted-neighborhood stabilizer

**Relation:** extension type compatibility  
**Decision:** same type not elementwise identity

The surface source limits the comparator match to extension type and retains nonuniqueness of the lift.

Views: [d8-lifted-holonomy](qr_structure_registry.md#d8-lifted-holonomy); [d8-native-root](qr_structure_registry.md#d8-native-root).  
Sources: [SURFACE](../provenance/inputs/README(20260920-001150).md#L1-L300), [MM](../provenance/inputs/C107.json#L1-L44).

## 15. Quaternionic alternative surface loop holonomy / Dihedral lifted surface loop holonomy

**Relation:** nonisomorphic alternatives  
**Decision:** do not merge

The element-order profiles differ; the quaternionic branch has only one involution.

Views: [q8-lifted-holonomy](qr_structure_registry.md#q8-lifted-holonomy); [d8-lifted-holonomy](qr_structure_registry.md#d8-lifted-holonomy).  
Sources: [SURFACE](../provenance/inputs/README(20260920-001150).md#L1-L300).

## 16. Registered phase-group dihedral factor / Four-phase coset permutation image

**Relation:** factor vs action image  
**Decision:** link keep embedding

One is the embedded dihedral factor; the other is the faithful permutation image of Gamma on four cosets.

Views: [d8-history-factor](qr_structure_registry.md#d8-history-factor); [history-coset-image](qr_structure_registry.md#history-coset-image).  
Sources: [HISTORY_PHASE](../provenance/inputs/draft6/sections/03F_history_phase_groupoid.tex#L1-L66).

## 17. Native free normal Klein deck register / Fiber-product parity-character Klein kernel

**Relation:** explicit model isomorphism  
**Decision:** link views keep coordinates

The full source isomorphism aligns the model kernel with native data; the group order alone would not.

Views: [v4-native](qr_structure_registry.md#v4-native); [v4-fp-kernel](qr_structure_registry.md#v4-fp-kernel).  
Sources: [FP](../provenance/inputs/native_g60_fiber_product_isomorphism_044.json#L37805-L37814).

## 18. Native free normal Klein deck register / Klein-valued quotient voltage label group

**Relation:** coefficient to deck identification  
**Decision:** conditional on voltage chart

A declared voltage chart uses native deck elements, while its edge assignment remains gauge dependent.

Views: [v4-native](qr_structure_registry.md#v4-native); [v4-voltage](qr_structure_registry.md#v4-voltage).  
Sources: [CORE](../provenance/inputs/qr_core_terms_consolidated.md#L1-L3141).

## 19. Native free normal Klein deck register / Rooted dihedral central quotient plane

**Relation:** same abstract type only  
**Decision:** hold for native crosswalk

No native identification of the rooted central quotient with the free deck register is inferred.

Views: [v4-native](qr_structure_registry.md#v4-native); [v4-root-projective](qr_structure_registry.md#v4-root-projective).  
Sources: [CORE](../provenance/inputs/qr_core_terms_consolidated.md#L1-L3141), [HISTORICAL_FIVEFOLD](../provenance/excerpts/historical_fivefold.md#L1-L9).

## 20. Rooted-comparator central subgroup / Native G60-to-G30 central deck subgroup

**Relation:** distinct native permutations  
**Decision:** do not merge

The relevant nonidentity native permutations fix four versus zero vertices.

Views: [c2-root-center](qr_structure_registry.md#c2-root-center); [c2-native-double-deck](qr_structure_registry.md#c2-native-double-deck).  
Sources: [MM](../provenance/inputs/C107.json#L1-L44).

## 21. Extra central factor of Gamma_hist / Constant kernel of the four-phase history action

**Relation:** distinct embedded subgroups  
**Decision:** do not merge

The source explicitly distinguishes <z> and <r^2 z> inside the phase group.

Views: [c2-history-extra](qr_structure_registry.md#c2-history-extra); [c2-history-kernel](qr_structure_registry.md#c2-history-kernel).  
Sources: [HISTORY_PHASE](../provenance/inputs/draft6/sections/03F_history_phase_groupoid.tex#L1-L66).

## 22. Central global sign in the signed-axis extension / Analyzer-sector exchange quotient

**Relation:** central sign vs sector character  
**Decision:** do not merge

The central sign and sector character belong to different order-120 groups with different centers.

Views: [c2-axis-central](qr_structure_registry.md#c2-axis-central); [c2-analyzer-sector](qr_structure_registry.md#c2-analyzer-sector).  
Sources: [SIGNED_AXIS](../provenance/inputs/draft6/sections/05A_signed_axis_reference.tex#L1-L86).

## 23. Composite elementary-abelian eight-fold deck group / Native G60 rooted-neighborhood stabilizer

**Relation:** nonisomorphic group types  
**Decision:** do not merge

The elementary-abelian deck has no element of order four; D8 does.

Views: [c2-threefold-deck](qr_structure_registry.md#c2-threefold-deck); [d8-native-root](qr_structure_registry.md#d8-native-root).  
Sources: [COVER](../provenance/inputs/draft6/sections/01B_common_cover.tex#L1-L101).

## 24. Abstract Klein automorphism triality / Native register-orientation quotient action

**Relation:** full abstract vs native image  
**Decision:** do not merge

Native conjugation realizes only C2, not the full abstract Aut(V4)=S3.

Views: [s3-abstract-klein](qr_structure_registry.md#s3-abstract-klein); [c2-register-parity](qr_structure_registry.md#c2-register-parity).  
Sources: [ANALYZER](../provenance/inputs/native_analyzer_constraints.md#L1-L450), [CORE](../provenance/inputs/qr_core_terms_consolidated.md#L1-L3141).

## 25. Event phase-Mode permutation action / Registered event-frame cyclic phase action

**Relation:** generated subgroup  
**Decision:** link not alias

The phase generator generates the order-three subgroup of the specified six-element event action.

Views: [s3-mode](qr_structure_registry.md#s3-mode); [c3-mode](qr_structure_registry.md#c3-mode).  
Sources: [MODE](../provenance/inputs/draft6/sections/03A_mode.tex#L1-L69).

## 26. Native five-address quotient symmetry / Six-Sylow-axis quotient permutation action

**Relation:** same group different representation  
**Decision:** link views keep domains

The six-axis action is a representation of the same quotient group on a different domain.

Views: [s5-native-quotient](qr_structure_registry.md#s5-native-quotient); [s5-six-axes](qr_structure_registry.md#s5-six-axes).  
Sources: [CONF_ACTION](../provenance/inputs/thalean_transport_conference_bridge_audit.json#L1-L123).

## 27. Split within-sector signed-axis extension / Two-sector projective analyzer symmetry

**Relation:** nonisomorphic groups of equal order  
**Decision:** do not merge

The within-sector extension has a central global sign, while the sector S5 has trivial center.

Views: [signed-axis-extension](qr_structure_registry.md#signed-axis-extension); [s5-analyzer-sectors](qr_structure_registry.md#s5-analyzer-sectors).  
Sources: [SIGNED_AXIS](../provenance/inputs/draft6/sections/05A_signed_axis_reference.tex#L1-L86).

## 28. Twelve-section closure surface state set / Twelve-point normalized relational-kernel carrier

**Relation:** similar count and product shape  
**Decision:** hold for source crosswalk

The two twelve-point descriptions retain different supplied relation and action data; the count does not identify them.

Views: [x12-sections](qr_structure_registry.md#x12-sections); [x12-kernel](qr_structure_registry.md#x12-kernel).  
Sources: [OLDER_SECTION_SURFACE](../provenance/excerpts/older_section_surface.md#L1-L9), [KERNEL](../provenance/inputs/draft6/sections/01C_relational_kernel.tex#L1-L68).

## 29. Twelve-point normalized relational-kernel carrier / Twelve directed-pair descriptor bins

**Relation:** points vs pair partition  
**Decision:** do not merge

Twelve points are not twelve bins, each containing eight ordered pairs.

Views: [x12-kernel](qr_structure_registry.md#x12-kernel); [twelve-pair-descriptors](qr_structure_registry.md#twelve-pair-descriptors).  
Sources: [KERNEL](../provenance/inputs/draft6/sections/01C_relational_kernel.tex#L1-L68).

## 30. Twelve face/relative-orientation objects / Registered-pentagon coefficient module

**Relation:** finite set vs vector space  
**Decision:** do not merge

Twelve face-phase objects are not vectors in a twelve-dimensional pentagon coefficient space.

Views: [twelve-face-phases](qr_structure_registry.md#twelve-face-phases); [history-pentagon-space](qr_structure_registry.md#history-pentagon-space).  
Sources: [CONNECTION](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_u2_gauge_bridge_connection_frontier_checkpoint_201fp7.v1.json#L1-L190), [HIST](../provenance/inputs/thalean_registered_history_conference_operator_audit.json#L1-L564).

## 31. Opposite-phase different-face crown orbital / Registered-pentagon conference support graph

**Relation:** same graph type only  
**Decision:** hold for vertex action crosswalk

Crown graph isomorphism does not identify face-phase objects with pentagon generators.

Views: [face-crown](qr_structure_registry.md#face-crown); [history-crown](qr_structure_registry.md#history-crown).  
Sources: [CONNECTION](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_u2_gauge_bridge_connection_frontier_checkpoint_201fp7.v1.json#L1-L190), [HIST](../provenance/inputs/thalean_registered_history_conference_operator_audit.json#L1-L564).

## 32. Five-frame golden contrast operator / Historical-register golden contrast operator

**Relation:** same formal group ring polynomial  
**Decision:** hold for native intertwiner

The group-ring polynomial is shared, but the represented cyclic actions remain separately sourced.

Views: [frame-contrast](qr_structure_registry.md#frame-contrast); [history-fivefold-contrast](qr_structure_registry.md#history-fivefold-contrast).  
Sources: [CHAT](../provenance/excerpts/current_chat_archive.md#L1-L21), [HISTORICAL_FIVEFOLD](../provenance/excerpts/historical_fivefold.md#L1-L9).

## 33. Real five-frame oriented difference operator / Hermitian five-frame current operator

**Relation:** scalar complexification relation  
**Decision:** link not alias

H5=iD5: one is real skew-symmetric, the other Hermitian after complexification.

Views: [frame-difference](qr_structure_registry.md#frame-difference); [frame-hermitian-current](qr_structure_registry.md#frame-hermitian-current).  
Sources: [CHAT](../provenance/excerpts/current_chat_archive.md#L1-L21).

## 34. Five-frame index-doubling permutation / Piecewise five-frame golden-sector exchange

**Relation:** piecewise operator construction  
**Decision:** link not alias

Z5 uses U2 and its inverse on opposite sectors; it is not the raw coordinate multiplier.

Views: [frame-multiplier](qr_structure_registry.md#frame-multiplier); [frame-sector-exchange](qr_structure_registry.md#frame-sector-exchange).  
Sources: [CHAT](../provenance/excerpts/current_chat_archive.md#L1-L21).

## 35. Five-frame index-doubling permutation / Continuous unitary envelope of a selected face complex fiber

**Relation:** permutation vs continuous group  
**Decision:** do not merge

The coordinate permutation U_2 and continuous group U(2) have different types and domains.

Views: [frame-multiplier](qr_structure_registry.md#frame-multiplier); [u2-face-envelope](qr_structure_registry.md#u2-face-envelope).  
Sources: [CHAT](../provenance/excerpts/current_chat_archive.md#L1-L21), [U2](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_event_vector_u2_u1_stabilizer_201ft.v1.json#L1-L71).

## 36. Connection-selected anti-complex face reflection / Unit-circle phase space

**Relation:** operator vs circle  
**Decision:** do not merge

The reflection operator S_1 and circle S^1 are not variants of a single name.

Views: [s1-residual-reflection](qr_structure_registry.md#s1-residual-reflection); [circle-space](qr_structure_registry.md#circle-space).  
Sources: [RESIDUAL](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_signed_event_s1_torsor_selector_201h65b.v1.json#L1-L42), [U2](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_event_vector_u2_u1_stabilizer_201ft.v1.json#L1-L71).

## 37. Connection-selected anti-complex face reflection / Selected native exchange-square residual

**Relation:** fiber actor vs base bundle action  
**Decision:** do not merge

The source explicitly says the native residual r1 is not the vertical S1 operator.

Views: [s1-residual-reflection](qr_structure_registry.md#s1-residual-reflection); [r1-native-residual](qr_structure_registry.md#r1-native-residual).  
Sources: [BUNDLE](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_r1_face_bundle_cocycle_triviality_201h69g.v1.json#L1-L50).

## 38. Selected native exchange-square residual / Primitive registered-history winding class

**Relation:** permutation vs homology class  
**Decision:** do not merge

A permutation and a primitive homology class cannot be identified from a shared r1 spelling.

Views: [r1-native-residual](qr_structure_registry.md#r1-native-residual); [r1-history-class](qr_structure_registry.md#r1-history-class).  
Sources: [BUNDLE](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_r1_face_bundle_cocycle_triviality_201h69g.v1.json#L1-L50), [CORE](../provenance/inputs/qr_core_terms_consolidated.md#L1-L3141).

## 39. Piecewise five-frame golden-sector exchange / Cyclic residue coordinate family

**Relation:** operator vs residue group  
**Decision:** do not merge

The frame Z5 operator is not the integer residue group modulo five.

Views: [frame-sector-exchange](qr_structure_registry.md#frame-sector-exchange); [residue-spaces](qr_structure_registry.md#residue-spaces).  
Sources: [CHAT](../provenance/excerpts/current_chat_archive.md#L1-L21), [KERNEL](../provenance/inputs/draft6/sections/01C_relational_kernel.tex#L1-L68).

## 40. Discrete cochain incidence/coboundary operators / Six-face quadratic disagreement scalar

**Relation:** linear map vs scalar functional  
**Decision:** do not merge

A degree-two incidence map and a quadratic scalar functional have different domains and codomains.

Views: [cochain-coboundaries](qr_structure_registry.md#cochain-coboundaries); [face-disagreement](qr_structure_registry.md#face-disagreement).  
Sources: [MAXWELL](../provenance/inputs/draft6/sections/09C_maxwell.tex#L1-L93), [FACE](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_face_field_higgs_bridge_checkpoint_receipt_201fk.v1.json#L1-L144).

## 41. Signed registered-pentagon incidence map / Registered-pentagon Gram operator

**Relation:** gram construction  
**Decision:** link not alias

Taking a Gram matrix changes the size, domain and meaning of the incidence map.

Views: [history-incidence](qr_structure_registry.md#history-incidence); [history-gram](qr_structure_registry.md#history-gram).  
Sources: [HIST](../provenance/inputs/thalean_registered_history_conference_operator_audit.json#L1-L564).

## 42. Registered-pentagon Gram operator / Registered-history centered conference operator

**Relation:** centering relation  
**Decision:** link not alias

Centering G_hist by subtracting 5I12 produces a different operator.

Views: [history-gram](qr_structure_registry.md#history-gram); [history-contrast](qr_structure_registry.md#history-contrast).  
Sources: [HIST](../provenance/inputs/thalean_registered_history_conference_operator_audit.json#L1-L564).

## 43. Receipt-family diagonal grading / Signed-chart history sheet-exchange operator

**Relation:** grading vs exchange  
**Decision:** do not merge

The raw receipt-family diagonal grading is not the spectral sheet-exchange observable.

Views: [history-sheet-grading](qr_structure_registry.md#history-sheet-grading); [history-sheet-exchange](qr_structure_registry.md#history-sheet-exchange).  
Sources: [CLIFF](../provenance/inputs/thalean_registered_history_clifford_measure_audit.json#L1-L54), [CHAT](../provenance/excerpts/current_chat_archive.md#L1-L21).

## 44. First positive-event anchor circle / Second positive-event anchor circle

**Relation:** complementary subgroups  
**Decision:** do not merge

The two anchor point stabilizers are differently embedded circles, with trivial intersection in the stated geometry.

Views: [u1-anchor-first](qr_structure_registry.md#u1-anchor-first); [u1-anchor-second](qr_structure_registry.md#u1-anchor-second).  
Sources: [CIRCLES](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_positive_pair_hermitian_geometry_201fv.v1.json#L1-L116).

## 45. First positive-event anchor circle / Central face phase circle

**Relation:** distinct circle subgroups  
**Decision:** do not merge

A0 is not J; J is the sum of the two event-anchor Lie generators.

Views: [u1-anchor-first](qr_structure_registry.md#u1-anchor-first); [u1-face-center](qr_structure_registry.md#u1-face-center).  
Sources: [NEUTRAL](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_neutral_generator_anatomy_201fw.v1.json#L1-L152).

## 46. Companion four-generator additive winding cochain / Primitive registered-history winding class

**Relation:** different winding domains  
**Decision:** hold for history crosswalk

The cellular source explicitly keeps its N winding separate from the original tau_T domain.

Views: [w4-winding](qr_structure_registry.md#w4-winding); [r1-history-class](qr_structure_registry.md#r1-history-class).  
Sources: [WINDING](../provenance/inputs/PHASE_RELATION_CELLULAR_PROOF.md#L1-L392), [CORE](../provenance/inputs/qr_core_terms_consolidated.md#L1-L3141).

## 47. Twelve-dimensional analyzer-frame candidate module / Registered-pentagon coefficient module

**Relation:** candidate module match  
**Decision:** native intertwiner open

Dimension, spectrum and Clifford relations do not select the native vector-space intertwiner.

Views: [h12-history-candidate](qr_structure_registry.md#h12-history-candidate); [history-pentagon-space](qr_structure_registry.md#history-pentagon-space).  
Sources: [CHAT](../provenance/excerpts/current_chat_archive.md#L1-L21).

## 48. 201EZ order-120 classification locator / Common AT4val-family bipartite cover graph

**Relation:** unresolved name collision  
**Decision:** do not merge without source

An upstream classification filename is not proof of graph/group identity.

Views: [k120-group-locator](qr_structure_registry.md#k120-group-locator); [k120-common-cover](qr_structure_registry.md#k120-common-cover).  
Sources: [FACE](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_face_field_higgs_bridge_checkpoint_receipt_201fk.v1.json#L1-L144), [COVER](../provenance/inputs/draft6/sections/01B_common_cover.tex#L1-L101).

## 49. Twelve-state phase factor of the serialized line map / Twelve face/relative-orientation objects

**Relation:** same source phase objects  
**Decision:** consolidate entity keep map domain

The line-map source explicitly says the twelve phase states are the six face carriers with their two relative orientations.

Views: [s12-phase-set](qr_structure_registry.md#s12-phase-set); [twelve-face-phases](qr_structure_registry.md#twelve-face-phases).  
Sources: [LINES](../provenance/inputs/draft6/provenance/draft6/native_snapshot/program02/artifacts/json/epr_reference_gauge_projective_line_map_018.v1.json#L1-L775), [CONNECTION](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_u2_gauge_bridge_connection_frontier_checkpoint_201fp7.v1.json#L1-L190).

## 50. Same-face forward and reverse connection maps / Native decagonal macro-transport subgroup

**Relation:** endpoint indices vs actor name  
**Decision:** do not merge

The edge map T_10 is an involutory inverse of T_01; macro T10 is a separately defined decagonal native actor.

Views: [t01-edge-connection](qr_structure_registry.md#t01-edge-connection); [c10-native](qr_structure_registry.md#c10-native).  
Sources: [TWISTED](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_6k2_twisted_selector_covariance_201fqd.v1.json#L1-L91), [MACRO_EXCERPT](../provenance/excerpts/macro_and_support.md#L1-L10).

## 51. Two relative-complex-line partitions / Frame-common zero-current projector

**Relation:** partition vs projector  
**Decision:** do not merge

P0/P1 partition local modes; P0_frame projects onto a frame-common linear subspace.

Views: [p01-line-partitions](qr_structure_registry.md#p01-line-partitions); [frame-common-projector](qr_structure_registry.md#frame-common-projector).  
Sources: [LINES](../provenance/inputs/draft6/provenance/draft6/native_snapshot/program02/artifacts/json/epr_reference_gauge_projective_line_map_018.v1.json#L1-L775), [CHAT](../provenance/excerpts/current_chat_archive.md#L1-L21).

## 52. Four local signed modes of the line-map domain / Full matrix algebra size notation

**Relation:** finite mode set vs algebra  
**Decision:** do not merge

The four local modes are a finite factor of a 48-record domain, not a full matrix algebra.

Views: [m4-mode-set](qr_structure_registry.md#m4-mode-set); [matrix-algebras](qr_structure_registry.md#matrix-algebras).  
Sources: [LINES](../provenance/inputs/draft6/provenance/draft6/native_snapshot/program02/artifacts/json/epr_reference_gauge_projective_line_map_018.v1.json#L1-L775).

## 53. Discrete Maxwell cochain-degree spaces / Complex scalar vector-space family

**Relation:** cochain degree vs complex dimension  
**Decision:** do not merge

C^2 can indicate degree-two cochains or a complex doublet; superscript syntax alone cannot decide.

Views: [cochain-spaces](qr_structure_registry.md#cochain-spaces); [complex-spaces](qr_structure_registry.md#complex-spaces).  
Sources: [DYN_TARGETS](../provenance/inputs/draft6/appendices/L2_dynamical_targets.tex#L1-L25), [U2](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_event_vector_u2_u1_stabilizer_201ft.v1.json#L1-L71).

## 54. Transverse and axial heavy-top moments / Identity operator family with domain size

**Relation:** physical parameter vs identity matrix  
**Decision:** do not merge

I1/I3 in the heavy-top calculation are inertia scalars, not identity matrices.

Views: [inertia-moments](qr_structure_registry.md#inertia-moments); [identity-matrices](qr_structure_registry.md#identity-matrices).  
Sources: [CONSERVATIVE](../provenance/inputs/draft6/appendices/N_conservative_calculations.tex#L1-L128).

## 55. Unoriented-axis stabilizer in rotations / Orthogonal winding-plane reference-transport envelope

**Relation:** same abstract envelope distinct action  
**Decision:** hold for native crosswalk

The rotor stabilizer is embedded in SO3 on axes; the surface envelope acts on winding planes.

Views: [rotor-o2](qr_structure_registry.md#rotor-o2); [o2-surface-envelope](qr_structure_registry.md#o2-surface-envelope).  
Sources: [CONSERVATIVE](../provenance/inputs/draft6/appendices/N_conservative_calculations.tex#L1-L128), [SURFACE](../provenance/inputs/README(20260920-001150).md#L1-L300).

## 56. Three primitive registered homology species / Primitive registered-history winding class

**Relation:** selected family member  
**Decision:** link family and member

The visibility map selects r1 from the three primitive homology species.

Views: [history-primitive-family](qr_structure_registry.md#history-primitive-family); [r1-history-class](qr_structure_registry.md#r1-history-class).  
Sources: [HISTORY_CLASSES](../provenance/inputs/draft6/appendices/E_history.tex#L1-L26).

## 57. Golden-sector and conjugate-current eigenvalue signs / Five-frame conjugate-mode sign observable

**Relation:** eigenvalue readout  
**Decision:** link not alias

r5 is an eigenvalue of R5, not the operator R5.

Views: [frame-sign-values](qr_structure_registry.md#frame-sign-values); [frame-current-sign](qr_structure_registry.md#frame-current-sign).  
Sources: [CORE](../provenance/inputs/qr_core_terms_consolidated.md#L1-L3141), [CHAT](../provenance/excerpts/current_chat_archive.md#L1-L21).

## 58. Twisted-covariant two-sheet connection object / Pair-registration connection residual

**Relation:** companion action  
**Decision:** link not alias

The residual involution relates the two connection sheets; the group and the doublet are not one object.

Views: [connection-doublet](qr_structure_registry.md#connection-doublet); [c2-phase-residual](qr_structure_registry.md#c2-phase-residual).  
Sources: [TWISTED](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_6k2_twisted_selector_covariance_201fqd.v1.json#L1-L91), [RESIDUAL](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_signed_event_s1_torsor_selector_201h65b.v1.json#L1-L42).

## 59. Three-section coordinate set / Twelve-section closure surface state set

**Relation:** coordinate factor  
**Decision:** link views keep domains

The older source explicitly supplies the product X12 ~= X3 x X4; a factor set is not the whole section object or its acting group.

Views: [three-section-coordinate](qr_structure_registry.md#three-section-coordinate); [x12-sections](qr_structure_registry.md#x12-sections).  
Sources: [OLDER_SECTION_SURFACE](../provenance/excerpts/older_section_surface.md#L1-L9).

## 60. Native decagonal macro-history actor / Native decagonal macro-transport subgroup

**Relation:** generates  
**Decision:** link not alias

A named permutation generates its cyclic subgroup; the actor and the ten-element group remain distinct objects.

Views: [t10-native-macro](qr_structure_registry.md#t10-native-macro); [c10-native](qr_structure_registry.md#c10-native).  
Sources: [MACRO_EXCERPT](../provenance/excerpts/macro_and_support.md#L1-L10), [CONF_ACTION](../provenance/inputs/thalean_transport_conference_bridge_audit.json#L1-L123).

## 61. Native decagonal macro-history actor / Same-face forward and reverse connection maps

**Relation:** notation collision  
**Decision:** do not merge

Native T10 is the decagonal macro actor. In the same-face connection source T_10 denotes the reverse edge and satisfies T_10=T_01^-1=T_01; numerical indices here identify endpoints, not a macro action.

Views: [t10-native-macro](qr_structure_registry.md#t10-native-macro); [t01-edge-connection](qr_structure_registry.md#t01-edge-connection).  
Sources: [MACRO_EXCERPT](../provenance/excerpts/macro_and_support.md#L1-L10), [TWISTED](../provenance/inputs/draft6/provenance/draft6/native_snapshot/project41/artifacts/provenance/project41_6k2_twisted_selector_covariance_201fqd.v1.json#L1-L91).

