# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    target = 200
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    ways = [0] * (target + 1)
    ways[0] = 1
    for coin in coins:
        for i in range(coin, target + 1):
            ways[i] += ways[i - coin]
    return ways[target]

if __name__ == "__main__":
    print(solve())
