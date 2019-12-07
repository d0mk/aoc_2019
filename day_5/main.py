def load_data():
    with open('day_5/input.txt') as data:
        return [int(n) for n in data.readline().split(',')]


class IntCodeComputer_v2:
    def __init__(self, data=None):
        self.data = load_data() if data is None else data
        self.running = True
        self.ip = 0 # ip - instruction pointer
        self.operations = {
            1 : lambda x, y, z : self.add(x, y, z),
            2 : lambda x, y, z : self.multiply(x, y, z),
            3 : lambda x, y, z : self.input_code(x),
            4 : lambda x, y, z : self.output_code(x),
            5 : lambda x, y, z : self.jump_if_true(x, y),
            6 : lambda x, y, z : self.jump_if_false(x, y),
            7 : lambda x, y, z : self.less_than(x, y, z),
            8 : lambda x, y, z : self.equals(x, y, z),
            99 : lambda x, y, z : self.stop()
        }

    def add(self, i_1, i_2, out):
        self.data[out] = self.data[i_1] + self.data[i_2]
        self.ip += 4

    def multiply(self, i_1, i_2, out):
        self.data[out] = self.data[i_1] * self.data[i_2]
        self.ip += 4

    def jump_if_true(self, i_1, i_2):
        if self.data[i_1]:
            self.ip = self.data[i_2]
        else:
            self.ip += 3

    def jump_if_false(self, i_1, i_2):
        if not self.data[i_1]:
            self.ip = self.data[i_2]
        else:
            self.ip += 3

    def less_than(self, i_1, i_2, out):
        self.data[out] = 1 if self.data[i_1] < self.data[i_2] else 0
        self.ip += 4

    def equals(self, i_1, i_2, out):
        self.data[out] = 1 if self.data[i_1] == self.data[i_2] else 0
        self.ip += 4

    def input_code(self, i):
        self.data[i] = 1
        self.ip += 2

    def output_code(self, i):
        print(f'Diagnostic code: {self.data[i]}')
        self.ip += 2

    def stop(self):
        self.running = False

    def parse_code(self, code):
        digits = []
        while len(digits) < 5:
            digits.append(code % 10)
            code //= 10
        E, D, C, B, A = digits
        return A, B, C, D * 10 + E

    def start(self):
        while self.running:
            i = self.ip
            
            A, B, C, opcode = self.parse_code(self.data[i])
            L = len(self.data)

            i_1 = i + 1 if C == 1 else self.data[(i + 1) % L]
            i_2 = i + 2 if B == 1 else self.data[(i + 2) % L]
            out = self.data[(i + 3) % L]

            self.operations[opcode](i_1, i_2, out)

            
if __name__ == '__main__':
    code_proc = IntCodeComputer_v2()
    code_proc.start()