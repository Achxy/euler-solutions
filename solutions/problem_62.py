# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

from collections import defaultdict

def solve():
    cubes = defaultdict(list)
    n = 1
    while True:
        c = n ** 3
        key = ''.join(sorted(str(c)))
        cubes[key].append(c)
        if len(cubes[key]) == 5:
            return min(cubes[key])
        n += 1

if __name__ == "__main__":
    print(solve())
