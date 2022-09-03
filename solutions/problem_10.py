# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    limit = 2_000_000
    sieve = [True] * limit
    sieve[0] = sieve[1] = False
    for i in range(2, int(limit ** 0.5) + 1):
        if sieve[i]:
            sieve[i*i::i] = [False] * len(sieve[i*i::i])
    return sum(i for i, v in enumerate(sieve) if v)

if __name__ == "__main__":
    print(solve())
