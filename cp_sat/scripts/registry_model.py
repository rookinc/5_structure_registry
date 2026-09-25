#!/usr/bin/env python3
"""Compile an immutable Thalean view registry into conservative alias constraints.

This module uses the standard library only. It does not prove source mathematics.
A compiled equality means source-supported editorial referent consolidation with
all view records retained. It does NOT mean equal coordinates, actors, or actions.
"""
from __future__ import annotations
import hashlib
import json
import zipfile
from collections import Counter, defaultdict, deque
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
UPSTREAM = ROOT / 'upstream' / 'thalean_symbol_registry_2026-09-24.zip'
PREFIX = 'thalean_symbol_registry_2026-09-24/'
EQUALITY_DECISIONS = {
    'consolidate_entity_keep_census_view',
    'consolidate_entity_keep_map_domain',
}
SEPARATE_DECISIONS = {
    'do_not_merge', 'link_not_alias', 'link_views_keep_domains',
    'same_type_not_elementwise_identity', 'link_keep_embedding',
    'link_views_keep_coordinates', 'link_family_and_member',
}
OPEN_DECISIONS = {
    'hold_for_action_crosswalk', 'hold_for_native_crosswalk', 'unresolved',
    'conditional_on_voltage_chart', 'hold_for_source_crosswalk',
    'hold_for_vertex_action_crosswalk', 'hold_for_native_intertwiner',
    'hold_for_history_crosswalk', 'native_intertwiner_open',
    'do_not_merge_without_source',
}


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def dump_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=True, ensure_ascii=True) + '\n', encoding='utf-8')


def read_upstream() -> tuple[dict, list[dict], list[dict]]:
    with zipfile.ZipFile(UPSTREAM) as archive:
        registry = json.loads(archive.read(PREFIX + 'data/structure_registry.json'))
        occurrences = [json.loads(line) for line in archive.read(PREFIX + 'data/occurrences.jsonl').decode('utf-8').splitlines() if line.strip()]
        labels = json.loads(archive.read(PREFIX + 'data/label_index.json'))
    return registry, occurrences, labels


def compile_registry(registry: dict) -> dict:
    records = registry['records']
    ids = [r['id'] for r in records]
    if len(ids) != len(set(ids)):
        raise ValueError('Duplicate stable view IDs')
    lookup = {r['id']: r for r in records}
    constraints, questions, bridges = [], [], []
    for index, relation in enumerate(registry['relations'], 1):
        rid = f'REL{index:03d}'
        decision = relation['decision']
        if decision in EQUALITY_DECISIONS:
            op, disposition = 'eq', 'source_supported_alias'
        elif decision in SEPARATE_DECISIONS:
            op, disposition = 'ne', 'preserve_distinct_views'
        elif decision in OPEN_DECISIONS:
            op, disposition = None, 'open_comparison'
        else:
            raise ValueError(f'Unmapped decision {decision!r}: human review required')
        for endpoint in ('source', 'target'):
            if relation[endpoint] not in lookup:
                raise ValueError(f'Unknown endpoint in {rid}')
        compiled = {
            'id': rid, 'left': relation['source'], 'right': relation['target'],
            'operator': op, 'disposition': disposition,
            'registry_relation': relation['relation'], 'registry_decision': decision,
            'reason': relation['reason'], 'source_ids': relation['source_ids'],
            'source_standings': {sid: registry['sources'][sid]['role'] for sid in relation['source_ids']},
            'evidence_level': 'inherited_registry_statement_not_independently_reproved',
            'scope': 'editorial_alias_bucket_with_domains_and_views_preserved',
        }
        bridges.append(compiled)
        questions.append({
            'id': rid, 'left': compiled['left'], 'right': compiled['right'],
            'origin': 'existing_registry_relation', 'disposition': disposition,
            'promotion_eligible_from_this_input': op == 'eq',
        })
        if op is not None:
            constraints.append(compiled)

    # Explicit, reviewed type/size controls. Never infer a group from its spelling.
    guards = [
        ('TYPE001', 'd5-history', 'frame-difference',
         'An order-ten finite group presentation is not the real linear operator D5_frame.',
         ['HISTORICAL_FIVEFOLD', 'CHAT'], 'group_vs_linear_operator'),
        ('TYPE002', 'd5-face-kernel', 'frame-difference',
         'A face-action kernel subgroup is not the real linear operator D5_frame.',
         ['D5_KERNEL', 'CHAT'], 'group_vs_linear_operator'),
        ('TYPE003', 'd5-face-kernel', 'd8-face-blocks',
         'The source records kernel order 10 and permutation-image order 8; they are not aliases.',
         ['D5_KERNEL', 'FACE'], 'unequal_recorded_group_orders'),
    ]
    for cid, left, right, reason, source_ids, subtype in guards:
        if subtype == 'unequal_recorded_group_orders':
            if (lookup[left]['group_order'], lookup[right]['group_order']) != (10, 8):
                raise ValueError('Type-control source sizes changed: review required')
        elif lookup[right]['kind'] != 'real linear operator':
            raise ValueError('Type-control operator kind changed: review required')
        constraint = {
            'id': cid, 'left': left, 'right': right, 'operator': 'ne',
            'disposition': 'reviewed_type_separation', 'registry_relation': subtype,
            'registry_decision': 'new_encoding_guard_not_new_native_theorem',
            'reason': reason, 'source_ids': source_ids,
            'source_standings': {sid: registry['sources'][sid]['role'] for sid in source_ids},
            'evidence_level': 'direct_type_or_order_deduction_from_registry',
            'scope': 'editorial_alias_bucket_with_domains_and_views_preserved',
        }
        constraints.append(constraint)
        questions.append({'id': cid, 'left': left, 'right': right, 'origin': 'reviewed_type_guard',
                          'disposition': 'reviewed_type_separation', 'promotion_eligible_from_this_input': False})

    return {
        'schema': 'thalean.registry-cp-sat-input.v1', 'date': '2026-09-24',
        'scope': 'registry_alias_consistency_not_native_structural_equivalence',
        'identity_predicate': 'same editorial alias bucket at the recorded referent level; never delete original view records',
        'objective': None,
        'candidate_scope': '61 recorded relationship pairs plus 3 reviewed typing controls; unqueried pairs are NOT_TESTED',
        'view_ids': ids, 'views': records, 'source_anchors': registry['sources'],
        'hard_constraints': constraints, 'preserved_relationships': bridges,
        'queries': questions,
        'policies': {
            'preserve_all_view_ids': True,
            'same_label_implies_same_object': False,
            'same_group_order_implies_identity': False,
            'same_spectrum_implies_intertwiner': False,
            'source_isomorphism_implies_same_coordinates': False,
            'missing_data_means_false': False,
            'optimize_number_of_entities': False,
            'source_claims_independently_replayed': False,
            'open_comparison_can_be_promoted_by_feasibility': False,
            'occurrence_candidates_are_semantically_verified': False,
        },
        'counts': {'views': len(records), 'original_relations': len(bridges),
                   'hard_equalities': sum(c['operator'] == 'eq' for c in constraints),
                   'hard_disequalities': sum(c['operator'] == 'ne' for c in constraints),
                   'queries': len(questions),
                   'open_registry_comparisons': sum(b['disposition'] == 'open_comparison' for b in bridges)},
    }


class UnionFind:
    def __init__(self, items: list[str]):
        self.parent = {item: item for item in items}
    def find(self, item: str) -> str:
        parent = self.parent[item]
        if parent != item:
            self.parent[item] = self.find(parent)
        return self.parent[item]
    def union(self, left: str, right: str) -> None:
        left, right = self.find(left), self.find(right)
        if left != right:
            low, high = sorted((left, right))
            self.parent[high] = low


def exact_fragment_check(ids: list[str], constraints: list[dict]) -> dict:
    """Complete checker for equalities/disequalities with at least len(ids) labels.

    It is deliberately independent of CP-SAT and the CP-SAT API. Satisfiability
    here is not a solver result, nor evidence about a missing native map.
    """
    uf = UnionFind(ids)
    for constraint in constraints:
        if constraint['operator'] == 'eq':
            uf.union(constraint['left'], constraint['right'])
        elif constraint['operator'] != 'ne':
            raise ValueError('Unsupported operation')
    conflicts = [c['id'] for c in constraints if c['operator'] == 'ne' and uf.find(c['left']) == uf.find(c['right'])]
    groups = defaultdict(list)
    for item in ids:
        groups[uf.find(item)].append(item)
    return {'consistent': not conflicts, 'conflicting_disequalities': conflicts,
            'classes': sorted((sorted(v) for v in groups.values()), key=lambda row: row[0])}


def deletion_minimal_core(ids: list[str], constraints: list[dict]) -> list[str]:
    """Deletion-minimal within this exact fragment; not minimum cardinality."""
    if exact_fragment_check(ids, constraints)['consistent']:
        return []
    core = list(constraints)
    pos = 0
    while pos < len(core):
        trial = core[:pos] + core[pos + 1:]
        if not exact_fragment_check(ids, trial)['consistent']:
            core = trial
        else:
            pos += 1
    return [c['id'] for c in core]


def probe_queries(model: dict) -> list[dict]:
    ids, constraints = model['view_ids'], model['hard_constraints']
    if not exact_fragment_check(ids, constraints)['consistent']:
        raise ValueError('Baseline contradiction; query classification is quarantined')
    results = []
    for question in model['queries']:
        row = dict(question)
        for op in ('eq', 'ne'):
            added = {'id': f'QUERY:{question["id"]}:{op}', 'left': question['left'],
                     'right': question['right'], 'operator': op}
            check = exact_fragment_check(ids, constraints + [added])
            row[op + '_consistent'] = check['consistent']
            row[op + '_conflict_core'] = deletion_minimal_core(ids, constraints + [added]) if not check['consistent'] else []
        if row['eq_consistent'] and not row['ne_consistent']:
            row['classification'] = 'FORCED_ALIAS_BY_FROZEN_INPUT'
        elif row['ne_consistent'] and not row['eq_consistent']:
            row['classification'] = 'SEPARATE_AT_RECORDED_VIEW_LEVEL'
        elif row['eq_consistent'] and row['ne_consistent']:
            row['classification'] = 'OPEN_UNDER_ENCODED_CONSTRAINTS'
        else:
            raise AssertionError('Impossible for a consistent equality/disequality fragment')
        row['method'] = 'independent_exact_equality_disequality_check_NOT_CP_SAT'
        results.append(row)
    return results


def candidate_components(model: dict) -> dict[str, list[int]]:
    """Domain partition is a search-scope policy, not a theorem of difference."""
    ids = model['view_ids']
    uf = UnionFind(ids)
    for question in model['queries']:
        uf.union(question['left'], question['right'])
    groups = defaultdict(list)
    for index, item in enumerate(ids):
        groups[uf.find(item)].append(index)
    return {item: groups[uf.find(item)] for item in ids}
