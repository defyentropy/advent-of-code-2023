from Grid import Grid
from enum import Enum


class Direction(Enum):
    UP = "^"
    RIGHT = ">"
    DOWN = "V"
    LEFT = "<"

    @classmethod
    def get_next_directions(cls, initial_direction, tile):
        match tile:
            case ".":
                return [initial_direction]
            case "|":
                if initial_direction == cls.UP or initial_direction == cls.DOWN:
                    return [initial_direction]
                else:
                    return [cls.UP, cls.DOWN]
            case "-":
                if initial_direction == cls.LEFT or initial_direction == cls.RIGHT:
                    return [initial_direction]
                else:
                    return [cls.LEFT, cls.RIGHT]
            case "\\":
                match initial_direction:
                    case cls.UP:
                        return [cls.LEFT]
                    case cls.RIGHT:
                        return [cls.DOWN]
                    case cls.DOWN:
                        return [cls.RIGHT]
                    case cls.LEFT:
                        return [cls.UP]
            case "/":
                match initial_direction:
                    case cls.UP:
                        return [cls.RIGHT]
                    case cls.RIGHT:
                        return [cls.UP]
                    case cls.DOWN:
                        return [cls.LEFT]
                    case cls.LEFT:
                        return [cls.DOWN]


class MirrorGrid(Grid):
    def get_next_pos(self, x, y, directions):
        next_pos = []
        for direction in directions:
            match direction:
                case Direction.UP:
                    next_pos.append(((x, y - 1), direction))
                case Direction.RIGHT:
                    next_pos.append(((x + 1, y), direction))
                case Direction.DOWN:
                    next_pos.append(((x, y + 1), direction))
                case Direction.LEFT:
                    next_pos.append(((x - 1, y), direction))

        return list(filter(lambda t: self.at(t[0]) != "*", next_pos))


def main():
    with open("input.txt", "r") as input:
        lines = [line.strip("\n") for line in input.readlines()]
        lines.insert(0, "*" * len(lines[0]))
        lines.append("*" * len(lines[0]))
        for i in range(len(lines)):
            lines[i] = "*" + lines[i] + "*"
        contraption = MirrorGrid([row.strip("\n") for row in lines])

    def trace_rays(init):
        energized = set()
        ray_queue = [init]

        while ray_queue:
            if ray_queue[0] in energized:
                ray_queue.pop(0)
                continue

            energized.add(ray_queue[0])
            ray_queue.extend(
                contraption.get_next_pos(
                    *ray_queue[0][0],
                    Direction.get_next_directions(
                        ray_queue[0][1], contraption.at(ray_queue[0][0])
                    ),
                )
            )
            ray_queue.pop(0)

        return len(set(map(lambda t: t[0], energized)))

    max_energized = 0

    for i in range(1, contraption.NUM_ROWS - 1):
        max_energized = max(max_energized, trace_rays(((1, i), Direction.RIGHT)))
        max_energized = max(
            max_energized, trace_rays(((contraption.NUM_COLS - 2, i), Direction.LEFT))
        )

    for i in range(1, contraption.NUM_COLS - 1):
        max_energized = max(max_energized, trace_rays(((i, 1), Direction.DOWN)))
        max_energized = max(
            max_energized, trace_rays(((i, contraption.NUM_ROWS - 2), Direction.UP))
        )

    print(max_energized)


if __name__ == "__main__":
    main()
