from termcolor import colored

cavern = []
num_rows = 0
num_cols = 0
lowest_risk = -1


def read_input(filename):
    global cavern, num_rows, num_cols, lowest_risk
    with open(filename) as f:
        cavern = [line.strip() for line in f.readlines()]
        num_rows = len(cavern)
        num_cols = len(cavern[0])
        # num_rows = 10
        # num_cols = num_rows
        lowest_risk = (num_rows + num_cols) * 10
        print(f"Read cavern with {num_rows} rows and {num_cols} columns")


colors = ["unused", "white", "magenta", "blue", "cyan", "green", "yellow", "red", "grey", "grey"]


def print_cavern(path=None):
    if path is None:
        path = []
    global cavern
    for row in range(num_rows):
        s = ""
        for col in range(num_cols):
            c = cavern[row][col]
            if (row, col) in path:
                c = colored(c, "red")
            s += c
        print(s)


def risk(path):
    if not path:
        # No path, return a risk bigger than all actual risks
        return (num_rows + num_cols) * 10
    return sum([int(cavern[row][col]) for row, col in path[1:]])


def seek(partial_path, next_position):
    global lowest_risk

    # print(f"seek partial_path={partial_path} next_position={next_position}")
    # print(f"seek path len={len(partial_path):3} next_position={next_position}")

    row, col = next_position

    # If the position is outside the cavern, reject
    if (not 0 <= row < num_rows) or (not 0 <= col < num_cols):
        # print("Out of bounds")
        return None

    # If we've been here before, the path is invalid
    if next_position in partial_path:
        # print("Already been here")
        return None

    # Add the new position to the path
    new_path = partial_path.copy()
    new_path.append(next_position)
    new_path_risk = risk(new_path)

    if next_position == (num_rows-1, num_cols-1):
        print(f"Complete path, len={len(new_path)}, risk={new_path_risk}")
        if new_path_risk < lowest_risk:
            lowest_risk = new_path_risk
            print(f"New lowest risk={lowest_risk}")
            print_cavern(new_path)
        return None

    # If the new path is riskier than the current lowest, it's already invalid
    # print(f"new_path={new_path}")
    if len(new_path) > 1 and new_path_risk >= lowest_risk:
        # print("Too risky")
        return None

    # Path is still valid. Check right, down, left, up.
    # print(f"Looking right from {next_position} to {(row, col+1)}")
    path_right = seek(new_path, (row, col+1))
    # print(f"Looking down")
    path_down = seek(new_path, (row+1, col))
    # print(f"Looking left")
    path_left = seek(new_path, (row, col-1))
    # print(f"Looking up")
    path_up = seek(new_path, (row-1, col))

    return min([path_right, path_down, path_left, path_up], key=risk)


def main():
    global lowest_risk

    read_input("input15.txt")
    print_cavern()

    print("========== Part 1 ==========")
    # Start with an initial risk that we know we can beat
    lowest_risk = (num_rows + num_cols) * 10
    path = []
    path = seek(path, (0, 0))
    print(f"Final path: {path}")
    print(f"Lowest risk: {lowest_risk}")

    print("========== Part 2 ==========")
    print("NYI")


if __name__ == '__main__':
    main()
