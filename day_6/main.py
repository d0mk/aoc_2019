def load_data():
    with open('day_6/input.txt') as data:
        return data.readlines()


def prepare_connections():
    pairs = [tuple(pair.strip().split(')')) for pair in load_data()]
    return {right : left for left, right in pairs}


def count_orbits():
    connections = prepare_connections()
    orbits = 0

    def traverse(obj):
        if connections[obj] == 'COM':
            return 1
        return 1 + traverse(connections[obj])

    for obj in connections:
        orbits += traverse(obj)

    return orbits


if __name__ == '__main__':
    print(count_orbits())