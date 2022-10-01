# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    def sieve(n):
        is_prime = [False, False] + [True] * (n - 1)
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i*i, n+1, i):
                    is_prime[j] = False
        return [i for i in range(2, n+1) if is_prime[i]]

    primes = sieve(1000)
    target = 5000
    for n in range(2, 1000):
        ways = [0] * (n + 1)
        ways[0] = 1
        for p in primes:
            if p > n:
                break
            for j in range(p, n + 1):
                ways[j] += ways[j - p]
        if ways[n] > target:
            return n

if __name__ == "__main__":
    print(solve())
