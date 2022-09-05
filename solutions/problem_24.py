# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

from math import factorial

def solve():
    digits = list(range(10))
    result = []
    remaining = 1_000_000 - 1
    for i in range(10, 0, -1):
        f = factorial(i - 1)
        idx, remaining = divmod(remaining, f)
        result.append(digits.pop(idx))
    return int(''.join(map(str, result)))

if __name__ == "__main__":
    print(solve())
