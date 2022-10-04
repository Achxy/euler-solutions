# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    target = 2000000
    best_diff = float('inf')
    best_area = 0
    for w in range(1, 2001):
        for h in range(1, w + 1):
            count = w * (w + 1) * h * (h + 1) // 4
            diff = abs(count - target)
            if diff < best_diff:
                best_diff = diff
                best_area = w * h
            if count > target:
                break
    return best_area

if __name__ == "__main__":
    print(solve())
