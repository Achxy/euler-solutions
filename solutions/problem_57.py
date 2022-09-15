# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    count = 0
    n, d = 1, 1
    for _ in range(1000):
        n, d = n + 2 * d, n + d
        if len(str(n)) > len(str(d)):
            count += 1
    return count

if __name__ == "__main__":
    print(solve())
