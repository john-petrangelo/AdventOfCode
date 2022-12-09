# Inputs
# First column - Opponent's play: A-rock, B-paper, C-scissors
# Second column - Outcome: X-lose, Y-draw, Z-win

# Points
# Play: 1 for rock, 2 for paper, 3 for scissors
# Outcome: 0 for lose, 3 for draw, 6 if won

score_map = {
    # Values: my play + win/lose/draw
    "A X": 3 + 0,  # I played scissors
    "A Y": 1 + 3,  # I played rock
    "A Z": 2 + 6,  # I played paper

    "B X": 1 + 0,  # I played rock
    "B Y": 2 + 3,  # I played paper
    "B Z": 3 + 6,  # I played scissors

    "C X": 2 + 0,  # I played paper
    "C Y": 3 + 3,  # I played scissors
    "C Z": 1 + 6,  # I played rock
}

total_score = 0
with open("Day02.txt") as f:
    for line in f:
        line = line.strip()
        total_score += score_map[line]
        print(f"Play {line} for {score_map[line]} points")

print(f"Total Score: {total_score}")
