# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    x, y = 1, 1
    while True:
        x, y = 3*x + 4*y, 2*x + 3*y
        n = (x + 1) // 2
        b = (y + 1) // 2
        if n > 10**12:
            return b

if __name__ == "__main__":
    print(solve())
