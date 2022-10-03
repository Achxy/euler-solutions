# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

from . import data
import heapq

def solve():
    matrix = [[int(x) for x in line.strip().split(',')] for line in data(83).splitlines() if line.strip()]

    n = len(matrix)
    dist = [[float('inf')] * n for _ in range(n)]
    dist[0][0] = matrix[0][0]
    heap = [(matrix[0][0], 0, 0)]

    while heap:
        d, r, c = heapq.heappop(heap)
        if d > dist[r][c]:
            continue
        if r == n-1 and c == n-1:
            return d
        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < n and 0 <= nc < n:
                nd = d + matrix[nr][nc]
                if nd < dist[nr][nc]:
                    dist[nr][nc] = nd
                    heapq.heappush(heap, (nd, nr, nc))

    return dist[n-1][n-1]

if __name__ == "__main__":
    print(solve())
