def part_1():
    width = 25
    height = 6
    layer_size = width * height

    with open('day_8/input.txt', 'r') as f:
        data = f.read()

    layers = [data[i : i + layer_size] for i in range(0, len(data) - layer_size, layer_size)]
    target_layer = min(layers, key=lambda x : x.count('0'))

    print(f'Part 1 result: {target_layer.count("1") * target_layer.count("2")}')


if __name__ == '__main__':
    part_1()