# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

from . import data

def solve():
    def solve_sudoku(grid):
        empty = []
        for r in range(9):
            for c in range(9):
                if grid[r][c] == 0:
                    empty.append((r, c))

        def is_valid(r, c, val):
            for i in range(9):
                if grid[r][i] == val:
                    return False
                if grid[i][c] == val:
                    return False
            br, bc = 3 * (r // 3), 3 * (c // 3)
            for i in range(br, br + 3):
                for j in range(bc, bc + 3):
                    if grid[i][j] == val:
                        return False
            return True

        def backtrack(idx):
            if idx == len(empty):
                return True
            r, c = empty[idx]
            for val in range(1, 10):
                if is_valid(r, c, val):
                    grid[r][c] = val
                    if backtrack(idx + 1):
                        return True
                    grid[r][c] = 0
            return False

        backtrack(0)
        return grid

    lines = [line.strip() for line in data(96).splitlines()]

    total = 0
    i = 0
    while i < len(lines):
        if lines[i].startswith("Grid"):
            grid = []
            for r in range(1, 10):
                grid.append([int(c) for c in lines[i + r]])
            solve_sudoku(grid)
            total += grid[0][0] * 100 + grid[0][1] * 10 + grid[0][2]
            i += 10
        else:
            i += 1

    return total

if __name__ == "__main__":
    print(solve())
