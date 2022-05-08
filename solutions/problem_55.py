# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    count = 0
    for n in range(10, 10000):
        val = n
        is_lychrel = True
        for _ in range(50):
            val = val + int(str(val)[::-1])
            if str(val) == str(val)[::-1]:
                is_lychrel = False
                break
        if is_lychrel:
            count += 1
    return count

if __name__ == "__main__":
    print(solve())
