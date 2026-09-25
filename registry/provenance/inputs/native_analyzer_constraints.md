# Native geometry recovered; phase-sensitive analyzer still unforced

Native structure supports a specific six-direction geometric construction.
In the relevant leading three-dimensional G60 modes, the six native
order-five subgroups determine six rank-one projectors. Their exact pair
and triple relations match the six Project39 dodecahedral face-pair
directions. This recovers an unordered geometric frame from native spectral
and symmetry data.

Those projectors give a positive quadratic response on native G1800
vertices. Each tested quotient has 120 distinct response profiles, and every
one of its 7200 native edges changes the profile. The response is invariant
under K and Delta, however, so it does not retain the orientation return
that the earlier phase-sensitive map was designed to display.

The original analyzer is not forced by the native constraints tested here.
Twenty-four distinct compatible analyzers, including the original, pass
with all native graphs, connections, and F actions held fixed. Native data
now grounds a six-direction geometry, but an additional construction is
needed to combine that geometry with the registered orientation phase.

## Result at a glance

| Question | Exact result |
|---|---|
| Does G60 distinguish a deck element? | Yes. a is its unique distance-six antipode. |
| Does the unpointed graph select one ordered axis pair? | No. Archived native automorphisms exchange b and ab; the six choices form three two-element orbits. |
| Is there a native complex structure? | Yes, given K: on the 900-dimensional real Delta-odd function space, K²=-I. |
| Does native adjacency select a four-dimensional odd eigenspace? | No complete four-dimensional band exists in any of the six registrations. |
| What are the leading odd bands? | Six or eight real dimensions, with irreducible three- or four-component complex structure. |
| Can six geometric directions be recovered? | Yes, in the two relevant three-dimensional G60 modes, from six native order-five fixed-axis projectors. |
| Do they match the supplied geometry? | Exact pair and triple projector traces match; 60 geometric label identifications per mode. |
| Does a native vertex readout respond to adjacency? | Yes. 120 profiles; all 7200 edges change profile in each tested quotient. |
| Does that quadratic readout retain K or Delta phase? | No. Both act trivially on it. |
| Does the original phase-sensitive analyzer become unique? | No. The original and 23 alternatives pass the same native transport and support gates. |

This is a new exact construction and audit. “Recovered geometry” here means
derived from the available native inputs and compared exactly with the
existing geometric frame. It does not mean that an identical historical
analyzer formula was found in an old transcript.

## 1. Native symmetry constrains the registration

All 60 native vertices have distance shells

\[
(1,4,8,16,24,6,1).
\]

Each vertex therefore has a unique distance-six opposite. The recovered
deck permutation a sends every vertex to that opposite. Both other named
nontrivial deck elements, b and ab, have displacement five everywhere.

Among the 480 archived native automorphisms, 240 fix all three named deck
elements and 240 fix a while exchanging b and ab. The ordered registrations
fall into three symmetry orbits:

| Orbit | Registered choices |
|---|---|
| Antipode in the orientation role | (a,b), (a,ab) |
| Antipode in the quotient-kernel role | (b,a), (ab,a) |
| Antipode in the remaining product role | (b,ab), (ab,b) |

No member of the six-element family is fixed by this native symmetry group.
Consequently the unpointed native graph cannot select one ordered pair
equivariantly from this family. A supplied root, named tower map, or
registration may legitimately select one; that is additional retained
structure, not a contradiction of this obstruction.

There is a further orientation reversal. Swapping the two G60 product
factors descends to a graph automorphism S of each native G1800 quotient,
and

\[
SKS^{-1}=K^{-1}.
\]

Thus the unoriented product graph does not select a positive K direction by
itself. The already registered positive F and K do provide a direction for
the current transport calculation; this audit does not erase that input.

## 2. Native orientation supplies a complex structure

Use real functions on the 1800 native vertices, with the standard counting
inner product. Let P_K push the coordinate basis at x to the coordinate
basis at Kx. The native odd sector is

\[
\mathcal H_-=
\{f:P_\Delta f=-f\}.
\]

Delta has 900 free pairs, so this space has real dimension 900. Since
K²=Delta,

\[
J_{\rm native}=P_K\big|_{\mathcal H_-},\qquad
J_{\rm native}^{,2}=-I.
\]

The permutation action is orthogonal, so J_native is an orthogonal complex
structure. Native adjacency commutes with it because K is a graph
automorphism. Equivalently, the native odd sector is a 450-component complex
space with a complex-linear adjacency operator.

This is a native finite linear structure once K is registered. It does not
select a physical state space, a probability interpretation, or the
particular two-complex-dimensional space used by the previous shape map.

## 3. Exact spectral constraint

The recovered V4 action is free on G60. For each character with signs
(s_a,s_b), its character functions form a 15-dimensional space. The audit
builds each signed integer adjacency matrix directly from the native graph
and certifies its characteristic polynomial exactly.

| Character (a,b) | G60 adjacency spectrum, with multiplicities |
|---|---|
| (+,+) | 4:1; 2:5; -1:4; -2:5 |
| (+,-) | 3:4; 0:5; -2:6 |
| (-,+) | 1+sqrt(5):3; 1-sqrt(5):3; 1:4; -2:5 |
| (-,-) | 1+sqrt(5):3; 1-sqrt(5):3; 1:4; -2:5 |

The native G1800 adjacency is the descent of A60 tensor I + I tensor A60.
For an ordered registration (a,b), the quotient keeps diagonal b parity +1
and the odd sector keeps diagonal a parity -1. Adding the exact G60 sector
eigenvalues with these parity constraints gives the full 900-dimensional
odd spectrum.

| Orientation | Kernel | Largest odd eigenvalue | Leading real dimension | Leading complex dimension |
|---|---|---|---:|---:|
| a | b | 5+sqrt(5) | 6 | 3 |
| a | ab | 5+sqrt(5) | 6 | 3 |
| b | a | 7 | 8 | 4 |
| b | ab | 5+sqrt(5) | 6 | 3 |
| ab | a | 7 | 8 | 4 |
| ab | b | 5+sqrt(5) | 6 | 3 |

No complete odd adjacency eigenspace has real dimension four. The smallest
complete bands have dimension six for the non-antipodal kernels and eight
for the antipodal kernel.

The leading spaces have a transparent form. Let V be the leading G60
character mode, with real dimension three or four. Functions depending on
the left coordinate and functions depending on the right coordinate give
two orthogonal copies L(V) and R(V). In the push convention,

\[
P_K L(\phi)=R(\phi),\qquad
P_K R(\phi)=-L(\phi).
\]

Thus the leading native band is V plus iV. The two coordinate lifts, their
native quotient labels, K action, and adjacency eigen-equations were
checked directly.

The native subgroup fixing the deck labels has order 240. On each relevant
leading V, its exact character satisfies

\[
\frac1{240}\sum_g |\chi_V(g)|^2=1.
\]

The averaging operator on endomorphisms therefore has a one-dimensional
invariant range. A proper invariant subspace would give a non-scalar
orthogonal projection in that range, so V is irreducible over the complex
numbers. Consequently no real four-dimensional K-stable subspace can be
selected inside these leading bands while preserving this native symmetry.

This rules out that particular route to the old shape space. It does not
rule out additional native observables, rooted restrictions, nonlinear
constructions, or other enriched selection principles.

## 4. Six directions from native order-five symmetry

The pointwise deck stabilizer contains 24 order-five elements, forming six
cyclic order-five subgroups. These subgroups are native group objects. Their
unordered set does not require assigning geometric face labels.

Take either three-dimensional G60 mode with eigenvalue 1+sqrt(5) and let P
be its spectral projector. For each cyclic subgroup C_i, form

\[
\Pi_i=\frac15\sum_{g\in C_i}U_g P.
\]

Here U_g is the native action on the character sector. The audit proves
that every Pi_i is an orthogonal rank-one projector and that

\[
\sum_{i=1}^6\Pi_i=2P,\qquad
\operatorname{tr}(\Pi_i\Pi_j)=\frac15\quad(i\ne j).
\]

Thus the native mode contains six equiangular unoriented lines. Their
triple projector traces are also computed exactly. Comparing all twenty
triple traces with the supplied Project39 normal lines gives 60 exact label
identifications for each mode.

The comparison is stronger than matching one angle or a spectrum. Pair
traces fix absolute inner products; triple traces fix the relative Gram
signs up to changing the sign of each line representative. Since these are
rank-three configurations, the matching Gram data gives an orthogonal
identification with the six dodecahedral face-pair directions.

The native projectors are constructed before this comparison and do not
use the Project39 coordinates as inputs. Covariance is checked on the four
generators of the archived 480-element action group, including generators
that exchange the two character modes. It therefore holds on the whole
generated group.

This construction is canonical within the specified native deck and
leading-mode choice. It recovers the unordered six-direction frame. It
does not select one geometric labeling, sign for each normal, or a single
fivefold rotation to identify with the registered frame clock F^16.

For the four-dimensional leading mode associated with the antipodal
quotient, the same order-five average has no fixed vector and yields zero.
This only excludes the same rank-one fixed-axis recipe in that band; other
six-channel constructions there have not been ruled out.

## 5. The native positive quadratic readout

Write a leading six-dimensional real mode as z=u+iv, with u and v in V.
Native K acts as multiplication by i; the product-factor swap acts as
z mapped to i times its complex conjugate.

The six native projector scores are

\[
q_i(z)=z^\dagger\Pi_i z
      =u^T\Pi_i u+v^T\Pi_i v\ge0.
\]

They satisfy the exact finite frame identity

\[
\sum_i q_i(z)=2\|z\|^2.
\]

These six projectors span the entire space of real symmetric quadratic
forms on V. Their Hilbert-Schmidt Gram matrix has diagonal entries one and
off-diagonal entries 1/5, with eigenvalues 2 once and 4/5 five times. It is
therefore nonsingular.

The dimension six also follows directly from native symmetries. General
real quadratic forms on V plus iV have dimension 21. Invariance under K
leaves nine, the real dimension of Hermitian forms on a three-component
complex space. Requiring factor-swap invariance leaves precisely

\[
q(u,v)=u^T C u+v^T C v,\qquad C=C^T,
\]

a six-dimensional space. The audit verifies these constraint ranks exactly.

This gives a specific native six-channel quadratic construction. It also
shows why that construction loses orientation phase:

\[
q_i(iz)=q_i(-z)=q_i(z).
\]

K and Delta are invisible to these single-state quadratic scores.

## 6. Response of actual native vertices

The audit applies the construction to canonical unit vertex probes in each
of the native b- and ab-kernel quotients. Project each probe onto the leading
odd band and evaluate the six projector scores.

The exact normalization follows from the native counting inner product.
The G60 character basis has squared column norm four; lifting either product
coordinate to G1800 multiplies its squared norm by thirty. Hence the
denominator is 4 times 30, or 120.

Let r(u) be the native V4 orbit of a G60 vertex u, equivalently its recovered
G15 vertex. For a native product-quotient point represented by (u,v),

\[
q_i(u,v)=
\frac{(\Pi_i)_{r(u),r(u)}+(\Pi_i)_{r(v),r(v)}}{120}.
\]

This is independent of the chosen product representative and obeys

\[
\sum_i q_i(u,v)=\frac1{150}.
\]

The full exact census is the same for both tested kernels:

| Native vertex response | Result |
|---|---:|
| Native vertices | 1800 |
| Distinct six-channel profiles | 120 |
| Profiles from repeated G15 pairs {r,r} | 15, each with 8 native preimages |
| Profiles from distinct G15 pairs {r,s} | 105, each with 16 native preimages |
| Native edges that change the profile | 7200 of 7200 |
| Image graph | 120 vertices; 450 edges |
| Image degrees | 15 vertices of degree 4; 105 of degree 8 |
| Native edges over each image edge | 16 |

The six-channel profile identifies exactly the unordered pair of G15
vertices, including repeated pairs. Its image graph is the graph of
unordered pairs obtained by moving one member along a G15 edge. This is
verified against the recovered native G15 quotient, not inferred solely
from the count 120.

The readout therefore has concrete native adjacency content. It is also a
coarsening: several native vertices and several orientation orbits share
one profile. K and Delta preserve every profile for both registered roots
available on each tested quotient.

The scores are not yet support distances. Some are zero. Converting them
to positive distances requires a baseline and a response scale, for example
a declared centered response around a positive common distance. The graph
counting normalization fixes the stated probe scores; it does not supply a
physical length scale. Normalizing their sum to one likewise does not
derive a physical probability interpretation.

### Two controls locate what the scores retain

The original altered action P=(0 1)(488 489) preserves the same Delta and
the old phase readout, but the new quadratic scores fail invariance at eight
native vertices. Thus the new scores detect something that the phase-only
map missed.

A second control tests their remaining loss. Keep the native graph fixed
and use P=(0 8)(488 480), exchanging states inside one quadratic-profile
fiber. Then K'=PKP inverse still squares to the same Delta and preserves
every quadratic score, while sending 64 native edges to non-edges. The full
native connection rejects it.

The quadratic scores therefore provide native geometric content but are
not a complete certificate of native graph compatibility. The connection
and the geometric response retain different parts of the native structure.

## 7. Four moving shape dimensions appear, with the wrong Delta parity

Every nonidentity native order-five rotation permutes the six derived axes
as one fixed axis and one five-cycle. This is checked for all 24 such
elements. Once one rotation is registered, the six-channel space splits into
two fixed directions and four moving shape directions, just as in the
geometric architecture of the earlier analyzer.

There is nevertheless a precise obstruction. Native Delta acts as identity
on these quadratic channels. On the earlier phase-sensitive shape space W,
the declared analyzer has T^10=-I. Therefore a linear map L identifying the
two spaces equivariantly would have to satisfy

\[
L\Delta_{\rm quadratic}=\Delta_W L,
\qquad L=-L,
\]

so L=0. A nonzero linear identification with the required Delta behavior
does not exist.

This is a parity obstruction between these two constructions. It does not
refute the earlier registered readout, which explicitly compares transport
records. It does show that the new single-state quadratic geometry cannot
silently be substituted for its phase-sensitive shape variable.

## 8. The original analyzer is not forced by the tested native gates

The native graphs, K actions, all 24 F arrays, frame registrations, and
edge connections are held fixed. The audit varies only analyzer inputs:

| Analyzer choice | Values tested |
|---|---|
| Quarter-turn signs on the two C5 harmonic planes | (+,+), (+,-), (-,+), (-,-) |
| Relative harmonic seed weights | (1,1), (3/2,1/2), (1/2,3/2) |
| Amplitude | 1/40, 1/80 |

All 24 combinations produce distinct exact transition maps. They retain
orthogonal order-twenty transport, T^5=J, T^10=-I on the shape space, twenty
distinct phase profiles, four-dimensional shape span, and the same certified
support box. All 9600 tested composition identities and 11,520 direct native
path/phase cases pass.

For the four sign choices, the traces of T on W are distinct. With
c=2 cos(pi/10), they are

\[
c^3-2c,\quad 4c-c^3,\quad c^3-4c,\quad 2c-c^3.
\]

Thus these four registered-F representations are not merely different
coordinates of one linear operator.

The original positive-polar prescription selects one sign choice, and its
localized seed prescription selects the equal-weight seed. Alternatives
outside those prescriptions test whether the added prescriptions follow
from native transport; they do not challenge uniqueness after those
prescriptions have already been imposed.

Even retaining the original signs and seed, both tested amplitudes survive.
More generally, positive seed weights summing to two and any amplitude in
(0,1/40] give continuous compatible families by the same linear transport
and support bound. A further normalization or selection principle is needed
to determine those choices.

## 9. What is now open

The native six-direction geometry and its positive quadratic response are
now explicit. What remains open is how to couple that geometry to the
registered orientation phase in a way determined by the retained native
data.

A concrete next candidate is a reference-dependent comparison,

\[
c_i(z_{\rm ref},z)=z_{\rm ref}^\dagger\Pi_i z.
\]

Its algebraic covariance has the right distinction: a common K phase on
both inputs cancels, while a K phase on the target multiplies the comparison
by i. That observation identifies a next test, not a completed replacement
analyzer. Its relation to recorded native paths, the twenty-step frame
clock, and a real support-distance readout still needs to be constructed
and verified.

Also open are the registration of a particular native fivefold rotation
against F^16, the choice of response seed and scale, and any rule for
combining unresolved alternative histories. No physical spin assignment,
physical probability rule, or independent-history superposition law follows
from this audit.

## Reproducibility and source boundary

The complete packet uses standard-library Python and exact rational
arithmetic in Q(sqrt(5)) for native spectral and geometric claims. The
unchanged analyzer uses its previous exact degree-four real field. Small
numerical spectra informed exploration; the delivered verification certifies
characteristic polynomials, projectors, group covariance, and line matches
without a floating-point eigensolver.

The native data remains the independently reconstructed source-defined
actions from the prior packet. Saved source transcripts, raw permutation
prefixes, full recovered input literals, and the archived actual G60 action
group remain nested in the unchanged upstream packets. No historical
producer chain was replayed.

`NATIVE_PROJECTORS.json` exports the native matrices, modes, subgroups,
projectors, and exact geometric identifications. `NATIVE_VERTEX_CHANNELS.json`
exports every tested vertex response and image graph.
`ANALYZER_COUNTEREXAMPLES.json` exports all 24 analyzer variants, including
the original. `REPORT.json`, `CERTIFICATE.json`, and `VERIFICATION.log`
record the gates and outcomes. `README.md` gives replay and readout examples.
