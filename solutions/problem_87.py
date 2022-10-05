# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    limit = 50000000

    def sieve(n):
        is_prime = [False, False] + [True] * (n - 1)
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i*i, n+1, i):
                    is_prime[j] = False
        return [i for i in range(2, n+1) if is_prime[i]]

    primes = sieve(int(limit**0.5) + 1)

    squares = [p*p for p in primes if p*p < limit]
    cubes = [p**3 for p in primes if p**3 < limit]
    fourths = [p**4 for p in primes if p**4 < limit]

    found = set()
    for f in fourths:
        for c in cubes:
            if f + c >= limit:
                break
            for s in squares:
                total = f + c + s
                if total >= limit:
                    break
                found.add(total)

    return len(found)

if __name__ == "__main__":
    print(solve())
