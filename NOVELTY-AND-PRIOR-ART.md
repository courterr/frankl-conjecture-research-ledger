# Priority assessment — limited check, 22 October 2026

**No claim of established novelty is made.** A failure to locate an exact match
in web searches does not establish priority, especially for a reformulation of
a long-studied conjecture. These results can still save readers time as explicit,
checkable examples and barriers, even if an expert identifies earlier work.

## What is already established

Weighted coordinate certificates for union-closed families originate in
Poonen's work. Pulaj develops a cutting-plane framework for finding such weights.
This package's generic use of nonnegative weights, exact feasibility,
separation constraints and computational certificates is not presented as new.
Hall's theorem, injection arguments and coordinate cloning are standard tools.

Colbert's discussion of basis sets includes a zero-proper-decomposition
condition, and discusses injection-based notions. Merely writing about proper
decompositions or injections is therefore not evidence of novelty. That does
not settle priority for maximizing the particular score used here.

## What has not been matched in the limited check

| Item | Defensible status |
| --- | --- |
| Positive global e-maximizer selector question | Exact prior-art/status match not established |
| Adjusted cap 2Q(G,H)+Q(H,H)-2|H|<=q_G(A) in this application | Derived in NOTE.md; priority unconfirmed |
| Explicit G38 17/4 classification and equality-only weights | Certificate-checked instance; priority unconfirmed |
| Sharp cost609 and protection through q629 | Proof and finite certificates supplied; priority unconfirmed |
| Distinct-column frequency-pair obstruction | Explicit checkable example; priority unconfirmed |
| Cloning obstruction for literal top-k recipe | Elementary application of an established technique; priority unconfirmed |

An exact earlier result, an equivalent semilattice formulation, or a general
theorem subsuming these instances may exist. No comprehensive MathSciNet or
zbMATH review and no independent subject-expert review has been completed.

## References and scope of inspection

1. Bjorn Poonen, *Union-closed families*, Journal of Combinatorial Theory,
   Series A 59(2), 253–268 (1992).
   https://doi.org/10.1016/0097-3165(92)90068-6
   Bibliographic information and weighted theorem checked via Pulaj; the original
   article was not successfully retrieved in this publication-preparation pass.
2. Jonad Pulaj, *Cutting Planes for Families Implying Frankl's Conjecture*,
   arXiv:1702.05947v2 (4 June 2018; first version 20 February 2017).
   https://arxiv.org/abs/1702.05947v2
   PDF inspected, including the weighted characterization and algorithmic framework.
   Related author code: https://github.com/JoniPulaj/cutting-planes-UC-families
   No code from that repository is included here.
3. Cory H. Colbert, *Chain Conditions and Optimal Elements in Generalized
   Union-Closed Families of Sets*, arXiv:2412.18740v3 (2 December 2025).
   https://arxiv.org/abs/2412.18740v3
   PDF inspected for related decomposition and injection notions. Its optimal
   elements are not automatically the e-maximizers studied in this package.
4. Timothy Gowers, *FUNC4: further variants* (22 February 2016).
   https://gowers.wordpress.com/2016/02/22/func4-further-variants/
   Follow-up lead. The entire comment corpus has not been comprehensively reviewed.

## Representative searches

Both available search engines were used, with stronger-engine follow-up for
priority checks. Queries included:

```text
"union-closed" "decompositions" abundant
"union-closed" "representations" "pairs" Frankl
"union-closed" "matching" "Poonen" weighted
union closed Frankl number union representations most decompositions maximal member
"Frankl" "decompositions" union
"union-closed" "nontrivial" "decompositions"
"union-closed" "most popular" union
"union-closed" "multiplicity" "union"
"Frankl" "join representations"
"union-closed" "proper decompositions"
"union-closed" "proper union"
"Frankl" "representation count"
"union-closed" "609" "597"
"union-closed" "support" "two" "Poonen"
```

Many returned irrelevant or incomplete results. No exact match was identified;
this is a search limitation, not a novelty certificate. Suggested expert question:
“Is this capped fibre formulation or selector already known, and are these
explicit support obstructions subsumed by an existing result?”
