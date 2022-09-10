# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

from math import gcd

def solve():
    counts = [0] * 1001
    for m in range(2, 23):
        for n in range(1, m):
            if (m + n) % 2 == 0 or gcd(m, n) != 1:
                continue
            p = 2 * m * (m + n)
            for kp in range(p, 1001, p):
                counts[kp] += 1
    return max(range(1, 1001), key=lambda i: counts[i])

if __name__ == "__main__":
    print(solve())
