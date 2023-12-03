from re import findall, split, search


def main():
    with open("input.txt", "r") as input:
        lines = input.readlines()

    sum = 0
    for line in lines:
        game_id, sets = parse_input(line.strip("\n"))

        if validate_game(sets):
            sum += game_id

    print(sum)


def validate_game(sets) -> bool:
    for set in sets:
        if set["blue"] > 14 or set["green"] > 13 or set["red"] > 12:
            return False
    return True


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
