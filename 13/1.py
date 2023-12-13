from Grid import Grid


def main():
    patterns = []

    with open("input.txt", "r") as input:
        line = input.readline()
        pattern = []
        while line:
            if line == "\n":
                patterns.append(Grid(pattern))
                pattern = []
            else:
                pattern.append(line.strip("\n"))
            line = input.readline()
        patterns.append(Grid(pattern))

    summary = 0
    for pattern in patterns:
        column_index = None
        for i in range(1, pattern.NUM_COLS):
            reflection_length = min(i, pattern.NUM_COLS - i)
            full_match = True
            for j in range(reflection_length, 0, -1):
                if pattern.get_col(i - j) != pattern.get_col(i + j - 1):
                    full_match = False
                    break

            if full_match:
                column_index = i
                break

        if column_index:
            summary += column_index
            continue

        row_index = None
        for i in range(1, pattern.NUM_ROWS):
            reflection_length = min(i, pattern.NUM_ROWS - i)
            full_match = True
            for j in range(reflection_length, 0, -1):
                if pattern.get_row(i - j) != pattern.get_row(i + j - 1):
                    full_match = False
                    break

            if full_match:
                row_index = i
                break

        if row_index:
            summary += row_index * 100

    print(summary)


if __name__ == "__main__":
    main()
