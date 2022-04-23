# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    a, b, total = 2, 8, 0
    while a <= 4_000_000:
        total += a
        a, b = b, 4 * b + a
    return total

if __name__ == "__main__":
    print(solve())
