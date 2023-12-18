from re import match


def main():
    instructions = []
    directions = ["R", "D", "L", "U"]

    with open("input.txt", "r") as input:
        line = input.readline()

        while line:
            color = match("(\w) (\d+) \(#(\w+)\)", line.strip("\n")).group(3)
            steps = int(color[:-1], base=16)
            direction = directions[int(color[-1])]

            instructions.append((steps, direction))
            line = input.readline()

    vertices = [(0, 0)]
    path_length = 0
    for steps, direction in instructions:
        path_length += steps
        x, y = vertices[-1]
        match direction:
            case "U":
                vertices.append((x, y - steps))
            case "R":
                vertices.append((x + steps, y))
            case "D":
                vertices.append((x, y + steps))
            case "L":
                vertices.append((x - steps, y))

    area = 0
    for i in range(len(vertices) - 1):
        x1, y1 = vertices[i]
        x2, y2 = vertices[i + 1]

        area += x1 * y2 - x2 * y1

    print(abs(area) // 2 + path_length // 2 + 1)


if __name__ == "__main__":
    main()
