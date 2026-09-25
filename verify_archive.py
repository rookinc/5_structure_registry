#!/usr/bin/env python3
"""Verify preserved package bytes without executing producers or the CP-SAT engine."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path, PurePosixPath
import sys

ROOT=Path(__file__).resolve().parent

def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()

def main() -> int:
    checks=0; failures=[]
    for folder in ('glossary','registry','cp_sat'):
        base=ROOT/folder
        for line in (base/'SHA256SUMS').read_text(encoding='utf-8').splitlines():
            want,rel=line.split('  ',1); pp=PurePosixPath(rel)
            if pp.is_absolute() or '..' in pp.parts or '\\' in rel:
                raise ValueError('Unsafe checksum path: '+rel)
            target=base/rel
            checks+=1
            if not target.is_file() or target.is_symlink() or sha(target)!=want:
                failures.append(folder+'/'+rel)
    checks+=1
    if sha(ROOT/'cp_sat/upstream/thalean_symbol_registry_2026-09-24.zip') != json.loads((ROOT/'SOURCE_ARCHIVES.json').read_text())['archives'][1]['sha256']:
        failures.append('registry_upstream_zip_identity')
    result=json.loads((ROOT/'cp_sat/reports/cp_sat_result.json').read_text())
    checks+=1
    if result.get('engine_status')!='NOT_RUN' or result.get('cp_sat_executed') is not False:
        failures.append('archived_engine_status_changed')
    print('ARCHIVE_BYTE_CHECKS='+str(checks))
    print('ARCHIVE_BYTE_CHECK_PASS='+str(not failures).lower())
    print('CP_SAT_ENGINE_EXECUTED_BY_THIS_CHECK=false')
    print('HISTORICAL_PRODUCERS_EXECUTED=false')
    if failures:print(json.dumps({'failures':failures},indent=2))
    return int(bool(failures))

if __name__=='__main__':sys.exit(main())
