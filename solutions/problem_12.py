# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    def ndivisors(n):
        count, d = 1, 2
        while d * d <= n:
            exp = 0
            while n % d == 0:
                n //= d
                exp += 1
            count *= exp + 1
            d += 1
        if n > 1:
            count *= 2
        return count

    n = 1
    dn = ndivisors(1)
    while True:
        n += 1
        dn1 = ndivisors(n + 1)
        if n % 2 == 0:
            total = ndivisors(n // 2) * dn1
        else:
            total = dn * ndivisors((n + 1) // 2)
        if total > 500:
            return n * (n + 1) // 2
        dn = dn1

if __name__ == "__main__":
    print(solve())
