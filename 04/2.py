from functools import reduce


def main():
    cards = []
    with open("input.txt", "r") as input:
        line = input.readline()
        while line:
            line = line.strip("\n")[10:].split(" | ")
            for i in range(2):
                # turn the arrays of strings into arrays of ints
                line[i] = [int(n) for n in line[i].split(" ") if n != ""]
            cards.append([1] + line)  # [number of copies, winning numbers, my numbers]
            line = input.readline()

    # for every card, do the same thing as in part 1 and calculate how many winning
    # numbers it has (match_count). then for `match_count` cards beneath the current
    # one, add as many copies of them as there are of the current card, because that
    # is how many times they will be incremented.
    for i in range(len(cards)):
        winning_numbers = cards[i][1]
        my_numbers = cards[i][2]
        match_count = 0

        for num in my_numbers:
            if num in winning_numbers:
                match_count += 1

        for j in range(i + 1, i + 1 + match_count):
            cards[j][0] += cards[i][0]

    # add up the number of copies of each card
    # since the reducer function needs all arguments to be of the same type,
    # store the accumulator in a list and take it out later
    total_cards = reduce(lambda card1, card2: [card1[0] + card2[0]], cards, [0])[0]
    print(total_cards)


if __name__ == "__main__":
    main()
