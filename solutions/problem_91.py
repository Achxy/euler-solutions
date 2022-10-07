# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

from math import gcd

def solve():
    n = 50
    count = n * n
    for x in range(0, n + 1):
        for y in range(0, n + 1):
            if x == 0 and y == 0:
                continue
            g = gcd(x, y)
            dy, dx = y // g, x // g
            bounds_pos = []
            if dy > 0: bounds_pos.append(x // dy)
            if dx > 0: bounds_pos.append((n - y) // dx)
            bounds_neg = []
            if dy > 0: bounds_neg.append((n - x) // dy)
            if dx > 0: bounds_neg.append(y // dx)
            count += (min(bounds_pos) if bounds_pos else n)
            count += (min(bounds_neg) if bounds_neg else n)
    return count

if __name__ == "__main__":
    print(solve())
