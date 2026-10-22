# Before uploading this draft

Suggested repository name: `union-closed-proper-decomposition-certificates`.
Suggested description: **Exploratory AI-assisted research on union-closed
families, with explicit certificates and reproducible checks; novelty unconfirmed.**

1. **Retain project attribution.** This release credits Strange Seed / Truth &
   Wonder project. You may add your preferred personal attribution before
   posting. Keep the AI-use disclosure; the AI tool is not a human author.
2. **Keep the adopted licenses.** Software is MIT, documentation is CC BY 4.0,
   and data/metadata are CC0 1.0. LICENSE.md specifies the exact scope and full
   terms are included. The project owner's authorization is quoted in
   OPEN-RELEASE-AUTHORIZATION.md. No further license choice is required for
   this package. Keep the copyright and license notices when required.
3. **Review the qualifications.** Keep novelty unconfirmed, the audit partial,
   and AI involvement visible. Passing finite checks is not peer review. These
   are not counterexamples to Frankl's conjecture or a proof of the selector.
4. **Upload extracted files.** Unzip this archive, then upload the contents of
   its `union-closed-proper-decomposition-certificates` folder to the repository
   root. Upload README.md, NOTE.md, code and data as individual files; publishing
   only the ZIP makes the contents less convenient to inspect. Keep relative
   paths intact. Do not upload the private source conversation.
5. **Run the two checks.** From the repository root, run `python3 verify.py` and
   `python3 test_verifier.py`. Preserve the outputs and note any environment
   differences. An incomplete optional enumeration is not a completed proof.
6. **Record the release.** After upload, fill `repository_url`, `publication_date`
   and `release_tag` in release-details.json with actual values. Update the
   matching fields in claims.json if applicable. A tag such as v0.4 identifies
   a reviewed snapshot; do not invent a DOI. Retain the draft label until a
   human has reviewed what is being released.
7. **Invite corrections.** Enable issues if desired, and use FEEDBACK.md to
   request prior-art matches, equivalent formulations, proof gaps and reproduction
   reports. The initial literature-search record is incomplete; do not claim
   that every approach was cleared before investigation.

If you edit any files, regenerate SHA256SUMS. From the repository root:

```sh
python3 - <<'PY'
from pathlib import Path
from hashlib import sha256
root = Path('.')
files = sorted(p for p in root.rglob('*') if p.is_file()
               and p.name != 'SHA256SUMS'
               and '__pycache__' not in p.parts
               and not any(part.startswith('.') for part in p.parts))
Path('SHA256SUMS').write_text(''.join(
    sha256(p.read_bytes()).hexdigest() + '  ' + p.as_posix() + '\n'
    for p in files))
PY
```

This checklist prepares a transparent exploratory release. It does not certify
novelty, legal ownership, archival eligibility or mathematical correctness.
