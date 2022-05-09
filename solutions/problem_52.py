# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    n = 1
    while True:
        if all(sorted(str(n)) == sorted(str(n * k)) for k in range(2, 7)):
            return n
        n += 1

if __name__ == "__main__":
    print(solve())
