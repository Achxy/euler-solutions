# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

from . import data
from math import log

def solve():
    lines = [line.strip() for line in data(99).splitlines() if line.strip()]

    best_val = 0
    best_line = 0
    for i, line in enumerate(lines):
        base, exp = line.split(',')
        val = int(exp) * log(int(base))
        if val > best_val:
            best_val = val
            best_line = i + 1

    return best_line

if __name__ == "__main__":
    print(solve())
