score_map = {}

def setup():
    for item in range(0, 26):
        score_map[chr(ord('a') + item)] = item+1
        score_map[chr(ord('A') + item)] = item+26+1


def part_1(filename):
    print(f"==========")
    print(f"Running part 1 with file {filename}")
    print(f"==========")

    with open(filename) as f:
        total_score = 0
        for line in f:
            line = line.strip()
            num_items = len(line)
            left = line[:num_items//2]
            right = line[num_items//2:]
            # print(f"Line contains {num_items} items, '{left}'--'{right}'")

            left_set = set()
            right_set = set()
            for item in left:
                left_set.add(item)
            for item in right:
                right_set.add(item)

            inter = left_set.intersection(right)
            if len(inter) != 1:
                print(f"Expected one intersection, found {inter} instead, line='{line}'")
                continue
            item = inter.pop()
            priority = score_map[item]

            # print(f"Intersection: {item} (priority)")
            total_score += priority

        print(f"Total Score: {total_score}")


def part_2(filename):
    print(f"==========")
    print(f"Running part 2 with file {filename}")
    print(f"==========")

    with open(filename) as f:
        total_score = 0

        for line1 in f:
            line1 = line1.strip()
            line2 = next(f).strip()
            line3 = next(f).strip()

            set1 = set()
            set2 = set()
            set3 = set()
            for item in line1:
                set1.add(item)
            for item in line2:
                set2.add(item)
            for item in line3:
                set3.add(item)

            inter = set1.intersection(set2).intersection(set3)
            if len(inter) != 1:
                print(f"Expected one intersection, found {inter} instead, line='{line}'")
                continue
            item = inter.pop()
            priority = score_map[item]

            # print(f"Intersection: {item} (priority)")
            total_score += priority

        print(f"Total Score: {total_score}")


setup()
part_1("Day03_example.txt")
part_1("Day03.txt")
part_2("Day03_example.txt")
part_2("Day03.txt")


