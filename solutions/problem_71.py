# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    best_n = 0
    best_d = 1
    for d in range(2, 1000001):
        n = (3 * d - 1) // 7
        if n * best_d > best_n * d:
            best_n = n
            best_d = d
    return best_n

if __name__ == "__main__":
    print(solve())
