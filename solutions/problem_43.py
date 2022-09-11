# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    divisors = [17, 13, 11, 7, 5, 3, 2]
    candidates = [s for i in range(17, 1000, 17) if len(set(s := str(i).zfill(3))) == 3]

    for div in divisors[1:]:
        new_candidates = []
        for cand in candidates:
            for d in range(10):
                sd = str(d)
                if sd in cand:
                    continue
                prefix = sd + cand
                if int(prefix[:3]) % div == 0:
                    new_candidates.append(prefix)
        candidates = new_candidates

    total = 0
    for cand in candidates:
        remaining = set("0123456789") - set(cand)
        for d in remaining:
            num = d + cand
            if num[0] != '0':
                total += int(num)
    return total

if __name__ == "__main__":
    print(solve())
