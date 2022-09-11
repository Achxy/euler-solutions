# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    def is_pentagonal(n):
        val = (1 + (1 + 24 * n) ** 0.5) / 6
        return val == int(val) and val > 0

    n = 144
    while True:
        h = n * (2 * n - 1)
        if is_pentagonal(h):
            return h
        n += 1

if __name__ == "__main__":
    print(solve())
