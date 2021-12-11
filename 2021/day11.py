from copy import deepcopy
from termcolor import colored


def read_input(filename):
    with open(filename) as f:
        octopuses = []
        while True:
            line = f.readline().strip()
            if not line:
                break
            octopuses.append([int(octopus) for octopus in line])

        print(f"Read octopuses map:")
        print_octopuses(octopuses)
        return octopuses


def print_octopuses(octopuses):
    for line in octopuses:
        s = ""
        for energy in line:
            if energy == 0:
                s += colored(energy, "yellow")
            elif energy == 9:
                s += colored(energy % 10, "green")
            elif energy < 0:
                s += colored('.', "red")
            else:
                s += str(energy)
            s += " "
        print(s)


def inc(octopuses, row, col):
    # Increment this octopus energy by one. Flash if high enough.
    octopuses[row][col] += 1
    if octopuses[row][col] > 9:
        return flash(octopuses, row, col)
    return 0


def flash(octopuses, row, col):
    if (not 0 <= row < 10) or (not 0 <= col < 10):
        # Out of bounds, just ignore it
        return 0

    if octopuses[row][col] < 0:
        # Already flashed, just ignore it
        return 0

    # Flash!
    num_flashes = 1
    octopuses[row][col] = -100
    for nr in filter(lambda i: 0 <= i < len(octopuses), [row-1, row, row+1]):
        for nc in filter(lambda i: 0 <= i < len(octopuses[0]), [col-1, col, col+1]):
            if nr != row or nc != col:
                num_flashes += inc(octopuses, nr, nc)

    return num_flashes


def part1(octopuses):
    octopuses = deepcopy(octopuses)
    total_flashes = 0

    num_steps = 100

    for step in range(num_steps):
        # Increment all octopuses by 1, check for flashes
        for row in range(len(octopuses)):
            for col in range(len(octopuses[row])):
                # print(f"Inc {(row, col)}, was {octopuses[row][col]}")
                total_flashes += inc(octopuses, row, col)

        # Reset flashed octopuses to 0
        for row in range(len(octopuses)):
            for col in range(len(octopuses[row])):
                if octopuses[row][col] < 0:
                    octopuses[row][col] = 0

        print(f"After {step+1} steps:")
        print_octopuses(octopuses)

    print(f"Part 1: {total_flashes} flashes")


def part2(octopuses):
    octopuses = deepcopy(octopuses)
    total_flashes = 0

    num_steps = 0

    while True:
        num_steps += 1

        # Increment all octopuses by 1, check for flashes
        for row in range(len(octopuses)):
            for col in range(len(octopuses[row])):
                # print(f"Inc {(row, col)}, was {octopuses[row][col]}")
                total_flashes += inc(octopuses, row, col)

        # Reset flashed octopuses to 0
        for row in range(len(octopuses)):
            for col in range(len(octopuses[row])):
                if octopuses[row][col] < 0:
                    octopuses[row][col] = 0

        target_energy = octopuses[0][0]
        is_solution = True
        for row in octopuses:
            for octopus in row:
                if octopus != target_energy:
                    is_solution = False
                    break
            if not is_solution:
                break

        if is_solution:
            print(f"Part 2: All octopuses will flash in step {num_steps}")
            return


def main():
    octopuses = read_input("input11.txt")
    part1(octopuses)
    part2(octopuses)


if __name__ == '__main__':
    main()
