# Copyright (c) 2022 Achyuth Jayadevan <achyuth@jayadevan.in>
# SPDX-License-Identifier: MIT

import random

def solve():
    random.seed(12345)

    GO, JAIL, G2J = 0, 10, 30
    CC_SQUARES = {2, 17, 33}
    CH_SQUARES = {7, 22, 36}

    def next_railway(pos):
        for r in [5, 15, 25, 35]:
            if pos < r:
                return r
        return 5

    def next_utility(pos):
        for u in [12, 28]:
            if pos < u:
                return u
        return 12

    cc_deck = list(range(16))
    ch_deck = list(range(16))
    random.shuffle(cc_deck)
    random.shuffle(ch_deck)
    cc_i = [0]
    ch_i = [0]

    def draw_cc():
        card = cc_deck[cc_i[0]]
        cc_i[0] = (cc_i[0] + 1) % 16
        return card

    def draw_ch():
        card = ch_deck[ch_i[0]]
        ch_i[0] = (ch_i[0] + 1) % 16
        return card

    def apply_landing(pos):
        if pos == G2J:
            return JAIL
        if pos in CC_SQUARES:
            card = draw_cc()
            if card == 0:
                return GO
            if card == 1:
                return JAIL
            return pos
        if pos in CH_SQUARES:
            card = draw_ch()
            if card == 0:
                return GO
            if card == 1:
                return JAIL
            if card == 2:
                return 11
            if card == 3:
                return 24
            if card == 4:
                return 39
            if card == 5:
                return 5
            if card in (6, 7):
                return next_railway(pos)
            if card == 8:
                return next_utility(pos)
            if card == 9:
                new_pos = (pos - 3) % 40
                if new_pos == G2J:
                    return JAIL
                if new_pos in CC_SQUARES:
                    cc_card = draw_cc()
                    if cc_card == 0:
                        return GO
                    if cc_card == 1:
                        return JAIL
                    return new_pos
                return new_pos
            return pos
        return pos

    sides = 4
    visits = [0] * 40
    pos = 0
    doubles_count = 0
    total = 6000000

    for _ in range(total):
        d1 = random.randint(1, sides)
        d2 = random.randint(1, sides)

        if d1 == d2:
            doubles_count += 1
        else:
            doubles_count = 0

        if doubles_count >= 3:
            pos = JAIL
            doubles_count = 0
            visits[pos] += 1
            continue

        pos = (pos + d1 + d2) % 40
        pos = apply_landing(pos)
        visits[pos] += 1

    indexed = sorted(range(40), key=lambda x: -visits[x])
    return int(f"{indexed[0]:02d}{indexed[1]:02d}{indexed[2]:02d}")

if __name__ == "__main__":
    print(solve())
