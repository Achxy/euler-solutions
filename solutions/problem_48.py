# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    mod = 10 ** 10
    return sum(pow(n, n, mod) for n in range(1, 1001)) % mod

if __name__ == "__main__":
    print(solve())
