# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

from itertools import combinations

def solve():
    limit = 1000000
    sieve = [True] * limit
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit, i):
                sieve[j] = False

    for n in range(10, limit):
        if not sieve[n]:
            continue
        s = str(n)
        digits = len(s)
        for size in range(1, digits):
            for positions in combinations(range(digits), size):
                family = []
                start = 0 if positions[0] != 0 else 1
                for d in range(start, 10):
                    candidate = list(s)
                    for p in positions:
                        candidate[p] = str(d)
                    candidate = int(''.join(candidate))
                    if candidate >= 10 ** (digits - 1) and candidate < limit and sieve[candidate]:
                        family.append(candidate)
                if len(family) == 8:
                    return min(family)

if __name__ == "__main__":
    print(solve())
