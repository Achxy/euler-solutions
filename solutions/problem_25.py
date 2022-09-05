# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

from math import log10, sqrt, ceil

def solve():
    phi = (1 + sqrt(5)) / 2
    return ceil((999 + 0.5 * log10(5)) / log10(phi))

if __name__ == "__main__":
    print(solve())
