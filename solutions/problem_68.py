# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

from itertools import permutations

def solve():
    best = ""
    for perm in permutations(range(1, 11)):
        outer = [perm[0], perm[1], perm[2], perm[3], perm[4]]
        inner = [perm[5], perm[6], perm[7], perm[8], perm[9]]
        lines = []
        target = outer[0] + inner[0] + inner[1]
        valid = True
        for i in range(5):
            s = outer[i] + inner[i] + inner[(i + 1) % 5]
            if s != target:
                valid = False
                break
            lines.append((outer[i], inner[i], inner[(i + 1) % 5]))
        if not valid:
            continue
        start = min(range(5), key=lambda i: lines[i][0])
        ordered = lines[start:] + lines[:start]
        s = ''.join(str(x) for line in ordered for x in line)
        if len(s) == 16 and s > best:
            best = s
    return int(best)

if __name__ == "__main__":
    print(solve())
