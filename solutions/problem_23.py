# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    limit = 28123
    d = [0] * (limit + 1)
    for i in range(1, limit + 1):
        for j in range(2 * i, limit + 1, i):
            d[j] += i
    abundants = [i for i in range(12, limit + 1) if d[i] > i]
    expressible = bytearray(limit + 1)
    for i, a in enumerate(abundants):
        for b in abundants[i:]:
            s = a + b
            if s > limit:
                break
            expressible[s] = 1
    return sum(i for i in range(1, limit + 1) if not expressible[i])

if __name__ == "__main__":
    print(solve())
