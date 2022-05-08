# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    def is_pentagonal(n):
        val = (1 + (1 + 24 * n) ** 0.5) / 6
        return val == int(val) and val > 0

    pentagonals = [n * (3 * n - 1) // 2 for n in range(1, 3000)]
    for i in range(1, len(pentagonals)):
        for j in range(i - 1, -1, -1):
            s = pentagonals[i] + pentagonals[j]
            d = pentagonals[i] - pentagonals[j]
            if is_pentagonal(s) and is_pentagonal(d):
                return d

if __name__ == "__main__":
    print(solve())
