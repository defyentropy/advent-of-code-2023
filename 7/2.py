from re import findall
from functools import cmp_to_key

HAND_TYPES = {}
CARD_RANKS = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]


def main():
    turns = []

    with open("input.txt", "r") as input:
        line = input.readline()
        while line:
            turns.append([[t[0], int(t[1])] for t in [line.strip("\n").split(" ")]][0])
            line = input.readline()

    turns.sort(key=cmp_to_key(compare_hands))

    winnings = 0
    for i in range(len(turns)):
        winnings += turns[i][1] * (i + 1)

    print(winnings)


def get_hand_type(turn):
    hand = turn[0]

    if hand in HAND_TYPES:
        return HAND_TYPES[hand]

    shape = list(
        filter(
            lambda s: s[0] != "J",
            sorted([(c, len(findall(c, hand))) for c in hand], key=lambda c: c[1]),
        )
    )

    if shape == []:
        shape = [("A", 5)]

    hand = hand.replace("J", shape[-1][0])

    print(hand)

    cards = set(hand)
    hand_type = None

    if len(cards) == 1:
        hand_type = 6  # five of a kind
    elif len(cards) == 2:
        shape = sorted([len(findall(c, hand)) for c in cards])

        if shape == [1, 4]:
            hand_type = 5  # four of a kind
        else:
            hand_type = 4  # full house
    elif len(cards) == 3:
        shape = sorted([len(findall(c, hand)) for c in cards])

        if shape == [1, 1, 3]:
            hand_type = 3  # 3 of a kind
        else:
            hand_type = 2  # two pair
    elif len(cards) == 4:
        hand_type = 1  # one pair
    else:
        hand_type = 0  # high card

    HAND_TYPES[hand] = hand_type
    return hand_type


def compare_hands(turn1, turn2):
    hand_type1 = get_hand_type(turn1)
    hand_type2 = get_hand_type(turn2)

    if hand_type1 != hand_type2:
        return hand_type1 - hand_type2

    for i in range(5):
        if turn1[0][i] == turn2[0][i]:
            continue
        elif CARD_RANKS.index(turn1[0][i]) > CARD_RANKS.index(turn2[0][i]):
            return 1
        else:
            return -1


if __name__ == "__main__":
    main()
