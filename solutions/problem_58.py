# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    def is_prime(n):
        if n < 2:
            return False
        if n < 4:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    primes = 0
    total = 1
    side = 1
    while True:
        side += 2
        for i in range(4):
            corner = side * side - i * (side - 1)
            if is_prime(corner):
                primes += 1
        total += 4
        if primes * 10 < total:
            return side

if __name__ == "__main__":
    print(solve())
