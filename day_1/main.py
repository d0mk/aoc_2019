def load_data():
    with open('day_1/input.txt') as data:
        return [int(mass) for mass in data]
    

def total_fuel(mass):
    final_mass = 0

    while True:
        mass = mass // 3 - 2

        if mass > 0:
            final_mass += mass
        else:
            return final_mass


def sum_of_fuel():
    masses = load_data()

    fuel_1 = [mass // 3 - 2 for mass in masses]
    fuel_2 = [total_fuel(mass) for mass in masses]
    
    return sum(fuel_1), sum(fuel_2)


if __name__ == '__main__':
    print(sum_of_fuel())