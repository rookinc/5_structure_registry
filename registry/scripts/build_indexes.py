#!/usr/bin/env python3
"""Index archived label occurrences and render the curated structure register.

No source theorem/audit producer is executed. No source files are modified.
Python standard library only. Run from any working directory.
"""
from __future__ import annotations
import re, json, hashlib, collections, csv, html
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
DATA=ROOT/'data'; NOTES=ROOT/'notes'
REG=json.loads((DATA/'structure_registry.json').read_text())
ROWS=REG['records']; SOURCES=REG['sources']

# Retain case, leading zeros, exponent placement, and compound notation.
FONT=r'\\(?:mathbb|mathbf|mathrm|mathsf|mathcal|mathscr|operatorname)\s*'
SIMPLE=re.compile(r'(?<![A-Za-z0-9])(?P<letter>[A-Za-z])(?P<sub>\s*_\s*(?:\{\s*(?P<braced>\d+)(?:[^}\n]*)\}|(?P<under>\d+))|(?P<plain>\d+))(?![A-Za-z0-9])')
WRAPPED=re.compile(FONT+r'\{\s*(?P<letter>[A-Za-z])\s*\}\s*_\s*(?:\{\s*(?P<braced>\d+)(?:[^}\n]*)\}|(?P<under>\d+))(?![A-Za-z0-9])')
SUP=re.compile(r'(?<![A-Za-z0-9_])(?P<letter>[A-Za-z])\s*\^\s*(?:\{\s*(?P<braced>\d+)\s*\}|(?P<plain>\d+))(?![A-Za-z0-9])')
WSUP=re.compile(FONT+r'\{\s*(?P<letter>[A-Za-z])\s*\}\s*\^\s*(?:\{\s*(?P<braced>\d+)\s*\}|(?P<plain>\d+))(?![A-Za-z0-9])')
PAREN=re.compile(r'(?<![A-Za-z0-9])(?P<letter>SU|SO|SL|GL|Sp|U|O|M|Herm|Cl)\s*(?:\(|\{)(?P<num>\d+)(?P<rest>[^)\n}]*)(?:\)|\})')
MULTI=re.compile(r'(?<![A-Za-z0-9])(?P<letter>SU|SO|SL|GL|CP|RP|FP)(?:_\{?|)(?P<num>\d+)\}?(?![A-Za-z0-9])')
USUB=re.compile(r'(?<![A-Za-z0-9])(?P<letter>[A-Za-z])(?P<num>[₀₁₂₃₄₅₆₇₈₉]+)')
TRANS=str.maketrans('₀₁₂₃₄₅₆₇₈₉','0123456789')

def matches(text):
 found=[]
 for regex,notation in [(WRAPPED,'subscript'),(SIMPLE,'letter-number'),(WSUP,'power-or-superscript'),(SUP,'power-or-superscript'),(PAREN,'parenthesized-type'),(MULTI,'multi-letter-number'),(USUB,'subscript')]:
  for m in regex.finditer(text):
   g=m.groupdict(); n=g.get('braced') or g.get('under') or g.get('plain') or g.get('num'); n=n.translate(TRANS)
   key=g['letter']+('^' if notation=='power-or-superscript' else '')+n
   if notation=='parenthesized-type':key=g['letter']+'('+n+(g.get('rest') or '').strip()+')'
   typ=notation
   if g.get('sub') and '_' in g['sub']:typ='subscript'
   found.append((m.start(),m.end(),key,typ,m.group()))
 # Longest enclosing match wins. This retains font braces without counting twice.
 found.sort(key=lambda a:(a[0],-(a[1]-a[0])))
 kept=[]
 for r in found:
  if any(r[0]>=p[0] and r[1]<=p[1] for p in kept):continue
  if any(r[0]<p[1] and r[1]>p[0] for p in kept):continue
  kept.append(r)
 # Preserve a suffix exponent as an additional compound lookup key. Base occurrences remain.
 for start,end,key,typ,raw in list(kept):
  if typ in ('subscript','letter-number'):
   m=re.match(r'\s*\^\s*(?:\{\s*(\d+)\s*\}|(\d+))',text[end:])
   if m:
    kept.append((start,end+m.end(),key+'^'+(m.group(1)or m.group(2)),'subscript-with-power',text[start:end+m.end()]))
 return sorted(kept)

# Build a lookup of all exact historical forms, plus their safe subscript spellings.
lookup=collections.defaultdict(set)
for row in ROWS:
 for label in row['source_labels']:
  # Ranges such as E01..E52 are descriptions, not a claim to match every mathematical E-label.
  if '..' in label:continue
  lookup[label].add(row['id'])
  for start,end,key,_,_ in matches(label):
   if not label[:start].strip() and not label[end:].strip():
    lookup[key].add(row['id'])
# Remove accidental components of compound display aliases. A composite C2xA4 includes the factors,
# but alias lookup must not treat it as literal identity to either factor.
for key in list(lookup):
 if key in ('C2','A4','A5','D10'):
  for id in ['kernel-color-group','answering-pair-stabilizer','signed-axis-extension']:
   if id in lookup[key]: lookup[key].remove(id)

# Explicit-only high-confidence metadata detection. Other ambiguous matches remain candidates.
def disposition(path,line,start,end,key,notation,candidates):
 if path.endswith('_label_protections.json') and re.fullmatch(r'[FMKS][0-9]+',key):
  return 'explicit-metadata','protected equation/statement label in source manifest'
 if 'wxyzti_contract_reconciliation.md' in path and re.fullmatch(r'S[0-9]+',key):
  return 'explicit-metadata','numbered WXYZTI contract obligation'
 if any(m.start()<=start and end<=m.end() for m in re.finditer(r'\([FMK][0-9]+\)',line)):
  return 'explicit-metadata','parenthesized equation label'
 for pat in [r'\\(?:tag|label|ref|eqref|input|include|citep|citet|cite|path)\{[^}]*\}',r'\[[Dd][0-9]+\]',r'#src-[a-z0-9-]+']:
  if any(m.start()<=start and end<=m.end() for m in re.finditer(pat,line)):
   return 'explicit-metadata','tag, reference, or source locator'
 if key in ('n0','n1') and start>0 and line[start-1]=='\\' and path.endswith('.json'):
  return 'serialization-fragment','escaped newline followed by a digit, not an indexed variable'
 for m in re.finditer(r'[A-Za-z0-9_./:#-]+\.(?:json|tex|md|py|html|zip)',line):
  if m.start()<=start and end<=m.end():
   return 'explicit-metadata','fragment of a complete source path or filename'
 if '/equations/' in path or '/statements/' in path:
  if 'include{' in line or 'input{' in line:return 'explicit-metadata','equation/statement file reference'
 if key in ('v0','v1','v2','v3','N015','N030','N060','N120','x012','x210'):
  surrounding=line[max(0,start-50):min(len(line),end+65)]
  if re.search(r'\.json|\.md|\.py|http|/|transport_label|schema|artifact_id|version',surrounding,re.I):
   return 'explicit-metadata','version, path, or source transport identifier'
 if key in ('C107',):return 'explicit-metadata','audit identifier in this corpus'
 if notation=='power-or-superscript':
  return 'superscript-review','exponent / dimension / sphere; never folded into subscript'
 if not candidates:return 'unresolved','no curated structure identity assigned'
 if all(next(r for r in ROWS if r['id']==i)['kind'].startswith(('metadata','source identifier','catalogue /','audit /')) for i in candidates):
  return 'source-locator-candidate','source metadata family; occurrence retained'
 if len(candidates)==1:return 'single-candidate','one registry candidate; not automatic semantic verification'
 return 'ambiguous','multiple named views; occurrence needs local context'

# Scan complete text source files; byte-identical copies count once with aliases preserved.
allfiles=[]
for folder in ['provenance/inputs','provenance/excerpts']:
 for p in (ROOT/folder).rglob('*'):
  if p.is_file() and p.suffix.lower() in ('.md','.tex','.json','.txt'):
   allfiles.append(p)
groups=collections.defaultdict(list)
for p in sorted(allfiles):groups[hashlib.sha256(p.read_bytes()).hexdigest()].append(p)
corpus=[]; occ=[]
for digest,paths in sorted(groups.items(),key=lambda x:str(x[1][0])):
 # Prefer a source path over generated glossary if literal duplicates exist.
 paths=sorted(paths,key=lambda p:(len(p.parts),str(p)))
 p=paths[0]; text=p.read_text(encoding='utf-8'); rel=str(p.relative_to(ROOT))
 lines=text.splitlines()
 source_role='retrieved-excerpt-digest' if '/excerpts/' in str(p) else ('secondary-glossary' if p.name in ['qr_core_terms_original.md','qr_core_terms_consolidated.md','qr_core_terms_2026-09-24.md','thalean_glossary_previous.md'] else 'archived-source-text')
 corpus.append(dict(path=rel,sha256=digest,size_bytes=p.stat().st_size,line_count=len(lines),role=source_role,duplicate_paths=[str(x.relative_to(ROOT)) for x in paths[1:]]))
 for num,line in enumerate(lines,1):
  for start,end,key,notation,raw in matches(line):
   candidates=sorted(lookup.get(key,[]))
   disp,why=disposition(rel,line,start,end,key,notation,candidates)
   if disp=='explicit-metadata':
    mid='source-equation-codes' if re.fullmatch(r'[EFKMSW]0?[0-9]+',key) else 'source-path-fragments'
    if key in ('D6','d6'):mid='source-draft-codes'
    if key=='C107':mid='source-audit-codes'
    candidates=sorted(set(candidates+[mid]))
   elif disp=='serialization-fragment':candidates=['escaped-string-fragment']
   elif notation in ('power-or-superscript','subscript-with-power') and not candidates:
    candidates=['power-expression']
    disp='derived-notation';why='power or repeated-composition expression, not a fresh letter-number object'
   occ.append(dict(occurrence_id=len(occ)+1,lookup_key=key,raw=raw,notation=notation,path=rel,line=num,column=start+1,end_column=end+1,context=line[max(0,start-110):min(len(line),end+180)],candidate_structure_ids=candidates,review_status=disp,review_note=why))
bylabel=collections.defaultdict(list)
for o in occ:bylabel[o['lookup_key']].append(o)
labels=[]
for key,found in sorted(bylabel.items(),key=lambda x:(x[0].lower(),x[0])):
 candidate_ids=sorted(set(i for o in found for i in o['candidate_structure_ids'])); statuses=collections.Counter(x['review_status'] for x in found)
 labels.append(dict(lookup_key=key,occurrence_count=len(found),source_count=len(set(x['path'] for x in found)),spellings=sorted(set(x['raw'] for x in found)),candidate_structure_ids=candidate_ids,review_status_counts=dict(statuses),occurrence_ids=[x['occurrence_id'] for x in found]))
(DATA/'source_files.json').write_text(json.dumps(corpus,indent=2)+'\n')
(DATA/'label_index.json').write_text(json.dumps(labels,indent=2,ensure_ascii=True)+'\n')
with (DATA/'occurrences.jsonl').open('w') as f:
 for o in occ:f.write(json.dumps(o,ensure_ascii=True)+'\n')
with (DATA/'label_index.csv').open('w',newline='') as f:
 w=csv.writer(f);w.writerow(['lookup_key','occurrences','source_files','candidate_structure_ids','review_states'])
 for b in labels:w.writerow([b['lookup_key'],b['occurrence_count'],b['source_count'],';'.join(b['candidate_structure_ids']),json.dumps(b['review_status_counts'])])
statistics=dict(text_file_paths=len(allfiles),unique_text_payloads=len(corpus),byte_identical_duplicate_paths=len(allfiles)-len(corpus),lexical_occurrences=len(occ),lookup_keys=len(labels),named_records=len(ROWS),typed_relationships=len(REG['relations']),curated_source_anchors=len(SOURCES),record_kinds=dict(collections.Counter(r['kind'] for r in ROWS)),unresolved_keys=sum(not b['candidate_structure_ids'] for b in labels),occurrence_review_statuses=dict(collections.Counter(o['review_status'] for o in occ)),source_hashes_verified=all(hashlib.sha256((ROOT/s['path']).read_bytes()).hexdigest()==s['sha256'] for s in SOURCES.values()))
(DATA/'scan_statistics.json').write_text(json.dumps(statistics,indent=2)+'\n')
print(json.dumps(statistics,indent=2))

# ---------- Render human-facing archive ----------
def md_escape(s):return str(s).replace('|',r'\|').replace('\n',' ')
def link(id):
 r=next(r for r in ROWS if r['id']==id);return f"[{r['qualified_name']}](#{id})"
def source_md(k):
 s=SOURCES[k];return f"[{k}](../{s['path']}#L{s['line_start']}-L{s['line_end']})"
def clean(s):return str(s)
sections=[
 ('Dihedral and quaternionic views','d8-native-root','answering-pair-stabilizer'),
 ('Klein and binary-register views','v4-native','c2-threefold-deck'),
 ('Cyclic, alternating and symmetric actions','c3-mode','a3-root-target'),
 ('Graphs, finite state sets, and counting conventions','g60-native','k120-group-locator'),
 ('Operators, indexed variables, and readouts','frame-contrast','identity-matrices'),
 ('Continuous envelopes, scalar spaces, and homology','u2-face-envelope','h12-history-candidate'),
 ('Source-code and metadata bins','source-h-locators','source-audit-codes'),
 ('Companion objects needed for typed relationships','face-stabilizer','history-alphabet'),
 ('Additional collisions from the exact occurrence sweep','adjacency-g15','escaped-string-fragment')]
index={r['id']:i for i,r in enumerate(ROWS)}
head=f'''# Thalean Structure and Label Registry

Date: 2026-09-24  
Edition: archival view inventory v1  
Purpose: separate the actual source-defined structures before consolidating their names.

**{len(ROWS)} named structure/view records; {len(REG['relations'])} typed relationship decisions.** The lexical scan found **{len(labels)} lookup keys in {len(corpus)} byte-distinct text payloads**. Those are not {len(labels)} mathematical objects. Counts include metadata, indexed variables, ordinary exponents and secondary glossary repetitions.

## Governing rule

A label is a lookup key. An object is identified by its domain, construction, action and evidence. An abstract group type is only one part of that identity.

For example, `D8` can label a root stabilizer, a presentation factor, a block permutation image, a selected operator group, an edge-transport group or a lifted loop group. Sharing an order-eight dihedral presentation does not erase those roles. Conversely, a source-derived descent may identify two views of the same rooted structure, and that relationship should be recorded rather than forbidden by blanket warnings.

The qualified names and semantic IDs in this edition are **editorial proposals**. Existing equations, source files, native generator labels, repository audits and `qr_core_terms.md` are not rewritten. A family record covers parameterized instances such as six faces or sixty roots; it does not assert that all embedded subgroup members are one literal subgroup.

## How the bins work

Every named record distinguishes the object type, carrier/domain, historical spellings, action or construction, numerical size with its meaning, source basis, and boundary. The relationship ledger then records one of: source-identified entity; faithful descent; quotient; subgroup/image; operator construction; abstract-type match only; incompatible structure; or unresolved comparison. No automatic identity closure is taken through quotient or same-type edges.

A `candidate_structure_ids` field in the occurrence index is a navigation aid, **not a completed semantic annotation**. Ambiguous and unmapped occurrences stay in the review queue. Superscripts are retained separately, so `C^2`, `C_2`, `C_2^3`, `U_2`, `U(2)`, `S_1`, and `S^1` are not normalized into one object.

## Evidence and coverage

The scan covers the four archived glossary/baseline texts, current Draft 6 TEX plus retained text/JSON sources, the recovered native analyzer/EPR/G9000 notes, selected source artifacts, and explicitly identified passage digests from earlier papers. It is not a complete export of the user's chat account or research repositories. The current conversation is represented by a clearly marked digest, not a claimed transcript dump.

No historical mathematical producer was executed for this inventory. A stored `audit_pass` flag is evidence about what its source reports, not a new verification performed here. In particular, the newest claimed full twelve-pentagon/action cocycle cancellation remains **conversation-reported pending its original action tables**. The previously recovered Gram and Clifford artifacts do not by themselves supply that later full-action verification.

Full lexical inventory: [label collision index](label_collision_index.md).  
Relations and consolidation decisions: [relationship ledger](consolidation_ledger.md).  
Cases requiring more evidence: [review queue](unresolved_label_queue.md).  
Source coverage and checksums: [coverage ledger](../provenance/coverage.md).

## Dihedral naming convention

The sources mix conventions. Their `D8` is the square dihedral group of total order eight; historical `D5` is the pentagonal dihedral group of total order ten; registered-decagon `D10` has total order twenty. This edition retains the original label and writes the order explicitly. Use the qualified view name first. If a compact neutral type is needed, write `Dih(rotation_order=4, total_order=8)` rather than changing a source subscript silently.

**A matched group order is not a domain map. A group, its matrix representation, the orbit it acts on, the stabilizer of a point, and a quotient image are separate records.**

## Section index

'''
for title,first,last in sections:head+=f'- [{title}](#section-{first})\n'
text=head+'\n'
for title,first,last in sections:
 text+=f'<a id="section-{first}"></a>\n\n# {title}\n\n'
 for r in ROWS[index[first]:index[last]+1]:
  text+=f'<a id="{r["id"]}"></a>\n\n## {r["qualified_name"]}\n\n'
  text+=f'**Stable ID:** `{r["id"]}`  \n**Historical labels / lookup forms:** '+', '.join('`'+s+'`' for s in r['source_labels'])+'  \n'
  text+=f'**Kind:** {r["kind"]}  \n**Domain:** {r["domain"]}  \n'
  sizes=[]
  for fld,title1 in [('group_order','Group order'),('point_count','Point/object count'),('bin_count','Pair-bin count'),('ordered_pair_count','Ordered-pair count'),('real_dimension','Real dimension'),('complex_dimension','Complex dimension'),('rank','Projector rank'),('carrier_real_dimension','Ambient real carrier dimension')]:
   if r.get(fld) is not None:sizes.append(f'{title1}: {r[fld]}')
  if sizes:text+='**Typed size:** '+'; '.join(sizes)+'  \n'
  if r.get('family_parameters'):text+=f'**Family parameters:** {r["family_parameters"]}  \n'
  text+=f'**Standing:** {r["standing"]}\n\n{r["definition"]}\n\n'
  text+='```text\n'+r['formula_or_action']+'\n```\n\n'
  text+='**Keep distinct:** '+r['boundary']+'\n\n'
  relevant=[z for z in REG['relations'] if r['id'] in (z['source'],z['target'])]
  if relevant:
   text+='**Recorded relationships:** '
   text+='; '.join(f'[{z["source"] if z["target"]==r["id"] else z["target"]}](#{z["source"] if z["target"]==r["id"] else z["target"]}) ({z["relation"].replace("_"," ")})' for z in relevant)+'.\n\n'
  text+='**Sources:** '+', '.join(source_md(k) for k in r['source_ids'])+'.\n\n---\n\n'
text+='## Source anchor index\n\n'
for k,s in sorted(SOURCES.items()):
 text+=f'- **{k}**: [{s["path"]}](../{s["path"]}), lines {s["line_start"]}-{s["line_end"]}; {s["role"]}.\n'
(NOTES/'qr_structure_registry.md').write_text(text)

# Collision index includes every detected lookup key, not only curated mathematical records.
ci=f'''# Letter-number collision index

Date: 2026-09-24

{len(labels)} exact lookup keys; {len(occ)} lexical occurrences across {len(corpus)} unique text payloads. Case and leading zeros are preserved. Font variants of a subscript are normalized for lookup only. Ordinary powers, spaces, source identifiers and mathematical objects are not conflated.

The table links to candidate named views. It does not claim an exhaustive semantic assignment of each occurrence. `occurrences.jsonl` preserves every matching spelling, source path, original line, character column and nearby text. Byte-identical source copies are counted once; their alternate paths remain in `source_files.json`.

| Lookup key | Occurrences | Text payloads | Candidate records / review disposition |
|---|---:|---:|---|
'''
for b in labels:
 cs='; '.join(f'[{x}](qr_structure_registry.md#{x})' for x in b['candidate_structure_ids']) or '**Unresolved / locator / indexed expression:** inspect queue'
 ci+=f'| `{md_escape(b["lookup_key"])}` | {b["occurrence_count"]} | {b["source_count"]} | {cs} |\n'
(NOTES/'label_collision_index.md').write_text(ci)

cl='''# Consolidation and relationship ledger

Date: 2026-09-24

These are archival decisions about source evidence, not newly executed mathematical theorems. A relationship never silently overwrites either endpoint's domain. In particular, quotient, subgroup, representation, normalization, common type, and common numeric size are not synonym relations.

**Consolidation now** means that a source identifies an entity or supplies the stated map. Keep separate view IDs when the domain, ambient group, representation, coefficient field or marking differs. **Hold** means a specific original producer or action-level crosswalk is still needed. No new native identification is admitted in this file merely by assigning a name.

'''
for i,z in enumerate(REG['relations'],1):
 a=next(r for r in ROWS if r['id']==z['source']);b=next(r for r in ROWS if r['id']==z['target'])
 cl+=f'## {i:02}. {a["qualified_name"]} / {b["qualified_name"]}\n\n'
 cl+=f'**Relation:** {z["relation"].replace("_"," ")}  \n**Decision:** {z["decision"].replace("_"," ")}\n\n{z["reason"]}\n\n'
 cl+=f'Views: [{a["id"]}](qr_structure_registry.md#{a["id"]}); [{b["id"]}](qr_structure_registry.md#{b["id"]}).  \nSources: '+', '.join(source_md(k) for k in z['source_ids'])+'.\n\n'
(NOTES/'consolidation_ledger.md').write_text(cl)

uq='''# Unresolved labels and occurrence-review queue

Date: 2026-09-24

This queue is an intentional part of the result. A label without a recovered domain is not promoted to a guessed group, graph or operator. Many matches are equation tags, audit references, ordinary variables or exponents. A key may also have a named view while its particular occurrences remain ambiguous; those are retained in `occurrences.jsonl` under `review_status`.

Named locator-only views include the 201EZ K120 classification reference, the charge-center D8 comparison target, H8/H10 references, and G21/O48 source locators. Recover the original payload before assigning an identity. Historical dihedral face/history matches and the frame-current/history module bridge remain explicit relationship holds.

## Keys with no curated object assignment

'''
for b in labels:
 if b['candidate_structure_ids']:continue
 uq+=f'### `{b["lookup_key"]}`\n\n{b["occurrence_count"]} occurrences in {b["source_count"]} text payload(s).\n\n'
 for o in bylabel[b['lookup_key']][:3]:
  uq+=f'- [{o["path"]}](../{o["path"]}), line {o["line"]}, column {o["column"]}; {o["review_status"]}. Context: `{o["context"].replace("`","'")}`\n'
 uq+='\n'
uq+='## Local occurrence annotations still pending\n\n'
pending=[o for o in occ if o['review_status']=='unresolved']
if not pending:uq+='No zero-candidate local occurrences remain after metadata triage. Ambiguous multi-view occurrences still require contextual selection; they are not declared resolved.\n\n'
for o in pending:
 uq+=f"- `{o['lookup_key']}` in [{o['path']}](../{o['path']}), line {o['line']}: `{o['context'].replace('`', chr(39))}`\n"
uq+='\n## Ambiguous occurrences\n\n'
uq+=f"The occurrence ledger retains {sum(o['review_status']=='ambiguous' for o in occ)} matches with multiple candidate views. Use source context, not frequency or a global replace rule, to select the intended view. A single candidate is likewise a lookup suggestion, not a new proof.\n"
(NOTES/'unresolved_label_queue.md').write_text(uq)

# Compact portable semantic names, never destructive automatic replacements.
names='''# Proposed qualified notation

Do not perform a global textual search-and-replace from this table. A bare label can have several meanings in one source. Select the source-defined view first, then apply its qualified name locally. Numeric suffixes should state what they count: group order, rotation order, vertices, matrix size, character index, phase index, audit ID or equation number.

| View ID | Qualified name | Historical lookup forms |
|---|---|---|
'''
for r in ROWS:names+=f'| `{r["id"]}` | {md_escape(r["qualified_name"])} | '+', '.join('`'+md_escape(x)+'`' for x in r['source_labels'])+' |\n'
(NOTES/'qualified_names.md').write_text(names)
print('WROTE',len(text.split()),'words in main registry')
