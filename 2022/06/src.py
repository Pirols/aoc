from pathlib import Path


def solvea(path):
    with open(path, mode='r') as f:
        curr_chars = set()
        inp = f.readline().rstrip()
        for idx in range(3, len(inp)):
            if len(set(inp[idx-3:idx+1])) == 4:
                return idx+1

def solveb(path):
    with open(path, mode='r') as f:
        inp = f.readline().rstrip()
        for idx in range(13, len(inp)):
            if len(set(inp[idx-13:idx+1])) == 14:
                return idx+1


if __name__ == "__main__":
    example_path = Path("example_data.txt")
    puzzle_path = Path("data.txt")

    print(f"Part a (example): {solvea(example_path)}")
    print(f"Part a: {solvea(puzzle_path)}")

    print(f"Part b (example): {solveb(example_path)}")
    print(f"Part b: {solveb(puzzle_path)}")
