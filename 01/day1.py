from pathlib import Path


def solve1a(path):
    increments = 0
    prev = float('inf')
    with open(path, mode='r') as f:
        for line in f:
            num = int(line)
            if num > prev:
                increments += 1
            prev = num

    return increments


def solve1b(path):
    increments = 0
    first, second, third = [float('inf')]*3
    with open(path, mode='r') as f:
        for line in f:
            num = int(line)
            if num > first:
                increments += 1
            first, second, third = second, third, num

    return increments


if __name__ == "__main__":
    print(f"Number of increments was: {solve1a(Path('01_data.txt'))}")
    print(f"Number of moving sum increments was: {solve1b(Path('01_data.txt'))}")
