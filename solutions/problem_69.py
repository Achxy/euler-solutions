# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    limit = 1000000
    result = 1
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    for p in primes:
        if result * p > limit:
            break
        result *= p
    return result

if __name__ == "__main__":
    print(solve())
