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


def make_polymer(template, rules, num_steps):
    for step in range(num_steps):
        new_template = ""
        for i in range(len(template)-1):
            pair = template[i:i+2]
            # print(f"Considering pair {pair}")
            new_polymer = rules[pair]
            new_template += template[i] + new_polymer
        template = new_template + template[-1]
        print(f"After step {step+1}: ({len(template)})")

    return template


def count_elements(template):
    freq = {}
    for t in template:
        if t in freq:
            freq[t] += 1
        else:
            freq[t] = 1
    sorted_keys = sorted(freq, key=freq.get, reverse=True)
    return freq, sorted_keys


def main():
    print("========== Reading input ==========")
    template, rules = read_input("test14.txt")
    print(f"Read template={template} and {len(rules)} rules")

    print("========== Part 1 ==========")
    template1 = make_polymer(template, rules, 10)
    freq, sorted_keys = count_elements(template1)
    print(f"Final result: {freq[sorted_keys[0]] - freq[sorted_keys[-1]]}")

    print("========== Part 2 ==========")
    template2 = make_polymer(template, rules, 40)
    freq, sorted_keys = count_elements(template2)
    print(f"Final result: {freq[sorted_keys[0]] - freq[sorted_keys[-1]]}")


if __name__ == '__main__':
    main()
