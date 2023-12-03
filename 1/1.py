from re import findall


def main():
    lines = []
    with open("input.txt", "r") as input:
        line = input.readline()
        while line:
            lines.append(line.strip("\n"))
            line = input.readline()

    sum = 0
    for line in lines:
        matches = findall("[0-9]", line)
        sum += int(matches[0] + matches[-1])

    print(sum)


if __name__ == "__main__":
    main()
