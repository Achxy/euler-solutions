# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

def solve():
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = 1
    count = 0
    for year in range(1901, 2001):
        for month in range(12):
            if day == 6:
                count += 1
            m_days = days_in_month[month]
            if month == 1 and (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
                m_days = 29
            day = (day + m_days) % 7
    return count

if __name__ == "__main__":
    print(solve())
