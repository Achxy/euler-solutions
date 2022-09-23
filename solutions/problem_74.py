# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

from math import factorial

def solve():
    fact = [factorial(d) for d in range(10)]

    def digit_fact_sum(n):
        return sum(fact[int(d)] for d in str(n))

    cache = {}
    def chain_length(n):
        seen = []
        visited = set()
        current = n
        while current not in visited:
            if current in cache:
                length = cache[current]
                for i, v in enumerate(seen):
                    cache[v] = length + len(seen) - i
                return cache[n]
            visited.add(current)
            seen.append(current)
            current = digit_fact_sum(current)
        cycle_start = seen.index(current)
        cycle_len = len(seen) - cycle_start
        for i in range(cycle_start, len(seen)):
            cache[seen[i]] = cycle_len
        for i in range(cycle_start - 1, -1, -1):
            cache[seen[i]] = cache[seen[i + 1]] + 1
        return cache[n]

    count = 0
    for n in range(1, 1000000):
        if chain_length(n) == 60:
            count += 1
    return count

if __name__ == "__main__":
    print(solve())
