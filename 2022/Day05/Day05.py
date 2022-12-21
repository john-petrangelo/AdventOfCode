def read_file(filename):
    stacks = [[] for _ in range(9)]
    procedures = []

    with open(filename) as f:
        # Read the stacks
        for line in f:
            if line[1] == "1":
                # print("Found column labels")
                break
            index = 0
            while line:
                # print(f"line={line.rstrip()}=")
                letter = line[1]
                if letter != ' ':
                    # print(f"Adding {letter} to stack {index}")
                    stacks[index].append(letter)
                index += 1
                line = line[4:]

        # Flip all of the stacks, we read the top-to-bottom
        for index in range(9):
            stacks[index].reverse()

        # Read the blank line separating stacks from procedures
        _ = f.readline()

        # Read the procedures
        for line in f:
            line = line.strip()
            parts = line.split(" ")
            procedures.append((int(parts[1]), int(parts[3]), int(parts[5])))
        print(f"Found {len(procedures)} procedures")

    return stacks, procedures


def part_1(filename):
    print(f"========================================")
    print(f"Running part 1 with file {filename}")

    stacks, procedures = read_file(filename)

    for p in procedures:
        print(f"Procedure: {p}")
        count, from_stack, to_stack = p
        print(f"BEFORE from:{stacks[from_stack-1]}  to:{stacks[to_stack-1]}")
        for _ in range(count):
            stacks[to_stack-1].append(stacks[from_stack-1].pop())
        print(f"AFTER  from:{stacks[from_stack - 1]}  to:{stacks[to_stack - 1]}")

    answer = ""
    for index in range(9):
        if stacks[index]:
            print(f"Top of stack {index} is {stacks[index][-1]}")
            answer += stacks[index][-1]
        else:
            print(f"Stack {index} is empty")
            answer += " "
    print(f"Stack tops are {answer}")


def part_2(filename):
    print(f"========================================")
    print(f"Running part 2 with file {filename}")

    stacks, procedures = read_file(filename)

    for p in procedures:
        print(f"Procedure: {p}")
        count, from_stack, to_stack = p
        print(f"BEFORE from:{stacks[from_stack-1]}  to:{stacks[to_stack-1]}")
        crates = []
        for _ in range(count):
            crates.append(stacks[from_stack-1].pop())
        crates.reverse()
        stacks[to_stack - 1].extend(crates)
        print(f"AFTER  from:{stacks[from_stack - 1]}  to:{stacks[to_stack - 1]}")

    answer = ""
    for index in range(9):
        if stacks[index]:
            print(f"Top of stack {index} is {stacks[index][-1]}")
            answer += stacks[index][-1]
        else:
            print(f"Stack {index} is empty")
            answer += " "
    print(f"Stack tops are {answer}")


part_1("Day05_example.txt")
part_1("Day05.txt")

part_2("Day05_example.txt")
part_2("Day05.txt")


