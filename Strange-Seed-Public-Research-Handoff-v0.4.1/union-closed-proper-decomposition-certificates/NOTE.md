# Capped fibre certificates for a union-decomposition selector

Draft v0.4.1, 22 October 2026. Novelty unconfirmed. Coordinates are indexed from 0;
subsets are encoded by integer bit masks, with union represented by bitwise OR.
All families below are finite and have no repeated members.

## 1. Question and notation

Let F be union-closed and contain the empty set. For T in F define

\[
q_F(T)=|\{(B,C)\in F^2:B\cup C=T\}|,\qquad
r_F(T)=|\{B\in F:B\subseteq T\}|.
\]

Write e_F(T) for the number of unordered pairs of distinct proper subsets
B,C in F with B union C = T. Then

\[
e_F(T)=\frac{q_F(T)-2r_F(T)+1}{2}.
\]

Indeed, 2r-1 ordered pairs involve T itself; every other ordered pair belongs
to an unordered proper pair of distinct members.

The motivating question is whether every A globally maximizing e_F, with
e_F(A)>0, contains an abundant coordinate: an i belonging to at least |F|/2
members of F. **This note does not answer that question.** It studies a
sufficient weighted certificate and limitations of particular support recipes.

## 2. The adjusted fibre cap

Identify A with a coordinate ground set and put G = F intersect 2^A. For a
nonempty exterior trace Z occurring in F, let

\[
H_Z=\{B\cap A:B\in F,\ B\setminus A=Z\}.
\]

Each H_Z contains A, is union-closed and is G-stable: g union h belongs to H_Z
for every g in G and h in H_Z. The fibre for empty Z is G itself.

Define Q_A(K,L) as the number of ordered pairs (k,l) in K times L whose union
is A, and define

\[
c_G(H)=2Q_A(G,H)+Q_A(H,H)-2|H|.
\]

If A globally maximizes e_F, then every occurring nonempty exterior fibre obeys

\[
c_G(H_Z)\le q_G(A). \tag{1}
\]

Proof: the subfamily consisting of G and the Z-fibre is union-closed. Its
number of ordered decompositions of A union Z is
2Q_A(G,H_Z)+Q_A(H_Z,H_Z), and all |G|+|H_Z| members lie below A union Z.
Its proper-decomposition score is therefore
(2Q_A(G,H_Z)+Q_A(H_Z,H_Z)-2|G|-2|H_Z|+1)/2.
This is at most e_F(A union Z), which is at most e_F(A)
= (q_G(A)-2|G|+1)/2. Rearranging proves (1).

The subtraction of 2|H| matters. The unadjusted inequality
2Q_A(G,H)+Q_A(H,H) <= q_G(A) is not justified by this comparison.
Condition (1) is necessary, not a characterization of globally realizable
collections of interacting fibres.

## 3. Sufficient certificates

For a family K on A define s_i(K)=2|{k in K:i in k}|-|K|. A weight vector
w_i >= 0, sum w_i = 1, is a sufficient certificate if

\[
\sum_i w_i s_i(G)\ge0,\qquad
\sum_i w_i s_i(H)\ge0
\]

for every union-closed G-stable H containing A with c_G(H) <= q_G(A).
Summing over all exterior fibres then gives a nonnegative weighted surplus
for F, so at least one coordinate in the positive support is abundant.
Failure to find these weights does not imply absence of an abundant coordinate.

For an equal pair (i,j), let n_00(K) count members missing both coordinates and
n_11(K) those containing both. Then s_i(K)+s_j(K)=2(n_11(K)-n_00(K)).
An injection from negative 00 traces to positive 11 traces, with each image
forced by G-stability, certifies the required inequality.

For t subset A, its principal stable family is I_t={t union g:g in G}.
It is union-closed, contains t and A, and is contained in any G-stable H
containing t. The cost c_G is monotone on families containing A: adding one
new trace increases 2Q(G,H) by at least 2, increases Q(H,H) by at least 2,
and subtracts 2, for a net increase of at least 2. Thus c_G(I_t)>L excludes
t from every H with c_G(H)<=L. An edge t -> t union g is forced by stability.

## 4. Explicit cores

Here A has seven coordinates and mask 127. The source core G37 is

```text
0 19 23 27 31 46 57 58 59 62 63 86 87 89 90 91 94 95
101 102 103 105 108 109 110 111 115 118 119 120 121 122
123 124 125 126 127
```

Its q is 597, its top proper-decomposition score is 262, and its coordinate
frequencies are (22,26,22,26,27,25,26). Let G38=G37 union {100}; this is
already union-closed, with q=613 and top score 269. In both cores the top
attains the maximum internal e score.

### Exact two-coordinate classification for G38

Of the 21 unordered coordinate pairs, precisely these four support a normalized
nonnegative weight vector satisfying all the capped fibre inequalities and
the core inequality:

```text
(1,4) (3,4) (3,5) (5,6)
```

On each of those supports the only feasible weights are (1/2,1/2).
`data/certificates.json` supplies finite infeasibility witnesses for each of
the other 17 supports and boundary witnesses forcing equality on the four.

To prove feasibility without exhaustively listing fibres, it also supplies
four full injections for G37 at the larger cost cap 629. Any G38-stable H
with c_G38(H)<=613 is G37-stable with c_G37(H)<=613<=629. The injections
apply, and the core inequalities are checked directly. The verifier recomputes
which traces are permitted, checks that every permitted 00 trace is covered,
that positive images are distinct, and that every edge is forced.

An infeasibility witness is a small list of actual admissible families whose
surplus rows make the one-variable weight interval empty. These witnesses
prove failure of every weight on that support, not merely a sampled weight.
Together the witnesses and injections prove the exact 17/4 classification.

### Sharp negative cost 609 for pair (4,6) on G37

Let S={37,39,45,47}. Its stable union closure is

```text
37 39 45 47 55 61 63 101 103 109 111 119 125 127
```

Call this H*. It has size 14, cost 609, and surplus (s_4,s_6)=(-2,0).
Consequently it is negative for equal weights on (4,6).

Any fibre of cost at most 608 must omit at least one member t of S, since
containing S forces H* and monotonicity forces cost at least 609. For each
of these four absence cases the data give a full forced injection from all
permitted negative traces except t into positive traces. Every fibre in
that case has nonnegative pair surplus. Therefore **609 is the exact minimum
cost of a negative equal-pair fibre**, not merely the cost of one example.

Adding mask 100 raises q by 16 but raises this witness's cost only by 4,
to 613. It becomes admissible for G38. The second admissible fibre
{15,31,47,63,95,111,127}, of cost 343, has (s_4,s_6)=(1,-1).
The two inequalities force both coordinates' weights to be zero, excluding
every normalized weighting on (4,6).

### A bounded extension barrier

For every union-closed G' containing G37 and satisfying q_G'(A)<=629, the
four pairs above still give certificates for all its capped fibres and core.

The fibre argument follows from G'-stability implying G37-stability and
c_G37(H)<=c_G'(H)<=629. For the core argument, G37 contains all seven
coatoms A minus {j}. Each added member t is nonempty and has at least two
old union-to-A partners: A and a coatom omitting a coordinate in t.
Thus q increases by at least four per added member. At most eight members
can be added under this q bound. Each added member reduces a pair surplus
by at most two, whereas the four original pair surpluses are 32,32,28,28.
They remain strictly positive.

Since q is odd, q>=631 is necessary to destroy these certificates by additions.
It is not sufficient. The statement says nothing about deleting members,
unrelated cores or alternative proof strategies.

## 5. Why frequency-ranked supports can fail

Consider the core G20

```text
0 45 60 61 63 83 86 87 91 94 95 106 107 110 111 115
119 123 126 127
```

It has q=219, top e=90 and frequencies (13,16,13,14,14,13,15).
All seven incidence columns are distinct, and its unique highest-frequency
pair is (1,6). Two admissible fibres are

```text
H1 = {13,29,45,61,63,95,111,127}   cost 217, surplus (0,-2)
H2 = {29,61,63,93,95,125,127}      cost 205, surplus (-1,1)
```

No normalized nonnegative weights on (1,6) satisfy both inequalities.
For each fibre separately, adjoining its sets with one new exterior coordinate
produces a union-closed family in which A is globally e-maximal. Thus the
obstructions are not merely artefacts of a fibre cost test disconnected from
any actual extension. They are still **not** counterexamples to abundance or
to the motivating selector question. Distinct columns need not be independent;
correlation and containment can remain. No minimality is asserted.

There is also a representation-dependent obstruction for every fixed top-k
recipe. On six coordinates take

```text
G0 = {0,19,22,23,27,31,42,43,44,45,46,47,51,55,59,60,61,62,63}
H0 = {13,29,31,45,47,61,63}
```

G0 has q=189. H0 is stable and union-closed, with cost 173. Coordinate 1
has uniquely highest core frequency 14; all others have frequency at most 13.
But its H0 frequency is 3 out of 7, giving surplus -1.
Replace coordinate 1 by k synchronized copies. This injective union-preserving
encoding preserves family sizes, union counts, costs and stability. The top k
coordinates are exactly the copies; every normalized weight supported on them
has surplus -1 in the encoded H0. This rules out the literal fixed top-k
frequency recipe in unrestricted representations. It does not rule out recipes
that first quotient duplicate columns or use structural information. Coordinate
cloning is standard; no invention of that method is claimed.

## 6. What remains open here

The main selector question remains unresolved in this project. The extent to
which these explicit capped results already occur in the literature is also
unresolved. No general impossibility result for weighted certificates has
been shown. None of these examples establishes a causal advantage for poetry
seeding: they are reusable mathematical outputs from an exploratory process.

All finite data are in the accompanying JSON files. `verify.py` recomputes the
checks; `test_verifier.py` checks that several corrupt certificates are rejected.
The proofs in this note, the checker implementation and the priority assessment
still warrant independent expert review.
