# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

from .problem_18 import _parse_triangle, max_path_sum
from . import data

def solve():
    triangle = _parse_triangle(data(67))
    return max_path_sum(triangle)

if __name__ == "__main__":
    print(solve())
