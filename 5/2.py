def main():
    seeds, maps = parse_input("input.txt")

    count = 0
    # print(seeds)
    for parameter_map in maps:
        for i in range(len(seeds)):
            seeds.extend(get_new_ranges(seeds.pop(0), parameter_map))
        # print(seeds)
        print(f"map {count} completed")
        count += 1

    print(sorted(seeds, key=lambda r: r[0])[0][0])


def get_new_ranges(seed_range, parameter_map):
    new_ranges = []
    start, length = seed_range
    new_start, new_length = check_map(start, length, parameter_map)
    while new_length < length:
        new_ranges.append([new_start, new_length])
        start += new_length
        length -= new_length
        new_start, new_length = check_map(start, length, parameter_map)

    new_ranges.append([new_start, length])
    return new_ranges


def check_map(idx, source_length, parameter_map):
    for dest_start, source_start, length in parameter_map:
        if source_start <= idx < source_start + length:
            return [dest_start + idx - source_start, source_start + length - idx]

    for dest_start, source_start, length in parameter_map:
        if idx < source_start:
            return [idx, source_start]

    return [idx, source_length]


def fill_map_set(map_set):
    if map_set[0][1] != 0:
        map_set.insert(0, [0, 0, map_set[0][1]])

    i = 0
    while i < len(map_set) - 1:
        if map_set[i][1] + map_set[i][2] != map_set[i + 1][1]:
            map_set.insert(
                i + 1,
                [
                    map_set[i][1] + map_set[i][2],
                    map_set[i][1] + map_set[i][2],
                    map_set[i + 1][1] - map_set[i][1] - map_set[i][2],
                ],
            )
        i += 1

    return map_set


def parse_input(file_name):
    with open(file_name, "r") as input:
        seeds = [int(seed) for seed in input.readline().strip("\n")[7:].split(" ")]
        for i in range(len(seeds) // 2):
            seeds[i] = [seeds[i], seeds.pop(i + 1)]
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

    maps = [sorted(map_range, key=lambda r: r[1]) for map_range in maps]
    maps = [fill_map_set(map_set) for map_set in maps]

    return seeds, maps


if __name__ == "__main__":
    main()
