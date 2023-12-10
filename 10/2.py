from copy import deepcopy


def main():
    grid = [list(line.strip("\n")) for line in open("input.txt", "r").readlines()]

    # pad grid for easier parsing
    for i in range(len(grid)):
        grid[i].append(".")
        grid[i].insert(0, ".")

    grid.append(list("." * len(grid[0])))
    grid.insert(0, list("." * len(grid[0])))

    # the directions NESW are represented by 0, 1, 2, and 3
    tiles = [".", "-", "|", "7", "J", "L", "F"]
    tile_outputs = [
        [-1, -1, 0, 3, -1, -1, 1],
        [-1, 1, -1, 2, 0, -1, -1],
        [-1, -1, 2, -1, 3, 1, -1],
        [-1, 3, -1, -1, -1, 0, 2],
    ]

    def follow_loop(pos, dirn, action):
        init = pos.copy()
        while True:
            action(tuple(pos), dirn)
            # print(pos, dirn)

            match dirn:
                case 0:
                    pos = [pos[0], pos[1] - 1]
                case 1:
                    pos = [pos[0] + 1, pos[1]]
                case 2:
                    pos = [pos[0], pos[1] + 1]
                case 3:
                    pos = [pos[0] - 1, pos[1]]

            action(tuple(pos), dirn)
            # print(pos, dirn)

            if pos == init:
                break

            dirn = tile_outputs[dirn][tiles.index(grid[pos[1]][pos[0]])]

    # find starting position
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "S":
                pos = [j, i]
                break

    # find starting direction
    dirns = []
    if tile_outputs[0][tiles.index(grid[pos[1] - 1][pos[0]])] != -1:
        dirns.append(0)
    if tile_outputs[1][tiles.index(grid[pos[1]][pos[0] + 1])] != -1:
        dirns.append(1)
    if tile_outputs[2][tiles.index(grid[pos[1] + 1][pos[0]])] != -1:
        dirns.append(2)
    if tile_outputs[3][tiles.index(grid[pos[1]][pos[0] - 1])] != -1:
        dirns.append(3)

    dirns.sort()

    match dirns:
        case [0, 1]:
            s_tile = "L"
        case [0, 2]:
            s_tile = "|"
        case [0, 3]:
            s_tile = "J"
        case [1, 2]:
            s_tile = "F"
        case [1, 3]:
            s_tile = "-"
        case [2, 3]:
            s_tile = "7"

    grid[pos[1]][pos[0]] = s_tile

    loop_tiles = set()
    follow_loop(pos, dirns[0], lambda t, d: loop_tiles.add(t))

    # visualisation = deepcopy(grid)
    # for tile in loop_tiles:
    #     visualisation[tile[1]][tile[0]] = " "

    # for line in visualisation:
    #     print("".join(line))

    # now mark inside tiles
    pos = sorted(loop_tiles, key=lambda t: (t[0], t[-1]))[0]
    dirn = 1

    inside_tiles = set()

    def mark_inside(pos, dirn):
        inside_dirn = (dirn + 1) % 4

        match inside_dirn:
            case 0:
                inside_tile = [pos[0], pos[1] - 1]
            case 1:
                inside_tile = [pos[0] + 1, pos[1]]
            case 2:
                inside_tile = [pos[0], pos[1] + 1]
            case 3:
                inside_tile = [pos[0] - 1, pos[1]]

        if tuple(inside_tile) not in loop_tiles:
            inside_tiles.add(tuple(inside_tile))

    follow_loop(list(pos), dirn, mark_inside)
    # print(len(inside_tiles))
    # print(inside_tiles)

    # now check remaining tiles
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[i]) - 1):
            if (i, j) not in loop_tiles and (i, j) not in inside_tiles:
                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):
                        if (k, l) in inside_tiles:
                            inside_tiles.add((i, j))

    print(len(inside_tiles))
    # print(inside_tiles)


if __name__ == "__main__":
    main()
