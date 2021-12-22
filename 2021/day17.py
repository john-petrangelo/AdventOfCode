import re
from termcolor import colored
from math import copysign, ceil, sqrt


START_CHAR = colored("S", "grey", "on_green")
PROBE_CHAR = colored("#", "white", "on_red")
TARGET_CHAR = colored("T", "grey", "on_yellow")
OPEN_CHAR = "."


def read_input(filename):
    with open(filename) as f:
        line = f.readline().strip()

        pattern = "target area: x=(-?\\d+)\\.\\.(-?\\d+), y=(-?\\d+)\\.\\.(-?\\d+)"
        print(f"pattern={pattern}")
        print(f"line={line}")
        m = re.match(pattern, line)
        print(f"m={m}")
        target = {
            "x1": int(m.group(1)),
            "x2": int(m.group(2)),
            "y1": int(m.group(3)),
            "y2": int(m.group(4)),
        }
        return target


def bounding_box(target, states):
    # Consider the target area, starting position (0,0) and probe positions
    box = {
        "x1": min([] + [0, target["x1"]] + [pos[0] for pos in states]),
        "x2": max([] + [0, target["x2"]] + [pos[0] for pos in states]),
        "y1": min([] + [0, target["y1"]] + [pos[1] for pos in states]),
        "y2": max([] + [0, target["y2"]] + [pos[1] for pos in states]),
    }

    return box


def print_trench(target, states):
    box = bounding_box(target, states)
    for y in range(box["y2"] + 1, box["y1"] - 2, -1):
        line = ""
        for x in range(box["x1"] - 1, box["x2"] + 2):
            if (x, y) == (0, 0):
                line += START_CHAR
            elif (x, y) in [(state[0], state[1]) for state in states]:
                line += PROBE_CHAR
            elif in_target(target, x, y):
                line += TARGET_CHAR
            else:
                line += OPEN_CHAR
        print(line)


def in_target(target, x, y):
    return y in range(target["y1"], target["y2"] + 1) and \
         x in range(target["x1"], target["x2"] + 1)


def step(px, py, vx, vy):
    px += vx
    py += vy
    if vx != 0:
        vx -= int(copysign(1, vx))
    vy -= 1
    return px, py, vx, vy


def launch_probe(target, vx, vy):
    states = [(0, 0, vx, vy)]
    while True:
        next_step = step(*states[-1])
        if next_step[1] < target["y1"]:
            break
        states.append(next_step)
        if in_target(target, states[-1][0], states[-1][1]):
            break

    return states, in_target(target, states[-1][0], states[-1][1])


def main():
    print("========== Reading input file ==========")
    target = read_input("input17.txt")

    print("========== Part 1 ==========")
    lower_x = ceil((-1 + sqrt(1 + 8 * target['x1'])) / 2)
    upper_x = target['x2']
    lower_y = target['y1']
    upper_y = -(target['y1'] + 1)

    states, _ = launch_probe(target, lower_x, upper_y)

    # print_trench(target, states)
    print(f"{lower_x} <= vx <= {upper_x}, {lower_y} <= vy <= {upper_y}")

    max_height = max([state[1] for state in states])
    print(f"Optimal vx={lower_x}, vy={upper_y}")
    print(f"ANSWER: max_height={max_height}")

    print("========== Part 2 ==========")
    lower_x = ceil((-1 + sqrt(1 + 8 * target['x1'])) / 2)
    upper_x = target['x2']
    lower_y = target['y1']
    upper_y = -(target['y1'] + 1)

    num_hits = 0
    num_tries = (upper_x+1 - lower_x) * (upper_y+1 - lower_y)
    progress_step = num_tries // 100
    try_num = 0
    print("|" + "---------|" * 10)
    for x in range(lower_x, upper_x+1):
        for y in range(lower_y, upper_y+1):
            try_num += 1
            if try_num % progress_step == 0:
                print(".", end="")
            _, hit = launch_probe(target, x, y)
            if hit:
                # print(f"hit {(x, y)}")
                num_hits += 1
    print()

    print(f"ANSWER: num_hits={num_hits}")


if __name__ == '__main__':
    main()
