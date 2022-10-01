# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    target = 100
    ways = [0] * (target + 1)
    ways[0] = 1
    for i in range(1, target):
        for j in range(i, target + 1):
            ways[j] += ways[j - i]
    return ways[target]

if __name__ == "__main__":
    print(solve())
