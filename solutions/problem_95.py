# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    limit = 1000000
    spd = [0] * (limit + 1)
    for i in range(1, limit + 1):
        for j in range(2 * i, limit + 1, i):
            spd[j] += i

    best_length = 0
    best_min = 0

    visited = [False] * (limit + 1)

    for start in range(2, limit + 1):
        if visited[start]:
            continue
        chain = []
        seen = {}
        n = start
        while True:
            if n > limit or n < 1:
                break
            if n in seen:
                idx = seen[n]
                cycle = chain[idx:]
                cycle_len = len(cycle)
                if cycle_len > best_length:
                    best_length = cycle_len
                    best_min = min(cycle)
                elif cycle_len == best_length:
                    m = min(cycle)
                    if m < best_min:
                        best_min = m
                break
            if visited[n]:
                break
            seen[n] = len(chain)
            chain.append(n)
            n = spd[n]

        for c in chain:
            if c <= limit:
                visited[c] = True

    return best_min

if __name__ == "__main__":
    print(solve())
