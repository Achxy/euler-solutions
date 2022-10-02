# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

from . import data
from collections import defaultdict

def solve():
    attempts = [line.strip() for line in data(79).splitlines() if line.strip()]

    edges = set()
    digits = set()
    for attempt in attempts:
        for i in range(len(attempt)):
            digits.add(attempt[i])
            for j in range(i + 1, len(attempt)):
                edges.add((attempt[i], attempt[j]))

    adj = defaultdict(set)
    indeg = defaultdict(int)
    for d in digits:
        indeg[d] = 0
    for a, b in edges:
        if b not in adj[a]:
            adj[a].add(b)
            indeg[b] += 1

    queue = [d for d in digits if indeg[d] == 0]
    queue.sort()
    result = []
    while queue:
        node = queue.pop(0)
        result.append(node)
        for neighbor in sorted(adj[node]):
            indeg[neighbor] -= 1
            if indeg[neighbor] == 0:
                queue.append(neighbor)
        queue.sort()

    return int(''.join(result))

if __name__ == "__main__":
    print(solve())
