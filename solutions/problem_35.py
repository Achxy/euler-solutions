# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    limit = 1000000
    sieve = [True] * limit
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, limit, i):
                sieve[j] = False

    count = 0
    for n in range(2, limit):
        if not sieve[n]:
            continue
        s = str(n)
        rotations = [int(s[i:] + s[:i]) for i in range(len(s))]
        if all(r < limit and sieve[r] for r in rotations):
            count += 1
    return count

if __name__ == "__main__":
    print(solve())
