# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    mod = 1000000
    p = [1]
    n = 0
    while True:
        n += 1
        px = 0
        k = 1
        while True:
            g1 = k * (3 * k - 1) // 2
            g2 = k * (3 * k + 1) // 2
            if g1 > n and g2 > n:
                break
            sign = (-1) ** (k + 1)
            if g1 <= n:
                px += sign * p[n - g1]
            if g2 <= n:
                px += sign * p[n - g2]
            k += 1
        px %= mod
        p.append(px)
        if px == 0:
            return n

if __name__ == "__main__":
    print(solve())
