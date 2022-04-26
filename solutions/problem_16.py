# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    return sum(int(d) for d in str(2 ** 1000))

if __name__ == "__main__":
    print(solve())
