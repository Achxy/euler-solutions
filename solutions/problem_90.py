# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

from itertools import combinations

def solve():
    squares = [(0,1),(0,4),(0,9),(1,6),(2,5),(3,6),(4,9),(6,4),(8,1)]

    def can_display(c1, c2):
        s1 = set(c1)
        s2 = set(c2)
        if 6 in s1: s1.add(9)
        if 9 in s1: s1.add(6)
        if 6 in s2: s2.add(9)
        if 9 in s2: s2.add(6)
        for a, b in squares:
            if not ((a in s1 and b in s2) or (a in s2 and b in s1)):
                return False
        return True

    cubes = list(combinations(range(10), 6))
    count = 0
    for i in range(len(cubes)):
        for j in range(i, len(cubes)):
            if can_display(cubes[i], cubes[j]):
                count += 1
    return count

if __name__ == "__main__":
    print(solve())
