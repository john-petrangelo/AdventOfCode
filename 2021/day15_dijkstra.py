from termcolor import colored
from timeit import default_timer as timer

lowest_risk = -1


def read_input(filename):
    cavern = []
    with open(filename) as f:
        cavern = [([int(c) for c in line.strip()]) for line in f.readlines()]

        num_rows = len(cavern)
        num_cols = len(cavern[0])
        print(f"Read cavern with {num_rows} rows and {num_cols} columns")

        return cavern


def print_cavern(cavern, path=None):
    if path is None:
        path = []
    for row in range(len(cavern)):
        s = ""
        for col in range(len(cavern[0])):
            c = str(cavern[row][col])
            if (row, col) in path:
                c = colored(c, "red")
            s += c
        print(s)


def dijkstra(cavern):
    num_rows = len(cavern)
    num_cols = len(cavern[0])

    # Dijkstra's Algorithm
    # Reference: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm#Algorithm
    unvisited_nodes = []
    risks = {}
    previous_node = {}
    for row in range(num_rows):
        for col in range(num_cols):
            # unvisited_nodes.append((row, col))
            risks[(row, col)] = float('inf')
            previous_node[(row, col)] = None
    unvisited_nodes.append((0, 0))
    risks[(0, 0)] = 0

    # 3. For the current node, consider all unvisited neighbors and calculate their
    #    tentative distances through the current node. Compare the newly calculated
    #    tentative distance to the current assigned value and assign the smaller one.
    while unvisited_nodes:
        unvisited_nodes.sort(key=lambda n: risks[n], reverse=True)
        row, col = unvisited_nodes[-1]
        unvisited_nodes.pop(-1)

        if len(unvisited_nodes) % 100 == 0:
            print(f"...thinking about {(row, col)} with {len(unvisited_nodes)} nodes remaining...")

        if (row, col) == (num_rows-1, num_cols-1):
            break

        # print(f"node={(row, col)}")
        for neighbor in [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]:
            nr, nc = neighbor

            if (not 0 <= nr < num_rows) or (not 0 <= nc < num_cols):
                continue

            new_risk = risks[(row, col)] + cavern[nr][nc]
            # print(f"Checking neighbor {neighbor} new risk={new_risk} old risk={risks[neighbor]}")
            if new_risk < risks[neighbor]:
                # print(f"Node {neighbor} has new risk={new_risk} and previous={(row, col)}")
                risks[neighbor] = new_risk
                previous_node[neighbor] = (row, col)
                unvisited_nodes.append(neighbor)

    path = [(num_rows-1, num_cols-1)]
    while previous_node[path[0]]:
        path.insert(0, previous_node[path[0]])

    return risks[(num_rows-1, num_cols-1)], path


def make_big_cavern(cavern):
    big_cavern = []

    for row_add in range(0, 5):
        for row in cavern:
            big_row = []
            for col_add in range(0, 5):
                for c in row:
                    c += row_add + col_add
                    if c > 9:
                        c -= 9
                    big_row.append(c)
            big_cavern.append(big_row)
    return big_cavern


def main():
    global lowest_risk

    cavern = read_input("input15.txt")
    print_cavern(cavern)

    print("========== Part 1 ==========")
    # lowest_risk, path = dijkstra(cavern)
    # print_cavern(cavern, path)
    # print(f"Lowest risk is {lowest_risk}")

    print("========== Part 2 ==========")
    big_cavern = make_big_cavern(cavern)
    lowest_risk, path = dijkstra(big_cavern)
    print_cavern(big_cavern, path)
    print(f"Lowest risk is {lowest_risk}")


if __name__ == '__main__':
    main()
