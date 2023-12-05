def main():
    seeds, maps = parse_input("input.txt")

    locations = []
    for seed in seeds:
        locations.append(get_location(seed, maps))
    print(sorted(locations)[0])


def get_location(seed, maps):
    for parameter_map in maps:
        seed = check_map(seed, parameter_map)
    return seed


def check_map(idx, parameter_map):
    for map_range in parameter_map:
        if map_range[1] <= idx < map_range[1] + map_range[2]:
            return map_range[0] + idx - map_range[1]
    return idx


def parse_input(file_name):
    with open(file_name, "r") as input:
        seeds = [int(seed) for seed in input.readline().strip("\n")[7:].split(" ")]
        input.readline()

        maps = []
        this_map = []
        line = input.readline()
        while line:
            if line[0].isalpha():
                pass
            elif line == "\n":
                maps.append(this_map)
                this_map = []
            else:
                this_map.append([int(num) for num in line.strip("\n").split(" ")])

            line = input.readline()
        maps.append(this_map)

    return seeds, maps


if __name__ == "__main__":
    main()
