# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    stack = [(1, 3, 1, 2)]
    count = 0
    while stack:
        a1, b1, a2, b2 = stack.pop()
        mb = b1 + b2
        if mb > 12000:
            continue
        count += 1
        stack.append((a1, b1, a1 + a2, mb))
        stack.append((a1 + a2, mb, a2, b2))
    return count

if __name__ == "__main__":
    print(solve())
