# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    ones = ["", "one", "two", "three", "four", "five", "six", "seven",
            "eight", "nine", "ten", "eleven", "twelve", "thirteen",
            "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty",
            "sixty", "seventy", "eighty", "ninety"]

    def to_words(n):
        if n == 1000:
            return "onethousand"
        if n >= 100:
            w = ones[n // 100] + "hundred"
            if n % 100:
                w += "and" + to_words(n % 100)
            return w
        if n >= 20:
            return tens[n // 10] + ones[n % 10]
        return ones[n]

    return sum(len(to_words(i)) for i in range(1, 1001))

if __name__ == "__main__":
    print(solve())
