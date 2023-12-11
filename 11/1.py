from Grid import Grid
from itertools import combinations


def main():
    image = Grid([row.strip("\n") for row in open("input.txt", "r").readlines()])
    galaxies = image.find("#")

    galaxy_cols, galaxy_rows = [set(t) for t in list(zip(*galaxies))]

    rows_to_duplicate = set(range(image.NUM_ROWS)).difference(galaxy_rows)
    cols_to_duplicate = set(range(image.NUM_COLS)).difference(galaxy_cols)

    for rows_added, row_index in enumerate(sorted(list(rows_to_duplicate))):
        image.insert_row(row_index + rows_added, image.get_row(row_index + rows_added))

    for cols_added, col_index in enumerate(sorted(list(cols_to_duplicate))):
        image.insert_col(col_index + cols_added, image.get_col(col_index + cols_added))

    galaxies = image.find("#")

    distance_sum = 0
    for g1, g2 in combinations(galaxies, 2):
        distance_sum += Grid.manhattan_distance(g1, g2)

    print(distance_sum)


if __name__ == "__main__":
    main()
