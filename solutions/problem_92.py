# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    max_sq = 567
    to_89 = set()
    for n in range(1, max_sq + 1):
        k = n
        while k != 1 and k != 89:
            k = sum(int(d) ** 2 for d in str(k))
        if k == 89:
            to_89.add(n)
    ways = [0] * (max_sq + 1)
    ways[0] = 1
    for _ in range(7):
        nw = [0] * (max_sq + 1)
        for s in range(max_sq + 1):
            if not ways[s]:
                continue
            for d in range(10):
                ns = s + d * d
                if ns <= max_sq:
                    nw[ns] += ways[s]
        ways = nw
    return sum(ways[s] for s in to_89)

if __name__ == "__main__":
    print(solve())
