import os

from PIL import Image


BLACK_PIXEL = (0, 0, 0, 255)


def convert_image_to_vline_data(image_path):
    img = Image.open(image_path)
    width, height = img.size
    pixels = img.load()

    result = []

    for x in range(width):
        column = []
        y = 0
        while y < height:
            if pixels[x, y] == BLACK_PIXEL:
                start_y = y
                length = 1
                y += 1
                while y < height and pixels[x, y] == BLACK_PIXEL:
                    length += 1
                    y += 1
                column.append((start_y, length))
            else:
                y += 1
        result.append(column)

    return result


def main():
    data_string = ""

    for path, _, files in os.walk('../assets'):
        for file in files:
            if not file.endswith('.png'):
                continue
            var = file.split('.')[0]
            vline = convert_image_to_vline_data(os.path.join(path, file))
            data_string += f'{var} = {vline}\n'

    with open('../pico/sprites.py', 'w') as file:
        file.write(data_string)


if __name__ == '__main__':
    main()
