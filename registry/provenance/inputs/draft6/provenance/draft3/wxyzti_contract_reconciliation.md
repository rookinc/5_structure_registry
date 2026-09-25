# Original-source crosswalk reconciliation

The uploaded packet verifies all 24 WXYZTI station transitions, confirms the nine previously inferred reverse rows, and reproduces the full reciprocal selector: 48 candidates, 12 selected. The native base-edge crosswalk remains unselected.

## Correction to the preceding candidate experiment

The original 201H827 contract has domain **the ten directed transition occurrences of WXYZTITZYXW**. The preceding `wxyzti_native_crosswalk` experiment used six-step overlay circuits. Its graph counts and parameterized native-edge checks remain valid for that experimental domain. They do not instantiate the original contract.

In particular, the preceding nontrivial six-cycle return result must not be transferred to the ten-step registered walk. The ten-step walk must be tested under its own endpoint and history conditions.

## Packet verification and full-row replay

All 13 uploaded files match their receipt hashes and byte counts. The duplicate Project18/21/24 station data agree. The generator-family artifact contains 24 complete edge records, including A, B, C, slot, fiber, columns, and endpoint keys. Its full role/ABC transitions match the 24 semantic station rows exactly.

All four reconstructed six-step register circuits are confirmed by these original transitions. Their nine formerly inferred reverse rows are now independently present in the packet. Crossing shared-B and reverse-partner rows within the same role-pair channel yields 48 candidates. Applying the reciprocal equations selects 12, four per shared role. This remains selection over realized rows, not native candidate generation.

## Original registered edge descriptors

The union of the three undirected edge orbits serialized in 201H831 is exactly the 30-edge native G15 quotient reconstructed in the preceding audit, including its vertex numbering. This establishes equality of those two graph presentations; it does not identify chamber C-values with their native vertices.

The marked-atom fiber can be recovered from the incident-edge orbit as the vertices with four incident edges in that orbit: {3,7,11}. The directed classes, using the original orbit indices, are:

| Original orbit | Meaning | Size |
|---|---|---:|
| 0 | Both endpoints outside the marked fiber, in the six-edge undirected orbit | 12 |
| 1 | Outside to marked fiber | 12 |
| 2 | Marked fiber to outside | 12 |
| 3 | Both endpoints outside, in the remaining twelve-edge undirected orbit | 24 |

The historical labels of all five atom fibers are not serialized in this packet. The 201H831 script reads them from `201AY.g15_vertex_addresses`, and reads the registered event from `201AZ.base_hinge`. It reconstructs its graph from Audit131 pentagon rows. These are exact direct dependencies, not a request for another broad scan.

## What the complete station fields do and do not supply

The station and overlay records contain no independently registered native endpoint or omitted-Petersen-atom map. Column pairs provide additional source context but no column-to-native-incidence crosswalk is present here. Comparing their integer values with native vertex numbers would manufacture a join.

Several simple position maps can be excluded directly. Any map depending only on A sends all 12 reverse-partner moves to loops. A B-only map sends all 12 shared moves to loops. A columns-only map also sends all 12 reverse-partner moves to loops. Native G15 is loopless. The earlier C-only injective-map obstruction remains applicable to the overlay graph.

These exclusions do not rule out a joint register/context map, a coarser observation, or a path-valued realization. They locate what the missing registration must explain.

## Exact ten-step control

Assume temporarily that each role W,X,Y,Z,T,I has one fixed native G15 vertex. Enumerate all five-edge outward walks, allowing repeated vertices. There are 15 × 4^5 = 15,360. Of these, 3,480 have six distinct outward vertices.

Under this assumption, the return word traverses the exact reversed edges. Lifting all 15,360 walks from all four starting sheets gives 61,440 ten-step native G60 walks. Every lift is palindromic, every endpoint returns to its start, and every T-I-T subwalk returns identically. None implements the nontrivial native deck element b at that subwalk.

This also follows without enumeration: a graph covering uniquely lifts an edge from a specified start; immediately lifting its reverse returns to that same start. For an outward path P, the return is P inverse and the total transport is identity.

The control is deliberately narrower than the contract. The 201H827 source explicitly permits repeated role labels to map to the same or different G15 edges. An occurrence-dependent realization remains open. The calculation rules out using a fixed role-vertex assignment plus ordinary reversal to establish T-I-T = b. It does not refute all admissible sections or the separately proved ordered-history exchange.

The complete ten-step orbit-descriptor strings also fail to select a unique fixed-role map. They form 140 profiles, with 12 to 384 outward maps per profile. No profile has been assigned to the actual WXYZTI occurrence data in this audit.

## Next bounded source step

Read the five direct inputs named by the supplied scripts:

1. `project41_g15_native_five_address_wxyzti_crosswalk_201ay.v1.json`
2. `project41_wxyzti_hinge_omitted_atom_equivariance_201az.v1.json`
3. `g1800_wxyzti_hinge_pentagon_selector_131.v1.json`
4. `project41_wxyzti_native_station_role_geometry_201h820.v1.json`
5. `project41_edgewise_lifted_sheet_live_or_die_201h824.v1.json`

The first three provide the actual registered event and five-address incidence. The last two distinguish the role occurrence geometry and lifted ordered-history exchange from ordinary edge reversal. No producer chain needs to run. The goal is a shared incidence invariant that supplies native endpoints for the ten occurrences.

S1/S2/S4/S5/S7 remain open. This packet closes the complete-row replay and records the correct domain and the fixed-role return obstruction.

## Reproduce

Run `python3 verify.py` in the extracted folder. All required finite inputs are included in `sources/`. No historical producer scripts execute.
