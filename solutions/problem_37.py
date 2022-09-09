# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    def is_prime(n):
        if n < 2:
            return False
        if n < 4:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    total = 0
    count = 0
    n = 11
    while count < 11:
        s = str(n)
        truncatable = True
        for i in range(1, len(s)):
            if not is_prime(int(s[i:])) or not is_prime(int(s[:i])):
                truncatable = False
                break
        if truncatable and is_prime(n):
            total += n
            count += 1
        n += 2
    return total

if __name__ == "__main__":
    print(solve())
