depths = []
with open("Day01.txt") as f:
    elf_index = 0
    elves = [[]]

    for line in f:
        line = line.strip()
        if not line:
            elf_index = elf_index + 1
            elves.append([])
            continue
        elves[elf_index].append(int(line))

print(f"{len(elves)} elves found")
sums = []
for index, elf in enumerate(elves):
    sum_calories = sum(elf)
    sums.append(sum_calories)

sums.sort()
sums.reverse()
top_three = sums[0:3]
print(f"Top three: {top_three}")
print(f"Sum of top three: {sum(top_three)}")