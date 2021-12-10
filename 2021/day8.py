def read_input(filename):
    displays = []
    with open(filename) as f:
        while True:
            line = f.readline().strip()
            if not line:
                break
            patterns, digits = line.split("|")
            patterns = [frozenset(pattern[:]) for pattern in patterns.split()[:]]
            digits = [frozenset(digit[:]) for digit in digits.split()[:]]
            displays.append((patterns, digits))

    print(f"Read {len(displays)} displays")
    return displays


def make_decoder_ring(patterns):
    ring = {}
    inv_ring = {}
    for pattern in patterns:
        if len(pattern) == 2:
            ring[pattern] = 1
            inv_ring[1] = pattern
        if len(pattern) == 4:
            ring[pattern] = 4
            inv_ring[4] = pattern
        if len(pattern) == 3:
            ring[pattern] = 7
            inv_ring[7] = pattern
        if len(pattern) == 7:
            ring[pattern] = 8
            inv_ring[8] = pattern

    for pattern in patterns:
        if len(pattern) == 6:
            # The six segment pattern that does not contain the 7 pattern is 6
            if not inv_ring[7].issubset(pattern):
                ring[pattern] = 6
                inv_ring[6] = pattern
            # The six segment pattern that contains the 4 pattern is 9
            elif inv_ring[4].issubset(pattern):
                ring[pattern] = 9
                inv_ring[9] = pattern
            # The only remaining six segment pattern is 0
            else:
                ring[pattern] = 0
                inv_ring[0] = pattern

    # All remaining patterns are five segments
    for pattern in patterns:
        if len(pattern) == 5:
            # The five segment pattern that contains the 1 pattern is 3
            if inv_ring[1].issubset(pattern):
                ring[pattern] = 3
                inv_ring[3] = pattern
            # The five segment pattern that is a subset of 6 is 5
            elif pattern.issubset(inv_ring[6]):
                ring[pattern] = 5
                inv_ring[5] = pattern
            # The only remaining five segment pattern is 2
            else:
                ring[pattern] = 2
                inv_ring[2] = pattern

    return ring


def main():
    displays = read_input("input8.txt")
    count = 0
    total = 0
    for patterns, digits in displays:
        ring = make_decoder_ring(patterns)
        # print(f"Decoder ring={ring}")

        result = ""
        for digit in digits:
            # "".join(sorted(digit))
            result += "x" if digit not in ring else str(ring[digit])
            if digit in ring:
                count += 1

        print(f"Code {digits} means {result}, count={count}")
        total += int(result)
    print(f"Count = {count}, total={total}")


if __name__ == '__main__':
    main()
