# REL010 Abstract Dihedral Consolidation

Status: PASS

## Result

REL010 closes at the abstract group-type layer.

Both retained views realize the same abstract finite group:

    Abstract Dihedral Group of Order 10

with presentation

    <r,s | r^5=1, s^2=1, srs=r^-1>.

The two retained realizations are:

1. Historical Fivefold Rotation-Reflection Register
2. Native Face Realization Kernel

They should therefore share the abstract-type parent

    dihedral-order-10-abstract

while retaining separate realization identities.

## Native face realization

The native face kernel has:

    group order = 10
    order-1 elements = 1
    order-2 elements = 5
    order-5 elements = 4

It is the kernel of the signed-block permutation action of an
order-80 selected-face stabilizer.

The kernel transports exactly by conjugation across the six native faces.

## Historical realization

The archived historical source gives

    a^2=b^2=1
    s=ab
    s^5=1
    ba=s^-1

which is the standard order-10 dihedral presentation.

The archived historical source does not preserve an explicit carrier,
permutation representation, or generator action sufficient for an
action-level comparison.

## What consolidates

The abstract group type consolidates.

    d5-history
        -> dihedral-order-10-abstract

    d5-face-kernel
        -> dihedral-order-10-abstract

## What does not consolidate

The realization views remain distinct.

No claim is made that they are:

    the same embedded subgroup
    the same carrier action
    the same generator realization
    naturally equivariantly equivalent

## Missing witness

An action-level identification requires either:

    an explicit historical carrier and generator action

or:

    a native map from the historical fivefold register
    into the face-kernel realization.

## Keeper

Same abstract group does not mean same realization.

REL010 is closed at the type layer and remains open at the action layer.
