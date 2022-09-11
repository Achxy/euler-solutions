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

    n = 9
    while True:
        if not is_prime(n) and n % 2 == 1:
            found = False
            for i in range(1, n):
                sq = i * i * 2
                if sq >= n:
                    break
                if is_prime(n - sq):
                    found = True
                    break
            if not found:
                return n
        n += 2

if __name__ == "__main__":
    print(solve())
