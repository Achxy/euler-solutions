# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

from math import log

def solve():
    n = 10001
    limit = int(n * (log(n) + log(log(n)))) + 100
    sieve = bytearray(b'\x01') * limit
    sieve[0] = sieve[1] = 0
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            sieve[i*i::i] = bytearray(len(sieve[i*i::i]))
    count = 0
    for i in range(2, limit):
        if sieve[i]:
            count += 1
            if count == n:
                return i

if __name__ == "__main__":
    print(solve())
