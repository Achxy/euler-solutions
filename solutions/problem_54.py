# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

from . import data

def card_value(card):
    values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
              '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    return values[card[0]]

def hand_rank(hand):
    values = sorted([card_value(c) for c in hand], reverse=True)
    suits = [c[1] for c in hand]
    flush = len(set(suits)) == 1
    straight = (values[0] - values[4] == 4 and len(set(values)) == 5)
    if values == [14, 5, 4, 3, 2]:
        straight = True
        values = [5, 4, 3, 2, 1]

    from collections import Counter
    counts = Counter(values)
    groups = sorted(counts.items(), key=lambda x: (x[1], x[0]), reverse=True)
    group_pattern = tuple(g[1] for g in groups)
    ordered = [g[0] for g in groups]

    if straight and flush:
        return (8, values)
    if group_pattern == (4, 1):
        return (7, ordered)
    if group_pattern == (3, 2):
        return (6, ordered)
    if flush:
        return (5, values)
    if straight:
        return (4, values)
    if group_pattern == (3, 1, 1):
        return (3, ordered)
    if group_pattern == (2, 2, 1):
        return (2, ordered)
    if group_pattern == (2, 1, 1, 1):
        return (1, ordered)
    return (0, ordered)

def solve():
    lines = data(54).strip().splitlines()

    wins = 0
    for line in lines:
        cards = line.split()
        hand1 = cards[:5]
        hand2 = cards[5:]
        if hand_rank(hand1) > hand_rank(hand2):
            wins += 1
    return wins

if __name__ == "__main__":
    print(solve())
