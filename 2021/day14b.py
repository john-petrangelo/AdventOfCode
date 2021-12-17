from collections import Counter


def read_input(filename):
    with open(filename) as f:
        template = f.readline().strip()

        # Skip the blank line
        _ = f.readline().strip()

        rules = {}
        while True:
            line = f.readline().strip()
            if not line:
                break
            key, value = line.split(" -> ")
            rules[key] = value

        return template, rules


cached_counts = {}
count_to_cache = 0
count_from_cache = 0
elems_from_cache = Counter()

def to_cache(pair, num_steps, counts):
    global cached_counts, count_to_cache, count_from_cache
    count_to_cache += 1
    cached_counts[(pair, num_steps)] = counts.copy()


def from_cache(pair, num_steps):
    global cached_counts, count_to_cache, count_from_cache
    # print(f"Reading {pair, num_steps} from cache, {count_from_cache} so far, cache contains {len(cached_counts)} elements")
    count_from_cache += 1
    cached_value = cached_counts[(pair, num_steps)]
    elems_from_cache.update({(pair, num_steps): sum(cached_value.values())})
    return cached_value.copy()


def step_pair(pair, rules, num_steps):
    global cached_counts

    # print(f"{num_steps:2}> Entering step_pair template={pair}")
    if num_steps <= 1:
        counter = Counter(pair[0] + rules[pair])
        # print(f"{num_steps:2}> Bottomed out with {pair[0] + rules[pair]}, returning {counter}")
        return counter

    # Consider each pair of the template
    if (pair, num_steps) in cached_counts:
        # We're already figured this one out, get it from the cache
        counter = from_cache(pair, num_steps)
        # print(f"{num_steps:2}> <<< Found {(pair, num_steps)} in cache {counter}")
        return counter
    else:
        # Not in cache, need to figure it out
        element = rules[pair]
        # print(f"{num_steps:2}> Considering pair {pair}, inserting {element}")

        counter = step_pair(pair[0] + element, rules, num_steps - 1)
        # print(f"{num_steps:2}> Left {pair[0] + element} {counter}")

        right_counter = step_pair(element + pair[1], rules, num_steps - 1)
        # print(f"{num_steps:2}> Right {element + pair[1]} {right_counter}")

        counter.update(right_counter)

        # print(f"{num_steps:2}> Returned {counter}")

        # Store our hard work in the cache, so we don't need to do this again
        # print(f"{num_steps:2}> >>> Stored {(pair, num_steps)} in cache {counter}")
        to_cache(pair, num_steps, counter)

    return counter


def main():
    # test_step_pair()
    # exit(0)
    #
    global cached_counts, count_to_cache, count_from_cache

    print("========== Reading input ==========")
    template, rules = read_input("input14.txt")
    print(f"Read template={template} and {len(rules)} rules")

    print("========== Part 1 ==========")
    num_steps = 10
    counter = Counter()
    for i in range(len(template) - 1):
        pair = template[i:i + 2]
        counter.update(step_pair(pair, rules, num_steps))

    # Add the final element
    counter.update(template[-1])

    print(f"Total: {sum(counter.values())}")
    print(f"Most common: {counter.most_common()}")
    print(f"Cache contains {len(cached_counts)} items")
    print(f"Stored items in cache {count_to_cache} times")
    print(f"Found items in cache {count_from_cache} times")
    _, most_common_count = counter.most_common()[0]
    _, least_common_count = counter.most_common()[-1]
    print(f"Answer: {most_common_count - least_common_count}")

    print("========== Part 2 ==========")
    num_steps = 40
    counter = Counter()
    for i in range(len(template) - 1):
        pair = template[i:i + 2]
        counter.update(step_pair(pair, rules, num_steps))

    # Add the final element
    print("Starting final update")
    counter.update(template[-1])
    print("Ending final update")

    print(f"Total: {sum(counter.values())}")
    print(f"Most common: {counter.most_common()}")
    print(f"Cache contains {len(cached_counts)} items")
    print(f"Stored items in cache {count_to_cache} times")
    print(f"Found items in cache {count_from_cache} times")
    print(f"Work saved by cache:")
    for key, freq in elems_from_cache.most_common():
        print(f"  {key} {freq:,}")
    _, most_common_count = counter.most_common()[0]
    _, least_common_count = counter.most_common()[-1]
    print(f"Answer: {most_common_count - least_common_count:,}")


if __name__ == '__main__':
    main()
