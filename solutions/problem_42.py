# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

from . import data

def solve():
    words = [w.strip('"') for w in data(42).split(",")]
    triangles = set(n * (n + 1) // 2 for n in range(1, 100))
    count = 0
    for word in words:
        val = sum(ord(c) - 64 for c in word)
        if val in triangles:
            count += 1
    return count

if __name__ == "__main__":
    print(solve())
