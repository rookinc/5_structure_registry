#!/usr/bin/env python3
"""Validate the input archive, mapping and exact equality/disequality fragment."""
from __future__ import annotations
import csv
import json
import zipfile
from collections import Counter
from pathlib import Path
from registry_model import (ROOT, UPSTREAM, PREFIX, compile_registry, dump_json,
                           exact_fragment_check, probe_queries, read_upstream, sha256,
                           deletion_minimal_core)


def main() -> None:
    registry, occurrences, labels = read_upstream()
    model = compile_registry(registry)
    ids = set(model['view_ids'])
    checks = []
    def check(name: str, passed: bool, scope: str = 'archive_or_encoding') -> None:
        checks.append({'name': name, 'passed': bool(passed), 'scope': scope})
        if not passed:
            raise AssertionError(name)
    check('unique_structure_ids', len(ids) == len(registry['records']))
    check('unique_occurrence_ids', len({r['occurrence_id'] for r in occurrences}) == len(occurrences))
    with zipfile.ZipFile(UPSTREAM) as archive:
        for sid, source in registry['sources'].items():
            payload = archive.read(PREFIX + source['path'])
            check('source_sha256:' + sid, sha256(payload) == source['sha256'], 'source_byte_integrity_not_mathematical_truth')
        input_hashes = {name: sha256(archive.read(PREFIX + name)) for name in
                        ['data/structure_registry.json', 'data/occurrences.jsonl', 'data/label_index.json']}
    check('all_candidate_references_exist', all(set(o['candidate_structure_ids']) <= ids for o in occurrences))
    check('all_relationships_mapped', len(model['preserved_relationships']) == len(registry['relations']))
    check('no_optimization_objective', model['objective'] is None)
    baseline = exact_fragment_check(model['view_ids'], model['hard_constraints'])
    check('frozen_alias_constraints_consistent', baseline['consistent'], 'exact_equality_disequality_fragment')
    check('all_views_retained', sum(map(len, baseline['classes'])) == len(ids))
    queries = probe_queries(model)
    check('every_scoped_query_classified', len(queries) == len(model['queries']))
    check('pending_comparisons_have_no_promotion', all(not q['promotion_eligible_from_this_input']
          for q in queries if q['disposition'] == 'open_comparison'))
    all_constraints = {c['id']: c for c in model['hard_constraints']}
    for q in queries:
        for op in ['eq', 'ne']:
            core_ids = q[op + '_conflict_core']
            if core_ids:
                query_id = f'QUERY:{q["id"]}:{op}'
                own = {'id': query_id, 'left': q['left'], 'right': q['right'], 'operator': op}
                core = [own if cid == query_id else all_constraints[cid] for cid in core_ids]
                check(f'core_inconsistent:{q["id"]}:{op}', not exact_fragment_check(model['view_ids'], core)['consistent'], 'exact_fragment_conflict')
                check(f'core_deletion_minimal:{q["id"]}:{op}', all(exact_fragment_check(model['view_ids'], core[:i] + core[i + 1:])['consistent'] for i in range(len(core))), 'exact_fragment_conflict')
    # Synthetic controls catch the usual loss of equivalence transitivity.
    toy = [{'id': 'AB', 'left': 'A', 'right': 'B', 'operator': 'eq'},
           {'id': 'BC', 'left': 'B', 'right': 'C', 'operator': 'eq'},
           {'id': 'AC', 'left': 'A', 'right': 'C', 'operator': 'ne'}]
    check('negative_control_transitive_contradiction', not exact_fragment_check(['A','B','C'], toy)['consistent'], 'synthetic_control')
    check('positive_control_remove_one_conflict', exact_fragment_check(['A','B','C'], toy[:2])['consistent'], 'synthetic_control')
    # Actual-record stress test: aliasing every D8 view is inconsistent with the ledger.
    d8 = [r['id'] for r in registry['records'] if any(s.replace('_','') == 'D8' for s in r['source_labels'])]
    injected = [{'id': f'HOMONYM{i:02d}', 'left': d8[0], 'right': other, 'operator': 'eq'} for i, other in enumerate(d8[1:],1)]
    homonym_check = exact_fragment_check(model['view_ids'], model['hard_constraints'] + injected)
    check('negative_control_all_D8_aliases_rejected', not homonym_check['consistent'], 'actual_record_stress_test_not_group_classification')
    homonym_core = deletion_minimal_core(model['view_ids'], model['hard_constraints'] + injected)
    # Small relational-arithmetic gate, from already named subgroup/kernel/image objects.
    lookup = {r['id']: r for r in registry['records']}
    face, kernel, image = [lookup[x]['group_order'] for x in ['face-stabilizer','d5-face-kernel','d8-face-blocks']]
    check('face_order_accounting_80_10_8', face == kernel * image, 'arithmetic_on_source_recorded_orders')
    alias_groups = [group for group in baseline['classes'] if len(group) > 1]
    representative = {sid: group[0] for group in baseline['classes'] for sid in group}
    report = {
        'schema': 'thalean.registry-cp-sat-preflight.v1', 'date': '2026-09-24',
        'input_zip_sha256': sha256(UPSTREAM.read_bytes()), 'input_member_sha256': input_hashes,
        'preflight_pass': all(c['passed'] for c in checks), 'checks': checks, 'check_count': len(checks),
        'mathematical_scope': 'complete equality/disequality consistency check with at least one available label per view',
        'native_producer_replayed': False, 'cp_sat_executed': False,
        'counts': {**model['counts'], 'all_possible_unordered_record_pairs': len(ids)*(len(ids)-1)//2,
                   'scoped_pairs': len(queries), 'unqueried_pairs': len(ids)*(len(ids)-1)//2-len(queries),
                   'supported_alias_buckets': len(baseline['classes']), 'original_label_occurrences': len(occurrences),
                   'lookup_keys': len(labels), 'source_anchors': len(registry['sources'])},
        'source_relation_dispositions': dict(Counter(b['disposition'] for b in model['preserved_relationships'])),
        'query_classification_counts': dict(Counter(q['classification'] for q in queries)),
        'supported_alias_groups': alias_groups, 'original_occurrence_statuses': dict(Counter(o['review_status'] for o in occurrences)),
        'occurrences_semantically_resolved_by_this_pass': 0,
        'unsupported_merges_admitted': 0,
        'stress_test_all_D8_aliases': {'views': d8, 'consistent': homonym_check['consistent'],
                                     'injected_constraints': injected, 'deletion_minimal_core': homonym_core,
                                     'minimum_cardinality_claim': False},
        'face_order_accounting': {'ambient': face, 'kernel': kernel, 'image': image, 'identity': '80=10*8',
                                  'is_new_group_theorem': False},
    }
    dump_json(ROOT/'inputs/model.json', model)
    dump_json(ROOT/'inputs/source_registry.json', registry)
    dump_json(ROOT/'reports/preflight.json', report)
    dump_json(ROOT/'reports/pair_queries.json', queries)
    dump_json(ROOT/'reports/supported_alias_classes.json', {
        'scope': 'editorial_source_aliases_only_all_225_view_records_preserved',
        'classes': baseline['classes'], 'not_a_count_of_distinct_mathematical_objects': True})
    with (ROOT/'data/occurrence_domains.jsonl').open('w',encoding='utf-8') as f:
        for occurrence in occurrences:
            row = dict(occurrence)
            row['unresolved_option_permitted'] = True
            row['candidate_alias_buckets'] = sorted({representative[sid] for sid in row['candidate_structure_ids']})
            row['semantic_assignment_admitted'] = False
            f.write(json.dumps(row, sort_keys=True, ensure_ascii=True) + '\n')
    dump_json(ROOT/'data/label_index.json', labels)
    with (ROOT/'reports/pair_queries.csv').open('w',encoding='utf-8',newline='') as f:
        names = ['id','left','right','classification','eq_consistent','ne_consistent','promotion_eligible_from_this_input','disposition']
        writer=csv.DictWriter(f,fieldnames=names,extrasaction='ignore'); writer.writeheader(); writer.writerows(queries)
    with (ROOT/'reports/constraint_ledger.csv').open('w',encoding='utf-8',newline='') as f:
        names = ['id','left','right','operator','disposition','registry_relation','registry_decision','reason','source_ids','evidence_level']
        writer=csv.DictWriter(f,fieldnames=names,extrasaction='ignore'); writer.writeheader()
        for row in model['hard_constraints']:
            writer.writerow({**row,'source_ids':';'.join(row['source_ids'])})
    print(json.dumps({k:report[k] for k in ['preflight_pass','check_count','counts','query_classification_counts','supported_alias_groups','face_order_accounting']}, indent=2))

if __name__ == '__main__':
    main()
