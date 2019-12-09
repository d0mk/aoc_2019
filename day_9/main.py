import os.path
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from day_7.main import IntCodeComputer_v3, load_data


class IntCodeComputer_v4(IntCodeComputer_v3):
    def __init__(self):
        super().__init__([2])
        self.data = {i : v for i, v in enumerate(load_data('day_9/input.txt'))}
        self.relative_base = 0
        self.operations[9] = lambda x, y, z : self.adjust_rel_base(x)

    def check_memory(self, *indices):
        for index in indices:
            if index not in self.data:
                self.data[index] = 0

    def adjust_rel_base(self, i):
        self.relative_base += self.data[i]
        self.ip += 2

    def output_code(self, i):
        print(self.data[i])
        self.ip += 2

    def start(self):
        while self.running:
            i = self.ip
            A, B, C, opcode = self.parse_code(self.data[i])
            i_1 = i_2 = out = None

            self.check_memory(i + 1, i + 2, i + 3)

            if C == 0:
                i_1 = self.data[i + 1]
            elif C == 1:
                i_1 = i + 1
            elif C == 2:
                i_1 = self.relative_base + self.data[i + 1]

            if B == 0:
                i_2 = self.data[i + 2]
            elif B == 1:
                i_2 = i + 2
            elif B == 2:
                i_2 = self.relative_base + self.data[i + 2]

            if A == 0 or A == 1:
                out = self.data[i + 3]
            elif A == 2:
                out = self.relative_base + self.data[i + 3]

            if not (i_1 or i_2 or out):
                break

            self.operations[opcode](i_1, i_2, out)


if __name__ == '__main__':
    IntCodeComputer_v4().start()