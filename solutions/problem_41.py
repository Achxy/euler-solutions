# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

from itertools import permutations

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

    for n in range(7, 0, -1):
        digits = list(range(n, 0, -1))
        for perm in permutations(digits):
            num = int("".join(map(str, perm)))
            if is_prime(num):
                return num

if __name__ == "__main__":
    print(solve())
