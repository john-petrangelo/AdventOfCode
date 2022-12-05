import re
from termcolor import colored
from math import copysign, ceil, sqrt


DOT = '.'
HASH = '#'


def read_input(filename):
    with open(filename) as f:
        # Read the algorithm
        algorithm = f.readline().strip()

        # Read the blank line
        f.readline()

        image = []
        while True:
            line = f.readline().strip()
            if not line:
                break
            image.append([DOT, DOT] + [c for c in line] + [DOT, DOT])

        print_image(image)

        dot_row = [DOT for i in range(len(image[0]))]
        image = [dot_row, dot_row] + image + [dot_row, dot_row]

        print(f"algorithm contains {len(algorithm)} characters")
        print(f"Padded image is {len(image)} rows tall and {len(image[0])} columns wide")
        print_image(image)

        return algorithm, image


def print_image(image):
    [print("".join(row)) for row in image]


def pixel(row, col, image):
    if (not 0 < row < len(image)) or (not 0 < col < len(image[0])):
        return '.'
    return image[row][col]


def enhance(algorithm, image):
    new_image = []
    for row in range(1, len(image)-1):
        new_row = [DOT, DOT]
        for col in range(1, len(image[0])-1):
            bin_num = 0
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    bin_num <<= 1
                    bit = 1 if image[row + i][col + j] == '#' else 0
                    bin_num |= bit
            new_pixel = algorithm[bin_num]
            # print(f"{row + i},{col + j} -- {bin_num} --> {new_pixel}")
            new_row += new_pixel
        new_image.append(new_row + [DOT, DOT])

    dot_row = [DOT for i in range(len(new_image[0]))]
    new_image = [dot_row, dot_row] + new_image + [dot_row, dot_row]
    print_image(new_image)

    return new_image


def count_lit_pixels(image):
    total = 0
    for row in range(len(image)):
        for col in range(len(image[0])):
            if image[row][col] == HASH:
                total += 1
    return total


def main():
    print("========== Reading input file ==========")
    algorithm, image = read_input("test20.txt")

    print("========== Part 1 ==========")
    image2 = enhance(algorithm, image)
    print()
    image3 = enhance(algorithm, image2)

    result = count_lit_pixels(image3)
    print(f"There are {colored(str(result), 'green')} lit pixels in the resulting image")

    print("========== Part 2 ==========")


if __name__ == '__main__':
    main()
