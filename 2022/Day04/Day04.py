def part_1(filename):
    print(f"========================================")
    print(f"Running part 1 with file {filename}")

    with open(filename) as f:
        total_score = 0
        for line in f:
            line = line.strip()
            ids1, ids2 = line.split(",")

            id1_lower, id1_upper = map(int, ids1.split("-"))
            id2_lower, id2_upper = map(int, ids2.split("-"))

            set1 = set(range(id1_lower, id1_upper+1))
            set2 = set(range(id2_lower, id2_upper+1))

            if len(set1.union(set2)) == max(len(set1), len(set2)):
                total_score += 1

        print(f"Total Score: {total_score}")


def part_2(filename):
    print(f"========================================")
    print(f"Running part 2 with file {filename}")

    with open(filename) as f:
        total_score = 0
        for line in f:
            line = line.strip()
            ids1, ids2 = line.split(",")

            id1_lower, id1_upper = map(int, ids1.split("-"))
            id2_lower, id2_upper = map(int, ids2.split("-"))

            set1 = set(range(id1_lower, id1_upper+1))
            set2 = set(range(id2_lower, id2_upper+1))

            if len(set1.union(set2)) < len(set1) + len(set2):
                total_score += 1

        print(f"Total Score: {total_score}")


part_1("Day04_example.txt")
part_1("Day04.txt")

part_2("Day04_example.txt")
part_2("Day04.txt")


