# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    return len({a ** b for a in range(2, 101) for b in range(2, 101)})

if __name__ == "__main__":
    print(solve())
