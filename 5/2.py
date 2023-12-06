def main():
    seeds, maps = parse_input("input.txt")

    for factor_map in maps:
        # treat the array of seed ranges like a queue and convert each
        # range to a range in the next stage of mapping
        for i in range(len(seeds)):
            seeds.extend(get_new_ranges(seeds.pop(0), factor_map))

    # sort the final location ranges and find the smallest start index
    print(sorted(seeds, key=lambda r: r[0])[0][0])


def get_new_ranges(seed_range, factor_map):
    """Given a range in one factor and a mapping from that factor to the
    next, return a list of ranges in the next factor that the given range
    maps onto."""
    new_ranges = []
    start, length = seed_range
    new_start, new_length = check_map(start, factor_map)
    # if new_length < length, that means we haven't mapped the entire range yet
    while new_length < length:
        new_ranges.append([new_start, new_length])
        # update the start and length values so they now reference the part
        # of the range that hasn't been mapped yet
        start += new_length
        length -= new_length
        new_start, new_length = check_map(start, factor_map)

    # this is the last prt of the range to be mapped
    new_ranges.append([new_start, length])
    return new_ranges


def check_map(idx, parameter_map):
    """Given an index and a mpping from the current factor to the next,
    return a slice of the range for the next factor starting at the mapping
    for the given index and ending at the end of the defined range within
    which that mapping falls."""
    for dest_start, source_start, length in parameter_map:
        if source_start <= idx < source_start + length:
            # the given index must fall within a certain range
            # return a slice of that range starting from that index
            # and ending at the end of that range
            return [idx + (dest_start - source_start), length - (idx - source_start)]


def fill_map_set(map_set):
    """Given a sparse list of mapping ranges, populate the list with the missing ranges
    to make sure that every number in the input range has a predefined mapping in
    the output range."""
    # make sure the map set begins at 0
    if map_set[0][1] != 0:
        map_set.insert(0, [0, 0, map_set[0][1]])

    i = 0
    while i < len(map_set) - 1:
        # if there is a gap between the end of the curren range and the start
        # of the next
        if map_set[i][1] + map_set[i][2] != map_set[i + 1][1]:
            # add a new range that exactly fills in that gap
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
        # group the integers into lists of two
        for i in range(len(seeds) // 2):
            seeds[i] = [seeds[i], seeds.pop(i + 1)]
        input.readline()  # ignore the first blank line because no map has been read yet

        maps = []
        this_map = []
        line = input.readline()
        while line:
            # ignore blank lines and labels
            if line[0].isalpha():
                pass
            elif line == "\n":
                maps.append(this_map)
                this_map = []
            else:
                this_map.append([int(num) for num in line.strip("\n").split(" ")])

            line = input.readline()
        maps.append(this_map)

    # sort the map ranges based on their stating index in the source range
    maps = [sorted(map_set, key=lambda r: r[1]) for map_set in maps]
    # fill in any gaps in the set of map ranges
    maps = [fill_map_set(map_set) for map_set in maps]

    return seeds, maps


if __name__ == "__main__":
    main()
