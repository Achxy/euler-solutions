# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

from . import data

def solve():
    numbers = [int(line) for line in data(13).splitlines()]
    return int(str(sum(numbers))[:10])

if __name__ == "__main__":
    print(solve())
