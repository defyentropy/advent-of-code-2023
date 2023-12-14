def main():
    rows = [list(line.strip("\n")) for line in open("input.txt").readlines()]
    NUM_ROWS = len(rows)

    for i in range(1, len(rows)):
        move_up(i, rows)

    total_load = 0
    for i, row in enumerate(rows):
        total_load += calculate_load(row, i, NUM_ROWS)
    print(total_load)


def move_up(row_index, rows):
    if row_index == 0:
        return rows
    else:
        for i in range(len(rows[row_index])):
            if rows[row_index][i] == "O" and rows[row_index - 1][i] == ".":
                rows[row_index][i] = "."
                rows[row_index - 1][i] = "O"
        return move_up(row_index - 1, rows)


def calculate_load(row, row_index, num_rows):
    return len(list(filter(lambda r: r == "O", row))) * (num_rows - row_index)


if __name__ == "__main__":
    main()
