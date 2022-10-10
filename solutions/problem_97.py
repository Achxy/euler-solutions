# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    return (28433 * pow(2, 7830457, 10**10) + 1) % 10**10

if __name__ == "__main__":
    print(solve())
