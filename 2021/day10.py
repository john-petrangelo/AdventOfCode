# For each opening bracket, the matching closing bracket
pairs = {
    "(": ")",
    "[": "]",
    "{": "}",
    "<": ">",
}

# The scores assigned to each bracket type for part 1
scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

# The scores assigned to each bracket type for part 2
scores2 = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


def read_input(filename):
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]
        print(f"Read {len(lines)} nav system lines")

        return lines


def check_line1(line):
    stack = []
    for c in line:
        if c in pairs:
            stack.append(pairs[c])
        elif stack[-1] == c:
            stack.pop()
        else:
            # print(f"Line corrupt, score {scores[c]}")
            return scores[c]

    # Either the line was valid or incomplete, either way return 0
    return 0


def part1(lines):
    total = 0
    for line in lines:
        total += check_line1(line)

    print(f"Part 1 total {total}")


def check_line2(line):
    stack = []
    for c in line:
        if c in pairs:
            stack.append(pairs[c])
        elif stack[-1] == c:
            stack.pop()
        else:
            # print(f"Line corrupt, discarded")
            return 0

    # Either the line was valid or incomplete
    if stack:
        total = 0;
        while stack:
            c = stack.pop()
            total = total * 5 + scores2[c]
            # print(f"Line was incomplete, score {scores2[c]} for {c}, total {total}")
        return total

    print("Line valid")
    return 0


def part2(lines):
    totals = []
    for line in lines:
        score = check_line2(line)
        if score:
            totals.append(score)

    totals.sort()
    print(f"There are {len(totals)} scores, midpoint is {len(totals)//2}")
    print(f"Part 2 middle score {totals[len(totals)//2]}")


def main():
    lines = read_input("input10.txt")
    part1(lines)
    print()
    part2(lines)


if __name__ == '__main__':
    main()
