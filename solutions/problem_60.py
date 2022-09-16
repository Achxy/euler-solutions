# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    def sieve(limit):
        s = [True] * limit
        s[0] = s[1] = False
        for i in range(2, int(limit ** 0.5) + 1):
            if s[i]:
                for j in range(i * i, limit, i):
                    s[j] = False
        return s

    def is_prime(n):
        if n < 2:
            return False
        if n < prime_limit:
            return prime_sieve[n]
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def pair_check(a, b):
        return is_prime(int(str(a) + str(b))) and is_prime(int(str(b) + str(a)))

    prime_limit = 100000
    prime_sieve = sieve(prime_limit)
    primes = [i for i in range(2, prime_limit) if prime_sieve[i]]

    pair_cache = {}
    def pairs(a, b):
        key = (a, b)
        if key not in pair_cache:
            pair_cache[key] = pair_check(a, b)
        return pair_cache[key]

    best = float('inf')
    for i in range(len(primes)):
        a = primes[i]
        if 5 * a >= best:
            break
        for j in range(i + 1, len(primes)):
            b = primes[j]
            if a + 4 * b >= best:
                break
            if not pairs(a, b):
                continue
            for k in range(j + 1, len(primes)):
                c = primes[k]
                if a + b + 3 * c >= best:
                    break
                if not pairs(a, c) or not pairs(b, c):
                    continue
                for l in range(k + 1, len(primes)):
                    d = primes[l]
                    if a + b + c + 2 * d >= best:
                        break
                    if not pairs(a, d) or not pairs(b, d) or not pairs(c, d):
                        continue
                    for m in range(l + 1, len(primes)):
                        e = primes[m]
                        s = a + b + c + d + e
                        if s >= best:
                            break
                        if not pairs(a, e) or not pairs(b, e) or not pairs(c, e) or not pairs(d, e):
                            continue
                        best = s
    return best

if __name__ == "__main__":
    print(solve())
