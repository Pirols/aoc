from pathlib import Path


def solvea(path):
    with open(path, mode='r') as f:
        stacks = list()
        for line in f:
            if not (line := line.rstrip()):
                break
            for i, idx in enumerate(range(1, len(line), 4)):
                if i >= len(stacks):
                    stacks.append([])
                if (stack_crate := line[idx]).isdigit():
                    break
                elif stack_crate != " ":
                    stacks[i].append(stack_crate)

        for inst in f:
            num, start, end = [int(num) for num in inst.rstrip().split() if num.isdigit()]
            for _ in range(num):
                el = stacks[start-1].pop(0)
                stacks[end-1].insert(0, el)

    return "".join([stack[0] for stack in stacks])


def solveb(path):
    with open(path, mode='r') as f:
        stacks = list()
        for line in f:
            if not (line := line.rstrip()):
                break
            for i, idx in enumerate(range(1, len(line), 4)):
                if i >= len(stacks):
                    stacks.append([])
                if (stack_crate := line[idx]).isdigit():
                    break
                elif stack_crate != " ":
                    stacks[i].append(stack_crate)

        for inst in f:
            num, start, end = [int(num) for num in inst.rstrip().split() if num.isdigit()]
            to_move = [stacks[start-1].pop(0) for _ in range(num)]
            for el in to_move[::-1]:
                stacks[end-1].insert(0, el)

    return "".join([stack[0] for stack in stacks])


if __name__ == "__main__":
    example_path = Path("example_data.txt")
    puzzle_path = Path("data.txt")

    print(f"Part a (example): {solvea(example_path)}")
    print(f"Part a: {solvea(puzzle_path)}")

    print(f"Part b (example): {solveb(example_path)}")
    print(f"Part b: {solveb(puzzle_path)}")
