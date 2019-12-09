from itertools import permutations, cycle
import os.path
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from day_5.main import IntCodeComputer_v2, load_data


class IntCodeComputer_v3(IntCodeComputer_v2):
    data = load_data('day_7/input.txt')

    def __init__(self, input_data=None):
        super().__init__(IntCodeComputer_v3.data[:])
        self.output = None
        self.input_data = input_data if type(input_data) == list else None

    def input_code(self, i):
        self.data[i] = self.input_data.pop(0)
        self.ip += 2

    def output_code(self, i):
        self.output = self.data[i]
        self.ip += 2

    def add_input_data(self, value):
        self.input_data.append(value)

    def start(self):
        try:
            super().start()
        except IndexError:
            pass
        finally:
            return self.output


def part_1():
    phases = (0, 1, 2, 3, 4)

    phase_orders = permutations(phases, len(phases))
    max_thrust = 0

    def find_max_thrust(input_signal, phases):
        try:
            amp_out = IntCodeComputer_v3([next(phases), input_signal]).start()
            return find_max_thrust(amp_out, phases)
        except StopIteration:
            return input_signal

    for phase_order in phase_orders:
        output = find_max_thrust(0, iter(phase_order))
        if output > max_thrust:
            max_thrust = output

    print(f'Part 1 max thrust: {max_thrust}')


def part_2():
    phases = (5, 6, 7, 8, 9)

    phase_orders = permutations(phases, len(phases))
    max_thrust = 0

    for phase_order in phase_orders:
        # setting phases on every amp
        amps = [IntCodeComputer_v3([phase]) for phase in phase_order]
        amps_cycled = cycle(amps)

        amp_input = 0

        # main feedback loop
        while True:
            amp = next(amps_cycled)
            amp.add_input_data(amp_input)
            amp_input = amp.start()

            # if all of the amps are no longer running, get the
            # output of the last one (E)
            if all(a.running == False for a in amps):
                if (thrust_signal := amps[-1].output) > max_thrust:
                    max_thrust = thrust_signal
                break

    print(f'Part 2 max thrust: {max_thrust}')


if __name__ == '__main__':
    part_1()
    part_2()