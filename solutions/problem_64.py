# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

from math import isqrt

def solve():
    count = 0
    for n in range(2, 10001):
        s = isqrt(n)
        if s * s == n:
            continue
        m, d, a = 0, 1, s
        period = 0
        while True:
            m = d * a - m
            d = (n - m * m) // d
            a = (s + m) // d
            period += 1
            if a == 2 * s:
                break
        if period % 2 == 1:
            count += 1
    return count

if __name__ == "__main__":
    print(solve())
