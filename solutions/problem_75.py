# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

from math import gcd

def solve():
    limit = 1500000
    counts = [0] * (limit + 1)
    mlimit = int((limit / 2) ** 0.5) + 1
    for m in range(2, mlimit):
        for n in range(1, m):
            if (m + n) % 2 == 0 or gcd(m, n) != 1:
                continue
            a = m * m - n * n
            b = 2 * m * n
            c = m * m + n * n
            p = a + b + c
            k = 1
            while k * p <= limit:
                counts[k * p] += 1
                k += 1
    return sum(1 for x in counts if x == 1)

if __name__ == "__main__":
    print(solve())
