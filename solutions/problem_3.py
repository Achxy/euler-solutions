# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    n = 600851475143
    d = 2
    while d * d <= n:
        while n % d == 0:
            n //= d
        d += 1
    return n

if __name__ == "__main__":
    print(solve())
