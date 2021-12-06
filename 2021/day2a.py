cmds = []
with open("input2.txt") as f:
    for line in f:
        cmd, value = line.strip().split()
        cmds.append((cmd, int(value)))

print(f"{len(cmds)} commands found")

currentX = 0
currentDepth = 0
for cmd, value in cmds:
    if cmd == "forward":
        currentX += value
    if cmd == "up":
        currentDepth -= value
        if currentDepth < 0:
            currentDepth = 0
    if cmd == "down":
        currentDepth += value

print(f"Current position x={currentX} depth={currentDepth}")
print(f"Product = {currentX * currentDepth}")
