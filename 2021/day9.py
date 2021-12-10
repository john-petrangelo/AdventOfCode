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
    return low_points


def part2(low_points):
    # List of basins we've discovered so far
    basins = []

    for low_point in low_points:
        # If this low point is already in a known basin, move on
        if True in [low_point in basin for basin in basins]:
            continue

        # The set of points that are part of this basin, starts with only the low_point
        basin = set()

        # Queue of points we need to check neighbors for
        queue = [low_point]

        while queue:
            point = queue.pop()
            if point in basin:
                # We already know about this point
                continue

            row, col = point
            height = get(row, col)
            if height >= 9:
                # This point is not in any basin
                continue

            basin.add(point)
            queue.extend([(row-1, col), (row+1, col), (row, col-1), (row, col+1)])

        basins.append(basin)

    sizes = []
    for basin in basins:
        sizes.append(len(basin))
    sizes.sort(reverse=True)

    result = sizes[0] * sizes[1] * sizes[2]
    print(f"Part 2: Product of sizes of largest three basins is {result}")

    return basins


def main():
    read_input("input9.txt")
    low_points = part1()
    part2(low_points)


if __name__ == '__main__':
    main()
