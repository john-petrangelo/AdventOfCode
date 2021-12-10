def read_input(filename):
    with open(filename) as f:
        crabs = [int(crab) for crab in f.readline().strip().split(",")[:]]
        print(f"Read {len(crabs)} crabs")

        return crabs


def calc_cost(crabs, position):
    return calc_gauss_cost(crabs, position)


def calc_simple_cost(crabs, position):
    total = 0
    for crab in crabs:
        total += abs(crab - position)
    return total


def calc_gauss_cost(crabs, position):
    total = 0
    for crab in crabs:
        dist = abs(crab - position)
        total += (dist * (dist + 1) // 2)
    return total


def main():
    crabs = read_input("input7.txt")

    lo_crab = min(crabs)
    hi_crab = max(crabs)
    print(f"Starting with lo={lo_crab} and hi={hi_crab}")

    while hi_crab - lo_crab >= 2:
        mid_crab = (lo_crab + hi_crab) // 2
        print(f"{lo_crab}({calc_cost(crabs, lo_crab)}) -> {hi_crab}({calc_cost(crabs, hi_crab)}), mid={mid_crab}")
        cost1 = calc_cost(crabs, mid_crab)
        cost2 = calc_cost(crabs, mid_crab+1)

        if cost1 < cost2:
            hi_crab = mid_crab
        else:
            lo_crab = mid_crab

    lo_cost = calc_cost(crabs, lo_crab)
    hi_cost = calc_cost(crabs, hi_crab)
    final = hi_crab
    if lo_cost < hi_cost:
        final = lo_crab

    print(f"Final position = {final}({calc_cost(crabs, final)})")


if __name__ == '__main__':
    main()
