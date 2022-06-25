# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

from math import prod
from . import data

def solve():
    grid = [[int(x) for x in line.split()] for line in data(11).splitlines()]

    best = 0
    for r in range(20):
        for c in range(20):
            if c + 3 < 20:
                best = max(best, prod(grid[r][c + k] for k in range(4)))
            if r + 3 < 20:
                best = max(best, prod(grid[r + k][c] for k in range(4)))
            if r + 3 < 20 and c + 3 < 20:
                best = max(best, prod(grid[r + k][c + k] for k in range(4)))
            if r + 3 < 20 and c - 3 >= 0:
                best = max(best, prod(grid[r + k][c - k] for k in range(4)))
    return best

if __name__ == "__main__":
    print(solve())
