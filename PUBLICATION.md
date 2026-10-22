# Suggested public home

Recommendation as of 22 October 2026: a public GitHub repository named
`union-closed-proper-decomposition-certificates`, with this note, the JSON data and verifier.
GitHub is a practical first home because readers can inspect changes, run the
checker and report errors or prior-art matches in issues. This is a recommendation;
this package was prepared before public release. An eventual repository URL
and release date should be recorded in release-details.json.

Suggested repository/README title: **Union-closed families: proper union
decompositions, weighted certificates, and support obstructions**.
The mathematical note retains its narrower title.
Suggested repository description: **An exploratory AI-assisted mathematical note
with explicit finite certificates; novelty unconfirmed.**

## Concrete release sequence

1. Have a human review NOTE.md, the checker and the prior-art qualifications.
2. Select the owning account. Open licenses and project attribution are now
   adopted in LICENSE.md; retain the full license texts and authorization note.
   A personal author name is not required to apply the included terms.
3. Create a public repository and upload the contents of this folder, including
   the data and verifier. Do not upload the private source conversation.
4. Run `python3 verify.py` and `python3 test_verifier.py` from a fresh checkout.
   Tag a reviewed release and preserve the exact version when requesting feedback.
5. Invite expert corrections and prior-art identifications with precise questions
   from QUESTIONS.md. Novelty can remain unconfirmed while the results are shared.

GitHub's official repository instructions:
https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository

## Archival DOI later, if eligible

Zenodo is a possible later archive, not an unconditional recommendation for this
draft. Its generative-AI guidance requires genuine human-conducted research
underlying a deposit, depositor accountability and substantive AI disclosure;
AI tools cannot be listed as authors/creators/contributors. This project's
AI-heavy mathematical work has not yet received independent human expert review.
Human review alone does not automatically establish eligibility: assess the
actual provenance against the policy and ask Zenodo support if uncertain.

Policy checked 22 October 2026:
https://support.zenodo.org/help/en-gb/13-policies/227-what-is-your-usage-policy-for-generative-ai-for-depositors

If appropriate after that check, a versioned deposit can archive a reviewed
release. No DOI has been reserved, assigned or claimed here. arXiv or journal
submission would be a separate step after subject-expert assessment, rather
than the first destination for an unreviewed exploratory package.

Public availability helps people and retrieval-enabled models find the work.
It does not ensure that future models will train on it or remember it.

For the current release, include HISTORICAL-AUDIT.md and audit-ledger.json in any release.
Do not describe the route summary as a complete historical novelty audit.
