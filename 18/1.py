from re import match


def main():
    instructions = []

    with open("input.txt", "r") as input:
        line = input.readline()

        while line:
            instructions.append(
                match("(\w) (\d+) \(#(\w+)\)", line.strip("\n")).groups()
            )
            line = input.readline()

    path = [(0, 0)]
    right = set()
    left = set()

    for instruction in instructions:
        direction = instruction[0]
        steps = int(instruction[1])

        while steps > 0:
            pos = path[-1]
            match direction:
                case "U":
                    path.append((pos[0], pos[1] - 1))
                    right.add((pos[0] + 1, pos[1]))
                    left.add((pos[0] - 1, pos[1]))
                case "R":
                    path.append((pos[0] + 1, pos[1]))
                    right.add((pos[0], pos[1] + 1))
                    left.add((pos[0], pos[1] - 1))
                case "D":
                    path.append((pos[0], pos[1] + 1))
                    right.add((pos[0] - 1, pos[1]))
                    left.add((pos[0] + 1, pos[1]))
                case "L":
                    path.append((pos[0] - 1, pos[1]))
                    right.add((pos[0], pos[1] - 1))
                    left.add((pos[0], pos[1] + 1))

            steps -= 1

    path.pop()
    right.difference_update(set(path))
    left.difference_update(set(path))

    if sorted(right)[0] < sorted(left)[0]:
        inside = left
        outside = right
    else:
        inside = right
        outside = left

    flood_fill_queue = list(inside)
    while flood_fill_queue:
        current = flood_fill_queue.pop(0)

        neighbors = [
            (current[0], current[1] - 1),
            (current[0] - 1, current[1]),
            (current[0] + 1, current[1]),
            (current[0], current[1] + 1),
        ]

        for neighbor in neighbors:
            if (
                neighbor not in outside
                and neighbor not in path
                and neighbor not in inside
            ):
                inside.add(neighbor)
                flood_fill_queue.append(neighbor)

    print(len(path) + len(inside))


if __name__ == "__main__":
    main()
