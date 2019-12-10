import math


with open('day_10/input.txt', 'r') as f:
    data = [line.strip() for line in f.readlines()]

asteroids = [(x, y) for y, _ in enumerate(data) for x, _ in enumerate(data[y]) if data[y][x] == '#']


def find_asteroid_axes(origin, candidates):
    horizontal_axis = [asteroid for asteroid in candidates if asteroid[1] == origin[1]]
    vertical_axis = [asteroid for asteroid in candidates if asteroid[0] == origin[0]]

    # filter out horizontal and vertical objects
    for asteroid in horizontal_axis:
        candidates.remove(asteroid)

    for asteroid in vertical_axis:
        candidates.remove(asteroid)

    def asteroid_parameters(origin, target):
        x1, y1 = origin
        x2, y2 = target
        a = (y2 - y1) / (x2 - x1)
        b = (y1 * x2 - y2 * x1) / (x2 - x1)
        return a, b

    asteroid_parameters = {asteroid : asteroid_parameters(origin, asteroid) for asteroid in candidates}
    distinct_axes = set(asteroid_parameters.values())
    grouped_by_axes = {}

    for axis in distinct_axes:
        grouped_by_axes[axis] = [asteroid for asteroid in asteroid_parameters.keys() if asteroid_parameters[asteroid] == axis]

    if horizontal_axis:
        grouped_by_axes['horiz'] = horizontal_axis
    
    if vertical_axis:
        grouped_by_axes['vert'] = vertical_axis

    return grouped_by_axes


asteroid_count = {}

for asteroid in asteroids:
    candidates = asteroids[:]
    candidates.remove(asteroid)
    grouped_by_axes = find_asteroid_axes(asteroid, candidates)

    a_x, a_y = asteroid
    count = len(grouped_by_axes)

    # for k, v in grouped_by_axes.items():
    #     print(f'{k}: {v}')

    for key, group in grouped_by_axes.items():
        if len(group) > 1:
            t1 = any(a[0] >= a_x and a[1] >= a_y for a in group)
            t2 = any(a[0] <= a_x and a[1] <= a_y for a in group)
            if t1 and t2:
                count += 1

    asteroid_count[asteroid] = count

best = max(asteroid_count, key=lambda x : asteroid_count[x])
print(best, asteroid_count[best])
