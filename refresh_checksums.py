#!/usr/bin/env python3
"""Regenerate the package integrity manifest after intentional local edits."""
from pathlib import Path
from hashlib import sha256

HERE=Path(__file__).resolve().parent
extensions={'.md','.txt','.py','.cpp','.json'}
files=sorted(p for p in HERE.rglob('*') if p.is_file()
             and p.name!='SHA256SUMS'
             and (p.suffix in extensions or p.name=='LICENSE')
             and '__pycache__' not in p.parts
             and not any(part.startswith('.') for part in p.relative_to(HERE).parts))
(HERE/'SHA256SUMS').write_text(''.join(
    sha256(p.read_bytes()).hexdigest()+'  '+p.relative_to(HERE).as_posix()+'\n'
    for p in files))
print('Updated SHA256SUMS for',len(files),'files.')
