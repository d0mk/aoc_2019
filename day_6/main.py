def count_orbits(connections):
    def traverse(obj):
        if connections[obj] == 'COM':
            return 1
        return 1 + traverse(connections[obj])

    orbits = 0

    for obj in connections:
        orbits += traverse(obj)

    return orbits


def orbital_transfers(connections):
    def build_path(path, obj):
        if obj == 'COM':
            return path + ['COM']
        return path + [obj] + build_path(path, connections[obj])

    you_com = build_path([], 'YOU')
    san_com = build_path([], 'SAN')

    def first_common_object():
        for a in you_com:
            for b in san_com:
                if a == b: return a

    first_common = first_common_object()
    i = you_com.index(first_common)
    j = san_com.index(first_common)
    num_of_transfers = len(you_com[:i]) + len(san_com[:j]) - 2

    return num_of_transfers


def main():
    with open('day_6/input.txt') as data:
        pairs = [tuple(pair.strip().split(')')) for pair in data.readlines()]
        connections = {right : left for left, right in pairs}

    print(f'Total orbits: {count_orbits(connections)}')
    print(f'Orbital transfers needed: {orbital_transfers(connections)}')


if __name__ == '__main__':
    main()