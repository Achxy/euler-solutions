# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

from . import data

def solve():
    matrix = [[int(x) for x in line.strip().split(',')] for line in data(81).splitlines() if line.strip()]

    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                matrix[i][j] += matrix[i][j-1]
            elif j == 0:
                matrix[i][j] += matrix[i-1][j]
            else:
                matrix[i][j] += min(matrix[i-1][j], matrix[i][j-1])
    return matrix[n-1][n-1]

if __name__ == "__main__":
    print(solve())
