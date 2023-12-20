from math import lcm

PRESS_COUNT = 1
PULSE_HISTORIES = {}


class Module:
    def __init__(self, name):
        self.name = name
        self.type = "untyped"
        self.inputs = set()
        self.outputs = set()

    def add_input(self, m):
        self.inputs.add(m)

    def add_output(self, m):
        self.outputs.add(m)

    def process_pulse(self, pulse):
        return []

    def __repr__(self):
        return f"{self.inputs} --> {self.name} --> {self.outputs}"


class FlipFlop(Module):
    def __init__(self, name):
        super().__init__(name)
        self.type = "flip-flop"
        self.state = False

    def process_pulse(self, pulse):
        if pulse[1] == True:
            return []

        self.state = not self.state
        return [(self.name, self.state, m) for m in self.outputs]


class Conjunction(Module):
    def __init__(self, name):
        super().__init__(name)
        self.type = "conjunction"
        self.input_memories = {}
        PULSE_HISTORIES[name] = []

    def add_input(self, m):
        super().add_input(m)
        self.input_memories[m] = False

    def process_pulse(self, pulse):
        self.input_memories[pulse[0]] = pulse[1]

        if all([self.input_memories[m] for m in self.input_memories]):
            PULSE_HISTORIES[self.name].append((PRESS_COUNT, False))
            return [(self.name, False, m) for m in self.outputs]

        else:
            return [(self.name, True, m) for m in self.outputs]


class Broadcast(Module):
    def __init__(self, name):
        super().__init__(name)
        self.type = "broadcast"

    def process_pulse(self, pulse):
        return [(self.name, pulse[1], m) for m in self.outputs]


MODULES = {"button": Module("button")}


def main():
    global PRESS_COUNT
    data = []
    with open("input.txt", "r") as input:
        line = input.readline()

        while line:
            line = line.strip("\n").split(" -> ")

            module_name = line[0]
            outputs = line[1].split(", ")

            data.append((module_name, outputs))
            line = input.readline()

    for module in data:
        if module[0] == "broadcaster":
            MODULES[module[0]] = Broadcast(module[0])
        elif module[0][0] == "%":
            MODULES[module[0][1:]] = FlipFlop(module[0][1:])
        elif module[0][0] == "&":
            MODULES[module[0][1:]] = Conjunction(module[0][1:])

    for module in data:
        for output in module[1]:
            if output not in MODULES:
                MODULES[output] = Module(output)

            if module[0] == "broadcaster":
                MODULES[module[0]].add_output(output)
                MODULES[output].add_input(module[0])
            else:
                MODULES[module[0][1:]].add_output(output)
                MODULES[output].add_input(module[0][1:])

    while PRESS_COUNT <= 4096:
        pulse_queue = [("button", False, "broadcaster")]

        while pulse_queue:
            pulse_queue.extend(
                MODULES[pulse_queue[0][2]].process_pulse(pulse_queue.pop(0))
            )

        PRESS_COUNT += 1

    least_count = 1
    for m in ["ft", "qr", "lk", "lz"]:
        least_count = lcm(least_count, PULSE_HISTORIES[m][0][0])

    print(least_count)


if __name__ == "__main__":
    main()
