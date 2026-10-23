#!/usr/bin/env python3
"""Check package integrity, source mappings and local navigation, not mathematics."""
from pathlib import Path
from hashlib import sha256
import json
import re

HERE=Path(__file__).resolve().parent

def require(ok,message):
    if not ok:
        raise ValueError(message)

def local_path(name):
    p=(HERE/name).resolve()
    require(p==HERE or HERE in p.parents,'path outside package: '+name)
    return p

def main():
    catalog=json.loads((HERE/'history/attempts.json').read_text())
    coverage=json.loads((HERE/'history/source-coverage.json').read_text())
    entries=catalog['attempts'];records=coverage['records'];draws=catalog['poem_draws']
    require(len(entries)==41 and len({x['id'] for x in entries})==41,'attempt count/IDs')
    require(len(records)==29 and len({x['id'] for x in records})==29,'source count/IDs')
    expected={'BASE','P01','P02','P03'}|{'E'+str(i).zfill(2) for i in range(1,26)}
    require({x['id'] for x in records}==expected,'source corpus is incomplete')
    require(len(draws)==8 and len({x['title'] for x in draws})==7,'draw lineage')
    ids={e['id'] for e in entries};source_ids={r['id'] for r in records}
    for e in entries:
        require(set(e['sources'])<=source_ids and e['sources'],'unknown/missing source for '+e['id'])
        for field in ['original_proposal','attempt_or_test','recorded_outcome','precise_limit','research_time_saving','verification_in_v05']:
            require(bool(e.get(field)),'missing '+field+' in '+e['id'])
        require(e['seed_lineage'] in {s['id'] for s in draws},'unknown seed')
    for r in records:
        p=local_path(r['excerpt_path'])
        require(p.is_file() and sha256(p.read_bytes()).hexdigest()==r['excerpt_sha256'],'source excerpt hash: '+r['id'])
        mapped={e['id'] for e in entries if r['id'] in e['sources']}
        require(mapped and mapped==set(r['mapped_attempts']),'coverage mapping: '+r['id'])
        require('"lines": [' not in p.read_text(),'unexpected raw poem JSON')
    checked=0;seen=set()
    for line in (HERE/'SHA256SUMS').read_text().splitlines():
        if not line.strip():
            continue
        digest,name=line.split('  ',1)
        require(name not in seen and re.fullmatch('[0-9a-f]{64}',digest),'bad/duplicate manifest entry')
        seen.add(name);p=local_path(name)
        require(p.is_file() and sha256(p.read_bytes()).hexdigest()==digest,'checksum mismatch: '+name)
        checked+=1
    relevant={p.relative_to(HERE).as_posix() for p in HERE.rglob('*') if p.is_file()
              and (p.suffix in {'.md','.txt','.py','.cpp','.json'} or p.name=='LICENSE')
              and '__pycache__' not in p.parts
              and not any(part.startswith('.') for part in p.relative_to(HERE).parts)}
    require(relevant==seen,'manifest omits/adds package files')
    links=0
    for p in HERE.rglob('*.md'):
        text=p.read_text()
        for target in re.findall(r'\]\(([^)]+)\)',text):
            if '://' in target or target.startswith('mailto:'):
                continue
            name,_,fragment=target.partition('#')
            q=(p.parent/name).resolve() if name else p
            require(q.is_file(),'broken Markdown target '+target+' in '+p.name)
            if fragment:
                dest=q.read_text()
                explicit=set(re.findall(r'<a id="([^"]+)"',dest))
                headings=[]
                for title in re.findall(r'^#+\s+(.+)$',dest,re.M):
                    headings.append(re.sub(r'[^\w\- ]','',title.lower()).replace(' ','-'))
                require(fragment in explicit or fragment in headings,'missing fragment '+target)
            links+=1
    quote="Wait, did you directly quote me with the misspelling 'sources'?"
    for name in ['HANDOFF.txt','OPEN-RELEASE-AUTHORIZATION.md']:
        require('open sources as possible' in (HERE/name).read_text() and quote in (HERE/name).read_text(),'requested quote/humor missing')
    print(json.dumps({'passed':True,'manifest_files':checked,'source_records':29,'catalog_entries':41,'poem_draws':8,'checked_local_links':links},indent=2))

if __name__=='__main__':
    main()
