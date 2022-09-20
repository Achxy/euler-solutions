# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

from math import isqrt

def solve():
    best_x = 0
    best_d = 0
    for d in range(2, 1001):
        s = isqrt(d)
        if s * s == d:
            continue
        m, k, a = 0, 1, s
        n0, n1 = 1, a
        d0, d1 = 0, 1
        while n1 * n1 - d * d1 * d1 != 1:
            m = k * a - m
            k = (d - m * m) // k
            a = (s + m) // k
            n0, n1 = n1, a * n1 + n0
            d0, d1 = d1, a * d1 + d0
        if n1 > best_x:
            best_x = n1
            best_d = d
    return best_d

if __name__ == "__main__":
    print(solve())
