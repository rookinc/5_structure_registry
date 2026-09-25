# WXYZTI as a chooser: reciprocal circuits

WXYZTI has a concrete candidate chooser structure: a shared-B transition participates in an alternating circuit of shared-B moves and reverse-partner swaps. The recovered rows determine four closed six-step circuits. This reconstructs the observed transition structure; it does not yet generate native G9000 choices.

## Evidence and scope

Two retrieved sources support this audit:

- Scott Cave, *The Gap A Answer-Pair Generator*, June 15, 2026, particularly sections 2–5 and 8. The paper states the reverse transform, the reciprocal pair law, and the conditional 48-to-12 and 16-to-4 selector results.
- `Pasted text(20260816-194035).txt`, a 79,007-byte source excerpt containing historical audit output. Parsing complete dictionaries and deduplicating by role and full transition recovers 12 shared-B rows and three reverse-partner rows. This excerpt is incomplete as a serialization of the original 24 rows.

The packet includes both sources, the recovered rows, a reproducible standard-library Python audit, and its exact results. Run `python3 verify.py` from the extracted audit directory.

## Four reconstructed circuits

Write a shared move as S(A,B,C)=(A′,B,C′), and the reverse move as R(A,B,C)=(A,C,B). Apply S followed by R, then look for the resulting full register in the next shared station. This joins all 12 recovered shared rows into four three-step cycles of the composite R∘S, hence four six-step WXYZTI circuits.

Each table cell is the register **before** that column's station transition. TI returns to the IW register in the same row.

| IW | WX | XY | YZ | ZT | TI |
|---|---|---|---|---|---|
| (1, 11, 2) | (7, 11, 14) | (7, 14, 11) | (3, 14, 2) | (3, 2, 14) | (1, 2, 11) |
| (2, 13, 1) | (9, 13, 10) | (9, 10, 13) | (0, 10, 1) | (0, 1, 10) | (2, 1, 13) |
| (10, 4, 5) | (3, 4, 2) | (3, 2, 4) | (12, 2, 5) | (12, 5, 2) | (10, 5, 4) |
| (12, 2, 5) | (1, 2, 0) | (1, 0, 2) | (10, 0, 5) | (10, 5, 0) | (12, 5, 2) |

All 12 shared transitions are retrieved. The swap rule supplies the 12 intervening reverse transitions: three agree with independently retrieved WX rows, while nine are derived completions not independently recovered in this excerpt. These are register circuits; native graph adjacency has not been established for them.

## What the reciprocal witness is doing

Opposite edges share a directed C transition: IW pairs with YZ, WX with ZT, and XY with TI. The reverse-partner operation swaps B and C within its own row; it does not undo its paired shared row.

This relationship follows algebraically from six-step closure. Start at (a,b,c). Let the first shared output be (a₁,b,t). After swapping, the second shared source is (a₁,t,b). Closure forces the next shared output to be (a₂,t,c), and the last shared output to be (a,c,b). The three shared C transitions are therefore c→t, b→c, and t→b. Their opposite reverse transitions repeat those same directed C edges.

Consequently, on these closed circuits, the reciprocal law is also a consistency condition across opposite edges. It cannot automatically be counted as an additional independent selector after closure has already been imposed.

The recovered WX/ZT subset permits an independent local replay: crossing four ZT rows with three retrieved WX rows gives 12 candidates; the reciprocal equations select three. The paper reports 48→12 for the complete realized universe. This audit does not claim an independent full replay using the nine inferred rows as if they were fresh evidence.

## Where apparent choice disappears

At IW, C=5 admits two recovered shared transitions:

- (12,2,5) → (1,2,0)
- (10,4,5) → (3,4,2)

The projected description `(station, C)` loses information needed to distinguish them. The full `(station, A, B, C)` source selects a unique row throughout the recovered table. This provides a concrete possibility for the chooser: contextual state resolves a projected ambiguity. It does not establish that the native system has no branching outside this admitted table.

## Why closure does not finish the chooser

As a countermodel, allow register entries in 0…14, require distinct A,B,C at every state, require shared moves to preserve B and change both A and C, and alternate with the exact swap. Do not restrict shared moves to the observed rows.

For each of the four observed starting registers, exhaustive enumeration gives **1,753 closed six-step completions**. Every completion also satisfies the opposite-edge C reciprocity just derived. These are relaxed arithmetic possibilities, not native graph candidates. They show that register preservation, swapping, closure, and this reciprocal equality together are insufficient to recover the observed circuit uniquely.

The paper's separate shell-and-rank selector accepts four of 16 observed C-cycle/anchor-cycle combinations. That adds a compatibility condition in a reduced universe, but the paper explicitly leaves the native origin of that universe open. The underlying anchor records were not recovered or independently replayed in this audit.

## The quarter-phase boundary

For each reconstructed circuit, the six integer C differences sum to zero, and their residues modulo 60 also sum to zero modulo 60. If d = (d mod 15) + 15q is used, the base-coordinate carry must accompany the sum of q values. The audit checks this exact bookkeeping. A bare sum of wrap labels must not be identified with native G9000 quarter-phase holonomy.

## Consequence for reconciled agreement

The working proposal is to let WXYZTI constrain which native paths may be attempted, then let the established transported-mode agreement test certify reconciliation along an actual native path. There is currently no proved mapping from these register transitions to native G9000 edges, so the proposal is not yet an executable native chooser.

The next decisive certificate needs:

1. A source-native registration of station and A,B,C data to native states, including any required history or anchor state.
2. A rule generating candidate shared-B moves before consulting realized row or pair labels, with alternatives that can genuinely fail.
3. A check that each accepted transition maps to an actual native edge or explicitly defined native path, and that reciprocal and circuit constraints reject the wrong candidates.
4. Agreement and phase measurements on those mapped paths, with remaining ties reported explicitly.

The strongest supported interpretation is therefore **a contextual transition grammar with reciprocal circuit consistency**. Whether it uniquely selects native motion remains open at the candidate-generation and registration steps.
