# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    limit = 1000001
    phi = list(range(limit))
    for i in range(2, limit):
        if phi[i] == i:
            for j in range(i, limit, i):
                phi[j] = phi[j] // i * (i - 1)
    return sum(phi[2:])

if __name__ == "__main__":
    print(solve())
