puzzle_input = (272091, 815432 + 1)


def validate_1(pwd):
    if all(pwd[i] <= pwd[i + 1] for i in range(len(pwd) - 1)):
        return any(pwd[i] == pwd[i + 1] for i in range(len(pwd) - 1))
    return False


def validate_2(pwd):
    if all(pwd[i] <= pwd[i + 1] for i in range(len(pwd) - 1)):
        digit_count = {digit : pwd.count(digit) for digit in pwd}
        doubles = {d : c for d, c in digit_count.items() if c == 2}

        if len(doubles) == 0:
            return False

        for digit in doubles:
            i = pwd.index(digit)
            if pwd[i - 1] == digit or pwd[i + 1] == digit:
                return True
                
        return False


import time

def main():
    matched_1 = 0
    matched_2 = 0

    for pwd in range(*puzzle_input):
        if validate_1(str(pwd)):
            matched_1 += 1
        if validate_2(str(pwd)):
            matched_2 += 1

    print(f'Matched passwords (part 1): {matched_1}')
    print(f'Matched passwords (part 2): {matched_2}')


if __name__ == '__main__':
    main()