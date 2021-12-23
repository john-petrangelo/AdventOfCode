LEFT = 0
RIGHT = 1


def parse_number(line):
    # Expect opening bracket
    if line[0] != "[":
        print(f"FAILED, expected number to start with '[', instead got {line}")
        return None, line
    line = line[1:]

    # Now start the left component. Next character should either be an opening bracket or a digit
    if line[0] == "[":
        left, line = parse_number(line)
    elif line[0].isdigit():
        left = int(line[0])
        line = line[1:]
    else:
        print("FAILED, expected left component to be '[' or digit, but wasn't: {line}")
        return None, line

    # Now we expect a comma separating left from right
    if line[0] != ",":
        print(f"FAILED, expected comma to separate left from right but got {line}")
        return None, line
    line = line[1:]

    # Now start the right component. Next character should either be an opening bracket or a digit
    if line[0] == "[":
        right, line = parse_number(line)
    elif line[0].isdigit():
        right = int(line[0])
        line = line[1:]
    else:
        print(f"FAILED, expected right component to be '[' or digit, but wasn't: {line}")
        return None, line

    # Now we expect a closing bracket
    if line[0] != "]":
        print(f"FAILED, expected closing bracket but got {line}")
        return None, line
    line = line[1:]

    # Return the parsed number as well as the remaining line
    number = (left, right)
    reduce(number)
    return number, line


def read_input(filename):
    with open(filename) as f:
        numbers = []
        while True:
            line = f.readline().strip()
            if not line:
                break

            # Parse the line into a number
            print(f"Parsing input line {line}")
            number, line = parse_number(line)
            numbers.append(number)

            if line:
                print(f"FAILED, expected line to be empty after parsing but instead got {line}")

        return numbers


# n is a number
# path is an array of 0/1 for left/right
def get_node(n, path):
    if not path:
        return n

    path = path.copy()
    print(f"get_node n={n} path={path} ", end="")
    while len(path) > 1:
        n = n[path[0]]
        path.pop(0)
    print(f"node={n[path[0]]}")
    return n[path[0]]


# n is a number
# path is an array of 0/1 for left/right
# value is the new value to store at this node
def set_node(n, path, value):
    path = path.copy()
    while len(path) > 1:
        n = n[path[0]]
        path.pop(0)
    n[path[0]] = value


# To add n1 and n2, simply make a new number with n1 on the left and n2 on the right.
# However, then you must immediately reduce the number.
def add(n1, n2):
    number = [n1, n2]
    reduce(number)
    return number


def node_on_left(path):
    if not path:
        return path

    if path[-1] == RIGHT:
        return path[:-1] + [LEFT]

    return path[:-1]


def node_on_right(path):
    if not path:
        return path

    if path[-1] == LEFT:
        return path[:-1] + [RIGHT]

    return path[:-1]


def explode_left(n, path):
    print(f"explode_left n={n} path={path}")

    left = path
    while left:
        left = node_on_left(left)
        node = get_node(n, left)
        if type(node) == int:
            break

    print(f"Explode left to {left} TODO")

    return left


def explode_right(n, path):
    print(f"explode_right path={path}")

    right = path
    while right:
        right = node_on_right(right)
        node = get_node(n, right)
        if type(node) == int:
            break;

    print(f"Explode right to {right} TODO")

    return right


# Traverses the number tree and returns a path to a node that needs
# to explode, otherwise None
def find_exploder(n, path):
    I = str(len(path)) + " " + "  " * (len(path))

    node = get_node(n, path)
    # print(f"{I}find_exploder n={n} path={path} node={get_node(n, path)}")
    if type(node) is not list:
        # The node is not a list, done with this path
        # print(f"{I}Node is not a list: {type(node)}")
        return None

    if len(path) < 4:
        # Not deep enough yet, keep digging
        # Look for an exploder under the left node, if we find one we're done
        # print(f"{I}checking left path={path}")
        exploder_path = find_exploder(n, path + [LEFT])
        if exploder_path:
            return exploder_path

        # Look for an exploder under the right node, if we find one we're done,
        # otherwise we're also done, return either way
        # print(f"{I}checking right")
        exploder_path = find_exploder(n, path + [RIGHT])
        return exploder_path
    else:
        return path


def reduce(n):
    path = find_exploder(n, [])
    print(f"reduce n={n} path={path}")
    if path:
        print(f"Found an exploder at path {path}")
        explode_left(n, path)
        explode_right(n, path)


def main():
    # print("========== Reading input ==========")
    # numbers = read_input("test18a.txt")
    # # numbers = read_input("input18.txt")
    # print(f"Finished reading {len(numbers)} numbers")
    # [print(f"{number}") for number in numbers]
    #
    # magnitude = None
    # print(f"Magnitude of final sum is {magnitude}")

    # Temporary test
    n1 = [[[[4, 3], 4], 4], [7, [[8, 4], 9]]]
    n2 = [1, 1]
    nsum = add(n1, n2)
    print(f"Test sum: {nsum}")

    # print(add(numbers[0], numbers[1]))
    # print(add(numbers[0], numbers[1]))


if __name__ == '__main__':
    main()
