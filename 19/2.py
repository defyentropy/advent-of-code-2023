from re import match, search

WORKFLOWS = {"R": "Rejected", "A": "Accepted"}
DEBUG = False


def main():
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

    print(
        count_acceptable_combinations(
            {"x": (1, 4000), "m": (1, 4000), "a": (1, 4000), "s": (1, 4000)},
            WORKFLOWS["in"],
            0,
        )
    )


def count_acceptable_combinations(constraints, rules, nest_count):
    if DEBUG:
        print("-" * nest_count, constraints, rules)

    if type(rules) == str:
        if rules == "Accepted":
            count = 1

            for cat in constraints.keys():
                count *= constraints[cat][1] + 1 - constraints[cat][0]

            return count
        else:
            return 0

    if type(rules[0]) == str:
        return count_acceptable_combinations(
            constraints.copy(), WORKFLOWS[rules[0]], nest_count + 1
        )

    match rules[0][1]:
        case "<":
            if constraints[rules[0][0]][0] > rules[0][2]:
                return count_acceptable_combinations(
                    constraints.copy(), rules[1:], nest_count + 1
                )
            else:
                return count_acceptable_combinations(
                    update_constraints(
                        constraints.copy(),
                        rules[0][0],
                        (constraints[rules[0][0]][0], rules[0][2] - 1),
                    ),
                    WORKFLOWS[rules[0][3]],
                    nest_count + 1,
                ) + count_acceptable_combinations(
                    update_constraints(
                        constraints.copy(),
                        rules[0][0],
                        (rules[0][2], constraints[rules[0][0]][1]),
                    ),
                    rules[1:],
                    nest_count + 1,
                )

        case ">":
            if constraints[rules[0][0]][1] < rules[0][2]:
                return count_acceptable_combinations(
                    constraints, rules[1:], nest_count + 1
                )
            else:
                return count_acceptable_combinations(
                    update_constraints(
                        constraints.copy(),
                        rules[0][0],
                        (rules[0][2] + 1, constraints[rules[0][0]][1]),
                    ),
                    WORKFLOWS[rules[0][3]],
                    nest_count + 1,
                ) + count_acceptable_combinations(
                    update_constraints(
                        constraints.copy(),
                        rules[0][0],
                        (constraints[rules[0][0]][0], rules[0][2]),
                    ),
                    rules[1:],
                    nest_count + 1,
                )


def update_constraints(constraints, cat, new):
    constraints[cat] = new
    return constraints


if __name__ == "__main__":
    main()
