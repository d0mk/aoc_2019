from PIL import Image

with open('day_8/input.txt', 'r') as f:
    data = f.read()

width = 25
height = 6
layer_size = width * height
layers = [data[i : i + layer_size] for i in range(0, len(data) - layer_size, layer_size)]


def part_1():
    target_layer = min(layers, key=lambda x : x.count('0'))
    print(f'Part 1 result: {target_layer.count("1") * target_layer.count("2")}')


def part_2():
    image = [pixel for pixel in layers[0]]

    # n - layer number, i - index of pixel in array
    def find_pixel_color(n, i):
        if n < len(layers) - 1:
            return layers[n][i] if layers[n][i] != '2' else find_pixel_color(n + 1, i)
        else:
            return layers[n][i]

    for n, layer in enumerate(layers[1:]):
        for i in range(len(layer)):
            if image[i] == '2':
                image[i] = find_pixel_color(n + 1, i)

    image_data = [[image[i * width + j] for j in range(width)] for i in range(height)]

    print('Displaying image...')
    draw_image(image_data)


def draw_image(image_data):
    pixel_size = 10

    img = Image.new('RGBA', (width * pixel_size, height * pixel_size))
    pixels = img.load()

    black = (0, 0, 0, 255)
    white = (255, 255, 255, 255)
    transparent = (0, 0, 0, 0)

    for i in range(height):
        for j in range(width):

            pixel = int(image_data[i][j])

            if pixel == 2:
                pixel = transparent
            else:
                pixel = white if pixel == 1 else black

            for x in range(pixel_size):
                for y in range(pixel_size):
                    pixels[pixel_size * j + y, pixel_size * i + x] = pixel

    img.show()


if __name__ == '__main__':
    part_1()
    part_2()