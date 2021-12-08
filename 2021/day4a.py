class Board:
    values = []

    def __init__(self, values):
        self.values = values[:]

    # Get the value at the specified row and column, both indexed 0-4, (0,0) at top left
    def get(self, row, col):
        return self.values[row * 5 + col]

    def __str__(self):
        return str(self.values)


def read_board(f):
    values = []
    for i in range(5):
        values.extend(f.readline().strip().split())
    return Board(values)


def read_input(filename):
    with open(filename) as f:
        # Read the list of numbers to call
        line = f.readline().strip()
        calls = line.split(",")

        # Read the bingo cards
        boards = []
        while True:
            line = f.readline()
            if not line:
                break
            boards.append(read_board(f))

        print(f"There are {len(calls)} numbers to call for {len(boards)} boards")

        return calls, boards


# Check if the board has won given the called numbers. Return True if won, otherwise return False
def did_board_win(board, called):
    # Check each row
    for row in range(5):
        row_did_win = True
        for col in range(5):
            if board.get(row, col) not in called:
                # Not a winner, next row
                row_did_win = False
                break
        if row_did_win:
            return True

    # No rows won. Now check the columns
    for col in range(5):
        col_did_win = True
        for row in range(5):
            if board.get(row, col) not in called:
                # Not a winner, next col
                col_did_win = False
                break
        if col_did_win:
            return True

    # No columns won, either. Board did not win
    return False


# Read the input file
numbers_to_call, boards = read_input("input4.txt")

# Do the thing
called_numbers = set()
winning_board = None
winning_call = None
for called_number in numbers_to_call:
    called_numbers.add(called_number)

    for board in boards:
        if did_board_win(board, called_numbers):
            # We have a winner
            print(f"Board {board} won when {called_number} was called")
            winning_board = board
            winning_call = called_number
            break

    if winning_board:
        break

# Print the results
print("\nResults")
sum = 0
for row in range(5):
    for col in range(5):
        if winning_board.get(row, col) not in called_numbers:
            sum += int(winning_board.get(row, col))
print(f"{sum} * {winning_call} = {sum * int(winning_call)}")

