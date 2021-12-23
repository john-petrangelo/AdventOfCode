from copy import deepcopy

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
            print(f"line={line} number={number}")

            if line:
                print(f"FAILED, expected line to be empty after parsing but instead got {line}")

        return numbers


# n is a number
# path is an array of 0/1 for left/right
def get_node(n, path):
    print(f"get_node n={n} path={path}")
    while len(path) > 1:
        print(f"get_node loop node={n} path={path}")
        n = n[path[0]]
        path.pop(0)
    # return n[path[0]]
    return n


# n is a number
# path is an array of 0/1 for left/right
# value is the new value to store at this node
def set_node(n, path, value):
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


def explode_left(n, path):
    right = get_node(n, path + [LEFT])
    print(f"explode_left path={path}")

    # TODO
    return


def explode_right(n, path):
    right = get_node(n, path + [RIGHT])
    print(f"explode_right path={path}")

    # TODO
    return


def reduce(n, path=None):
    if path is None:
        path = []

    I = " " * (len(path)+1)

    print(f"{I}reduce n={n} path={path}")
    if get_node(n, path) is not list:
        # The node is not a list, done with this path
        return False

    if len(path) < 4:
        # Not deep enough yet, keep digging
        # Reduce the left node, if it explodes, we're done
        if reduce(n, path + [LEFT]):
            return True

        # Reduce the right node, if it explodes, we're done
        if reduce(n, path + [RIGHT]):
            return True
    else:
        # We're nested three deep, peek into the fourth level and explode if needed
        # Is the left ready to explode?
        print(f"{I}Checking if should explode n={n}")
        if get_node(n, path + [LEFT]) is list:
            explode_left(n, path)
            return True

        # Is the right ready to explode?
        if get_node(n, path + [RIGHT]) is list:
            explode_right(n, path)
            return True

    return False


def main():
    print("========== Reading input ==========")
    numbers = read_input("test18a.txt")
    # numbers = read_input("input18.txt")
    print(f"Finished reading {len(numbers)} numbers")
    [print(f"{number}") for number in numbers]

    magnitude = None
    print(f"Magnitude of final sum is {magnitude}")

    # Temporary test
    n1 = [[[[4, 3], 4], 4], [7, [[8, 4], 9]]]
    n2 = [1, 1]
    nsum = add(n1, n2)
    print(f"Test sum: {nsum}")

    # print(add(numbers[0], numbers[1]))
    # print(add(numbers[0], numbers[1]))


if __name__ == '__main__':
    main()
