# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

from decimal import Decimal, getcontext

def solve():
    getcontext().prec = 110
    perfect = {i*i for i in range(11)}
    total = 0
    for n in range(1, 101):
        if n in perfect:
            continue
        root = Decimal(n).sqrt()
        digits_str = str(root).replace('.', '')[:100]
        total += sum(int(d) for d in digits_str)
    return total

if __name__ == "__main__":
    print(solve())
