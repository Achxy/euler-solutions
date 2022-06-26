# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    result = 1
    for i in range(20):
        result = result * (40 - i) // (i + 1)
    return result

if __name__ == "__main__":
    print(solve())
