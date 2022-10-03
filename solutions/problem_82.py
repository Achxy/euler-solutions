# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

from . import data

def solve():
    matrix = [[int(x) for x in line.strip().split(',')] for line in data(82).splitlines() if line.strip()]

    n = len(matrix)
    dp = [matrix[i][0] for i in range(n)]

    for j in range(1, n):
        new_dp = [dp[i] + matrix[i][j] for i in range(n)]
        for i in range(1, n):
            new_dp[i] = min(new_dp[i], new_dp[i-1] + matrix[i][j])
        for i in range(n-2, -1, -1):
            new_dp[i] = min(new_dp[i], new_dp[i+1] + matrix[i][j])
        dp = new_dp

    return min(dp)

if __name__ == "__main__":
    print(solve())
