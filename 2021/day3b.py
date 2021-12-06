def read_input(filename):
    file_lines = []
    with open(filename) as f:
        for line in f:
            file_lines.append(line.strip())

    file_bits = len(file_lines[0])

    print(f"{len(file_lines)} lines found, {file_bits} bits per line")

    return file_bits, file_lines


def count_bits(bit, lines_in):
    # Gather the counts of zeros and ones for all lines in a single bit column
    count = {"0": 0, "1": 0}
    for line in lines_in:
        count[line[bit]] += 1

    return count


def calc_o2_rating(num_bits_in, lines_in):
    calc_lines = lines_in[:]

    for bit in range(num_bits_in):
        # Are we already done? Maybe we can leave early.
        if len(calc_lines) == 1:
            return calc_lines[0]

        count = count_bits(bit, calc_lines)

        # Match on one if more common or equally common
        match_value = "1"
        if count["0"] > count["1"]:
            # Zero is more common, match on zero
            match_value = "0"
        print(f"O2 generator rating: bit={bit}, match={match_value} remaining lines={calc_lines}")
        calc_lines = list(filter(lambda line: line[bit] == match_value, calc_lines))

    print(f"O2 generator rating finished with {len(calc_lines)} remaining lines:  {calc_lines}")

    return calc_lines[0]


def calc_co2_rating(num_bits_in, lines_in):
    calc_lines = lines_in[:]

    for bit in range(num_bits_in):
        # Are we already done? Maybe we can leave early.
        if len(calc_lines) == 1:
            return calc_lines[0]

        count = count_bits(bit, calc_lines)

        # Match on zero if more common or equally common
        match_value = "0"
        if count["0"] > count["1"]:
            # One is more common, match on one
            match_value = "1"
        print(f"CO2 scrubber rating: bit={bit}, match={match_value} remaining lines={calc_lines}")
        calc_lines = list(filter(lambda line: line[bit] == match_value, calc_lines))

    print(f"CO2 scrubber rating finished with {len(calc_lines)} remaining lines:  {calc_lines}")

    return calc_lines[0]


# Read the input file
num_bits, lines = read_input("test3.txt")

o2_rating = calc_o2_rating(num_bits, lines)
o2_rating_int = int(o2_rating, 2)

co2_rating = calc_co2_rating(num_bits, lines)
co2_rating_int = int(co2_rating, 2)

print()
print(f"O2 generator rating={o2_rating}")
print(f"CO2 scrubber rating={co2_rating}")
print(f"product={o2_rating_int * co2_rating_int}")