def load_data():
    with open('day_5/input.txt') as data:
        return [int(n) for n in data.readline().split(',')]


class IntCodeComputer_v2:
    def __init__(self, data=None):
        self.data = load_data() if data is None else data
        self.running = True
        self.ip = 0 # ip - instruction pointer
        self.operations = {

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
        # hardcoding ID instead of taking input
        self.data[i] = 5
        # self.data[i] = int(input('Enter ID (1 for part 1, 5 for part 2): '))
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

            if opcode == 99: break

            i_1 = i + 1 if C == 1 else self.data[i + 1]
            i_2 = i + 2 if B == 1 else self.data[i + 2]
            out = self.data[i + 3]

            if opcode == 1:
                self.add(i_1, i_2, out)
            elif opcode == 2:
                self.multiply(i_1, i_2, out)
            elif opcode == 3:
                self.input_code(self.data[i + 1])
            elif opcode == 4:
                self.output_code(self.data[i + 1])
            elif opcode == 5:
                self.jump_if_true(i_1, i_2)
            elif opcode == 6:
                self.jump_if_false(i_1, i_2)
            elif opcode == 7:
                self.less_than(i_1, i_2, out)
            elif opcode == 8:
                self.equals(i_1, i_2, out)
            else:
                return print(f'Invalid code: {opcode}')

            
if __name__ == '__main__':
    code_proc = IntCodeComputer_v2()
    code_proc.start()