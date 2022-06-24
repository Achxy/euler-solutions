# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    cache = {}
    def chain_len(n):
        orig = n
        steps = 0
        while n != 1 and n not in cache:
            n = 3 * n + 1 if n & 1 else n >> 1
            steps += 1
        steps += cache.get(n, 0)
        cache[orig] = steps
        return steps

    best_n, best_len = 1, 1
    for i in range(2, 1_000_000):
        cl = chain_len(i)
        if cl > best_len:
            best_n, best_len = i, cl
    return best_n

if __name__ == "__main__":
    print(solve())
