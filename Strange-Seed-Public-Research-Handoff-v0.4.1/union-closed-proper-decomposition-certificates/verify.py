#!/usr/bin/env python3
"""Check explicit finite certificates; Python >=3.9, standard library only.

This is a proof-certificate checker, not a formal proof assistant. See NOTE.md
for why the checked injections and inequalities imply the infinite-class claims.
"""
from pathlib import Path
from itertools import combinations
from collections import Counter
from fractions import Fraction
import json

HERE = Path(__file__).resolve().parent
TOP = 127
PAIRS = set(combinations(range(7), 2))

def require(condition, explanation):
    if not condition:
        raise ValueError(explanation)

def union_closed(family):
    s = set(family)
    return len(s) == len(family) and all(a | b in s for a in s for b in s)

def q(family):
    return sum(a | b == TOP for a in family for b in family)

def decompositions(family):
    return Counter(a | b for a, b in combinations(family, 2)
                   if (a | b) not in (a, b))

def frequencies(family):
    return [sum(bool(a & (1 << j)) for a in family) for j in range(7)]

def surplus(family):
    return [2 * n - len(family) for n in frequencies(family)]

def cost(core, fibre):
    return (2 * sum(g | h == TOP for g in core for h in fibre)
            + sum(a | b == TOP for a in fibre for b in fibre)
            - 2 * len(fibre))

def check_core(core):
    require(all(isinstance(t, int) and 0 <= t <= TOP for t in core), 'core range')
    require(0 in core and TOP in core and union_closed(core), 'invalid core')

def check_fibre(core, fibre, cap=None):
    require(all(isinstance(t, int) and 0 <= t <= TOP for t in fibre), 'fibre range')
    require(TOP in fibre and union_closed(fibre), 'invalid fibre')
    s = set(fibre)
    require(all(g | h in s for g in core for h in fibre), 'fibre not core-stable')
    if cap is not None:
        require(cost(core, fibre) <= cap, 'fibre exceeds adjusted cost cap')

def feasible_interval(rows, pair):
    """Independent exact feasibility for normalized weights (p, 1-p)."""
    a, b = pair
    lo, hi = Fraction(0), Fraction(1)
    for row in rows:
        delta = row[a] - row[b]
        if delta == 0:
            if row[b] < 0:
                return None
        elif delta > 0:
            lo = max(lo, Fraction(-row[b], delta))
        else:
            hi = min(hi, Fraction(-row[b], delta))
    return None if lo > hi else (lo, hi)

def check_matching(core, pair, cap, matching, absent=None):
    a, b = pair
    principals = [{t | g for g in core} for t in range(128)]
    allowed = {t for t in range(128) if cost(core, list(principals[t])) <= cap}
    negative = {t for t in allowed if not (t & (1 << a)) and not (t & (1 << b))}
    if absent is not None:
        negative.discard(absent)
    left = [t for t, s in matching]
    right = [s for t, s in matching]
    require(len(left) == len(set(left)) and set(left) == negative, 'matching misses domain')
    require(len(right) == len(set(right)), 'matching is not injective')
    for t, s in matching:
        require(s in allowed and s & (1 << a) and s & (1 << b), 'bad matching image')
        require(any(t | g == s for g in core), 'matching edge is not forced by stability')

def stable_closure(core, initial):
    s = set(initial)
    while True:
        enlarged = s | {a | b for a in s for b in s} | {g | h for g in core for h in s}
        if enlarged == s:
            return sorted(s)
        s = enlarged

def check_certificates(data):
    source, best = data['source_core'], data['best_core']
    check_core(source)
    check_core(best)
    require(set(source) <= set(best), 'best core is not an extension')
    require(q(source) == data['source_q'] == 597, 'source q mismatch')
    require(q(best) == data['best_q'] == 613, 'best q mismatch')
    for core, expected in [(source, 262), (best, 269)]:
        e = decompositions(core)
        require(e[TOP] == max(e.values()) == expected, 'internal proper-decomposition score')
    maps = data['survivor_matchings']
    protected = set()
    for record in maps:
        pair = tuple(record['pair'])
        require(record['cost_cap'] == 629, 'unexpected protection cap')
        check_matching(source, pair, 629, record['matching'])
        require(sum(surplus(best)[i] for i in pair) >= 0, 'negative best-core pair surplus')
        protected.add(pair)
    require(len(protected) == 4 and q(best) <= 629, 'survivor coverage')
    blocked = set()
    for record in data['blocked_pair_proofs']:
        pair = tuple(record['pair'])
        require(pair in PAIRS and pair not in blocked, 'invalid or duplicate blocked support')
        rows = []
        for constraint in record['constraints']:
            family = constraint['family']
            if constraint['kind'] == 'core':
                require(family == best, 'wrong core constraint')
            else:
                require(constraint['kind'] == 'fibre', 'constraint kind')
                check_fibre(best, family, q(best))
            rows.append(surplus(family))
        require(feasible_interval(rows, pair) is None, 'support obstruction does not prove infeasibility')
        blocked.add(pair)
    require(len(blocked) == 17 and blocked.isdisjoint(protected)
            and blocked | protected == PAIRS, 'not an exact 17/4 support partition')
    boundary_pairs = set()
    for record in data['survivor_weight_boundaries']:
        pair = tuple(record['pair'])
        require(pair in protected and pair not in boundary_pairs, 'boundary support')
        lower, upper = record['forces_p_ge_half'], record['forces_p_le_half']
        check_fibre(best, lower, q(best))
        check_fibre(best, upper, q(best))
        require(feasible_interval([surplus(lower), surplus(upper)], pair)
                == (Fraction(1, 2), Fraction(1, 2)), 'weights are not forced to equality')
        boundary_pairs.add(pair)
    require(boundary_pairs == protected, 'missing boundary proof')
    sharp = data['sharp_negative_cost']
    forced = stable_closure(source, sharp['joint_trace_set'])
    require(forced == sharp['forced_closure'] and cost(source, forced) == 609, 'joint closure/cost')
    require(sum(surplus(forced)[j] for j in sharp['pair']) < 0, 'no negative witness at 609')
    require(sharp['proof_cap'] == 608 and cost(source, forced) > sharp['proof_cap'], 'joint exclusion')
    absences = set()
    for branch in sharp['absence_branches']:
        t = branch['absent']
        require(t in sharp['joint_trace_set'], 'absence outside excluded set')
        check_matching(source, sharp['pair'], 608, branch['matching'], t)
        absences.add(t)
    require(absences == set(sharp['joint_trace_set']), 'absence branches incomplete')
    # Core margin protection for every core extension with q <= 629.
    require(all(TOP ^ (1 << j) in source for j in range(7)), 'missing source coatom')
    dmax = (629 - q(source)) // 4
    require(dmax == 8, 'extension bound')
    for pair in protected:
        require(sum(surplus(source)[j] for j in pair) - 2 * dmax > 0,
                'extension core surplus not protected')
    return {'blocked_supports': len(blocked), 'surviving_supports': len(protected),
            'exact_minimum_negative_cost_for_pair_4_6': 609, 'extension_protection_q': 629}

def check_ranking(data):
    core, pair = data['core'], data['ranked_pair']
    check_core(core)
    require(q(core) == data['q'] == 219, 'ranking core q')
    f = frequencies(core)
    top_pairs = [p for p in PAIRS if sum(f[j] for j in p) == sum(sorted(f, reverse=True)[:2])]
    require(top_pairs == [tuple(pair)], 'ranked pair not unique')
    require(len({tuple(bool(t & (1 << j)) for t in core) for j in range(7)}) == 7,
            'coordinate columns not distinct')
    rows = []
    for fibre in data['obstruction_fibres']:
        check_fibre(core, fibre, q(core))
        rows.append(surplus(fibre))
        family = core + [h | 128 for h in fibre]
        require(union_closed(family), 'global extension not union-closed')
        e = decompositions(family)
        require(e[TOP] == max(e.values()) == 90, 'global target not e-maximal')
    require(feasible_interval(rows, pair) is None, 'ranked support not obstructed')
    seed = data['cloning_seed']
    G, H = seed['G'], seed['H']
    require(all(isinstance(t, int) and 0 <= t <= 63 for t in G + H), 'cloning seed range')
    require(0 in G and 63 in G and 63 in H, 'cloning seed endpoints')
    require(union_closed(G) and union_closed(H), 'cloning seed closure')
    require(all(g | h in H for g in G for h in H), 'cloning seed stability')
    f = [sum(bool(g & (1 << j)) for g in G) for j in range(6)]
    h = sum(bool(t & 2) for t in H)
    require(f[1] == 14 and all(f[1] > f[j] for j in range(6) if j != 1), 'clone frequency rank')
    require(2 * h - len(H) == -1, 'cloning obstruction missing')
    seed_q = sum(a | b == 63 for a in G for b in G)
    seed_cost = (2 * sum(g | t == 63 for g in G for t in H)
                 + sum(a | b == 63 for a in H for b in H) - 2 * len(H))
    require(seed_q == 189 and seed_cost == 173 <= seed_q, 'cloning seed cost')
    return {'distinct_column_rank_counterexample': True, 'cloning_seed_checked': True}

def main():
    data = json.loads((HERE / 'data/certificates.json').read_text())
    ranking = json.loads((HERE / 'data/ranking_counterexample.json').read_text())
    print(json.dumps({'passed': True, **check_certificates(data), **check_ranking(ranking)}, indent=2))

if __name__ == '__main__':
    main()
