import math
import itertools

with open('day_10/input.txt', 'r') as f:
    data = [line.strip() for line in f.readlines()]
    asteroids = [(x, y) for y, _ in enumerate(data) for x, _ in enumerate(data[y]) if data[y][x] == '#']
    

def get_angle(origin, target):
    return (math.atan2(origin[0] - target[0], origin[1] - target[1]) + 2 * math.pi) % (2 * math.pi)


def get_distance(origin, target):
        x1, y1 = origin
        x2, y2 = target
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def part_1():
    max_asteroids = 0
    location = None

    for asteroid in asteroids:
        candidates = asteroids[:]
        candidates.remove(asteroid)

        angles = [get_angle(asteroid, target) for target in candidates]

        if (num_of_asteroids := len(set(angles))) > max_asteroids:
            max_asteroids = num_of_asteroids
            location = asteroid

    print(f'Max asteroids: {max_asteroids} at {location}')
    return location


def part_2(origin):

    class Asteroid:
        def __init__(self, angle, distance, coords):
            self.angle = angle
            self.dist_to_origin = distance
            self.coords = coords

        def __hash__(self):
            return hash(self.angle)

        def __eq__(self, other):
            if not isinstance(other, type(self)):
                return NotImplemented
            return self.angle == other.angle


    asteroids.remove(origin)
    objects = []

    for target in asteroids:
        angle = get_angle(origin, target)
        distance = get_distance(origin, target)
        objects.append(Asteroid(angle, distance, target))


    def compress(objects):
        objects_set = set(objects)
        distinct_angles = [a.angle for a in objects_set]
        compressed = [[obj for obj in objects if obj.angle == a] for a in distinct_angles]

        compressed.sort(key=lambda x : x[0].angle, reverse=True)

        for i, group in enumerate(compressed):
            group.sort(key=lambda x : x.dist_to_origin)

        return compressed


    objects = compress(objects)
    cycled_angles = itertools.cycle(objects)
    vaporized = 0
    last = None

    while vaporized < 199:
        group = next(cycled_angles)

        if len(group) == 0:
            continue
        else:
            last = group.pop(0)
            vaporized += 1

    print(f'200th asteroid vaporized: {last.coords}')


if __name__ == '__main__':
    location = part_1()
    part_2(location)