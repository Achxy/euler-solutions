# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

from . import data

def solve():
    names = sorted(data(22).replace('"', '').split(','))
    return sum(
        (i + 1) * sum(ord(c) - 64 for c in name)
        for i, name in enumerate(names)
    )

if __name__ == "__main__":
    print(solve())
