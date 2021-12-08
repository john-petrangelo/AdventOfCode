from termcolor import colored


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


def print_boards(boards, called_numbers):
    # Display 'width' boards at once
    width = 10
    for i in range(0, len(boards), width):
        board_subset = boards[i : min((i+width), len(boards))]
        for row in range(5):
            line = ""
            for board in board_subset:
                for col in range(5):
                    s = f" {board.get(row, col):>2s}"
                    line += colored(s, "grey", attrs=['reverse']) if board.get(row, col) in called_numbers else s
                line += "  "

            print(line)
        print()


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
            print(f"Won in row {row}")
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
            print(f"Win col {col}")
            return True

    # No columns won, either. Board did not win
    return False


def get_uncalled_sum(board, called_numbers):
    accum = 0
    for row in range(5):
        for col in range(5):
            if board.get(row, col) not in called_numbers:
                accum += int(board.get(row, col))
    return accum


def find_winners(boards, numbers_to_call):
    called_numbers = set()
    winners = []
    for called_number in numbers_to_call:
        print(f"Calling {called_number}, checking {len(boards)} boards...")
        called_numbers.add(called_number)
        print_boards(boards, called_numbers)

        for board in boards:
            if did_board_win(board, called_numbers):
                # We have a winner
                print(f"Board {board} won when {called_number} was called, {len(boards)} remaining")
                winners.append((board, called_number, called_numbers.copy()))
                boards.remove(board)

    return winners


def main():
    # Read the input file
    numbers_to_call, boards = read_input("input4.txt")

    print("Initial boards:")

    # Find all of the winning boards
    print(f"Will call these numbers: {numbers_to_call}")
    winners = find_winners(boards, numbers_to_call)

    # Print the results
    print("\nResults")
    print(f"There were {len(boards)} boards remaining")
    print(f"There were {len(winners)} winning boards")
    first_board, first_call, first_called_numbers = winners[0]
    last_board, last_call, last_called_numbers = winners[-1]
    print(f"The first win was made with call {first_call} for board {first_board}")
    print(f"The last win was made with call {last_call} for board {last_board}")

    uncalled_sum = get_uncalled_sum(first_board, first_called_numbers)
    print(f"First win: {uncalled_sum} * {first_call} = {uncalled_sum * int(first_call)}")

    uncalled_sum = get_uncalled_sum(last_board, last_called_numbers)
    print(f"Last win: {uncalled_sum} * {last_call} = {uncalled_sum * int(last_call)}")


if __name__ == '__main__':
    main()
