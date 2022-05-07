# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    total = 0
    for i in range(1, 10):
        b = bin(i)[2:]
        if b == b[::-1]:
            total += i
    for i in range(1, 10):
        n = 11 * i
        b = bin(n)[2:]
        if b == b[::-1]:
            total += n
    for a in range(1, 10):
        for b in range(10):
            n = 100 * a + 10 * b + a
            s = bin(n)[2:]
            if s == s[::-1]:
                total += n
    for a in range(1, 10):
        for b in range(10):
            n = 1001 * a + 110 * b
            s = bin(n)[2:]
            if s == s[::-1]:
                total += n
    for a in range(1, 10):
        for b in range(10):
            for c in range(10):
                n = 10001 * a + 1010 * b + 100 * c
                s = bin(n)[2:]
                if s == s[::-1]:
                    total += n
    for a in range(1, 10):
        for b in range(10):
            for c in range(10):
                n = 100001 * a + 10010 * b + 1100 * c
                s = bin(n)[2:]
                if s == s[::-1]:
                    total += n
    return total

if __name__ == "__main__":
    print(solve())
