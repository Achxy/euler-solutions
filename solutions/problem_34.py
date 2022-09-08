# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

from math import factorial

def solve():
    facts = [factorial(i) for i in range(10)]
    return sum(n for n in range(3, 100000) if n == sum(facts[int(d)] for d in str(n)))

if __name__ == "__main__":
    print(solve())
