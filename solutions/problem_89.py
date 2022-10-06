# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

from . import data

def solve():
    roman_values = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]

    def roman_to_int(s):
        vals = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        total = 0
        prev = 0
        for ch in reversed(s):
            v = vals[ch]
            if v < prev:
                total -= v
            else:
                total += v
            prev = v
        return total

    def int_to_roman(n):
        result = []
        for val, sym in roman_values:
            while n >= val:
                result.append(sym)
                n -= val
        return ''.join(result)

    lines = [line.strip() for line in data(89).splitlines() if line.strip()]

    saved = 0
    for line in lines:
        val = roman_to_int(line)
        minimal = int_to_roman(val)
        saved += len(line) - len(minimal)

    return saved

if __name__ == "__main__":
    print(solve())
