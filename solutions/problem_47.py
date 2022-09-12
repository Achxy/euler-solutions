# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    limit = 200000
    factor_count = [0] * limit
    for i in range(2, limit):
        if factor_count[i] == 0:
            for j in range(i, limit, i):
                factor_count[j] += 1
    for i in range(2, limit - 3):
        if (factor_count[i] == 4 and factor_count[i + 1] == 4 and
                factor_count[i + 2] == 4 and factor_count[i + 3] == 4):
            return i

if __name__ == "__main__":
    print(solve())
