# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    count = 0
    for base in range(1, 10):
        n = 1
        while len(str(base ** n)) == n:
            count += 1
            n += 1
    return count

if __name__ == "__main__":
    print(solve())
