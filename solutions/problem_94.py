# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    limit = 10**9
    total = 0
    x, y = 2, 0

    while True:
        x, y = 2*x + 3*y, x + 2*y
        if (x + 1) % 3 == 0:
            a = (x + 1) // 3
            if a > 1:
                p = 3 * a + 1
                if p <= limit:
                    total += p
        if (x - 1) % 3 == 0:
            a = (x - 1) // 3
            if a > 1:
                p = 3 * a - 1
                if p <= limit:
                    total += p

        if x > 3 * limit:
            break

    return total

if __name__ == "__main__":
    print(solve())
