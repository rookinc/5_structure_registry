# CP-SAT Mac Execution Receipt

Date: 2026-09-24

This directory preserves the first executed OR-Tools CP-SAT run
of the frozen Thalean registry alias model.

## Result

- OR-Tools: 9.15.6755
- Baseline: OPTIMAL
- Queries completed: 64
- Forced aliases: 2
- Recorded-view separations: 50
- Open under encoded constraints: 12
- Optimization objective: none
- Native theorem promotion: none

OPTIMAL here means the satisfaction model is feasible.
The merge/separate opposition probes determine the pair classifications.

## Open comparisons

- REL010: d5-face-kernel <-> d5-history
- REL011: d8-selected-face-operators <-> d8-charge-center-locator
- REL012: d8-selected-face-operators <-> d8-face-blocks
- REL018: v4-native <-> v4-voltage
- REL019: v4-native <-> v4-root-projective
- REL028: x12-sections <-> x12-kernel
- REL031: face-crown <-> history-crown
- REL032: frame-contrast <-> history-fivefold-contrast
- REL046: w4-winding <-> r1-history-class
- REL047: h12-history-candidate <-> history-pentagon-space
- REL048: k120-group-locator <-> k120-common-cover
- REL055: rotor-o2 <-> o2-surface-envelope

## Boundary

This run checks only the frozen registry alias model.
It does not establish abstract group isomorphism, equality of embedded
subgroups, equivariant action equivalence, quotient identification,
or a linear intertwiner.
