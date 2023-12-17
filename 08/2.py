from re import findall
from math import lcm


def main():
    with open("input.txt", "r") as input:
        directions = input.readline().strip("\n")
        input.readline()

        network = {}
        line = input.readline()
        while line:
            locations = findall("\w\w\w", line)
            network[locations[0]] = {"L": locations[1], "R": locations[2]}
            line = input.readline()

    LEN_DIRECTIONS = len(directions)
    pos = [node for node in network.keys() if node[-1] == "A"]
    step_counts = []

    for node in pos:
        steps = 0
        while not node[-1] == "Z":
            node = network[node][directions[steps % LEN_DIRECTIONS]]
            steps += 1
        step_counts.append(steps)

    print(lcm(*step_counts))


if __name__ == "__main__":
    main()
