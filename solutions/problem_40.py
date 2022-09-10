# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    def champernowne_digit(pos):
        digits, start, count = 1, 1, 9
        while pos > digits * count:
            pos -= digits * count
            digits += 1
            count *= 10
            start *= 10
        num = start + (pos - 1) // digits
        return int(str(num)[(pos - 1) % digits])

    result = 1
    for p in (1, 10, 100, 1000, 10000, 100000, 1000000):
        result *= champernowne_digit(p)
    return result

if __name__ == "__main__":
    print(solve())
