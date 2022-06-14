# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

from math import prod
from . import data

def solve():
    digits = "".join(data(8).split())
    return max(
        prod(int(c) for c in digits[i:i + 13])
        for i in range(len(digits) - 12)
    )

if __name__ == "__main__":
    print(solve())
