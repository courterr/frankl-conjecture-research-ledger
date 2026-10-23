# Uploading the expanded v0.5 handoff

The existing public repository is:
https://github.com/courterr/union-closed-proper-decomposition-certificates

1. Extract the v0.5 ZIP. Open its inner
   `union-closed-proper-decomposition-certificates` folder until README.md,
   NOTE.md, verify.py, history/, data/ and LICENSES/ are visible together.
2. On the repository's MAIN page choose Add file -> Upload files. Upload all
   those inner contents. Keep internal paths intact; upload files/folders rather
   than the ZIP or an enclosing download folder. Existing names are updated,
   and the new history/catalog files are added. No repository rename is needed.
3. Review the uploaded draft and commit with a message such as
   `Expand handoff with poetry-associated failures and source coverage`.
4. Confirm the homepage shows the new navigation table and the catalog/coverage
   links work. The package checksums already reflect this update; no manual
   hash edits are required unless you change additional content.

For a local verification before or after upload:

```sh
python3 verify.py
python3 test_verifier.py
python3 verify_history.py
python3 verify_release.py
```

After intentional edits, including release metadata:

```sh
python3 refresh_checksums.py
python3 verify_release.py
```

Regenerate once after all changes. SHA256SUMS does not checksum itself.
The source-excerpt hashes in history/source-coverage.json are separate provenance
fields; if you deliberately edit a source excerpt, update its recorded hash
and document the change before refreshing the outer manifest. Do not silently
alter historical claims while calling the result an unchanged excerpt.

Licenses are already selected and included: MIT software, CC BY 4.0 documentation,
CC0 1.0 data/metadata. Retain LICENSE.md's scope and the AI-use disclosure. The
general claims remain unresolved, novelty unconfirmed, and historical appendix
coverage incomplete even though all 29 narrative records are mapped.

The repository URL and initial-publication date are already recorded. The v0.5
upload date and any release tag may be filled when actually assigned, followed
by regenerating checksums. No DOI has been assigned. Creating a tagged release
is optional. This preparation does not itself upload or publish the update.
