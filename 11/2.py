from Grid import Grid
from itertools import combinations


def main():
    EXPANSION_FACTOR = 1_000_000

    image = Grid([row.strip("\n") for row in open("input.txt", "r").readlines()])

    galaxies = image.find("#")
    galaxy_cols, galaxy_rows = [set(t) for t in list(zip(*galaxies))]

    expansion_counts_cols = []
    count = 0
    for i in range(image.NUM_COLS):
        expansion_counts_cols.append(count)

        if i not in galaxy_cols:
            count += 1

    expansion_counts_rows = []
    count = 0
    for i in range(image.NUM_ROWS):
        expansion_counts_rows.append(count)

        if i not in galaxy_rows:
            count += 1

    distance_sum = 0
    for g1, g2 in combinations(galaxies, 2):
        row_dist = abs(g2[1] - g1[1]) + (EXPANSION_FACTOR - 1) * abs(
            expansion_counts_rows[g2[1]] - expansion_counts_rows[g1[1]]
        )

        col_dist = abs(g2[0] - g1[0]) + (EXPANSION_FACTOR - 1) * abs(
            expansion_counts_cols[g2[0]] - expansion_counts_cols[g1[0]]
        )

        distance_sum += row_dist + col_dist

    print(distance_sum)


if __name__ == "__main__":
    main()
