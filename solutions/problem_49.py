# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    sieve = [True] * 10000
    sieve[0] = sieve[1] = False
    for i in range(2, 100):
        if sieve[i]:
            for j in range(i * i, 10000, i):
                sieve[j] = False

    for a in range(1000, 10000):
        if not sieve[a] or a == 1487:
            continue
        for d in range(1, (10000 - a) // 2 + 1):
            b = a + d
            c = a + 2 * d
            if c >= 10000:
                break
            if sieve[b] and sieve[c]:
                if sorted(str(a)) == sorted(str(b)) == sorted(str(c)):
                    return int(str(a) + str(b) + str(c))

if __name__ == "__main__":
    print(solve())
