# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    best = 0
    result = 0
    for d in range(2, 1000):
        remainders = {}
        r = 1
        pos = 0
        while r != 0 and r not in remainders:
            remainders[r] = pos
            r = (r * 10) % d
            pos += 1
        if r != 0:
            cycle_len = pos - remainders[r]
            if cycle_len > best:
                best = cycle_len
                result = d
    return result

if __name__ == "__main__":
    print(solve())
