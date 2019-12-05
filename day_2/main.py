def load_data():
    with open('day_2/input.txt') as data:
        return [int(n) for n in data.readline().split(',')]


class IntCodeComputer:
    def __init__(self, noun_verb=None, data=None):
        self.data = load_data() if data is None else data
        if noun_verb:
            self.data[1], self.data[2] = noun_verb
        self.running = True

    def add(self, in_1, in_2, out):
        self.data[out] = self.data[in_1] + self.data[in_2]

    def multiply(self, in_1, in_2, out):
        self.data[out] = self.data[in_1] * self.data[in_2]

    def stop(self):
        self.running = False

    def result(self):
        return self.data[0]

    def start(self):
        i = 0
        while self.running:
            in_1 = self.data[i + 1]
            in_2 = self.data[i + 2]
            out = self.data[i + 3]

            if self.data[i] == 1:
                self.add(in_1, in_2, out)
            elif self.data[i] == 2:
                self.multiply(in_1, in_2, out)
            elif self.data[i] == 99:
                self.stop()

            i += 4


class InitialStateFinder:
    def __init__(self, match):
        self.match = match
        self.data = load_data()

    def start(self):
        for noun in range(100):
            for verb in range(100):
                int_code = IntCodeComputer((noun, verb), self.data[:])
                int_code.start()

                if int_code.result() == self.match:
                    print(f'Part 2 result code: {100 * noun + verb}')
                    return


if __name__ == '__main__':
    # part 1
    int_code = IntCodeComputer((12, 2))
    int_code.start()
    print(f'Part 1 result code: {int_code.result()}')

    # part 2
    finder = InitialStateFinder(19690720)
    finder.start()