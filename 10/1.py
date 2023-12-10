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

    # find starting position
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "S":
                pos = [j, i]
                break

    # find starting direction
    if tile_outputs[0][tiles.index(grid[pos[1] - 1][pos[0]])] != -1:
        dirn = 0
    elif tile_outputs[1][tiles.index(grid[pos[1]][pos[0] + 1])] != -1:
        dirn = 1
    else:
        dirn = 2

    tile_count = 0
    while True:
        match dirn:
            case 0:
                pos = [pos[0], pos[1] - 1]
            case 1:
                pos = [pos[0] + 1, pos[1]]
            case 2:
                pos = [pos[0], pos[1] + 1]
            case 3:
                pos = [pos[0] - 1, pos[1]]

        if grid[pos[1]][pos[0]] == "S":
            break

        dirn = tile_outputs[dirn][tiles.index(grid[pos[1]][pos[0]])]
        tile_count += 1

    print(tile_count // 2 + 1)


if __name__ == "__main__":
    main()
