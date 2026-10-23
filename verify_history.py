#!/usr/bin/env python3
"""Recheck selected finite witnesses from the expanded history, Python >=3.9.

No search, new conjecture, solver, or full historical enumeration is run.
These checks do not establish historical priority or a causal poetry effect.
"""
from collections import Counter
from fractions import Fraction
from itertools import combinations
import json
import math
from pathlib import Path

HERE=Path(__file__).resolve().parent

def require(ok,message):
    if not ok:
        raise ValueError(message)

def countbits(x):
    return bin(x).count('1')

def uc(f):
    s=set(f)
    return len(s)==len(f) and all(a|b in s for a in s for b in s)

def freq(f,n):
    return [sum(bool(a&(1<<i)) for a in f) for i in range(n)]

def surplus(f,n):
    return [2*x-len(f) for x in freq(f,n)]

def unioncounts(f):
    return Counter(a|b for a in f for b in f)

def propercounts(f):
    return Counter(a|b for a,b in combinations(f,2) if a|b not in (a,b))

def cost(g,h,top,adjusted=True):
    c=2*sum(a|b==top for a in g for b in h)+sum(a|b==top for a in h for b in h)
    return c-2*len(h) if adjusted else c

def stable(g,h):
    return all(a|b in h for a in g for b in h)

def closure(gens):
    s={0}
    for g in gens:
        s|={a|g for a in tuple(s)}
    return sorted(s)

def irreducibles(f):
    out=[]
    for a in f:
        if not a:
            continue
        below=[b for b in f if b!=a and b|a==a]
        total=0
        for b in below:
            total|=b
        if total!=a:
            out.append(a)
    return out

def private_scores(f,n):
    """Enumerate generator subfamilies; test every deletion for minimality."""
    gens=irreducibles(f)
    by_target={}
    for mask in range(1,1<<len(gens)):
        chosen=[g for i,g in enumerate(gens) if mask&(1<<i)]
        target=0
        for g in chosen:
            target|=g
        private=0
        minimal=True
        for i,g in enumerate(chosen):
            others=0
            for j,h in enumerate(chosen):
                if i!=j:
                    others|=h
            if others==target:
                minimal=False
                break
            private|=g&~others
        if minimal:
            by_target.setdefault(target,[]).append(private)
    require(set(by_target)==set(f)-{0},'minimal representation coverage')
    raw=[0]*n
    normalized=[Fraction(0)]*n
    for rows in by_target.values():
        for i in range(n):
            credits=sum(bool(x&(1<<i)) for x in rows)
            raw[i]+=credits
            normalized[i]+=Fraction(credits,len(rows))
    return raw,normalized,sum(map(len,by_target.values()))

def max_inclusion_matching(f,i):
    left=[a for a in f if not a&(1<<i)]
    right=[a for a in f if a&(1<<i)]
    matched={}
    def augment(a,seen):
        for b in right:
            if a|b!=b or b in seen:
                continue
            seen.add(b)
            if b not in matched or augment(matched[b],seen):
                matched[b]=a
                return True
        return False
    return sum(augment(a,set()) for a in left),len(left)

def check_triples():
    families=[]
    negative=[]
    for mask in range(128):
        h={7}|{a for a in range(7) if mask&(1<<a)}
        if not uc(h):
            continue
        families.append(h)
        d=sum(2*countbits(a)-3 for a in h)
        require(3*d>=-len(h),'general triple balance')
        if 0 not in h:
            require(7*d>=3*len(h),'empty-free triple balance')
        if d<0:
            require(d==-1,'negative triple balance value')
            negative.append(sorted(h))
    require(len(families)==90 and len(negative)==6,'triple class counts')
    return dict(fibres=90,negative_fibres=negative)

def check_fano():
    k={0}
    for i in range(7):
        line=[i,(i+1)%7,(i+3)%7]
        for subset in range(8):
            a=sum(1<<line[j] for j in range(3) if subset&(1<<j))
            if a&(1<<i):
                k.add(a)
    f=sorted(127^a for a in k)
    require(uc(f) and len(f)==29,'Fano family closure/count')
    require(freq(f,7)==[21]*7,'Fano frequencies')
    matches=[max_inclusion_matching(f,i) for i in range(7)]
    require(matches==[(7,8)]*7,'Fano inclusion deficits')
    return dict(family=f,frequencies=freq(f,7),matching_sizes=[7]*7,source_sizes=[8]*7)

def check_localization():
    results=[]
    for q in [3,4,6,10]:
        n=3*q;s=7;x=((1<<n)-1)<<3;f={s}
        for i in range(n):
            t=x^(1<<(3+i));f.update([t,t|(1<<(i%3)),t|s])
        f.update(x|r for r in range(8))
        z=0
        for j in range(q-2):
            z|=1<<(3+n+j);f.update(x|z|r for r in range(1,8))
        require(uc(f),'localization construction closure')
        y=0
        for a in f:
            if not a&s:
                y|=a
        inside=sum(a&~(s|y)==0 for a in f)
        require(len(f)==16*q-5 and inside==9*q+9,'localization counts')
        require(freq(f,3)==[8*q-3]*3 and 16*inside>9*len(f),'localization deficiency')
        results.append(dict(q=q,m=len(f),inside=inside,triple_frequencies=freq(f,3)))
    return results

def check_lifting():
    s=7;x=((1<<12)-1)<<3;g={s}
    for i in range(12):
        t=x^(1<<(3+i));label=1 if i<6 else 2 if i<9 else 4
        g.update([t,t|label,t|s])
    g.update(x|r for r in range(8))
    z=1<<15;t=x^(1<<(3+6))
    b={t|z|r for r in [2,4,6,7]}
    c={x|z|r for r in [2,4,3,5,6,7]};f=g|b|c
    require(uc(f) and (len(g),len(b),len(c),len(f))==(45,4,6,55),'55-set closure/count')
    require(freq(g,3)==[23,20,20] and freq(f,3)==[27]*3,'55-set margins')
    y=56;g2={s}|{y|r for r in range(8)};f2=set(g2);z2=0
    for j in range(8):
        z2|=1<<(6+j)
        f2.update(z2|s|(y^(hole<<3)) for hole in [0,1,2,3,7])
    require(uc(f2) and len(f2)==49,'49-set closure/count')
    require(freq(g2,6)[3:]==[8]*3 and freq(f2,6)[3:]==[24,24,40],'49-set margins')
    core={r|h for r in range(8) for h in [0,32,56]}
    require(uc(core) and len(core)==24 and freq(core,6)==[12,12,12,8,8,16],'24-set core')
    require(sum(freq(core,6))==68<72,'24-set density failure')
    return dict(naive_lift=dict(m=55,core_triple=[23,20,20],global_triple=[27]*3),
                depth_three=dict(m=49,core_anchor=[8]*3,global_anchor=[24,24,40]),
                low_density_core=dict(m=24,incidences=68))

def check_union_root():
    f=[0,3,5,6,7];root={}
    for a in sorted(f,key=lambda a:(countbits(a),a)):
        c=sum(b|a==a for b in f)/5
        root[a]=math.sqrt(c)-sum(v for b,v in root.items() if b|a==a)
    # Exact sign: 3sqrt(2)>2+sqrt(5), since 9>4sqrt(5), since81>80.
    lower2,upper5=Fraction(707,500),Fraction(2237,1000)
    require(lower2*lower2<2 and upper5*upper5>5
            and 3*lower2>2+upper5 and root[7]<0,'negative union-root coefficient')
    conv={a:sum(root[b]*root[c] for b in f for c in f if b|c==a) for a in f}
    require(max(abs(v-.2) for v in conv.values())<1e-12,'signed convolution sanity check')
    return dict(family=f,negative_top_mass=root[7],exact_sign_argument='81>80; see source E04',floating_sanity_tolerance=1e-12)

def check_private_scores():
    f=closure([6,17,21,22,40,48])
    raw,v,reps=private_scores(f,6)
    require(len(f)==18 and freq(f,6)==[9,8,11,7,14,12],'raw score family')
    require(raw==[18,19,16,11,14,18] and reps==28,'raw private scores')
    results=[]
    for k in [3,4,5]:
        family=[0]+[a for a in range(1<<(k+2)) if a&3]
        raw2,v2,reps2=private_scores(family,k+2)
        a=Fraction(k+1)+Fraction(k+3,2)*Fraction(3,2)**(k-1)
        b=Fraction(3*2**(k-1))-Fraction(1,3)
        require(v2==[a,a]+[b]*k and b>a,'normalized score failure')
        require(freq(family,k+2)==[2**(k+1)]*2+[3*2**(k-1)]*k,'normalized frequencies')
        results.append(dict(k=k,m=len(family),anchor_score=str(a),other_score=str(b),frequencies=freq(family,k+2)))
    return dict(raw_counterexample=dict(family=f,frequencies=freq(f,6),scores=raw),normalized_examples=results)

def check_old_modal_transfer():
    g=[0,19,22,23,27,31,42,43,44,45,46,47,51,55,59,60,61,62,63]
    h=[13,29,31,45,47,61,63];f=g+[a|64 for a in h]
    require(uc(g) and uc(h) and stable(g,h) and uc(f),'old transfer closure')
    counts=unioncounts(f)
    require(unioncounts(g)[63]==189 and cost(g,h,63,False)==187,'old transfer cap')
    require(freq(g,6)==[12,14,12,13,12,13] and freq(h,6)[1]==3,'old transfer rank')
    require(counts[63]==max(counts.values())==189 and freq(f,6)[1]==17,'actual q-modal extension')
    return dict(q=189,old_cost=187,core_maximizer_frequency=14,fibre_frequency='3/7',global_frequency='17/26')

def product_core_and_fibre(sizes):
    blocks=[];pos=0
    for size in sizes:
        blocks.append(((1<<size)-1)<<pos);pos+=size
    p,q,r,d,e=blocks;k=[0,p,q,p|q,p|q|r]
    g=sorted(a|b|c for a in k for b in [0,d] for c in [0,e])
    h=sorted(a|d|e for a in k)
    return g,h,(1<<pos)-1,pos,blocks

def check_uniform_and_threshold():
    g,h,top,n,blocks=product_core_and_fibre([3,3,13,3,3]);f=g+[a|(1<<n) for a in h]
    require(uc(f) and len(f)==25 and min(countbits(a) for a in f if a)==3,'uniform product example')
    require(unioncounts(g)[top]==81 and cost(g,h,top,False)==81,'uniform modal cap')
    require(unioncounts(f)[top]==max(unioncounts(f).values())==81,'uniform actual modal status')
    require(sum(surplus(h,n))==-3 and sum(surplus(g,n))==-132,'uniform failure margins')
    # B=three singleton coordinates, D/E=three-coordinate blocks each.
    b,d,e=7,56,448;top2=511
    g2=sorted(k|dd|ee for k in range(8) for dd in [0,d] for ee in [0,e])
    h2=sorted(b|dd|ee for dd in [0,8,d] for ee in [0,e])
    f2=g2+[a|512 for a in h2]
    weights=[0]*3+[1]*6
    margin=sum(w*s for w,s in zip(weights,surplus(h2,9)))
    require(uc(f2) and len(f2)==38 and stable(g2,h2),'threshold example closure')
    require(cost(g2,h2,top2,False)==207 and unioncounts(g2)[top2]==243 and margin==-2,'threshold counterexample')
    require(unioncounts(f2)[top2]==max(unioncounts(f2).values())==243,'threshold actual modality')
    return dict(uniform=dict(m=25,core_surplus=-132,fibre_surplus=-3,q=81),outside_balanced_threshold=dict(m=38,q=243,fibre_cost=207,balanced_surplus=-2))

def check_nonproduct_clone():
    g=[0,23,31,46,57,58,59,62,63,86,87,89,90,91,94,95,101,102,103,105,108,109,110,111,115,118,119,120,121,122,123,124,125,126,127]
    h=[14,30,31,46,62,63,78,94,95,110,111,126,127]
    b=15;n=b+6;top=(1<<n)-1
    def lift(a):return ((1<<b)-1 if a&1 else 0)|((a>>1)<<b)
    gg=list(map(lift,g));hh=list(map(lift,h));f=gg+[a|(1<<n) for a in hh]
    require(uc(f) and len(f)==48 and stable(gg,hh),'nonproduct clone closure')
    require(sum(surplus(hh,n))==-1 and sum(surplus(gg,n))==159,'nonproduct clone uniform scores')
    require(unioncounts(gg)[top]==555 and cost(gg,hh,top,False)==521,'nonproduct clone cost')
    counts=unioncounts(f)
    require(counts[top]==555 and [a for a,v in counts.items() if v==555]==[top],'nonproduct unique q-mode')
    return dict(clone_size=15,target_size=21,m=48,q=555,fibre_cost=521,fibre_surplus=-1,core_surplus=159)

def check_joint_cost():
    g=[0,23,27,29,30,31,39,43,45,46,47,51,53,55,58,59,60,61,62,63]
    i14={a|14 for a in g};i50={a|50 for a in g};cap=unioncounts(g)[63]
    values=[cost(g,i14,63,False),cost(g,i50,63,False),cost(g,i14|i50,63,False)]
    require(cap==225 and values==[199,199,365],'joint-cost conflict')
    for h in [[56,58,59,60,61,62,63],[14,30,31,46,47,62,63]]:
        require(uc(h) and stable(g,h) and cost(g,h,63,False)==199 and surplus(h,6)[0]==-1,'invalid point weighting')
    return dict(q=225,individual_costs=values[:2],joint_cost=values[2],negative_point_witnesses=2)

def check_adjusted_pair_failures():
    g=[0,7,11,15,47,50,51,53,54,55,59,60,61,62,63];rows=[]
    for pair,h,expected in [((0,4),[14,15,46,47,62,63],117),((3,4),[7,15,39,47,55,63],109)]:
        require(uc(h) and stable(g,h) and cost(g,h,63)==expected,'adjusted pair witness')
        require(sum(surplus(h,6)[i] for i in pair)==-2,'pair failure margin')
        f=g+[a|64 for a in h];ec=propercounts(f)
        require(uc(f) and ec[63]==max(ec.values())==44,'pair failure global e-mode')
        rows.append(dict(pair=pair,cost=expected,pair_surplus=-2,global_target_e=44))
    return rows

def check_stabilizer_near_miss():
    data=json.loads((HERE/'data/ranking_counterexample.json').read_text());g=data['core'];h=data['obstruction_fibres'][0]
    near=[a for a in g if a!=94];f=near+[a|128 for a in h];ec=propercounts(f)
    require(uc(near) and uc(f) and stable(near,h),'near-miss closure')
    require(unioncounts(near)[127]==201 and cost(near,h,127)==207,'near-miss gap')
    require(ec[127]==82 and ec[255]==85,'near-miss global score reversal')
    require(unioncounts(g)[127]==219 and cost(g,h,127)==217,'stabilizer repair')
    return dict(near_q=201,near_cost=207,near_target_e=82,near_exterior_e=85,repaired_q=219,repaired_cost=217)

def check_additive_path():
    data=json.loads((HERE/'data/certificates.json').read_text());g37=data['source_core']
    g35=[a for a in g37 if a not in [19,27]];g36=sorted(g35+[19])
    for g,want in [(g35,555),(g36,571),(g37,597)]:
        require(uc(g) and unioncounts(g)[127]==want,'accepted additive core path')
    h=[7,23,31,39,47,55,63,87,95,103,111,119,127]
    require(stable(g35,h) and stable(g36,h) and cost(g35,h,127)==565 and cost(g36,h,127)==569,'first additive witness')
    require([surplus(h,7)[i] for i in [3,6]]==[-1,-1],'first new blocked pair')
    ha=[69,71,79,87,93,95,101,103,109,111,119,125,127]
    hb=[7,15,23,31,47,63,71,79,87,95,103,111,119,127]
    require(all(uc(hh) and stable(g37,hh) for hh in [ha,hb]),'second additive witness structure')
    require([cost(g36,hh,127) for hh in [ha,hb]]==[561,589] and [cost(g37,hh,127) for hh in [ha,hb]]==[575,597],'second additive costs')
    require([surplus(ha,7)[i] for i in [4,5]]==[-1,1] and [surplus(hb,7)[i] for i in [4,5]]==[0,-2],'second blocked pair rows')
    return dict(core_q_path=[555,571,597],first_cost_path=[565,569],second_costs_before=[561,589],second_costs_after=[575,597])

def main():
    checks={}
    for name,fn in [('triple_fibres',check_triples),('fano_matching',check_fano),('localization_examples',check_localization),('core_lifting_failures',check_lifting),('union_roots',check_union_root),('private_witness_scores',check_private_scores),('old_modal_transfer',check_old_modal_transfer),('uniform_and_balanced_threshold',check_uniform_and_threshold),('nonproduct_clone',check_nonproduct_clone),('joint_cost_conflict',check_joint_cost),('adjusted_pair_failures',check_adjusted_pair_failures),('stabilizer_near_miss',check_stabilizer_near_miss),('additive_path_witnesses',check_additive_path)]:
        checks[name]=fn()
    print(json.dumps({'passed':True,'check_groups':len(checks),'scope':'Selected finite witnesses only; see VERIFICATION-SCOPE.md','checks':checks},indent=2))

if __name__=='__main__':
    main()
