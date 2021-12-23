from termcolor import colored


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

    print(f"get_node n={n} path={path} ", end="")
    path = path.copy()
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
    # reduce(number)
    return number


def traverse_up(n, path, direction):
    print(f"traverse_up path={path} direction={direction}")

    # If the path is empty, there is no neighbor
    if not path:
        print("traverse_up path is empty")
        return path

    # If the path has one element, then don't go up anymore
    if len(path) == 1 and path[-1] == direction:
        print("traverse_up path has one element, stop climbing")
        return []

    # If this node is on the traverse-direction (LEFT or RIGHT) of the parent, keep climbing
    parent_path = path[:-1]
    child_direction = parent_path[-1]
    if child_direction == direction:
        print("traverse_up same side, climbing up")
        return traverse_up(n, parent_path, direction)

    # We've found the pivotal ancestor
    print(f"traverse_up found pivotal ancestor path={parent_path}")
    return parent_path


def traverse_down(n, path, direction):
    print(f"traverse_down path={path} direction={direction}")

    # If it's an integer, we found it
    node = get_node(n, path)
    if type(node) is int:
        print(f"traverse_down found value={node}")
        return path

    # Otherwise, continue down in the desired direction (LEFT or RIGHT)
    return traverse_down(n, path + [direction], direction)


def next_node(n, path, direction):
    print(f"next_node path={path} direction={direction}")
    if direction == LEFT:
        other_direction = RIGHT
    else:
        other_direction = LEFT

    # Special case, if the next neighbor is in the same pair
    if path[-1] != direction:
        new_path = path[:-1] + [direction]
        node = get_node(n, new_path)
        print(f"next_node switching to the other node in pair, type={type(node)}")
        if type(node) is int:
            return new_path
        else:
            return traverse_down(n, new_path, other_direction)

    # Look up and <direction> until you are a <other-direction> child or hit root.
    # If you hit root, then there is no neighbor on that side
    ancestor = traverse_up(n, path, direction)
    print(f"next_node found ancestor ancestor={ancestor}")
    if not ancestor:
        print(f"next_node no neighbor found")
        return []

    # We have the pivotal ancestor, now look down the other side of the pair.
    # If the other side is an int, we're done.
    other_path = ancestor[:-1] + [direction]
    node = get_node(n, other_path)
    if type(node) is int:
        return other_path

    # Choose the <direction> child of the ancestor, now look down and
    # <other direction> until you hit an integer
    new_path = traverse_down(n, other_path + [other_direction], other_direction)
    print(f"next_node new_path={new_path}")
    return new_path


def explode_left(n, path):
    print(f"explode_left n={n} path={path}")

    left = path
    while left:
        left = node_on_left(n, left)
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


def verify(n, path, expected_left=None, expected_right=None):
    print(colored(f"number={n}  path={path}", "green"))
    print(colored(f"Looking for left neighbor for path {path}", "green"))
    next_path = next_node(n, path, LEFT)
    print(colored(f"Left neighbor for path {path} ({get_node(n, path)}) is {next_path} ({get_node(n, next_path)})",
                  "grey", "on_green"))
    print(colored(f"expected {expected_left}", "green" if next_path == expected_left else "red"))
    print(colored(f"Looking for right neighbor for path {path}", "green"))
    next_path = next_node(n, path, RIGHT)
    print(colored(f"right neighbor for path {path} ({get_node(n, path)}) is {next_path} ({get_node(n, next_path)})",
                  "grey", "on_green"))
    print(colored(f"expected {expected_right}", "green" if next_path == expected_right else "red"))


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

    verify(nsum, [1, 0], [0, 1, 1, 1], [1, 1])
    verify(nsum, [1, 1], [1, 0], [])
    verify(nsum, [0, 1, 0], [0, 0, 1], [0, 1, 1, 0, 0])
    verify(nsum, [0, 1, 1, 0, 1], [0, 1, 1, 0, 0], [0, 1, 1, 1])
    verify(nsum, [0, 1, 1, 0, 0], [0, 1, 0], [0, 1, 1, 0, 1])
    verify(nsum, [0, 0, 0, 0, 0], [], [0, 0, 0, 0, 1])
    verify(nsum, [0, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 0, 1])


if __name__ == '__main__':
    main()
