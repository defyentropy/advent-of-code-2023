from Grid import Grid
from itertools import combinations


def main():
    EXPANSION_FACTOR = 1000000

    image = Grid([row.strip("\n") for row in open("input.txt", "r").readlines()])
    galaxies = image.find("#")

    galaxy_cols, galaxy_rows = [set(t) for t in list(zip(*galaxies))]

    empty_rows = set(range(image.NUM_ROWS)).difference(galaxy_rows)
    empty_cols = set(range(image.NUM_COLS)).difference(galaxy_cols)

    distance_sum = 0
    for g1, g2 in combinations(galaxies, 2):
        manhattan_distance = abs(g2[1] - g1[1])
        for row in empty_rows:
            if g1[1] < row < g2[1] or g2[1] < row < g1[1]:
                manhattan_distance += EXPANSION_FACTOR - 1

        manhattan_distance += abs(g2[0] - g1[0])
        for col in empty_cols:
            if g1[0] < col < g2[0] or g2[0] < col < g1[0]:
                manhattan_distance += EXPANSION_FACTOR - 1

        distance_sum += manhattan_distance

    print(distance_sum)


if __name__ == "__main__":
    main()
