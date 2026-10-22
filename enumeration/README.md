# Optional historical enumerators

The main proofs do not require these programs. Use `../verify.py` first.
These are earlier exploratory C++ sources, preserved for reproducibility and
inspection rather than offered as a polished search library. Full enumerations
were not rerun during packaging. Only trusted, correctly formatted input is
supported; input validation differs between the programs.

With a GNU-compatible compiler supporting `bits/stdc++.h` and `unsigned __int128`:

```sh
g++ -O2 -std=c++17 enumerate.cpp -o enumerate
g++ -O2 -std=c++17 independent.cpp -o independent
./enumerate families.hex < best-core-input.txt
./independent independent-families.hex < best-core-input.txt
```

Both accept a log filename and optional integer offset added to the cost cap.
Input is: dimension, core size, core masks, coordinate weights, node limit,
time limit in seconds. The sample requests at most 2,000,000 nodes / roughly
three seconds; time is checked periodically and is not a hard external deadline.
An `unresolved` status is incomplete and cannot certify exhaustion.

The early-negative-return branches are intentionally disabled in these archived
enumeration variants. In particular, `enumerate.cpp`'s `complete_no_violation`
label means the permitted enumeration completed; it is **not** itself a check
that a chosen weighting has no violation. Its logged families require separate
analysis. `independent.cpp` reports minima over completed leaves. Never interpret
any reported minimum from an interrupted search as a universal lower bound.

Logs encode families as bitsets in hexadecimal; bit t means trace t is present.
For seven coordinates each line is 32 hexadecimal digits. These optional
search logs are not included in the archive; finite certificates are instead.
