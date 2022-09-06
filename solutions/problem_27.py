# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    def sieve(n):
        s = bytearray(b'\x01') * n
        s[0] = s[1] = 0
        for i in range(2, int(n**0.5) + 1):
            if s[i]:
                s[i*i::i] = bytearray(len(s[i*i::i]))
        return s

    is_prime = sieve(100000)
    primes_under_1000 = [p for p in range(2, 1000) if is_prime[p]]

    best, result = 0, 0
    for b in primes_under_1000:
        for a in range(-999, 1000, 2):
            n = 0
            while True:
                val = n * n + a * n + b
                if val < 2 or not is_prime[val]:
                    break
                n += 1
            if n > best:
                best, result = n, a * b
    return result

if __name__ == "__main__":
    print(solve())
