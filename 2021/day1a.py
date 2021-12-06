depths = []
with open("input1.txt") as f:
    for line in f:
        line = line.strip()
        depths.append(line)

print(f"{len(depths)} records found")

numIncreases = 0
numDecreases = 0
numSame = 0
for i in range(1, len(depths)):
    prev = int(depths[i-1])
    current = int(depths[i])

    if prev < current:
        numIncreases += 1
        result = "increase"

    if prev > current:
        numDecreases += 1
        result = "decrease"

    if prev == current:
        numSame += 1
        result = "same"

    print(f"i={i} {prev} ?< {current} = {result}")

print(f"{numIncreases} increases found")
print(f"{numDecreases} decreases found")
print(f"{numSame} sames found")
