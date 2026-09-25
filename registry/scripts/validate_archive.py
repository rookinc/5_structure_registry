#!/usr/bin/env python3
"""Validate archive integrity and cross-references, not mathematical claims."""
from pathlib import Path
import json, hashlib, re, sys
ROOT=Path(__file__).resolve().parents[1]
def main():
 d=json.loads((ROOT/'data/structure_registry.json').read_text())
 sources=d['sources'];records=d['records'];ids=[r['id'] for r in records];known=set(ids)
 checks=[]
 def check(name,ok,detail=''):
  checks.append(dict(name=name,passed=bool(ok),detail=detail))
 check('record_ids_unique',len(ids)==len(known))
 check('all_record_sources_exist',all(k in sources for r in records for k in r['source_ids']))
 check('all_relationship_endpoints_exist',all(z['source'] in known and z['target'] in known for z in d['relations']))
 check('all_relationship_sources_exist',all(k in sources for z in d['relations'] for k in z['source_ids']))
 for k,s in sources.items():
  p=ROOT/s['path'];exists=p.is_file();check('source_exists:'+k,exists)
  if exists:
   b=p.read_bytes();check('source_hash:'+k,hashlib.sha256(b).hexdigest()==s['sha256'])
   check('source_lines:'+k,1<=s['line_start']<=s['line_end']<=len(b.decode('utf-8').splitlines()))
 corpus=json.loads((ROOT/'data/source_files.json').read_text())
 for x in corpus:
  for rel in [x['path']]+x['duplicate_paths']:
   p=ROOT/rel;check('scanned_payload:'+rel,p.is_file() and hashlib.sha256(p.read_bytes()).hexdigest()==x['sha256'])
 text=(ROOT/'notes/qr_structure_registry.md').read_text()
 anchors=re.findall(r'<a id="([^"]+)"',text)
 check('all_records_rendered',all(i in anchors for i in ids))
 check('record_anchors_unique',len(anchors)==len(set(anchors)))
 check('main_registry_ascii',text.isascii())
 occ=[json.loads(l) for l in (ROOT/'data/occurrences.jsonl').read_text().splitlines()]
 check('occurrence_ids_sequential',[o['occurrence_id'] for o in occ]==list(range(1,len(occ)+1)))
 check('occurrence_candidate_ids_valid',all(i in known for o in occ for i in o['candidate_structure_ids']))
 check('source_occurrence_paths_valid',all((ROOT/o['path']).is_file() for o in occ))
 check('matching_offsets_valid',all(o['column']>=1 and o['end_column']>o['column'] for o in occ))
 lines_cache={x['path']:(ROOT/x['path']).read_text().splitlines() for x in corpus}
 check('raw_matches_recover_exactly',all(lines_cache[o['path']][o['line']-1][o['column']-1:o['end_column']-1]==o['raw'] for o in occ))
 idx=json.loads((ROOT/'data/label_index.json').read_text())
 check('all_occurrences_indexed',sorted(i for k in idx for i in k['occurrence_ids'])==list(range(1,len(occ)+1)))
 check('all_index_candidates_valid',all(i in known for x in idx for i in x['candidate_structure_ids']))
 check('coverage_present',(ROOT/'provenance/coverage.md').is_file())
 check('readme_present',(ROOT/'README.md').is_file())
 check('explorer_present',(ROOT/'structure_explorer.html').is_file())
 h=(ROOT/'structure_explorer.html').read_text();m=re.search(r'<script id="data" type="application/json">(.*?)</script>',h,re.S)
 check('explorer_inline_data_matches',m is not None and json.loads(m.group(1))==d)
 stats=json.loads((ROOT/'data/scan_statistics.json').read_text())
 check('statistics_match',stats['named_records']==len(ids) and stats['lexical_occurrences']==len(occ) and stats['lookup_keys']==len(idx) and stats['typed_relationships']==len(d['relations']))
 files=[p for p in ROOT.rglob('*') if p.is_file()]
 check('no_font_files',all(p.suffix.lower() not in ('.ttf','.otf','.woff','.woff2') for p in files))
 check('development_only_scripts_removed',not (ROOT/'scripts/build_registry.py').exists() and not (ROOT/'scripts/polish_registry.py').exists())
 report=dict(archive_validation_pass=all(c['passed'] for c in checks),scope='File and registry integrity only. No mathematical theorem or original producer verified.',check_count=len(checks),failed_checks=[c for c in checks if not c['passed']],checks=checks)
 (ROOT/'data/validation_report.json').write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps({k:report[k] for k in ['archive_validation_pass','scope','check_count','failed_checks']},indent=2))
 return 0 if report['archive_validation_pass'] else 1
if __name__=='__main__':sys.exit(main())
