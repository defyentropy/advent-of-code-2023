def main():
    histories = []

    with open("input.txt", "r") as input:
        line = input.readline()

        while line:
            histories.append([int(n) for n in line.strip("\n").split(" ")])
            line = input.readline()

    future_extrapolations = extrapolate(histories)
    past_extrapolations = extrapolate(
        [list(reversed(history)) for history in histories]
    )

    print(future_extrapolations, past_extrapolations)


def extrapolate(histories):
    sum_of_extrapolations = 0

    for history in histories:
        sequences = [history]
        while not all_zeros(sequences[-1]):
            diffs = []
            for i in range(1, len(sequences[-1])):
                diffs.append(sequences[-1][i] - sequences[-1][i - 1])
            sequences.append(diffs)

        sequences[-1].append(0)
        for i in range(len(sequences) - 2, -1, -1):
            sequences[i].append(sequences[i][-1] + sequences[i + 1][-1])

        sum_of_extrapolations += sequences[0][-1]
    return sum_of_extrapolations


def all_zeros(sequence):
    for n in sequence:
        if n != 0:
            return False
    return True


if __name__ == "__main__":
    main()
