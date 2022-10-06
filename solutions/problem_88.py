# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    kmax = 12000
    min_prodsum = [2 * kmax + 1] * (kmax + 1)

    def generate(prod, total, factors, start):
        k = prod - total + factors
        if k <= kmax:
            if prod < min_prodsum[k]:
                min_prodsum[k] = prod
            for f in range(start, 2 * kmax // prod + 1):
                generate(prod * f, total + f, factors + 1, f)

    generate(1, 0, 0, 2)

    return sum(set(min_prodsum[2:]))

if __name__ == "__main__":
    print(solve())
