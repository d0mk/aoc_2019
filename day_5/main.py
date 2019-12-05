def load_data():
    with open('day_5/input.txt') as data:
        return [int(n) for n in data.readline().split(',')]


class IntCodeComputer_v2:
    def __init__(self, data=None):
        self.data = load_data() if data is None else data
        self.running = True

    def add(self, i_1, i_2, out):
        self.data[out] = self.data[i_1] + self.data[i_2]

    def multiply(self, i_1, i_2, out):
        self.data[out] = self.data[i_1] * self.data[i_2]

    def input_code(self, i):
        # self.data[i] = int(input('Enter ID: '))
        self.data[i] = 1
        # self.data[i] = 5

    def output_code(self, i):
        print(f'Diagnostic code: {self.data[i]}')

    def stop(self):
        self.running = False

    def result(self):
        return self.data[0]

    def parse_code(self, code):
        digits = []
        while len(digits) < 5:
            digits.append(code % 10)
            code //= 10
        E, D, C, B, A = digits
        return A, B, C, D * 10 + E

    def start(self):
        # i - instruction pointer
        i = 0

        while self.running:
            A, B, C, opcode = self.parse_code(self.data[i])

            i_1 = i + 1 if C == 1 else self.data[i + 1]
            i_2 = i + 2 if B == 1 else self.data[i + 2]
            out = self.data[i + 3]

            if opcode == 1:
                self.add(i_1, i_2, out)
                i += 4
            elif opcode == 2:
                self.multiply(i_1, i_2, out)
                i += 4
            elif opcode == 3:
                self.input_code(i_1)
                i -= 2
            elif opcode == 4:
                self.output_code(i_1)
                i -= 2
            elif opcode == 5:
                pass
            elif opcode == 6:
                pass
            elif opcode == 7:
                pass
            elif opcode == 8:
                pass
            elif opcode == 99:
                self.stop()

            


if __name__ == '__main__':
    code_proc = IntCodeComputer_v2()
    code_proc.start()