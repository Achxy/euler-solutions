# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    def triangle(n): return n * (n + 1) // 2
    def square(n): return n * n
    def pentagonal(n): return n * (3 * n - 1) // 2
    def hexagonal(n): return n * (2 * n - 1)
    def heptagonal(n): return n * (5 * n - 3) // 2
    def octagonal(n): return n * (3 * n - 2)

    funcs = [triangle, square, pentagonal, hexagonal, heptagonal, octagonal]
    sets = []
    for f in funcs:
        s = set()
        n = 1
        while True:
            v = f(n)
            if v >= 10000:
                break
            if v >= 1000:
                s.add(v)
            n += 1
        sets.append(s)

    from itertools import permutations
    for perm in permutations(range(1, 6)):
        order = [0] + list(perm)
        pools = [sorted(sets[i]) for i in order]
        def search(chain, used_indices):
            if len(chain) == 6:
                if chain[-1] % 100 == chain[0] // 100:
                    return sum(chain)
                return None
            idx = len(chain)
            last_two = chain[-1] % 100
            for val in pools[idx]:
                if val // 100 == last_two:
                    result = search(chain + [val], used_indices | {idx})
                    if result is not None:
                        return result
            return None

        for start in pools[0]:
            result = search([start], {0})
            if result is not None:
                return result

if __name__ == "__main__":
    print(solve())
