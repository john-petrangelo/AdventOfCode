from termcolor import colored
from math import prod

LITERAL_VALUE_TYPE = 4
OPERATOR_SUM_TYPE = 0
OPERATOR_PRODUCT_TYPE = 1
OPERATOR_MIN_TYPE = 2
OPERATOR_MAX_TYPE = 3
OPERATOR_GREATER_THAN_TYPE = 5
OPERATOR_LESS_THAN_TYPE = 6
OPERATOR_EQUAL_TO_TYPE = 7

indent = 0


def read_input(filename):
    with open(filename) as f:
        inputs = []
        while True:
            line = f.readline().strip()
            if not line:
                break

            bits = format(int(line, 16), f"0{len(line)*4}b")
            print(f"Read {line} expanding to {len(bits)} binary digits")
            inputs.append((line, bits))

        return inputs


def parse_literal(bits):
    value = 0
    while True:
        value = (value << 4) | (int(bits[1:5], 2))
        print(f"{' ' * indent}Literal value accumulator {value}: {colored(bits[:5], 'blue')}{bits[5:]}")
        if bits[0] == '0':
            break
        bits = bits[5:]

    return value, bits[5:]


def parse_operator(bits, type_id):
    sum_versions = 0
    sub_values = []

    # Parse the length type ID
    length_type_id = bits[0]
    bits = bits[1:]

    if length_type_id == '0':
        # Next 15 bits are the total length of sub-packets contained by this packet
        len_packets = int(bits[:15], 2)
        print(f"{' ' * indent}Length type 0: {colored(bits[:15], 'blue')}{bits[15:]} => {len_packets} bits, total={sum_versions}")
        bits = bits[15:]
        sub_bits = bits[:len_packets]
        while sub_bits:
            sub_version, sub_value, sub_bits = parse_packet(sub_bits)
            sum_versions += sub_version
            sub_values.append(sub_value)
            print(f"{' ' * indent}(0) adding {sub_value} to total to get {sum_versions}")
        bits = bits[len_packets:]
    else:
        # Next 11 bits are a number that represents the number of sub-packets immediately contained by this packet
        num_packets = int(bits[:11], 2)
        print(f"{' ' * indent}Length type 1: {colored(bits[:11], 'blue')}{bits[11:]} => {num_packets} sub-packets, total={sum_versions}")
        bits = bits[11:]

        for n in range(num_packets):
            sub_version, sub_value, bits = parse_packet(bits)
            sum_versions += sub_version
            sub_values.append(sub_value)
            print(f"{' ' * indent}(1) adding {sub_value} to total to get {sum_versions}")

    value = 0
    if type_id == OPERATOR_SUM_TYPE:
        value = sum(sub_values)
    elif type_id == OPERATOR_PRODUCT_TYPE:
        value = prod(sub_values)
    elif type_id == OPERATOR_MIN_TYPE:
        value = min(sub_values)
    elif type_id == OPERATOR_MAX_TYPE:
        value = max(sub_values)
    elif type_id == OPERATOR_GREATER_THAN_TYPE:
        value = 1 if sub_values[0] > sub_values[1] else 0
    elif type_id == OPERATOR_LESS_THAN_TYPE:
        value = 1 if sub_values[0] < sub_values[1] else 0
    elif type_id == OPERATOR_EQUAL_TO_TYPE:
        value = 1 if sub_values[0] == sub_values[1] else 0

    print(f"{' ' * indent}parse_operator returning sum_versions={sum_versions} value={value}")
    return sum_versions, value, bits


def parse_packet(bits):
    global indent

    # Extract the version and type_id
    version = int(bits[:3], 2)
    type_id = int(bits[3:6], 2)
    print(f"{' ' * indent}Parsing packet version={colored(str(version), 'blue')} type_id={colored(str(type_id), 'green')}: {colored(bits[:3], 'blue')}{colored(bits[3:6], 'green')}{bits[6:]}")
    bits = bits[6:]
    indent += 4

    sum_versions = 0
    value = 0
    if type_id == LITERAL_VALUE_TYPE:
        # Type ID is "literal value"
        value, bits = parse_literal(bits)
    else:
        # Type ID is an operator
        sum_versions, value, bits = parse_operator(bits, type_id)
        print(f"{' ' * indent}Parsed sub-packet, sum_versions is {sum_versions}")

    indent -= 4
    sum_versions += version
    return sum_versions, value, bits


def main():
    for hex_string, bits in read_input("input16.txt"):
        print(f"*** Beginning to parse {hex_string}")
        sum_versions, value, _ = parse_packet(bits)
        print(f"*** Final for {hex_string} => sum of version is {sum_versions} and the final value is {value}")


if __name__ == '__main__':
    main()
