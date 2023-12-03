def main():
    cards = []
    with open("input.txt", "r") as input:
        line = input.readline()
        while line:
            line = line.strip("\n")[10:].split(" | ")
            # turn the arrays of strings into arrays of ints
            for i in range(2):
                line[i] = [int(n) for n in line[i].split(" ") if n != ""]
            cards.append(line)
            line = input.readline()

    # for each number from the card, check if it is winning
    # and count how many are winning per card. raise 2 to that
    # number - 1, and add these points to the sum
    points = 0

    for card in cards:
        winning_numbers = card[0]
        my_numbers = card[1]
        match_count = 0

        for num in my_numbers:
            if num in winning_numbers:
                match_count += 1

        points += 2 ** (match_count - 1) if match_count > 0 else 0

    print(points)


if __name__ == "__main__":
    main()
