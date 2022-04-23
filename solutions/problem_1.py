# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    def sum_mults(n, k):
        m = (n - 1) // k
        return k * m * (m + 1) // 2
    return sum_mults(1000, 3) + sum_mults(1000, 5) - sum_mults(1000, 15)

if __name__ == "__main__":
    print(solve())
