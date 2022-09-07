# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    total = 0
    for n in range(2, 999999):
        if n == sum(int(d) ** 5 for d in str(n)):
            total += n
    return total

if __name__ == "__main__":
    print(solve())
