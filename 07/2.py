from re import findall
from functools import cmp_to_key

HAND_TYPES = {}
CARD_RANKS = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]


def main():
    turns = []

    with open("input.txt", "r") as input:
        line = input.readline()
        while line:
            turns.append([(t[0], int(t[1])) for t in [line.strip("\n").split(" ")]][0])
            line = input.readline()

    turns.sort(key=cmp_to_key(lambda t1, t2: compare_hands(t1[0], t2[0])))

    winnings = 0
    for i in range(len(turns)):
        winnings += turns[i][1] * (i + 1)

    print(winnings)


def get_shape(hand):
    return sorted(
        list(map(list, set([(c, len(findall(c, hand))) for c in hand]))),
        key=lambda c: c[1],
    )


def joker(hand):
    shape = get_shape(hand)

    for i in range(len(shape)):
        if shape[i][0] == "J":
            j = shape.pop(i)

            if shape == []:
                shape.append(["A", 0])

            shape[-1][1] += j[1]
            break

    return list(zip(*shape))[1]


def get_hand_type(hand):
    if hand in HAND_TYPES:
        return HAND_TYPES[hand]

    shape = joker(hand)

    match shape:
        case (5,):
            hand_type = 6
        case (1, 4):
            hand_type = 5
        case (2, 3):
            hand_type = 4
        case (1, 1, 3):
            hand_type = 3
        case (1, 2, 2):
            hand_type = 2
        case (1, 1, 1, 2):
            hand_type = 1
        case (1, 1, 1, 1, 1):
            hand_type = 0

    HAND_TYPES[hand] = hand_type
    return hand_type


def compare_hands(hand1, hand2):
    if get_hand_type(hand1) != get_hand_type(hand2):
        return get_hand_type(hand1) - get_hand_type(hand2)

    for i in range(5):
        if hand1[i] == hand2[i]:
            continue
        else:
            return CARD_RANKS.index(hand1[i]) - CARD_RANKS.index(hand2[i])


if __name__ == "__main__":
    main()
