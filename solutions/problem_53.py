# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    count = 0
    for n in range(1, 101):
        c = 1
        for r in range(1, n + 1):
            c = c * (n - r + 1) // r
            if c > 1_000_000:
                count += n + 1 - 2 * r
                break
    return count

if __name__ == "__main__":
    print(solve())
