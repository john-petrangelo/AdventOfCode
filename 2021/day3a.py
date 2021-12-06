lines = []
with open("input3.txt") as f:
    for line in f:
        lines.append(line.strip())

numBits = len(lines[0])

print(f"{len(lines)} lines found")
print(f"{numBits} bits per line")

# Gather the counts of zeros and ones
counts = []
for bit in range(numBits):
    count = {"0": 0, "1": 0}
    for line in lines:
        count[line[bit]] += 1
    counts.append(count)

# Calculate gamma and epsilon
gamma = ""
epsilon = ""
for bit in range(numBits):
    count = counts[bit]
    if count["0"] > count["1"]:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"

gammaInt = int(gamma, 2)
epsilonInt = int(epsilon, 2)

print(f"gamma={gamma}({gammaInt}) epsilon={epsilon}({epsilonInt}) product={gammaInt * epsilonInt}")
