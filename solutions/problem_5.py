# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

from math import log

def solve():
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    result = 1
    for p in primes:
        result *= p ** int(log(20) / log(p))
    return result

if __name__ == "__main__":
    print(solve())
