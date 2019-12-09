import os.path
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from day_7.main import IntCodeComputer_v3, load_data


class IntCodeComputer_v4(IntCodeComputer_v3):
    def __init__(self):
        super().__init__([2])
        self.memory = {i : v for i, v in enumerate(load_data('day_9/input.txt'))}
        self.relative_base = 0
        self.operations[9] = lambda x, y, z : self.adjust_rel_base(x)

    def check_memory(self, *indices):
        for index in indices:
            if index not in self.memory:
                self.memory[index] = 0

    def adjust_rel_base(self, i):
        self.relative_base += self.memory[i]
        self.ip += 2
            
    def add(self, i_1, i_2, out):
        self.memory[out] = self.memory[i_1] + self.memory[i_2]
        self.ip += 4

    def multiply(self, i_1, i_2, out):
        self.memory[out] = self.memory[i_1] * self.memory[i_2]
        self.ip += 4

    def jump_if_true(self, i_1, i_2):
        if self.memory[i_1]:
            self.ip = self.memory[i_2]
        else:
            self.ip += 3

    def jump_if_false(self, i_1, i_2):
        if not self.memory[i_1]:
            self.ip = self.memory[i_2]
        else:
            self.ip += 3

    def less_than(self, i_1, i_2, out):
        self.memory[out] = 1 if self.memory[i_1] < self.memory[i_2] else 0
        self.ip += 4

    def equals(self, i_1, i_2, out):
        self.memory[out] = 1 if self.memory[i_1] == self.memory[i_2] else 0
        self.ip += 4

    def input_code(self, i):
        self.memory[i] = self.input_data.pop(0)
        self.ip += 2

    def output_code(self, i):
        print(self.memory[i])
        self.ip += 2

    def start(self):
        while self.running:
            i = self.ip
            A, B, C, opcode = self.parse_code(self.memory[i])
            i_1 = i_2 = out = None

            self.check_memory(i + 1, i + 2, i + 3)

            if C == 0:
                i_1 = self.memory[i + 1]
            elif C == 1:
                i_1 = i + 1
            elif C == 2:
                i_1 = self.relative_base + self.memory[i + 1]

            if B == 0:
                i_2 = self.memory[i + 2]
            elif B == 1:
                i_2 = i + 2
            elif B == 2:
                i_2 = self.relative_base + self.memory[i + 2]

            if A == 0 or A == 1:
                out = self.memory[i + 3]
            elif A == 2:
                out = self.relative_base + self.memory[i + 3]

            if not (i_1 or i_2 or out):
                break

            self.operations[opcode](i_1, i_2, out)


if __name__ == '__main__':
    IntCodeComputer_v4().start()