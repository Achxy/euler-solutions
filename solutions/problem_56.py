# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    best = 0
    for a in range(1, 100):
        for b in range(1, 100):
            s = sum(int(d) for d in str(a ** b))
            if s > best:
                best = s
    return best

if __name__ == "__main__":
    print(solve())
