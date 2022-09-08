# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    products = set()
    for a in range(2, 10):
        for b in range(1234, 9877):
            p = a * b
            s = f"{a}{b}{p}"
            if len(s) > 9:
                break
            if len(s) == 9 and len(set(s)) == 9 and '0' not in s:
                products.add(p)
    for a in range(12, 99):
        for b in range(123, 988):
            p = a * b
            s = f"{a}{b}{p}"
            if len(s) > 9:
                break
            if len(s) == 9 and len(set(s)) == 9 and '0' not in s:
                products.add(p)
    return sum(products)

if __name__ == "__main__":
    print(solve())
