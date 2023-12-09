from re import findall


def main():
    with open("input.txt", "r") as input:
        directions = input.readline().strip("\n")
        input.readline()

        network = {}
        line = input.readline()
        while line:
            locations = findall("\w\w\w", line)
            network[locations[0]] = {"L": locations[1], "R": locations[2]}
            line = input.readline()

    steps = 0
    LEN_DIRECTIONS = len(directions)
    pos = "AAA"

    while pos != "ZZZ":
        pos = network[pos][directions[steps % LEN_DIRECTIONS]]
        steps += 1

    print(steps)


if __name__ == "__main__":
    main()
