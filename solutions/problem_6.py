# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    n = 100
    sum_sq = n * (n + 1) * (2 * n + 1) // 6
    sq_sum = (n * (n + 1) // 2) ** 2
    return sq_sum - sum_sq

if __name__ == "__main__":
    print(solve())
