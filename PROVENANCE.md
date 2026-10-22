# Provenance and limits

This package arose from a human-directed exploration called Strange Seed,
which investigates whether abstract prompts, including poetry, can suggest
useful problem-solving moves. ChatGPT/Codex was used substantially for approach
generation, mathematical derivation, code, computational exploration, literature
search and writing. The mathematical claims are presented independently of that
origin so readers can inspect them directly.

The handoff was assembled on 22 October 2026. Its Python verifier was executed
on the included finite certificates, with exact integer/rational checks and
several rejection tests for deliberately corrupted input. The accompanying
proofs explain the universal claims those certificates support. This is not
independent human expert review, peer review or formal proof-assistant verification.
The checker and the explanations may share errors and warrant independent review.

The optional C++ programs preserve earlier search implementations. Their labels
and historical search counts are not used as substitutes for the finite proofs.
This packaging pass did not rerun the full searches. No external research code,
private conversation transcript or third-party poems are included.

The package does not establish that poetry caused a useful result or that any
mathematical idea is new. It does not solve the motivating selector question,
Frankl's conjecture or P versus NP. Public release can be useful without those
claims, provided the status remains clear.

Public attribution for this package is Strange Seed / Truth & Wonder project.
The human project owner authorized open licensing in v0.4; see LICENSE.md and
OPEN-RELEASE-AUTHORIZATION.md. No personal author name has been assigned. AI tool use should be disclosed in any eventual submission;
the tool should not be treated as an accountable human author.

Revision v0.2 adds an evidence-bounded audit based on the opening sections of
Exploration18 and Exploration25, v0.1 and the visible workflow discussion. It
does not reconstruct the entire historical record. No new literature search
or mathematical exploration was performed. Historical check timing is marked
undocumented where the inspected records do not establish it.
