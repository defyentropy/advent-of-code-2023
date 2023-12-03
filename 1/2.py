from re import findall, search

NUMS = {
    "one": "on1e",
    "two": "tw2o",
    "three": "thre3e",
    "four": "fou4r",
    "five": "fiv5e",
    "six": "si6x",
    "seven": "seve7n",
    "eight": "eigh8t",
    "nine": "nin9e",
}


def replace_num(line):
    result = search("(one|two|three|four|five|six|seven|eight|nine)", line)

    while result:
        return (
            line[: result.start()]
            + NUMS[result.group()]
            + replace_num(line[result.end() :])
        )

    return line


def main():
    lines = []
    with open("input.txt", "r") as input:
        line = input.readline()
        while line:
            lines.append(line.strip("\n"))
            line = input.readline()

    sum = 0

    for line in lines:
        for num in NUMS:
            line = line.replace(num, NUMS[num])
        matches = findall("[0-9]", line)
        sum += int(matches[0] + matches[-1])

    print(sum)


if __name__ == "__main__":
    main()
