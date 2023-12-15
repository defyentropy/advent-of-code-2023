from functools import reduce
from operator import add


def main():
    with open("input.txt", "r") as input:
        steps = [hash_step(step) for step in input.readline().strip("\n").split(",")]

    print(reduce(add, steps))


def hash_step(step):
    h = 0
    for char in step:
        h += ord(char)
        h *= 17
        h %= 256

    return h


if __name__ == "__main__":
    main()
