# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

from . import data

def _parse_triangle(text):
    return [[int(x) for x in line.split()] for line in text.strip().splitlines()]

def _reform(triangle):
    lrow = triangle[-1]
    triangle.append([max(lrow[i], lrow[i + 1]) + v for i, v in enumerate(triangle[-2])])
    del triangle[-3:-1]

def max_path_sum(triangle):
    while len(triangle) != 1:
        _reform(triangle)
    return triangle[0][0]

def solve():
    triangle = _parse_triangle(data(18))
    return max_path_sum(triangle)

if __name__ == "__main__":
    print(solve())
