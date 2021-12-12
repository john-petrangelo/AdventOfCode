from collections import Counter
from termcolor import colored

def add_cave_pair(caves, cave1, cave2):
    if cave1 not in caves:
        caves[cave1] = set()
    if cave2 not in caves:
        caves[cave2] = set()

    caves[cave1].add(cave2)
    caves[cave2].add(cave1)


def read_input(filename):
    with open(filename) as f:
        caves = {}
        gv = "graph {"
        while True:
            line = f.readline().strip()
            if not line:
                break
            cave1, cave2 = line.split("-")
            add_cave_pair(caves, cave1, cave2)
            gv += f"{cave1}--{cave2};"
        gv += "}"

        print(f"Read cave map containing {len(caves)} caves:\n{caves}")
        print(f"Graph vis: {gv}")
        print()
        return caves


def is_small_cave(cave):
    return cave[0] == cave[0].lower()


def enter_cave_part1(caves, partial_path, cave):
    # print(f"{partial_path} => '{cave}'")

    # If the next cave is "start", reject
    if partial_path != [] and cave == "start":
        # print(colored("Rejected return to 'start'", "red"))
        return []

    # If the next cave is "end" then we've found a complete path
    if cave == "end":
        # print(colored(f"Completed path: {partial_path + [cave]}", "green"))
        return [partial_path + [cave]]

    # If it's a small cave, one cave can be
    if is_small_cave(cave) and cave in partial_path:
        # print(colored(f"Small cave '{cave}' rejected", "red"))
        return []

    # Enter each of the caves this cave connects to
    complete_path = []
    for next_cave in caves[cave]:
        complete_path.extend(enter_cave_part1(caves, partial_path + [cave], next_cave))
    return complete_path


# Return true if we have already visited any small cave twice
def has_visited_any_small_twice(path):
    visited_caves = set()
    special_caves = ["start", "end"]

    # We're only going to look at small caves
    small_caves = filter(lambda c: is_small_cave(c) and c not in special_caves, path)

    for cave in small_caves:
        if cave in visited_caves:
            return True
        visited_caves.add(cave)

    # No re-visits
    return False


def enter_cave_part2(caves, partial_path, cave):
    # print(f"{partial_path} => '{cave}'")

    # If the next cave is "start", reject
    if partial_path != [] and cave == "start":
        # print(colored("Rejected return to 'start'", "red"))
        return []

    # If the next cave is "end" then we've found a complete path
    if cave == "end":
        # print(colored(f"Completed path: {partial_path + [cave]}", "green"))
        return [partial_path + [cave]]

    # If it's a small cave, we can only visit twice if no other small cave has been visited twice,
    # otherwise we can only visit this cave once
    if is_small_cave(cave) and cave in partial_path:
        if has_visited_any_small_twice(partial_path):
            # print(colored(f"Reject small cave {cave}", "red"))
            return []

    # Enter each of the caves this cave connects to
    complete_path = []
    for next_cave in caves[cave]:
        complete_path.extend(enter_cave_part2(caves, partial_path + [cave], next_cave))
    return complete_path


def part1(caves):
    print("========== Starting part 1 ==========")
    complete_paths = enter_cave_part1(caves, [], "start")
    print(f"Finished part 1, found {len(complete_paths)} paths")
    # [print(f"  {path}") for path in sorted(complete_paths)]


def part2(caves):
    print("========== Starting part 2 ==========")
    complete_paths = enter_cave_part2(caves, [], "start")
    print(f"Finished part 2, found {len(complete_paths)} paths")
    # [print(f"  {path}") for path in sorted(complete_paths)]


def main():
    caves = read_input("input12.txt")
    part1(caves)
    part2(caves)


if __name__ == '__main__':
    main()
