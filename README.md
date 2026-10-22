# Union-closed families: proper union decompositions, weighted certificates, and support obstructions

Draft v0.4.1 — 22 October 2026. Prepared from the human-directed, substantially
AI-assisted Strange Seed project. **Novelty and priority are unconfirmed.**
This is a reproducible mathematical note for scrutiny, not a peer-reviewed paper.
It concerns Frankl's union-closed sets conjecture, abundant elements, global
maximizers of proper union-decomposition counts, stable trace fibres, and
Poonen-style weighted certificates. These terms identify its subject, not a
claim to have solved the conjecture or invented the established machinery.

The motivating question asks whether a positive global maximizer of the number
of proper union decompositions in a finite union-closed family must contain an
element belonging to at least half the family. This work does not resolve that
question and does not prove Frankl's union-closed sets conjecture.

What can be reused here:

- A necessary adjusted cost bound for exterior trace fibres.
- Explicit finite certificates classifying all 21 two-coordinate supports for
  one seven-coordinate core: 17 blocked and four feasible only at equal weights.
- An exact minimum cost of 609 for a negative fibre on one equal-weight pair.
- A bound protecting four certificates under core extensions with q <= 629.
- Counterexamples to selecting local certificate supports by internal frequency.

Weighted certificates, cutting planes, Hall's theorem, injections and coordinate
cloning are established ideas. The possible contribution here is the particular
capped formulation and explicit results; exact prior art has not been excluded.

## Open licensing in v0.4

- **Software: MIT.** See [LICENSE](LICENSE).
- **Documentation: CC BY 4.0.** See [LICENSES/CC-BY-4.0.txt](LICENSES/CC-BY-4.0.txt).
- **Data and metadata: CC0 1.0.** See [LICENSES/CC0-1.0.txt](LICENSES/CC0-1.0.txt).

See [LICENSE.md](LICENSE.md) for exact scope and [OPEN-RELEASE-AUTHORIZATION.md](OPEN-RELEASE-AUTHORIZATION.md)
for the project owner's explicit authorization. Reuse, modification and
commercial use are permitted under the applicable terms.

## Publication preparation

Suggested repository: `union-closed-proper-decomposition-certificates`.
See [RELEASE-CHECKLIST.md](RELEASE-CHECKLIST.md) for upload instructions and
[release-details.json](release-details.json) for the adopted licenses and
project attribution. Repository URL, publication date and DOI remain unassigned.

We welcome prior-art references, equivalent formulations, proof-gap reports,
and independently reproduced checks. See [FEEDBACK.md](FEEDBACK.md).

## Audit correction introduced in v0.2

Start with [HANDOFF.txt](HANDOFF.txt) and [HISTORICAL-AUDIT.md](HISTORICAL-AUDIT.md).
The old approach ledger was a selected results summary, not a complete chronological
novelty audit. This revision separates documented checks from retrospective
assessments and undocumented timing. It does not establish a count of redundant
approaches or upgrade any novelty claim.

## Start here

Run, with Python 3.9 or later and no third-party dependencies:

```sh
python3 verify.py
python3 test_verifier.py
```

`verify.py` checks small finite witnesses and matching maps using integer and
rational arithmetic. Read [NOTE.md](NOTE.md) for the mathematical arguments
connecting those checks to the claimed classes of families. This is executable
certificate checking, not machine-checked formal mathematics or independent
human verification.

## Contents

| File | Purpose |
| --- | --- |
| NOTE.md | Definitions, proofs, exact scope and examples |
| HISTORICAL-AUDIT.md | Evidence-bounded audit and missing historical checks |
| audit-ledger.json | Machine-readable audit entries |
| HANDOFF.txt | Plain-text restart and publication handoff |
| RELEASE-CHECKLIST.md | Concrete steps before uploading |
| release-details.json | Adopted licenses, project attribution and release fields |
| LICENSE.md | Exact license scope and attribution guidance |
| OPEN-RELEASE-AUTHORIZATION.md | Project owner's express open-release instruction |
| FEEDBACK.md | How to report prior art, proof gaps and reproduction results |
| CHANGELOG.md | Revision scope and corrections |
| APPROACH-LEDGER.md | Routes tested and shortcuts ruled out |
| NOVELTY-AND-PRIOR-ART.md | Literature, search limits and priority status |
| QUESTIONS.md | Concrete questions for mathematicians and future models |
| PROVENANCE.md | AI involvement and verification limits |
| PUBLICATION.md | Suggested public home and release steps |
| claims.json | Machine-readable claim ledger |
| data/ | Explicit families, witnesses and matching certificates |
| verification-result.json | Checker output at preparation time |
| SHA256SUMS | Integrity hashes for the package contents |
| enumeration/ | Optional historical search programs and input |

No personal author name, repository URL or DOI has been invented.
Licenses were adopted under the project owner's express authorization. This draft was prepared before public release;
consult release-details.json for any subsequently recorded repository and date. No private conversation transcript or third-party poetry is included.

For another model: treat the finite results as claims to check; treat novelty
as unknown; do not turn failure of a sufficient certificate into a counterexample
to abundance. Please report errors and prior-art matches before extending the search.
