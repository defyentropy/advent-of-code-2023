from re import findall, split


def main():
    with open("input.txt", "r") as input:
        lines = input.readlines()

    sum = 0
    for line in lines:
        game_id, sets = parse_input(line.strip("\n"))
        sum += power(get_minimum_set(sets))

    print(sum)


def get_minimum_set(sets):
    minimum = {"blue": 0, "green": 0, "red": 0}

    for set in sets:
        for color in set:
            if set[color] > minimum[color]:
                minimum[color] = set[color]

    return minimum


def power(set):
    p = 1
    for color in set:
        p *= set[color]
    return p


def parse_input(line: str) -> tuple[int, list[dict]]:
    game_id, game_string = split(": ", line)

    # get game id
    game_id = int(findall("[0-9]+", game_id)[0])

    # get game data
    sets = []
    for set in split("; ", game_string):
        colors = {}
        set = split(", ", set)

        for count in set:
            count = split(" ", count)
            colors[count[1]] = int(count[0])

        if not colors.get("blue"):
            colors["blue"] = 0
        if not colors.get("green"):
            colors["green"] = 0
        if not colors.get("red"):
            colors["red"] = 0

        sets.append(colors)

    return (game_id, sets)


if __name__ == "__main__":
    main()
