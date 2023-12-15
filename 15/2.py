from re import match
from collections import OrderedDict


def main():
    with open("input.txt", "r") as input:
        steps = input.readline().strip("\n").split(",")

    boxes = {}

    for step in steps:
        label = match("(?P<label>\w+)(?P<ins>[=-])(?P<focus>\d*)", step)
        label, ins, focus = label.groups()

        box_num = hash_step(label)
        if not boxes.get(box_num):
            boxes[box_num] = OrderedDict()

        if ins == "=":
            boxes[box_num][label] = int(focus)
        else:
            boxes[box_num].pop(label, None)

    total_focusing_power = 0
    for box in boxes:
        for i, lens in enumerate(boxes[box]):
            total_focusing_power += get_focusing_power(box, i, boxes[box][lens])

    print(total_focusing_power)


def hash_step(step):
    h = 0
    for char in step:
        h += ord(char)
        h *= 17
        h %= 256

    return h


def get_focusing_power(box_num, lens_index, focal_length):
    return (1 + box_num) * (1 + lens_index) * focal_length


if __name__ == "__main__":
    main()
