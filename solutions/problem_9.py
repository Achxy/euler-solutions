# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

from math import gcd

def solve():
    for m in range(2, 25):
        for n in range(1, m):
            if (m + n) % 2 == 0 or gcd(m, n) != 1:
                continue
            s = 2 * m * (m + n)
            if 1000 % s == 0:
                k = 1000 // s
                a = k * (m * m - n * n)
                b = k * 2 * m * n
                c = k * (m * m + n * n)
                return a * b * c

if __name__ == "__main__":
    print(solve())
