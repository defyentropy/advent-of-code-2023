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
            smudge_found = False

            for j in range(reflection_length, 0, -1):
                smudges = error_count(
                    pattern.get_col(i - j), pattern.get_col(i + j - 1)
                )
                if (smudge_found and smudges) or (smudges > 1):
                    full_match = False
                    break
                elif smudges == 1:
                    smudge_found = True

            if full_match and smudge_found:
                column_index = i
                break

        if column_index:
            summary += column_index
            continue

        row_index = None
        for i in range(1, pattern.NUM_ROWS):
            reflection_length = min(i, pattern.NUM_ROWS - i)
            full_match = True
            smudge_found = False

            for j in range(reflection_length, 0, -1):
                smudges = error_count(
                    pattern.get_row(i - j), pattern.get_row(i + j - 1)
                )
                if (smudges and smudge_found) or (smudges > 1):
                    full_match = False
                    break
                elif smudges == 1:
                    smudge_found = True

            if full_match and smudge_found:
                row_index = i
                break

        if row_index:
            summary += row_index * 100

    print(summary)


def error_count(list1, list2):
    count = 0
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            count += 1
    return count


if __name__ == "__main__":
    main()
