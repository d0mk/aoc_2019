from day_5.main import IntCodeComputer_v2
from itertools import permutations


def load_data():
    with open('day_7/input.txt') as data:
        return [int(n) for n in data.readline().split(',')]


class IntComputer_v3(IntCodeComputer_v2):
    data = load_data()

    def __init__(self, stdin):
        super().__init__(IntComputer_v3.data[:])
        self.output = None
        self.stdin = (n for n in stdin)

    def input_code(self, i, value):
        self.data[i] = value
        self.ip += 2

    def output_code(self, i):
        self.output = self.data[i]
        self.ip += 2

    def start(self):
        super().start()
        return self.output


def main():
    phases = (0, 1, 2, 3, 4)
    phase_orders = permutations(phases, len(phases))
    max_thrust = 0

    def find_max_thrust(input_signal, phases):
        if (phase := next(phase)) is not None:
            pass
        else:
            return IntComputer_v3().start()


    for phase_order in phase_orders:
        output = find_max_thrust(0, phase_order)
        if output > max_thrust:
            max_thrust = output

    print(max_thrust)


if __name__ == '__main__':
    main()