# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    best = 0
    for i in range(999, 99, -1):
        j_start = 999 if i % 11 == 0 else 990
        j_step = 1 if i % 11 == 0 else 11
        for j in range(j_start, 99, -j_step):
            p = i * j
            if p <= best:
                break
            s = str(p)
            if s == s[::-1]:
                best = p
    return best

if __name__ == "__main__":
    print(solve())
