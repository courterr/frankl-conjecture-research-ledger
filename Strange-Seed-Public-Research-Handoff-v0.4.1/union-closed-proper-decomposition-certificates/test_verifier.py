#!/usr/bin/env python3
"""A few meaningful rejection checks; not a proof of checker correctness."""
from copy import deepcopy
import json
from verify import HERE, check_certificates, check_ranking

def rejected(label, action):
    try:
        action()
    except ValueError:
        return label
    raise AssertionError('Corrupt certificate was accepted: ' + label)

def main():
    data = json.loads((HERE / 'data/certificates.json').read_text())
    ranking = json.loads((HERE / 'data/ranking_counterexample.json').read_text())
    check_certificates(data)
    check_ranking(ranking)
    tests = []
    corrupt = deepcopy(data)
    m = corrupt['survivor_matchings'][0]['matching']
    m[1][1] = m[0][1]
    tests.append(rejected('duplicate positive matching image', lambda: check_certificates(corrupt)))
    corrupt = deepcopy(data)
    corrupt['best_q'] = 611
    tests.append(rejected('incorrect recomputed core q', lambda: check_certificates(corrupt)))
    corrupt = deepcopy(data)
    proof = corrupt['blocked_pair_proofs'][0]
    proof['constraints'] = [{'kind': 'fibre', 'family': [127]}]
    tests.append(rejected('non-obstructing replacement fibre', lambda: check_certificates(corrupt)))
    corrupt_ranking = deepcopy(ranking)
    corrupt_ranking['cloning_seed']['H'].append(64)
    tests.append(rejected('out-of-range cloning seed', lambda: check_ranking(corrupt_ranking)))
    print(json.dumps({'passed': True, 'rejection_checks': tests}, indent=2))

if __name__ == '__main__':
    main()
