# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    largest = 0
    for a in range(1, 100000):
        s = ""
        for n in range(1, 10):
            s += str(a * n)
            if len(s) >= 9:
                break
        if len(s) == 9 and set(s) == set("123456789"):
            largest = max(largest, int(s))
    return largest

if __name__ == "__main__":
    print(solve())
