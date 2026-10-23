# Union-closed families: poetry-associated approaches, failures and certificates

Version **0.5**, prepared 23 October 2026. A human-directed, substantially
AI-assisted Strange Seed / Truth & Wonder research handoff.
**Novelty unconfirmed. Historical reconstruction, not peer review.**

This package documents poetry-conditioned approaches to Frankl's union-closed
sets conjecture and their mathematical follow-ups in one conversation. It
preserves false selectors, blocked mechanisms, inconclusive searches and useful
restricted results so mathematicians and models can avoid repeating them blindly.
It also retains explicit certificates for the later proper-decomposition branch.
Topics include proper union decompositions, modal union distributions, stable
trace fibres, private-witness selectors, Poonen-style weighted certificates,
Hall matching obstructions and failed abundance-transfer rules.

The expanded catalog contains **41 claim/subroute entries mapped to all 29 saved
Frankl records**: the baseline, three pilots and Explorations01–25. There were
eight poem draws, selecting seven different titles. Those counts are not counts
of independent discoveries, and do not establish that poetry improves reasoning.

## Start here

| Want to… | Read |
| --- | --- |
| Avoid known dead ends quickly | [Research stopping points](RESEARCH-STOPPING-POINTS.md) |
| Inspect each proposal, outcome and precise limitation | [Poetry approach catalog](POETRY-APPROACH-CATALOG.md) |
| Trace a poem-associated move through later work | [Seed lineage](SEED-LINEAGE.md) |
| Check that earlier branches were included | [Source coverage](SOURCE-COVERAGE.md) |
| See what has actually been rechecked | [Verification scope](VERIFICATION-SCOPE.md) |
| Read the later self-contained certificate arguments | [Mathematical note](NOTE.md) |
| Examine literature overlap and timing | [Prior art](NOVELTY-AND-PRIOR-ART.md), [historical audit](HISTORICAL-AUDIT.md) |
| Resume in another conversation | [Plain-text handoff](HANDOFF.txt) |
| Report prior art or an error | [Feedback guide](FEEDBACK.md) |
| Upload this update | [Release checklist](RELEASE-CHECKLIST.md) |

The catalog's sources are linked narrative excerpts, not full raw conversations
or complete copies of every earlier computational appendix. Every saved report
has a coverage mapping; unrecorded transient ideas cannot be guaranteed recovered.
Historical enumeration claims are distinguished from fresh finite checks.

## Run the checks

Python 3.9 or later; no third-party dependencies:

```sh
python3 verify.py
python3 test_verifier.py
python3 verify_history.py
python3 verify_release.py
```

The first checks cover the retained finite certificates; verify_history.py
recomputes 13 selected earlier witness groups. verify_release.py checks integrity,
coverage and local navigation. The checks do not establish priority, a solution
to Frankl, or a causal poetry effect. The general q-mode and positive-e-mode
selectors remain unresolved within this project.

After intentional edits, run `python3 refresh_checksums.py`, then
`python3 verify_release.py`. Regenerate the manifest once after all edits; it
does not checksum itself.

## Open reuse

- **Original software: MIT**, full text in [LICENSE](LICENSE).
- **Original documentation: CC BY 4.0**, full text in [LICENSES/CC-BY-4.0.txt](LICENSES/CC-BY-4.0.txt).
- **Data and metadata: CC0 1.0**, full text in [LICENSES/CC0-1.0.txt](LICENSES/CC0-1.0.txt).

See [license scope](LICENSE.md) and the owner's explicit
[open-release authorization](OPEN-RELEASE-AUTHORIZATION.md). Commercial reuse
and modification are welcome under those terms. External cited works are not
relicensed. No poems or frozen poem corpus are distributed.

Repository: https://github.com/courterr/union-closed-proper-decomposition-certificates

The repository first published the smaller v0.4.1 package on 22 October 2026.
This v0.5 package is a prepared update; its upload/release date is not assigned
by this document. Mathematical exploration remains paused; this work expands
the research record rather than launches another search.
