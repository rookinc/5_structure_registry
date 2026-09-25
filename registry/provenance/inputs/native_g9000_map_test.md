# Native G9000 test of the registered six-distance map

All 24 source-defined native five-frame actions pass the registered map's
compatibility test. The audit reconstructs their actual labeled permutations
from recovered source data and checks 4,320,000 ordered comparable pairs.

The test also establishes two limits. Every native G1800 graph edge joins
different transport orbits, outside the current readout's domain. A modified
action keeps the same native deck flip and the same twenty-step return law,
passes the readout, and sends 64 native edges to non-edges. The map therefore
describes native transport phase, but has not earned native adjacency or a
geometric analyzer forced by the graph.

## Test result

| Gate | Exact result | What it establishes |
|---|---:|---|
| Recovered native G60 graph | 60 vertices; 120 edges | Concrete labeled graph input |
| Archived native G60 actions | 480/480 preserve all edges | Agreement with the separate Audit044 actual-action export |
| Native product quotients | 3 connected graphs, each 1800 vertices, 7200 edges, degree 8 | Native G1800 quotient geometry |
| Ordered native axis actions | 6/6 | Descended graph automorphisms K with K² equal to the appropriate native Delta |
| Five-frame constructions | 24/24; 120 frame instances | Exact quotient, frame transport, native registration, and orientation intertwining |
| Return law | F⁵ = local K; F¹⁰ = native Delta; F²⁰ = I | Verified on 216,000 state instances |
| Orbit structure | 450 cycles of length 20 per construction | Full labeled actions, with no shorter cycles |
| Native phase comparison | 4,320,000/4,320,000 | Readout phase agrees with independent frame/K coordinates |
| Geometric transition composition | 400/400 phase pairs | Exact transported addition law |
| Transition shapes and magnitudes | 20 distinct profiles; 9 squared magnitudes | Same exact finite geometric map on the native input |
| Native within-frame edges in the readout domain | 0/7200 for every ordered axis choice | The map presently omits native adjacency comparisons |
| Graph-incompatible control | Accepted by the phase readout | Return laws do not certify native graph compatibility |

Counts of state or frame instances include repetitions across the 24
constructions. They are not counts of distinct physical states or separate
graphs. The 4,320,000 pairs include reference-equals-target pairs and are
exactly the ordered pairs sharing an F orbit in each construction.

## What was reconstructed

The available runtime transcripts contain two complete 60-point connection
generators, their declared inverse pairing, the complete source-to-native
label map, and all three named native deck permutations a, b, and ab. The
inverse pairing reconstructs the other two connection generators. Saved
source windows specify the product coordinates, quotient enumeration,
descended actions, four transport words, six ordered source axes, and F.

The reconstruction uses those formulas and literals directly. It does not
build an arbitrary collection of 20-cycles and fit it to the desired law.
No historical producer chain was replayed. Complete archived 9000-entry F
arrays were unavailable for a full original-versus-reconstruction comparison;
the saved complete literals and available prefixes were checked instead.

This distinction matters: the result certifies an independent reconstruction
of the recovered source-defined native actions. It does not certify every
unseen dependency in the historical pipeline.

The reconstructed native G60 edge set also agrees exactly with the orbit of
the saved edge (0,16) under the 480 actual 60-point automorphisms exported in
`native_g60_fiber_product_isomorphism_044.json`. The four exported actual
generators generate exactly that 480-element set, and every action preserves
the reconstructed edge set. The named deck actions form a free normal V4
inside this action group.

### Saved-data comparisons

| Reconstructed item | Available saved data compared | Result |
|---|---:|---|
| Final F | First 82 complete entries | Exact |
| Final F inverse | First 82 complete entries | Exact |
| Final-frame a, b, ab, frame-to-native map, and transport | Five full 60-entry permutations | Exact |
| Frame-zero local K | First 94 complete entries | Exact |
| Native K for (a,b) | Prefixes of 90 and 109 entries | Exact |
| Frame-zero native registration | First 133 entries | Exact |
| Final-frame native registration | First 107 entries | Exact |
| Final-frame transport | First 99 entries | Exact |
| Frame-zero transport | First 99 entries | Exact |
| Frame-zero quotient fibers | First 54 complete fibers | Exact |
| Native a-kernel quotient fibers | First 49 complete fibers | Exact |
| Native G60 edges | 50 and 60 complete printed edges | All present |

Initial/frame G60 and native/frame product-edge samples also agree; their
counts are in `REPORT.json`. Overlapping transcript prefixes are corroboration,
not independent additional states. Tokens touching an ellipsis were excluded.
The parser uses complete literals only and never executes transcript code.

## Native construction and the map

Use product labels (u,v) ↦ 60u+v. For each ordered pair of distinct native
deck elements (a,b), quotient G60 □ G60 by the diagonal action of b. Assign
quotient labels by the source's ascending scan through all 3600 product
states, collecting the two-element fibers.

On that quotient, K is the descent of

\[
(u,v)\longmapsto(ab(v),b(u)).
\]

Its square is the descent of diagonal a, the native Delta for this registered
quotient. It is an actual graph automorphism with 450 free four-cycles.

For each of the four source transports and six ordered source-axis choices,
construct all five frame graphs, their quotients, local K actions, and
source-prescribed native registration maps C_f. If U_f is the descended
transport to the next frame, the recovered source constructs

\[
F(f,q)=\bigl(f+1,\ U_f K_f q\bigr).
\]

Both f and f+1 are taken modulo five. The explicit registration
C(f,q)=(f,C_f q) satisfies

\[
CFC^{-1}(f,x)=(f+1,Kx).
\]

Every graph map and every pointwise intertwining equation is checked.
There are 24 distinct raw F arrays. Applying the prescribed registration
produces six distinct native-coordinate F arrays, with the four transport
choices agreeing for each ordered axis pair. This does not select one
canonical axis registration or establish a canonical G9000 graph.

For comparable native records, let delta-f be the frame difference modulo
five and delta-k the native K displacement modulo four. The independent
phase oracle is the recovered Chinese remainder formula

\[
t=16\,\delta f+5\,\delta k\pmod{20}.
\]

For every reference state, the test constructs all twenty target states
from these native coordinates and compares them with the supplied F
permutation's relative-step readout. Both the initialized support profile
and the transition profile agree exactly in all 4,320,000 cases.

The unchanged geometric transition map is

\[
\rho_{\mathrm{tr}}(x,y)=\mathbf1+d(t),\qquad
d(t)=(T^t-I)r_0,\qquad y=F^t x.
\]

The analyzer uses the previously declared dodecahedral rotation, quarter-turn
prescription, initial shape, and epsilon=1/40. Its exact composition law is

\[
d(t+s)=d(t)+T^t d(s).
\]

This transports the second deformation into the first record's frame before
addition. All 400 phase-pair identities and all twenty affine step identities
pass. The squared transition magnitude remains

\[
\|d(t)\|^2=\frac{1}{320}
\left(2-\cos\frac{\pi t}{10}-\cos\frac{3\pi t}{10}\right).
\]

It is 0 at t=0, 1/160 at t=5 and t=15, and 1/80 at t=10. Every support remains
inside [9/10,11/10], the support box certified by the prior geometric audit.
This run checks membership in that box; it reuses the prior incidence
certificate instead of claiming a new polytope-incidence proof.

## The adjacency obstruction

At one fixed frame, two vertices share an F orbit exactly when their native
G1800 coordinates share a K orbit. The full native edge census is:

| Orientation a | Quotient kernel b | Native edges | Endpoints in one K orbit | Endpoints in different K orbits |
|---|---|---:|---:|---:|
| a | b | 7200 | 0 | 7200 |
| a | ab | 7200 | 0 | 7200 |
| b | a | 7200 | 0 | 7200 |
| b | ab | 7200 | 0 | 7200 |
| ab | a | 7200 | 0 | 7200 |
| ab | b | 7200 | 0 | 7200 |

Thus none of the 7200 within-frame native edges is in the current readout's
pair domain, for any of the six axis choices. Exact frame isomorphisms carry
this result to all 120 tested frame instances. This statement concerns the
within-frame native G1800 edges; F's transport arrows are in the readout
domain and pass the test.

The current readout retains relative twenty-step phase and forgets which
of the 450 transport orbits contains the pair. Extending it across native
edges requires an additional rule for aligning different orbits. Assigning
arbitrary origins to those orbits would add a choice without showing that
the native graph determines it.

## A control with the same native Delta

Fix the native (a,b) quotient and its edge set. In its actual 1800-point
labels, use

\[
P=(0\ 1)(488\ 489),\qquad K'=PKP^{-1}.
\]

Here Delta(0)=488 and Delta(1)=489, so P commutes with the same native Delta.
The control is the first pair-swap in a declared lexicographic scan that
breaks graph compatibility. No control parameters were fitted to geometric
profiles. Exactly:

\[
(K')^2=\Delta,\qquad (K')^4=I,\qquad
F'(f,x)=(f+1,K'x).
\]

F' has 450 twenty-cycles and preserves the same five-frame advance,
F'¹⁰=Delta and F'²⁰=I. The readout accepts all 180,000 comparable control
pairs and returns the same twenty geometric profiles and nine magnitude
values as for native F.

But K' sends 64 of the fixed native graph's edges to non-edges. There are
also 64 missing edges in its image, for a symmetric difference of 128.
A concrete witness is

\[
\{0,16\}\in E(G1800),\qquad
K'\{0,16\}=\{555,1260\}\notin E(G1800).
\]

The graph is held fixed in this control. Relabeling the graph together with
K would instead be an ordinary coordinate change. The present control tests
whether the phase-only map notices a loss of compatibility with the actual
native graph; it does not.

This result does not invalidate the map's declared orbitwise domain. It
prevents using a successful phase readout as evidence that the input action
is native or that native geometry forces the analyzer.

## What this changes and what comes next

The earlier map had been tested on an abstract action obeying the recovered
return laws. It has now been tested on all 24 independently reconstructed
source-defined native actions, with exact quotient labels, graph checks,
source-prescribed registrations, and saved-data comparisons.

The next mathematical requirement is a native rule for comparing different
transport orbits, constrained by the G1800 edges and compatible with F and
Delta. That extension must satisfy the native edges and reject the explicit
graph-incompatible control. Only then can the map begin to represent native
adjacency. Whether such a rule forces the geometric rotation, initial shape,
or calibration remains a separate question.

The tested addition law is composition along a registered transport orbit.
This audit supplies no rule for superposing independent histories and no
physical probability or quantum interpretation.

## Reproducible evidence

`SOURCE_RECEIPTS.json` supplies original filenames, available source IDs,
and hashes. `INPUTS.json` contains the extracted literals and comparison
prefixes. `NATIVE_ACTIONS.json` exports all 24 F arrays, their native
registrations, local K and frame-transport arrays, all three native quotient
graphs, the six native K/Delta pairs, and the explicit control.

`test_native.py` performs the reconstruction and exact tests using only the
standard library and the unchanged analyzer code. `REPORT.json` and
`CERTIFICATE.json` record the machine-verifiable results. `VERIFICATION.log`
records the successful run. `README.md` gives the replay command and a short
example. Original source transcripts are included as evidence and are never
executed.

### Construction ledger

Each row passes 9000 states and 180,000 ordered comparable pairs. Full hashes
are in the machine report; shortened F hashes below identify the exported
arrays for review.

| Source transport | Source axis row | Native (a,b) | Raw F SHA-256 prefix | Result |
|---|---:|---|---|---|
| 02_x_210 | 0 | (ab,b) | `4d741308733acf26` | PASS |
| 02_x_210 | 1 | (ab,a) | `13e18c041dcc7cb7` | PASS |
| 02_x_210 | 2 | (b,ab) | `12a487b3f8d5b28a` | PASS |
| 02_x_210 | 3 | (b,a) | `140a6609cc22d364` | PASS |
| 02_x_210 | 4 | (a,ab) | `2e6b1dce671fca44` | PASS |
| 02_x_210 | 5 | (a,b) | `9d447242c7701b38` | PASS |
| 02_x_012 | 0 | (ab,b) | `cc6001b034c71412` | PASS |
| 02_x_012 | 1 | (ab,a) | `e22606b28c50ae41` | PASS |
| 02_x_012 | 2 | (b,ab) | `972b5b6b9fd02049` | PASS |
| 02_x_012 | 3 | (b,a) | `61df96f4c8c3ed62` | PASS |
| 02_x_012 | 4 | (a,ab) | `44d28bbbaada7119` | PASS |
| 02_x_012 | 5 | (a,b) | `18c8d84e83b36673` | PASS |
| 021_x_210 | 0 | (ab,b) | `974dfced912eacb1` | PASS |
| 021_x_210 | 1 | (ab,a) | `b730d2a095500638` | PASS |
| 021_x_210 | 2 | (b,ab) | `3343003af6a1e6d2` | PASS |
| 021_x_210 | 3 | (b,a) | `ee01acab903f516e` | PASS |
| 021_x_210 | 4 | (a,ab) | `eaeaa6791f30f841` | PASS |
| 021_x_210 | 5 | (a,b) | `99282db0eb418252` | PASS |
| 021_x_012 | 0 | (ab,b) | `4ea5d3968960862d` | PASS |
| 021_x_012 | 1 | (ab,a) | `703933e64ebd7490` | PASS |
| 021_x_012 | 2 | (b,ab) | `b452d72bc1e885cb` | PASS |
| 021_x_012 | 3 | (b,a) | `621952ff8befd563` | PASS |
| 021_x_012 | 4 | (a,ab) | `52b93d3f1b16ba6b` | PASS |
| 021_x_012 | 5 | (a,b) | `43cd5ab2cf12edb2` | PASS |
