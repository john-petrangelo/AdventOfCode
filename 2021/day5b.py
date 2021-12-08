def print_floor(floor, size):
    for y in range(size):
        line = ""
        for x in range(size):
            line += str(floor[(x, y)]) if (x, y) in floor else "."
        print(line)


def read_input(filename):
    with open(filename) as f:
        # Vents are represented as a pair of pairs, e.g. (x1, y1), (x2, y2)
        vents = []

        max_x = 0
        max_y = 0

        while True:
            line = f.readline().strip()
            if not line:
                break

            coords = line.split(" -> ")
            coord1 = [int(coord) for coord in coords[0].split(",")[:]]
            coord2 = [int(coord) for coord in coords[1].split(",")[:]]
            vents.append([coord1, coord2])
            max_x = max(max_x, coord1[0], coord2[0])
            max_y = max(max_y, coord1[1], coord2[1])

        print(f"There are {len(vents)} vents, max x={max_x}, max y={max_y}")

        return vents


def inc_floor(floor, x, y):
    if (x, y) in floor:
        floor[(x, y)] += 1
    else:
        floor[(x, y)] = 1


def fill_floor(vents):
    floor = {}
    for vent in vents:
        x1 = vent[0][0]
        y1 = vent[0][1]
        x2 = vent[1][0]
        y2 = vent[1][1]

        if x1 == x2:
            # It's vertical
            for y in range(min(y1, y2), max(y1, y2)+1):
                inc_floor(floor, x1, y)
        elif y1 == y2:
            # It's horizontal
            for x in range(min(x1, x2), max(x1, x2)+1):
                inc_floor(floor, x, y1)
        elif x1 < x2 and y1 < y2:
            for x, y in zip(range(x1, x2+1), range(y1, y2+1)):
                # print(f"D1 {x},{y})")
                inc_floor(floor, x, y)
        elif x1 < x2 and y1 > y2:
            for x, y in zip(range(x1, x2+1), range(y1, y2-1, -1)):
                # print(f"D2 {x},{y})")
                inc_floor(floor, x, y)
        elif x1 > x2 and y1 < y2:
            for x, y in zip(range(x1, x2-1, -1), range(y1, y2+1)):
                # print(f"D3 {x},{y})")
                inc_floor(floor, x, y)
        else:
            for x, y in zip(range(x1, x2-1, -1), range(y1, y2-1, -1)):
                # print(f"D4 {x},{y})")
                inc_floor(floor, x, y)

    return floor


def count_danger(floor):
    count = 0
    for point in floor:
        if floor[point] >= 2:
            count += 1
    return count


def main():
    vents = read_input("input5.txt")
    floor = fill_floor(vents)

    # Print the results
    print("\nResults")
    print_floor(floor, 10)
    count = count_danger(floor)
    print(f"There are {count} points with two or more vents")


if __name__ == '__main__':
    main()
