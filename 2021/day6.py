def read_input(filename):
    with open(filename) as f:
        file_fish = [int(fish) for fish in f.readline().strip().split(",")[:]]
        print(f"Starting with {len(file_fish)} fish")
        buckets = [0 for i in range(9)]

        for fish in file_fish:
            buckets[fish] += 1

        return buckets


def simulate_day(buckets):
    mama_fish = buckets[0]
    for i in range(0, 8):
        buckets[i] = buckets[i+1]
    buckets[6] += mama_fish
    buckets[8] = mama_fish

    return buckets


def sum_fish(buckets):
    total = 0
    for fish in buckets:
        total += fish

    return total

def main():
    buckets = read_input("input6.txt")
    print(f"Initial state: {buckets}")

    num_days = 256
    for i in range(num_days):
        buckets = simulate_day(buckets)
        print(f"After {i+1:3d} days: Total {sum_fish(buckets)} fish in buckets {buckets}")


if __name__ == '__main__':
    main()
