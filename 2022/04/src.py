from pathlib import Path


def solvea(path):
    with open(path, mode='r') as f:
        completely_overlapping_pairs = 0
        for pair in f:
            elf1, elf2 = pair.rstrip().split(',')
            start1, end1 = [int(x) for x in elf1.split('-')]
            start2, end2 = [int(x) for x in elf2.split('-')]
            if (start1 >= start2 and end1 <= end2) or \
               (start2 >= start1 and end2 <= end1):
                completely_overlapping_pairs += 1

    return completely_overlapping_pairs


def solveb(path):
    with open(path, mode='r') as f:
        overlapping_pairs = 0
        for pair in f:
            elf1, elf2 = pair.rstrip().split(',')
            start1, end1 = [int(x) for x in elf1.split('-')]
            start2, end2 = [int(x) for x in elf2.split('-')]
            if max([start1, start2]) <= min([end1, end2]):
                overlapping_pairs += 1

    return overlapping_pairs


if __name__ == "__main__":
    example_path = Path("example_data.txt")
    puzzle_path = Path("data.txt")

    print(f"Part a (example): {solvea(example_path)}")
    print(f"Part a: {solvea(puzzle_path)}")

    print(f"Part b (example): {solveb(example_path)}")
    print(f"Part b: {solveb(puzzle_path)}")
