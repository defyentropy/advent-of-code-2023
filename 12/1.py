def main():
    lines = [
        (row, tuple([int(n) for n in shape.split(",")]))
        for row, shape in [
            line.strip("\n").split(" ") for line in open("input.txt", "r").readlines()
        ]
    ]

    def count_matches(row, shape):
        if shape == ():
            if "#" not in row:
                return 1
            else:
                return 0

        elif len(row) < shape[0]:
            return 0

        elif not any(s == "." for s in row[0 : shape[0]]) and (
            len(row) == shape[0] or row[shape[0]] in ".?"
        ):
            if row[0] == "?":
                return count_matches(row[shape[0] + 1 :], shape[1:]) + count_matches(
                    row[1:], shape
                )
            else:
                return count_matches(row[shape[0] + 1 :], shape[1:])

        else:
            if row[0] in ".?":
                return count_matches(row[1:], shape)
            else:
                return 0

    sum = 0
    for line in lines:
        possible_arrangements = count_matches(*line)
        sum += possible_arrangements
    # print(sum)


if __name__ == "__main__":
    for i in range(1000):
        main()
