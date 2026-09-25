#!/usr/bin/env python3
"""Run the compiled registry alias model with OR-Tools CP-SAT.

No optimization objective. Query both merge and separation. Each inherited
constraint is assumption-tagged so a contradiction can cite the input ledger.
This is registry consistency, not a native group/action/intertwiner proof.
"""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path
from registry_model import ROOT, candidate_components, dump_json, sha256


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--seconds-per-solve', type=float, default=10.0)
    parser.add_argument('--include-occurrences', action='store_true', help='Add unresolved-or-candidate variables. This does not supply semantic evidence.')
    args = parser.parse_args()
    if args.seconds_per_solve <= 0:
        parser.error('--seconds-per-solve must be positive')
    model_path = ROOT/'inputs/model.json'
    if not model_path.is_file():
        print('Run python3 scripts/preflight.py first.',file=sys.stderr)
        return 2
    data=json.loads(model_path.read_text(encoding='utf-8'))
    try:
        import ortools
        from ortools.sat.python import cp_model
    except ImportError as exc:
        result={'schema':'thalean.registry-cp-sat-result.v1','engine_status':'NOT_RUN',
                'cp_sat_executed':False,'model_validation':'NOT_RUN',
                'reason':'OR-Tools CP-SAT is not installed in this Python environment.',
                'import_error':str(exc),'input_model_sha256':sha256(model_path.read_bytes()),
                'preflight_is_not_cp_sat':True,'no_native_theorem_promotion':True}
        dump_json(ROOT/'reports/cp_sat_result.json',result)
        print(json.dumps(result,indent=2))
        return 2
    domains=candidate_components(data)
    ids=data['view_ids']; integer_id={sid:i for i,sid in enumerate(ids)}
    occurrence_rows=[]
    if args.include_occurrences:
        occurrence_rows=[json.loads(x) for x in (ROOT/'data/occurrence_domains.jsonl').read_text(encoding='utf-8').splitlines() if x]
    logs=[]
    def build(query: dict|None=None, operator: str|None=None):
        model=cp_model.CpModel()
        bucket={sid:model.new_int_var_from_domain(cp_model.Domain.from_values(domains[sid]),'bucket:'+sid) for sid in ids}
        index_to_constraint={}
        constraints=list(data['hard_constraints'])
        if query is not None:
            constraints.append({'id':f'QUERY:{query["id"]}:{operator}', 'left':query['left'],'right':query['right'],'operator':operator})
        for c in constraints:
            assumption=model.new_bool_var('assume:'+c['id'])
            expression=(bucket[c['left']] == bucket[c['right']]) if c['operator']=='eq' else (bucket[c['left']] != bucket[c['right']])
            model.add(expression).only_enforce_if(assumption)
            model.add_assumption(assumption)
            index_to_constraint[assumption.index]=c['id']
        for occurrence in occurrence_rows:
            values=[-1]+[integer_id[sid] for sid in occurrence['candidate_structure_ids']]
            model.new_int_var_from_domain(cp_model.Domain.from_values(sorted(set(values))),f'occurrence:{occurrence["occurrence_id"]}')
        return model,bucket,index_to_constraint,constraints
    def solve(query=None,operator=None):
        model,bucket,index_map,constraints=build(query,operator)
        validation=model.validate()
        if validation:
            return {'status':'MODEL_INVALID','validation_error':validation}
        if query is None:
            (ROOT/'reports/models').mkdir(parents=True,exist_ok=True)
            model.export_to_file(str(ROOT/'reports/models/registry_alias_model.textproto'))
        solver=cp_model.CpSolver()
        solver.parameters.num_search_workers=1
        solver.parameters.random_seed=0
        solver.parameters.max_time_in_seconds=args.seconds_per_solve
        solver.parameters.log_search_progress=True
        solver.parameters.log_to_stdout=False
        solver.log_callback=logs.append
        status=solver.solve(model)
        answer={'status':solver.status_name(status),'validation_error':'',
                'wall_time_seconds':solver.wall_time,'response_stats':solver.response_stats()}
        if status in (cp_model.OPTIMAL,cp_model.FEASIBLE):
            witness={sid:solver.value(v) for sid,v in bucket.items()}
            failures=[c['id'] for c in constraints if ((witness[c['left']]==witness[c['right']]) != (c['operator']=='eq'))]
            failures += ['DOMAIN:'+sid for sid,value in witness.items() if value not in domains[sid]]
            if failures:
                raise AssertionError('Independent witness check failed: '+repr(failures))
            answer['witness_constraints_checked']=len(constraints)
            answer['witness_verification_pass']=True
            if query is None:
                dump_json(ROOT/'reports/arbitrary_feasible_witness.json', {
                    'warning':'One feasible assignment only. Do not promote its optional merges.', 'buckets':witness})
        if status == cp_model.INFEASIBLE:
            answer['sufficient_assumption_core']=[index_map.get(i,f'UNMAPPED_LITERAL:{i}') for i in solver.sufficient_assumptions_for_infeasibility()]
            answer['core_is_guaranteed_minimal']=False
        return answer
    baseline=solve()
    results=[]
    satisfiable={'OPTIMAL','FEASIBLE'}
    if baseline['status'] in satisfiable:
        expected={q['id']:q for q in json.loads((ROOT/'reports/pair_queries.json').read_text())}
        for q in data['queries']:
            yes,no=solve(q,'eq'),solve(q,'ne')
            row={'id':q['id'],'left':q['left'],'right':q['right'],'merge':yes,'separate':no}
            if yes['status'] in satisfiable and no['status']=='INFEASIBLE':
                classification='FORCED_ALIAS_BY_FROZEN_INPUT'
            elif no['status'] in satisfiable and yes['status']=='INFEASIBLE':
                classification='SEPARATE_AT_RECORDED_VIEW_LEVEL'
            elif no['status'] in satisfiable and yes['status'] in satisfiable:
                classification='OPEN_UNDER_ENCODED_CONSTRAINTS'
            else:
                classification='INCONCLUSIVE_OR_ENCODING_FAILURE'
            row['classification']=classification
            if classification!='INCONCLUSIVE_OR_ENCODING_FAILURE' and classification!=expected[q['id']]['classification']:
                raise AssertionError('CP-SAT disagrees with independent exact fragment checker: '+q['id'])
            results.append(row)
    result={'schema':'thalean.registry-cp-sat-result.v1','engine_status':baseline['status'],
            'cp_sat_executed':True,'ortools_version':ortools.__version__,
            'model_validation':'PASS' if baseline.get('validation_error','')=='' else 'FAIL',
            'input_model_sha256':sha256(model_path.read_bytes()),'objective':None,
            'worker_count':1,'random_seed':0,'seconds_per_solve':args.seconds_per_solve,
            'occurrence_variables_enabled':args.include_occurrences,
            'baseline':baseline,'queries':results,'no_native_theorem_promotion':True,
            'scope':'only the frozen registry alias model; not an action-table reconstruction'}
    dump_json(ROOT/'reports/cp_sat_result.json',result)
    (ROOT/'reports/cp_sat_search.log').write_text('\n'.join(logs),encoding='utf-8')
    print(json.dumps({'engine_status':baseline['status'],'queries_completed':len(results),'ortools_version':ortools.__version__},indent=2))
    return 0 if baseline['status'] in satisfiable else 1

if __name__=='__main__':
    raise SystemExit(main())
