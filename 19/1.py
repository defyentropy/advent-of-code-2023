from re import match, search, findall


def main():
    WORKFLOWS = {}
    PARTS = []

    with open("input.txt", "r") as input:
        line = input.readline()

        while line != "\n":
            wf_name = match("\w+", line).group(0)

            rules = []
            for rule in search("\{(.*)\}", line).group(1).split(","):
                specs = match("([xmas])([<=>])(\d+):(\w+)", rule)
                rules.append(
                    (lambda r: (r[0], r[1], int(r[2]), r[3]))(specs.groups())
                    if specs
                    else rule
                )

            WORKFLOWS[wf_name] = rules
            line = input.readline()

        line = input.readline()
        while line:
            ratings = findall("([xmas])=(\d+)", line)

            part = {}
            for rating in ratings:
                part[rating[0]] = int(rating[1])

            PARTS.append(part)
            line = input.readline()

    rating_sum = 0
    for part in PARTS:
        wf_name = "in"

        while wf_name != "R" and wf_name != "A":
            rules = WORKFLOWS[wf_name]

            for rule in rules:
                if not type(rule) == tuple:
                    wf_name = rule
                    break

                match rule[1]:
                    case "<":
                        if part[rule[0]] < rule[2]:
                            wf_name = rule[3]
                            break
                    case ">":
                        if part[rule[0]] > rule[2]:
                            wf_name = rule[3]
                            break

        if wf_name == "A":
            for cat in part.keys():
                rating_sum += part[cat]

    print(rating_sum)


if __name__ == "__main__":
    main()
