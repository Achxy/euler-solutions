# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    limit = 1_000_000
    sieve = bytearray(b'\x01') * limit
    sieve[0] = sieve[1] = 0
    for i in range(2, int(limit**0.5) + 1):
        if sieve[i]:
            sieve[i*i::i] = bytearray(len(sieve[i*i::i]))
    primes = [i for i in range(2, limit) if sieve[i]]
    prime_set = set(primes)
    prefix = [0]
    for p in primes:
        prefix.append(prefix[-1] + p)
    for length in range(len(prefix) - 1, 0, -1):
        for start in range(len(prefix) - length):
            s = prefix[start + length] - prefix[start]
            if s >= limit:
                break
            if s in prime_set:
                return s

if __name__ == "__main__":
    print(solve())
