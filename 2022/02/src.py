from pathlib import Path


def get_score(move, opp_move):
    if move == 'X':     # Rock
        return 1 + \
               (opp_move == 'C') * 6 + \
               (opp_move == 'A') * 3
    elif move == 'Y':   # Paper
        return 2 + \
               (opp_move == 'A') * 6 + \
               (opp_move == 'B') * 3
    else:                       # Scissor
        return 3 + \
               (opp_move == 'B') * 6 + \
               (opp_move == 'C') * 3


def solvea(path):
    with open(path, mode='r') as f:
        tot = 0
        for line in f:
            opp_move, move = line.rstrip().split()
            tot += get_score(move, opp_move)

    return tot


def solveb(path):
    with open(path, mode='r') as f:
        tot = 0
        for line in f:
            opp_move, res = line.rstrip().split()
            if res == 'Y':
                move = (opp_move == 'A')*'X' + \
                       (opp_move == 'B')*'Y' + \
                       (opp_move == 'C')*'Z'
            elif res == 'X':
                move = (opp_move == 'A')*'Z' + \
                       (opp_move == 'B')*'X' + \
                       (opp_move == 'C')*'Y'
            else:
                move = (opp_move == 'A')*'Y' + \
                       (opp_move == 'B')*'Z' + \
                       (opp_move == 'C')*'X'

            tot += get_score(move, opp_move)

    return tot


if __name__ == "__main__":
    example_path = Path("example_data.txt")
    puzzle_path = Path("data.txt")

    print(f"Part a (example): {solvea(example_path)}")
    print(f"Part a: {solvea(puzzle_path)}")

    print(f"Part b (example): {solveb(example_path)}")
    print(f"Part b: {solveb(puzzle_path)}")
