# A finite cellular presentation of the integral phase receipt

## Result

The constructed integral companion register admits a complete presentation with four generators and nine relators. Its presentation complex has first integral homology Z. The two-sheet cover that retains even companion words has two vertices, eight oriented edges, eighteen relation cells, and first integral homology Z with no torsion.

On this even cover, the signed quarter-turn cochain W4 and a primitive integer cochain N satisfy

    W4 = 2N + dh,

where h is the vertex coordinate 0 or 1. Consequently W4=2N on every closed history.

Every real edge-additive scalar that respects all eighteen relation cells has exactly the form

    a = kappa W4 + beta dh.

Thus on closed histories its value is kappa W4. If such a scalar is independently normalized to value two on the primitive residual loop, it equals W4 on every closed history in this constructed complex.

This is a complete all-word statement for the integral companion register, not a census of finitely many agreeing loops. It does not assert that Project41's original execution/cellular map already factors through this presentation. The new complex encodes companion-word relations; it is not the original G60 or Project41 cellular complex.

## 1. Input and inherited convention

The input is the supplied exact sixty-point permutation certificate

    inputs/native_g60_fiber_product_isomorphism_044.json.

Its native group coordinates are

    G = {(sigma,r,f): sigma in S5, r in Z4, f in Z2,
                      parity(sigma)=r mod2},

with multiplication

    (sigma,r,f)(eta,u,h)
      = (sigma eta, r+(-1)^f u mod4, f+h mod2).

The preceding INTEGRAL_PHASE_RECEIPT.md constructs the integral lift of the companion subgroup:

    Gamma_tilde = {(sigma,n): sigma in S5, n in Z,
                            parity(sigma)=n mod2},

    (sigma,n)(eta,m)=(sigma eta,n+m).

Its finite projection reduces n modulo four and sets f=0. The signed companion rule is inherited: a positive r=1 companion has integer increment +1; its inverse, r=3, has increment -1. Ordinary d4 connectors contribute no factor to this particular extracted companion word. That convention concerns this receipt, not a claim of zero physical action on connectors.

This continuation does not select a new interpolation or physical phase law. It proves that the declared integral word receipt is compatible with a complete finite set of relations.

## 2. Four native generators and nine relations

Temporarily order the five addresses as 0,1,2,3,4. Let

    t_i = (i-1 i),  i=1,2,3,4,
    x_i = (t_i,1) in Gamma_tilde.

The images of x_i in the finite native group are actual history-24 companions, not introduced permutations outside the supplied group.

Consider the following presentation P.

### Adjacent braid relations: three

    x_i x_(i+1) x_i = x_(i+1) x_i x_(i+1),  i=1,2,3.

Both sides have the same permutation and signed quarter-turn count three.

### Disjoint commutation relations: three

    x_i x_j = x_j x_i,  j-i>1.

The pairs are (1,3), (1,4), (2,4). Both sides have the same permutation and count two.

### Equal-square relations: three

    x_j^2 = x_1^2,  j=2,3,4.

Each square is (identity,2). This element is the lift of the native central deck half-turn, not the identity of the integral register.

These nine relations are invariant under replacing the five-address ordering by another ordering and under reversing the common companion phase orientation. The verifier checks all 120 orderings in both orientations: 2,160 exact native relator checks. The chosen chain is a presentation coordinate, not a preferred physical frame.

## 3. Completeness of the presentation

**Theorem.** The nine-relation group P is isomorphic to Gamma_tilde under x_i -> (t_i,1).

**Proof.** The displayed target elements satisfy every relation, so they define a homomorphism.

Write z=x_1^2. The equal-square relations imply z=x_i^2 for every i. It follows that z commutes with every generator x_i, since x_i commutes with its own square. Hence z is central in P.

After imposing z=1, the generators become involutions. The remaining relations are the adjacent-transposition presentation of S5: adjacent generators satisfy the braid relation and nonadjacent ones commute. For completeness, the elementary insertion/bubble-sort normal form for this presentation has at most 2*3*4*5=120 words: at each stage a new address can be inserted in one of the available positions. The evident map to the 120 permutations of five addresses is onto, so this quotient is precisely S5.

Consequently any element of P with trivial permutation image is a power z^m.

The map P -> Gamma_tilde is onto. Represent any sigma by a word in the adjacent transpositions, and lift its letters to x_i. If that lifted word has count l, then l has the same parity as sigma. A desired count n with that parity differs from l by an even integer. Multiplication by z^((n-l)/2) supplies exactly the correction.

Finally, an element in the kernel of P -> Gamma_tilde has trivial S5 image, so it is z^m. But its image in Gamma_tilde is (identity,2m), which is the identity only for m=0. The map is injective as well as surjective. QED.

This establishes the presentation for all words. Finite checks of the native images alone would not have established completeness.

### A usable normal form

Choose a canonical adjacent-transposition word b(sigma) for each sigma in S5, of length l(sigma). Every integral element has a unique expression

    z^m b(sigma),
    n = 2m + l(sigma).

For two canonical words,

    b(sigma)b(eta) = z^c b(sigma eta),
    c = [l(sigma)+l(eta)-l(sigma eta)]/2.

The verifier checks this coordinate multiplication for all 14,400 permutation pairs. Arbitrary central powers follow algebraically.

## 4. The presentation complex and its homology

Let K have one vertex, four oriented loop edges x_1,...,x_4, and one two-cell attached along each of the nine relators. A relator is written as its left side followed by the inverse of its right side.

Then

    C0(K;Z)=Z,
    C1(K;Z)=Z^4,
    C2(K;Z)=Z^9,
    boundary1=0.

The columns of boundary2 are the signed exponent vectors of the relators. In the order braid, disjoint, equal-square, the matrix is

    [ 1  0  0 | 0  0  0 | -2 -2 -2 ]
    [-1  1  0 | 0  0  0 |  2  0  0 ]
    [ 0 -1  1 | 0  0  0 |  0  2  0 ]
    [ 0  0 -1 | 0  0  0 |  0  0  2 ].

Its image is exactly the lattice of four-vectors whose coordinate sum is zero. The first three columns already form a basis for that lattice; the remaining nonzero columns lie in it. Hence

    H1(K;Z) = Z^4 / im(boundary2) ~= Z.

The primitive dual cochain is

    W4=(1,1,1,1).

It vanishes on every two-cell boundary. It therefore evaluates consistently on homology classes and on all words modulo the nine defining relations.

This is a cellular proof of the integral winding coordinate. It is not an interpretation of the two-cells as physical area.

## 5. The even-history parity cover

The parity homomorphism W4 mod2 defines a connected two-sheet cellular cover K_even -> K.

The vertices are 0 and 1. For each positive generator x_i there are two oriented edges:

    e_(i,0): 0 -> 1,
    e_(i,1): 1 -> 0.

Each of the nine relation cells lifts once at each vertex, so the cell counts are

    vertices: 2,
    edges:    8,
    faces:   18.

The full integer matrices are in CELLULAR_MATRICES.json. Direct reconstruction gives

    rank(boundary1)=1,
    rank(boundary2)=6,
    boundary1 boundary2=0.

Collapsing the spanning-tree edge e_(1,0) leaves a free cycle lattice of rank seven. The resulting seven-by-eighteen two-boundary matrix contains a six-by-six minor of determinant -1. Its rank-six image is therefore saturated, so no torsion is hidden in the quotient. Thus

    H1(K_even;Z) ~= Z.

The independent group check agrees:

    pi1(K_even) ~= Gamma_tilde_even = A5 x 2Z,

whose abelianization is the integer factor.

### An explicit primitive integral cocycle

On each positive edge define

    N(e_(i,0))=0,
    N(e_(i,1))=1.

Negative traversals have the opposite value of the corresponding positive edge. Let h(0)=0, h(1)=1, and write dh(e)=h(end)-h(start).

The inherited quarter-turn cochain assigns +1 to either positively oriented edge. Edge by edge,

    W4 = 2N + dh.

On e_(i,0) this reads 1=0+1. On e_(i,1) it reads 1=2-1.

Both W4 and dh annihilate the lifted relators, and the reconstructed matrix independently confirms N boundary2=0. For any path gamma from u to v,

    W4(gamma) = 2N(gamma)+h(v)-h(u).

For closed histories,

    W4(gamma)=2N(gamma).

The loop x_1^2 has N=1, so N is primitive. No division of an odd integer is required: the cochain N is integer-valued on individual cover edges.

### Scope of N

N is the winding coordinate of this constructed companion presentation. The notation does not assert that N is the original Project41 tau_T on arbitrary balanced-release paths. An explicit comparison to that registered-history system remains necessary.

## 6. Exact classification of relation-preserving additive scalars

Let a assign a real scalar to each of the eight oriented positive edges, with reversed traversal contributing its negative. Let the value of a path be the sum of its edge contributions.

Require the eighteen relation identities:

    a boundary2 = 0.

**Theorem.** Every such cochain has the form

    a = kappa W4 + beta dh

for unique real constants kappa,beta.

**Proof.** The boundary2 matrix has rank six, so its left nullspace in R^8 has dimension two. The two independent cochains W4 and dh lie in that nullspace. They form a basis. QED.

Equivalently, all four positive edges from vertex 0 have one common value u, and all four positive edges from vertex 1 have one common value v:

    a(e_(i,0))=u,
    a(e_(i,1))=v,

where

    kappa=(u+v)/2,
    beta=(u-v)/2.

For a path from p to q,

    A(gamma)=kappa W4(gamma)+beta[h(q)-h(p)].

For a closed history,

    A(gamma)=kappa W4(gamma).

For two endpoint-matched histories,

    A(gamma)-A(gamma')
      =kappa[W4(gamma)-W4(gamma')].

The endpoint term is irrelevant to such comparisons. This is a complete classification of the declared edge-additive relation-preserving scalars, not of arbitrary nonlocal dynamics or all physical action functionals.

For integer edge scalars u and v are integers; kappa and beta may then be half-integers. On closed histories the primitive law is

    A(gamma)=(u+v)N(gamma).

If the scalar is independently required to take value two on a loop with N=1, then u+v=2, kappa=1, and

    A=W4 on all closed histories.

The normalization determines the closed-history scalar but leaves the endpoint potential free.

## 7. Explicit residual and full-turn examples

In the chosen adjacent-address frame, let

    r = (x_1^(-1) x_2 x_3)^2,
    r3 = (x_1 x_2 x_3)^2,
    ell = x_1^4.

The actual native permutation calculation gives

    product(r)=rho1,   W4(r)=2, N(r)=1;
    product(r3)=rho1,  W4(r3)=6, N(r3)=3;
    product(ell)=1,    W4(ell)=4, N(ell)=2.

These are the companion-word forms of the preceding primitive/third-power and full-turn witnesses. The prior packet supplies their admitted balanced-history realization. The present verifier recomputes their companion endpoints and edge-chain coordinates, not the 1,980-state balanced grammar.

Every relation-preserving scalar with primitive value two must assign these values respectively:

    2, 6, 4.

An endpoint-only evaluation that identifies the first two, or kills the third, fails the comparison.

## 8. The exact relation that erases the integral record

The finite companion group is recovered by adding

    x_1^4=1,

equivalently z^2=1, to the integral presentation.

On K, this adds a two-cell whose boundary has W4=4. Therefore

    H1(K;Z)=Z
        ->
    H1(K_finite;Z)=Z/4Z.

On the parity cover the two lifted fourth-return cells each have N=2, so

    H1(K_even;Z)=Z
        ->
    H1(K_even_finite;Z)=Z/2Z.

This is also obtained by the explicit boundary matrices. Over the reals, the new even-cover boundary rank is seven instead of six. Its cocycle space is now only the endpoint coboundaries. Every relation-preserving real additive scalar vanishes on closed histories.

The unit-complex phase survives the added relation because exp(i*pi*4/2)=1. The real accumulated phase does not.

This identifies the precise loss of information: declaring a completed finite return to be a null history erases the whole-turn register while retaining the modular phase.

One should not forbid complete returns. The issue is whether their retained history is kept or quotiented to zero.

## 9. An exact comparison theorem for the original cellular pipeline

Let C_*(Y) be the chain complex used by an independently supplied registered-history construction. Suppose maps F0 and F1 are defined on the vertices and eight edge generators of K_even. Require

    boundary1_Y F1 = F0 boundary1_K.

To induce a homology map, require the eighteen lifted relation boundaries to be boundaries in Y:

    F1 im(boundary2_K) subset im(boundary2_Y).

At the chain-map level one may supply F2 and check

    F1 boundary2_K = boundary2_Y F2.

Finally, verify independently that the primitive residual loop r maps to the selected temporal class r1.

Because H1(K_even;Z)=Z and [r] is its positive generator, these conditions force

    F_*([gamma])=N(gamma) r1

for every closed companion history. If the reported target law

    A_T(Phi_cell(n r1))=2n

is valid on that target line, then

    A_T(Phi_cell(F_*[gamma]))=2N(gamma)=W4(gamma).

This is a complete conditional comparison theorem. There are eighteen finite relation checks plus one primitive homology check after the actual edge map and boundary data are supplied. It does not require searching unboundedly for pairs of histories with equal outputs.

A scalar-only version can be tested even more directly if the independently supplied scalar is edge-additive on this cover: test a boundary2=0 and A(r)=2. Section 6 gives the entire conclusion.

A mere abstract isomorphism Z -> <r1> is not a substitute for these checks. Nor does this theorem imply that the full rank-three H_reg is identical to this one-coordinate companion sector.

The original Project41 chain map was not available in the inputs. Its eighteen compatibility equations and primitive evaluation have therefore not been run here.

## 10. Consequence for the action-phase problem

The inherited resolved phase lift is

    Phi_word=(pi/2)W4.

If an independently defined action contribution obeys the same additive relation contract, then on closed histories

    S=kappa W4 = (2kappa/pi) Phi_word.

On open histories it may additionally carry the endpoint potential beta dh, which cancels from endpoint-matched differences.

Thus the action-to-phase coefficient in this model must be

    a=2kappa/pi.

The theorem proves this functional form under an explicit, finite set of compatibility conditions. It does not determine kappa, show that every physical action obeys those conditions, or equate a to hbar.

The calibration scale for a complete W4=4 turn would be H=4kappa, and the reduced per-radian scale would be a=H/(2pi). Calling H the physical Planck constant would require an independent identification; the ratio itself follows from the established phase convention.

The mathematical advance is a finite cellular and relation-level test for the proposed identification. The integral receipt is no longer only a bookkeeping extension: it has a complete presentation, a torsion-free primitive homology coordinate, and a uniqueness theorem for closed-history additive scalars.

## 11. Verification and tamper controls

Run with Python 3.10 or newer, standard library only:

    python3 verify_phase_relations.py

The verifier reconstructs:

- all 230,400 native permutation products from the supplied certificate;
- 2,160 nine-relator checks over all address orderings and both phase orientations;
- 14,400 coordinate normal-form products;
- the exact integral boundary matrices of K and K_even;
- boundary squared equal to zero, exact ranks, and a determinant -1 saturation witness;
- the cochain identity W4=2N+dh and complete two-dimensional cocycle space;
- the residual/third-power/full-turn example words;
- the effect of attaching the finite fourth-return relation;
- rejection of a corrupted cell boundary, an inconsistent scalar, a lost full-turn relation, and an incorrect primitive-cocycle sign.

Finite sample-word tests supplement the algebraic all-word proofs; they do not replace them. The complete presentation proof is in Section 3. The homology proof uses the actual integer matrix and a saturated minor, not floating-point rank.

## Sources and construction ledger

1. `INTEGRAL_PHASE_RECEIPT.md`, preceding packet: defines the integral companion group, W4, the primitive cyclic comparison, and explicit resolved-history witnesses. Source file id: `file_000000003df482309a0682a77603bc94`.
2. `inputs/native_g60_fiber_product_isomorphism_044.json`: original supplied sixty-point permutation/reference-coordinate mapping. Its content hash is recorded in RESULT.json; prior audit result flags are not inputs to this proof.
3. `Pasted text(20260902-155317).txt`: source-recorded Project41 checkpoint 201ES, stating A_T o Phi_cell=2 tau_T. Source file id: `file_000000002a648230b84d768187d668be`. This is an imported statement, not an independently rerun cellular computation.
4. The nine-relator presentation, finite presentation complex, parity-cover matrices, cochain classification, fourth-return comparison, and finite compatibility theorem are new derivations in this packet.

### Final status

    Complete presentation of constructed integral receipt: proved.
    Cellular homology and all-word scalar uniqueness: proved.
    Equality with original Project41 cellular pipeline: requires the stated map checks.
    Physical coefficient or hbar calibration: not obtained by these computations.
