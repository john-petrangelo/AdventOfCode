def read_input(filename):
    with open(filename) as f:
        dots = set()
        folds = []
        while True:
            line = f.readline().strip()
            if not line:
                break
            x, y = line.split(",")
            dots.add((int(x), int(y)))

        while True:
            line = f.readline().strip()
            if not line:
                break
            fold_words = line.split(" ")
            fold_axis, fold_line = fold_words[2].split("=")
            folds.append((fold_axis, int(fold_line)))

        return dots, folds


def fold_x(dots, fold_line):
    new_dots = set()
    discarded_dots = set()

    # Copy/mirror dots from the left to the right
    for x, y in dots:
        if x < fold_line:
            new_x = fold_line + (fold_line - x)
            new_dots.add((new_x, y))
            discarded_dots.add((x, y))

    # Add the new mirrored dots and remove the old dots
    new_dots = (dots | new_dots) - discarded_dots

    # We've moved all of the dots to the right side of the fold, now shift them all back to 0
    shifted_dots = set()
    for x, y in new_dots:
        shifted_dots.add((x - (fold_line+1), y))

    return shifted_dots


def fold_y(dots, fold_line):
    new_dots = set()
    discarded_dots = set()

    # Copy/mirror dots from the bottom to the top
    for x, y in dots:
        if y > fold_line:
            new_y = fold_line - (y - fold_line)
            new_dots.add((x, new_y))
            discarded_dots.add((x, y))

    return (dots | new_dots) - discarded_dots


def get_page_size(dots):
    max_x = 0
    max_y = 0
    for x, y in dots:
        max_x = max(x, max_x)
        max_y = max(y, max_y)

    return max_x, max_y


def print_page(dots):
    max_x, max_y = get_page_size(dots)

    rows = []
    for y in range(max_y+1):
        rows.append([" " for x in range(max_x+1)])

    for x,y in dots:
        rows[y][x] = "#"

    for row in rows:
        print("".join(row))


def main():
    print("========== Reading input ==========")
    dots, folds = read_input("input13.txt")
    print(f"Read complete, paper contains {len(dots)} dots, will fold {len(folds)} times")

    print("========== Folding ==========")
    n = 0
    for (fold_axis, fold_line) in folds:
        n += 1
        print(f"Fold {n} is along {fold_axis} axis at line {fold_line}")
        if fold_axis == "x":
            dots = fold_x(dots, fold_line)

        if fold_axis == "y":
            dots = fold_y(dots, fold_line)

        print(f"After fold there are {len(dots)} dots")

    print("========== Displaying page ==========")
    print_page(dots)

    print("========== Displaying flipped page ==========")
    max_x, _ = get_page_size(dots)
    dots = fold_x(dots, max_x+1)
    print_page(dots)


if __name__ == '__main__':
    main()
