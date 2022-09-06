# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    n = 500
    return 1 + (16 * n * (n + 1) * (2 * n + 1) // 6) + 2 * n * (n + 1) + 4 * n

if __name__ == "__main__":
    print(solve())
