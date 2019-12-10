import math

def load_data():
    with open('day_10/input.txt', 'r') as f:
        data = [line.strip() for line in f.readlines()]
    return [(x, y) for y, _ in enumerate(data) for x, _ in enumerate(data[y]) if data[y][x] == '#']
    

def angle(origin, target):
    return math.atan2(origin[0] - target[0], origin[1] - target[1])


def part_1():
    asteroid_count = {}
    asteroids = load_data()

    for asteroid in asteroids:
        candidates = asteroids[:]
        candidates.remove(asteroid)

        angles = [angle(asteroid, target) for target in candidates]

        num_of_asteroids = len(set(angles))
        asteroid_count[asteroid] = num_of_asteroids

    print(f'Max asteroids: {max(asteroid_count.values())}')


if __name__ == '__main__':
    part_1()