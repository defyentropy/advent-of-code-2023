def main():
    lines = [
        (
            "?".join([row for i in range(5)]),
            tuple([int(n) for n in ",".join([shape for i in range(5)]).split(",")]),
        )
        for row, shape in [
            line.strip("\n").split(" ") for line in open("input.txt", "r").readlines()
        ]
    ]

    def count_matches(memo, row, shape):
        if (row, shape) in memo:
            return memo[(row, shape)]

        elif shape == ():
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
                count = count_matches(
                    memo, row[shape[0] + 1 :], shape[1:]
                ) + count_matches(memo, row[1:], shape)
                memo[(row, shape)] = count
                return count
            else:
                count = count_matches(memo, row[shape[0] + 1 :], shape[1:])
                memo[(row, shape)] = count
                return count

        else:
            if row[0] in ".?":
                count = count_matches(memo, row[1:], shape)
                memo[(row, shape)] = count
                return count
            else:
                return 0

    sum = 0
    for line in lines:
        possible_arrangements = count_matches({}, *line)
        sum += possible_arrangements
    print(sum)


if __name__ == "__main__":
    main()
