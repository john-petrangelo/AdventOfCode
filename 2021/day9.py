lines = []
n_rows = 0
n_cols = 0


def read_input(filename):
    global lines, n_rows, n_cols
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
        n_rows = len(lines)
        n_cols = len(lines[0])
        print(f"Read map with {n_rows} rows and {n_cols} cols")


def print_map():
    global lines, n_rows, n_cols
    print("*" * (n_cols + 2))
    for line in lines:
        print(f"*{line}*")
    print("*" * (n_cols + 2))


def get(row, col):
    global n_rows, n_cols
    if (not 0 <= row < n_rows) or (not 0 <= col < n_cols):
        return 100
    else:
        return int(lines[row][col])


def part1():
    total = 0
    low_points = set()
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            center = get(row, col)
            above = get(row-1, col)
            below = get(row+1, col)
            left = get(row, col-1)
            right = get(row, col+1)
            if center < above and center < below and center < left and center < right:
                total += center + 1
                low_points.add((row, col))
    print(f"Part 1: Sum of risk levels of low points = {total}")


def part2():
    print("Part 2: not yet written")



def main():
    read_input("input9.txt")
    part1()
    part2()


if __name__ == '__main__':
    main()
