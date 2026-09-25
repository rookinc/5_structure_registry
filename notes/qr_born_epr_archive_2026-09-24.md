# QR Born / EPR Archive Checkpoint

Date: 2026-09-24

Status: archive checkpoint

Purpose: freeze the current double-slit, Born, EPR, registered-history, analyzer, and G9000 research ledge before further investigation.

This note distinguishes proved finite structure, exact crosswalks, candidate constructions, and still-open physical correspondence. Do not silently promote candidate bridges.

---

## 1. Research architecture

The current Born/EPR thread links four structures that must remain distinct:

1. the registered five-frame G9000 carrier;
2. the registered-history pentagon carrier;
3. the six-axis native analyzer geometry;
4. the Program 02/03 singlet/readout construction.

Several bridges between them are now exact.

Others remain candidate or provenance-level only.

Core discipline:

    matching arithmetic is not identification

and

    matching representations require an explicit intertwiner
    or a common action domain.

---

## 2. Double-slit interpretation

The working QR interpretation is:

A realized event is singular.

Before registration, plurality belongs to the set of admissible continuations supported by the complete apparatus relation.

The source, slits, screen, phase relations, and any which-path apparatus jointly determine the admissibility structure.

A which-path detector therefore changes the relational grammar rather than merely revealing a pre-existing classical path.

The finite local routing result remains:

    180 = 60 + 120

with

    60 forbidden same-pivot continuations
    120 lawful switched-pivot continuations.

Locally:

    1 forbidden + 2 lawful.

The geometry determines permission but does not uniquely designate one member of the lawful pair.

Keeper:

    Admissibility can be canonical even when realization is not.

---

## 3. Certified G9000 five-frame structure

The registered G9000 construction consists of five transported G1800 frames.

Each frame contains 1800 states:

    5 * 1800 = 9000.

In registered native coordinates:

    F(f,x) = (f+1, Kx)

with

    F^5  = K
    K^4  = I
    F^20 = I.

The five-frame groupoid therefore has 450 free 20-cycles.

Frame transport is a graph isomorphism and intertwines the local K action.

The registered coordinate change trivializes the inter-frame maps in native coordinates.

This supports treating the frame index as a C5 register.

It does NOT identify the five G9000 frame labels with five of the six analyzer axes.

That shortcut is rejected.

---

## 4. Candidate G9000 Born decomposition

Introduce the pure frame shift

    S(f,x) = (f+1,x).

Then

    S^5 = I.

The linearized carrier has the form

    V_9000 ~= R^1800 tensor R[C5].

The real regular C5 representation decomposes as

    R[C5] = 1 + V_72 + V_144

with dimensions

    1 + 2 + 2 = 5.

Therefore

    9000 = 1800 + 3600 + 3600.

Interpretation:

    1800 = frame-common mode
    7200 = nontrivial fivefold relational sector.

Define

    K5 = S + S^-1 - S^2 - S^-2.

On the nontrivial frame sector:

    K5^2 = 5 P_evt.

The two real golden sectors have dimensions

    3600
    3600.

The candidate normalized density is

    rho5 = (5 P_evt + K5) / 36000.

Its two total sector masses are

    (5 + sqrt(5)) / 10
    (5 - sqrt(5)) / 10.

After complexification the four nontrivial C5 character blocks have masses

    (5 + sqrt(5)) / 20
    (5 + sqrt(5)) / 20
    (5 - sqrt(5)) / 20
    (5 - sqrt(5)) / 20.

This is the correct four-cell Born mass pattern.

Boundary:

This is not yet a physical probability theorem.

---

## 5. Five-frame current-square result

Define the real oriented frame difference

    D5 = S - S^-1.

Since S is orthogonal,

    D5^T = -D5

and therefore

    D5^T D5 = -D5^2.

On the complexified carrier define

    H5 = i(S - S^-1).

Then

    D5^T D5 = H5^2.

The exact C5 group-algebra identity is

    5 P_evt + K5 = 2 H5^2.

Therefore

    rho5 = H5^2 / 18000

and equivalently

    rho5
      = D5^T D5
        / Tr(D5^T D5).

Candidate interpretation:

    Born weight = normalized squared five-frame current.

The common frame mode is automatically annihilated:

    D5 P0 = 0.

More strongly:

    ker(D5) = V_ref
    dim ker(D5) = 1800

and

    im(D5) = V_evt
    dim im(D5) = 7200.

Keeper:

    The missing 1,800 was not extra room.
    It was the zero-current reference mode needed
    to make the other 7,200 relational.

Boundary:

The quadratic current norm is a strong native measure candidate.
The physical rule identifying it with observed probability remains open.

---

## 6. Native six-axis analyzer geometry

The native analyzer construction supplies six projective axes.

For their rank-one projectors:

    tr(Pi_i Pi_j) = 1/5

for every distinct pair i != j.

Equivalently:

    |n_i dot n_j| = 1/sqrt(5).

A symmetric conference representative C satisfies

    C^2 = 5 I_6.

Define

    J_C = C / sqrt(5).

Then

    J_C^2 = I_6.

Its two eigenspaces each have dimension 3.

The corresponding Gram kernels are

    G_+ = I + C/sqrt(5)
    G_- = I - C/sqrt(5).

The analyzer and G9000 magnitudes therefore agree:

    (E_ij)^2
      = 1/5
      = tr(Pi_i Pi_j)

for every distinct native analyzer pair.

This is the exact orientation-free Born magnitude bridge.

---

## 7. Registered-history carrier

There are twelve registered quotient pentagons.

Their holonomy split is

    6 b + 6 ab.

The signed cycle-incidence construction produces

    K_hist = M^T M - 5 I

with

    K_hist^2 = 5 I_12.

The canonical history density is

    rho_hist = (5 I + K_hist) / 60.

Its two six-dimensional spectral sectors carry masses

    (5 + sqrt(5)) / 10
    (5 - sqrt(5)) / 10.

Define the receipt grading

    Z_hist = +1 on b pentagons
    Z_hist = -1 on ab pentagons.

Then

    Z_hist^2 = I

and

    Z_hist K_hist = -K_hist Z_hist.

Writing

    J_hist = K_hist / sqrt(5)

gives

    J_hist^2 = I

and

    (Z_hist J_hist)^2 = -I.

Thus registered history contains an exact real Clifford structure.

---

## 8. Exact history sheet-axis normal form

Order the twelve registered pentagons as

    (ab sheet, b sheet).

Using only the signed permutations already stored in the history audit,

    K_hist

is put exactly into the form

          [ 0  C ]
          [ C  0 ]

or

    K_hist = X_sheet tensor C.

No dense spectral basis change is required.

Therefore the twelve registered pentagons have a literal signed coordinate structure

    {two receipt sheets}
        x
    {six analyzer axes}.

Define

    Q = X_sheet tensor I_6

and

    T = I_2 tensor J_C.

Then

    Q^2 = I
    T^2 = I
    [Q,T] = 0

and

    J_hist = Q T.

Hence

    rho_hist
      = (1/12) (I + Q T / sqrt(5)).

---

## 9. Exact four-cell history decomposition

Let

    q,t in {+1,-1}

be the simultaneous eigenvalues of Q and T.

Each (q,t) cell has rank 3.

Its probability mass is

    p(q,t)
      = (1/4)(1 + q t / sqrt(5))
      = (5 + q t sqrt(5)) / 20.

Thus the actual history carrier contains four rank-3 cells with masses

    (5 + sqrt(5))/20
    (5 + sqrt(5))/20
    (5 - sqrt(5))/20
    (5 - sqrt(5))/20.

For a fixed distinct analyzer context C_ij define

    a = eta q

    b = -C_ij eta t

with

    eta = +/-1.

Then

    p(a,b | i,j)
      = (1/4)(1 - a b C_ij / sqrt(5)).

The two values of eta differ by global reversal

    (a,b) -> (-a,-b).

Thus the Program 03 distinct-axis singlet table is the spectral table of two commuting operators on the registered-history carrier.

Same-axis anticorrelation remains a separate Program 03 gate.

---

## 10. Native history-analyzer common domain

The full 480 native automorphisms act on the twelve registered pentagons.

Their induced unsigned action contains only 120 distinct permutations.

Its kernel is the native V4.

Therefore the action factors through

    S5 = Aut(G60) / V4.

The same S5 acts intrinsically on the six Sylow-5 analyzer axes.

Direct comparison gives exactly two equivariant bijections

    {12 registered pentagons}
        <->
    {sheet +/-} x {six analyzer axes}.

They differ only by global sheet reversal.

Therefore the common history/analyzer domain that Draft 6 left abstract is now constructively recovered at the registered-pentagon level.

---

## 11. Projective analyzer action and history cocycle cancellation

Let

    p(g) in {0,1}

be the parity of the induced S5 element.

Define

          [ 0  1 ]
    J2 =  [      ]
          [-1  0 ]

so that

    J2^2 = -I.

In the sheet-axis history chart, native automorphisms act as

    U_H(g) = I_2 tensor M_g

for even g, and

    U_H(g) = J2 tensor M_g

for odd g.

The signed analyzer matrices satisfy

    M_g C M_g^T = (-1)^p(g) C.

Their multiplication law is

    M_g M_h
      = (-1)^(p(g)p(h)) M_gh.

Thus the signed analyzer action is projective.

But the sheet phase obeys the same cocycle:

    J2^p(g) J2^p(h)
      = (-1)^(p(g)p(h)) J2^p(gh).

The two signs cancel.

Therefore

    U_H(g) U_H(h) = U_H(gh).

Keeper:

    Registered history linearizes the projective signed
    six-axis analyzer action by carrying the compensating
    order-four sheet phase.

Conceptual keeper:

    What looks projective after projection becomes linear
    when retained history is restored.

---

## 12. G1800 swap-odd analyzer bridge

The native EPR tensor construction contains compatible 9D sectors

    V_chi tensor V_chi

inside actual G1800 quotients.

Native factor swap preserves the same-character sectors.

Their antisymmetric part is

    wedge^2 V_chi.

Since

    dim(V_chi) = 3,

we obtain

    dim(wedge^2 V_chi) = 3.

This supplies a native rank-3 multiplicity candidate.

An important representation-theoretic feature is that scalar deck signs disappear under exterior square:

    (-I) wedge (-I) = +I.

So the swap-odd carrier is naturally suited to quotient-visible analyzer geometry.

---

## 13. Candidate 12D G1800 x C5 history carrier

The nontrivial real C5 frame module has dimension 4.

Therefore

    wedge^2 V_chi
      tensor
    E_C5_nontriv

has dimension

    3 * 4 = 12.

This matches the registered-history carrier.

At the golden-sector level the dimensions become

    6 + 6.

At the four-character level they become

    3 + 3 + 3 + 3.

This is a construction-motivated candidate carrier.

It is not yet the final native G9000-to-history identification.

---

## 14. C5 frame Clifford structure

On the four-dimensional nontrivial C5 module define

    J5 = K5 / sqrt(5).

Then

    J5^2 = I.

The frame-register multiplier

    f -> 2f mod 5

sends

    S -> S^2

and therefore

    K5 -> -K5.

This gives a candidate sector-exchange involution Z5 satisfying

    Z5^2 = I

    Z5 J5 = -J5 Z5

    (Z5 J5)^2 = -I.

Thus the nontrivial C5 frame module carries the same abstract Clifford algebra as registered history.

Boundary:

The full native status of this multiplier on the actual registered G9000 groupoid still requires certification.

---

## 15. Natural C5-to-history label map

Let

    s = sgn(K5)

label the golden sector, and let

    r = sgn(H5)

label conjugate current orientation.

Define

    q = r
    t = s r.

Then

    q t = s.

So the Born sector is preserved.

Under frame reversal

    S -> S^-1,

we have

    s -> s
    r -> -r

and therefore

    (q,t) -> (-q,-t).

This exchanges both registered outcomes while preserving their product parity and Born mass.

Under the candidate sector-exchange Z5,

    (s,r) -> (-s,-r),

hence

    (q,t) -> (-q,t).

This matches the algebraic form of the history receipt-sheet grading.

This is a strong algebraic correspondence.

The final native G9000-to-history vector-space intertwiner remains open.

---

## 16. EPR interpretation

The current factorization is

    fivefold/history geometry
        -> 1/sqrt(5)

    analyzer incidence
        -> C_ij

    history sheet
        -> q

    conference sector
        -> t

    registered readout
        -> (a,b).

For distinct axes

    Gamma_ij = -C_ij / sqrt(5)

and

    p(a,b | i,j)
      = (1/4)(1 + a b Gamma_ij).

Local marginals are exactly balanced:

    P(A=+1) = P(A=-1) = 1/2
    P(B=+1) = P(B=-1) = 1/2.

Joint parity is nontrivial.

The finite analyzer set supports the CHSH value

    1 + 3/sqrt(5)
      ~= 2.341640786
      > 2

when combined with the same-axis singlet condition.

This is not an ordinary Bell-local hidden-variable model.

The primitive structure is relational/contextual rather than a pair of context-independent local response tables.

---

## 17. What is currently strong

Treat the following as established finite structure or exact crosswalk at their stated domains:

- G9000 five-frame recurrence F^5=K and F^20=I.
- Native six-axis projective analyzer geometry.
- Distinct-axis squared overlap 1/5.
- Registered-history identity K_hist^2=5I.
- Exact history Born sector masses.
- Exact sheet-axis normal form K_hist=X_sheet tensor C.
- Four rank-3 history cells with exact Born masses.
- Common domain between twelve registered pentagons and two sheets times six analyzer axes.
- Exactly two equivariant history/analyzer identifications differing by global reversal.
- Projective signed analyzer cocycle.
- Matching history-sheet cocycle.
- Exact cocycle cancellation producing an ordinary native history action.
- Native swap-stable 9D G1800 analyzer tensor sectors.
- Native 3D exchange-odd carrier wedge^2 V_chi.

---

## 18. What remains candidate or open

Do not silently promote:

- G9000 current square as the completed physical Born rule.
- Literal identification of four complex C5 character blocks with physical registered outcomes.
- Native action of f->2f on the actual registered G9000 groupoid.
- Identification of five G9000 frame labels with five analyzer axes.
- Any 7200-element receipt set inferred from a 7200-dimensional harmonic subspace.
- Physical spin interpretation.
- Physical analyzer/instrument implementation.
- Laboratory EPR realization.
- Native chronological source law generating irrational Born frequencies from a finite autonomous endpoint state.

---

## 19. Explicit rejected shortcuts

### Matching cardinality is not an intertwiner

A 7200-element set is not automatically a 7200-dimensional linear sector.

### Matching phase arithmetic is not matching carrier action

C5, C10, and C20 structures retain different domains and provenance.

### G9000 frame labels are not analyzer-axis labels

Audit040 does not establish that identification.

### Projective geometry does not choose absolute axis signs

[n] = [-n].

Absolute analyzer orientation remains a torsor/gauge issue.

### Registered history is not a selector

Registration records which lawful continuation occurred.

It does not by itself determine which continuation must occur next.

### Finite autonomous deterministic endpoint evolution cannot force an irrational limiting frequency

If literal long-run frequency generation is required, the source must involve unbounded retained history, stochasticity, or another enlarged/non-autonomous domain.

---

## 20. Current conceptual picture

The working chain is

    relation
      -> admissibility
      -> event
      -> receipt
      -> history
      -> measure.

Probability is downstream of registered relation.

Born weights appear as finite structural spectral masses.

EPR correlation belongs to the joint relation and analyzer context rather than independently to either endpoint.

Registered history is not passive bookkeeping.

It carries the phase that linearizes the projected analyzer action.

Keeper:

    Born tells us how relational weight is distributed.
    EPR tells us that the information being measured belongs to the relation.

Newest keeper:

    Registered history carries the phase that the projected
    analyzer description is missing.

---

## 21. Next research ledge

When research resumes, do not begin another broad Born/EPR search.

The next exact target is:

    G9000 frame current
        ->
    registered-history sheet intertwiner.

The analyzer/history side is now substantially closed.

The remaining question is whether the independently constructed G9000 five-frame current feeds into the already-native history-sheet structure.

The desired native bridge should explain

    D5 -> (Q,T)

or equivalently

    (s,r) -> (q,t)

with

    q = r
    t = s r

while preserving the certified native actions.

Until that bridge is constructed, the G9000 current-square Born derivation remains a strong candidate rather than part of the closed history/analyzer theorem chain.
