# What this release checks

Version 0.5 — 23 October 2026. Fresh finite checks and historical reconstruction
are different kinds of evidence. None establishes mathematical priority or
that poetry caused a useful result. All programs were written in this same
investigation; this is not external expert review or formal proof-assistant work.

## Existing compact certificates retained

`python3 verify.py` checks the later seven-coordinate certificate data, including
the exact17/4 support partition, minimum negative equal-pair cost609, extension
protection through q629, and ranked-support obstructions. Read NOTE.md for the
proofs connecting the finite maps to the universal-in-a-class claims.

`python3 test_verifier.py` checks that four deliberate corruptions are rejected.
The mathematical code and data for these checks are unchanged from the published
base package. Rejection tests are useful controls, not a proof of correctness.

## Selected earlier finite witnesses freshly rechecked

`python3 verify_history.py` uses Python's standard library and runs13 groups:

| Check | What is recomputed |
| --- | --- |
| Triple fibres | All90 top-containing union-closed triple fibres; six negative cases; both local balance inequalities |
| Fano matching obstruction | Explicit29-set family, closure,21 occurrences per coordinate and all seven maximum matching sizes7 from domains of size8 |
| Localization examples | Four sharp-sequence instances with q=3,4,6,10; closure, concentration and deficient triple counts |
| Core lifting | The55-set,49-set and24-set examples, their relevant frequency/count failures |
| Union roots | Exact sign separation using rational bounds for the square roots; floating-point signed-convolution sanity check at tolerance1e-12 |
| Private witnesses | Minimal generator representations checked by deletions; raw18-set scores and exact normalized scores for k=3,4,5 |
| Old q-mode transfer | The19-member core, negative point fibre, cap187<=189 and actual26-set modal extension |
| Uniform/balanced failures | The no-small-sets25-member product example and38-member outside-threshold balanced failure; actual q-modal status |
| Nonproduct clone | One explicit21-coordinate target /48-set extension with genuine uniform fibre deficit and unique q-mode |
| Joint costs | Core406's two individually admissible principal images, their over-cap combination, and two invalid point-weight witnesses |
| Adjusted pair failures | Both failing pairs of the 15-member core, adjusted costs and actual global e-maximizers |
| Stabilizer near miss | q201/cost207 rejected instance, its global score reversal, and q219/cost217 repair |
| Additive path | Accepted core q-values555->571->597 and the exact new obstruction rows/costs |

The checker reconstructs these specific examples from recorded definitions; it
does not run an adaptive search. Finite checks of parameter values do not prove
the unbounded formulas; the corresponding arguments remain in the source
excerpts. The Fano construction uses an explicit cyclic line/center choice;
it verifies a member of the recorded construction class, rather than claiming
to have recovered every byte of the original worker output.

One historical wording issue is clarified: the projective-plane formula
(q+2)2^(q-1) counts ABSENCE in the union-closed complement family, not its
occurrence frequency. The latter is m minus that quantity. Both the catalog
and the editorial note on sourceP02 preserve this distinction; the q=2 check
gives frequency21 and absence8 in a 29-set family.

## Historical results not freshly recertified in full

The narrative excerpts record earlier complete five-coordinate classifications,
larger sampled-core enumerations, flow/cut and branching certificates, and
the parameterized hand arguments. Their original evidence and scope are
described, but their multi-megabyte appendices are not all distributed here
and their complete runs were not repeated during this reconstruction.

In particular, this release's selected checker must NOT be cited as freshly
verifying the historical119-core coverage, the 1483/2178 fibre classifications,
the 959-core or1533-case surveys, every large orbit-flow certificate, or every
preserved-bank search outcome. Catalog entries say “historical report only”
unless a particular fresh check is identified. Their reports can guide research
and identify what to reverify, but are not a replacement for the omitted full
evidence when those results are used as proof premises.

## Package integrity and coverage

`python3 verify_release.py` checks SHA256SUMS, source-excerpt hashes, all 29
record mappings, the 41-entry catalog structure, eight draw records, and local
Markdown links/anchors. It checks no mathematical theorem by itself.

The current run's outputs are saved in history-verification-result.json and
verification-result.json. Each status is specific to the checks described here.
