from pathlib import Path


def solvea(path):
    with open(path, mode='r') as f:
        mas = 0
        cur = 0
        for line in f:
            line = line.rstrip()
            if not line:
                mas, cur = max(cur, mas), 0
            else:
                cur += int(line)

    return max(cur, mas)


def solveb(path):
    with open(path, mode='r') as f:
        first, second, third = 0, 0, 0
        cur = 0
        for line in f:
            line = line.rstrip()
            if not line:
                if cur > first:
                    third, second, first = second, first, cur
                elif cur > second:
                    third, second = second, cur
                elif cur > third:
                    third = cur

                cur = 0
            else:
                cur += int(line)

    return first+second+max(third, cur)


if __name__ == "__main__":
    example_path = Path("example_data.txt")
    puzzle_path = Path("data.txt")

    print(f"Part a (example): {solvea(example_path)}")
    print(f"Part a: {solvea(puzzle_path)}")

    print(f"Part b (example): {solveb(example_path)}")
    print(f"Part b: {solveb(puzzle_path)}")
