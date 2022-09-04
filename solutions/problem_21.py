# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    limit = 10000
    d = [0] * limit
    for i in range(1, limit):
        for j in range(2 * i, limit, i):
            d[j] += i
    return sum(a for a in range(2, limit) if d[a] < limit and d[a] != a and d[d[a]] == a)

if __name__ == "__main__":
    print(solve())
