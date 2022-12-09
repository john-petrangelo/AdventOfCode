# Inputs
# First column - Opponent's play: A-rock, B-paper, C-scissors
# Second column - My play: X-rock, Y-paper, Z-scissors

# Points
# Play: 1 for rock, 2 for paper, 3 for scissors
# Outcome: 0 for lose, 3 for draw, 6 if won

score_map = {
    "A X": 1 + 3,
    "A Y": 2 + 6,
    "A Z": 3 + 0,
    "B X": 1 + 0,
    "B Y": 2 + 3,
    "B Z": 3 + 6,
    "C X": 1 + 6,
    "C Y": 2 + 0,
    "C Z": 3 + 3,
}

total_score = 0
with open("Day02.txt") as f:
    for line in f:
        line = line.strip()
        total_score += score_map[line]
        print(f"Play {line} for {score_map[line]} points")

print(f"Total Score: {total_score}")
