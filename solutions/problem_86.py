# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

from math import isqrt

def solve():
    target = 1000000
    count = 0
    M = 0
    while count <= target:
        M += 1
        for jk in range(2, 2 * M + 1):
            d = M * M + jk * jk
            sqrt_d = isqrt(d)
            if sqrt_d * sqrt_d == d:
                if jk <= M:
                    count += jk // 2
                else:
                    count += M - (jk - 1) // 2
    return M

if __name__ == "__main__":
    print(solve())
