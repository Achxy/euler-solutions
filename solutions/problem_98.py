# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

from . import data
from itertools import permutations
from math import isqrt

def solve():
    words = data(98).replace('"', '').split(',')

    anagram_groups = {}
    for word in words:
        key = ''.join(sorted(word))
        if key not in anagram_groups:
            anagram_groups[key] = []
        anagram_groups[key].append(word)

    anagram_pairs = []
    for key, group in anagram_groups.items():
        if len(group) >= 2:
            for i in range(len(group)):
                for j in range(i + 1, len(group)):
                    anagram_pairs.append((group[i], group[j]))

    best = 0

    for w1, w2 in anagram_pairs:
        unique_chars = list(set(w1))
        n_digits = len(str(10 ** (len(w1) - 1)))  # min digits
        lo = isqrt(10 ** (len(w1) - 1))
        if lo * lo < 10 ** (len(w1) - 1):
            lo += 1
        hi = isqrt(10 ** len(w1) - 1)

        for sq in range(lo, hi + 1):
            s = str(sq * sq)
            if len(s) != len(w1):
                continue
            char_to_digit = {}
            digit_to_char = {}
            valid = True
            for ch, d in zip(w1, s):
                if ch in char_to_digit:
                    if char_to_digit[ch] != d:
                        valid = False
                        break
                else:
                    if d in digit_to_char:
                        if digit_to_char[d] != ch:
                            valid = False
                            break
                    char_to_digit[ch] = d
                    digit_to_char[d] = ch
            if not valid:
                continue
            s2 = ''.join(char_to_digit[ch] for ch in w2)
            if s2[0] == '0':
                continue
            n2 = int(s2)
            r = isqrt(n2)
            if r * r == n2:
                best = max(best, sq * sq, n2)

    return best

if __name__ == "__main__":
    print(solve())
