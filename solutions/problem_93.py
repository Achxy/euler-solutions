# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

from itertools import combinations, permutations, product

def solve():
    def evaluate(a, b, op):
        if op == 0: return a + b
        if op == 1: return a - b
        if op == 2: return a * b
        if op == 3:
            if b == 0: return None
            return a / b
        return None

    def all_results(nums):
        results = set()
        for perm in permutations(nums):
            for ops in product(range(4), repeat=3):
                a, b, c, d = [float(x) for x in perm]
                r = evaluate(a, b, ops[0])
                if r is not None:
                    r = evaluate(r, c, ops[1])
                    if r is not None:
                        r = evaluate(r, d, ops[2])
                        if r is not None and r > 0 and r == int(r):
                            results.add(int(r))
                a, b, c, d = [float(x) for x in perm]
                r1 = evaluate(a, b, ops[0])
                r2 = evaluate(c, d, ops[1])
                if r1 is not None and r2 is not None:
                    r = evaluate(r1, r2, ops[2])
                    if r is not None and r > 0 and r == int(r):
                        results.add(int(r))
                a, b, c, d = [float(x) for x in perm]
                r = evaluate(b, c, ops[0])
                if r is not None:
                    r = evaluate(a, r, ops[1])
                    if r is not None:
                        r = evaluate(r, d, ops[2])
                        if r is not None and r > 0 and r == int(r):
                            results.add(int(r))
                a, b, c, d = [float(x) for x in perm]
                r = evaluate(b, c, ops[0])
                if r is not None:
                    r = evaluate(r, d, ops[1])
                    if r is not None:
                        r = evaluate(a, r, ops[2])
                        if r is not None and r > 0 and r == int(r):
                            results.add(int(r))
                a, b, c, d = [float(x) for x in perm]
                r = evaluate(c, d, ops[0])
                if r is not None:
                    r = evaluate(b, r, ops[1])
                    if r is not None:
                        r = evaluate(a, r, ops[2])
                        if r is not None and r > 0 and r == int(r):
                            results.add(int(r))
        return results

    best = 0
    best_digits = None
    for combo in combinations(range(1, 10), 4):
        results = all_results(combo)
        n = 1
        while n in results:
            n += 1
        consecutive = n - 1
        if consecutive > best:
            best = consecutive
            best_digits = combo

    return int(''.join(str(d) for d in best_digits))

if __name__ == "__main__":
    print(solve())
