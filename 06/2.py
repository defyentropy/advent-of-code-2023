from re import findall
from math import sqrt, ceil, floor


def main():
    with open("input.txt", "r") as input:
        times = [
            int(time) for time in findall("\d+", input.readline().replace(" ", ""))
        ]
        dists = [
            int(dist) for dist in findall("\d+", input.readline().replace(" ", ""))
        ]

    margin = 1
    for i in range(len(times)):
        roots = solve_quadratic(-1, times[i], -dists[i] - 1)
        time_bounds = (ceil(roots[0]), floor(roots[1]))
        margin *= time_bounds[1] - time_bounds[0] + 1

    print(margin)


def solve_quadratic(a, b, c):
    determinant = b**2 - 4 * a * c
    if determinant > 0:
        return ((-b + sqrt(determinant)) / (2 * a), (-b - sqrt(determinant)) / (2 * a))
    elif determinant == 0:
        return -b / 2 / a
    else:
        # not handling equations with complex roots because in this situation
        # it's guaranteed to not happen
        return None


if __name__ == "__main__":
    main()
