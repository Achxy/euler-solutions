# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    limit = 10 ** 7
    sieve = bytearray(b'\x01') * 5000
    sieve[0] = sieve[1] = 0
    for i in range(2, int(5000**0.5) + 1):
        if sieve[i]:
            sieve[i*i::i] = bytearray(len(sieve[i*i::i]))
    primes = [i for i in range(2, 5000) if sieve[i]]
    best_ratio, best_n = float('inf'), 0
    for i in range(len(primes)):
        for j in range(i, len(primes)):
            n = primes[i] * primes[j]
            if n >= limit:
                break
            phi = (primes[i] - 1) * (primes[j] - 1)
            if sorted(str(n)) == sorted(str(phi)):
                ratio = n / phi
                if ratio < best_ratio:
                    best_ratio, best_n = ratio, n
    return best_n

if __name__ == "__main__":
    print(solve())
