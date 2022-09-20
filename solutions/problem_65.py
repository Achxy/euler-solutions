# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    def e_cf(n):
        if n == 0:
            return 2
        if n % 3 == 2:
            return 2 * (n // 3 + 1)
        return 1

    n, d = 1, 0
    for i in range(99, -1, -1):
        n, d = d + n * e_cf(i), n
    return sum(int(c) for c in str(n))

if __name__ == "__main__":
    print(solve())
