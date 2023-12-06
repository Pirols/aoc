import re
from pathlib import Path


def solvea(data):
    tot = 0

    find_nums = re.compile(r"(\d+)(?!\d*:)")
    winning_nums = set()
    for line in data.splitlines():
        nums = find_nums.finditer(line)
        bar_idx = line.find("|")

        got_winning_nums = 0
        for num in nums:
            if bar_idx > num.span()[0]:
                winning_nums.add(num[0])
            elif num[0] in winning_nums:
                got_winning_nums += 1
        if got_winning_nums:
            tot += 2 ** (got_winning_nums - 1)

        winning_nums.clear()

    return tot


def solveb(data):
    lines = data.splitlines()
    n = len(lines)
    num_scratchcards = {i: 1 for i in range(1, n + 1)}

    find_nums = re.compile(r"(\d+)(?!\d*:)")
    winning_nums = set()
    for i, line in enumerate(lines, start=1):
        nums = find_nums.finditer(line)
        bar_idx = line.find("|")

        got_winning_nums = 0
        for num in nums:
            if bar_idx > num.span()[0]:
                winning_nums.add(num[0])
            elif num[0] in winning_nums:
                got_winning_nums += 1
        for j in range(1, got_winning_nums + 1):
            if i + j > n:
                break
            num_scratchcards[i + j] += num_scratchcards[i]

        winning_nums.clear()

    return sum(num_scratchcards.values())


if __name__ == "__main__":
    ex_data = Path("example_data.txt").read_text()
    data = Path("data.txt").read_text()

    print(f"Part a (example): {solvea(ex_data)}")
    print(f"Part a: {solvea(data)}")

    print(f"Part b (example): {solveb(ex_data)}")
    print(f"Part b: {solveb(data)}")
