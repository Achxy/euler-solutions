# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

from math import gcd

def solve():
    num_prod = 1
    den_prod = 1
    for d in range(10, 100):
        for n in range(10, d):
            n1, n2 = n // 10, n % 10
            d1, d2 = d // 10, d % 10
            if n2 == 0 and d2 == 0:
                continue
            if n2 == d1 and d2 != 0 and n * d2 == d * n1:
                num_prod *= n1
                den_prod *= d2
    return den_prod // gcd(num_prod, den_prod)

if __name__ == "__main__":
    print(solve())
