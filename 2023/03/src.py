import re
from collections import defaultdict
from math import prod
from pathlib import Path


def solvea(data):
    tot = 0

    syms_regex = re.compile(r"([^\.\d])")
    nums_regex = re.compile(r"(\d+)")

    prev_line_syms_indices = set()
    prev_line_nums_indices = {}

    for line in data.splitlines():
        curr_line_syms_indices = {
            sym.span()[0] for sym in syms_regex.finditer(line.rstrip())
        }

        for start, end in prev_line_nums_indices:
            if set(range(start - 1, end + 1)).intersection(curr_line_syms_indices):
                tot += prev_line_nums_indices[(start, end)]
        prev_line_nums_indices.clear()

        syms_indices = curr_line_syms_indices.union(prev_line_syms_indices)
        nums = nums_regex.finditer(line.rstrip())
        for num in nums:
            start, end = num.span()
            n = int(num[0])
            if set(range(start - 1, end + 1)).intersection(syms_indices):
                tot += n
            else:
                prev_line_nums_indices[(start, end)] = n

        prev_line_syms_indices = curr_line_syms_indices.copy()

    return tot


def solveb(data):
    tot = 0

    gear_regex = re.compile(r"(\*)")
    nums_regex = re.compile(r"(\d+)")

    prev_line_gear_indices = defaultdict(set)
    prev_line_nums_indices = {}

    for line in data.splitlines():
        curr_line_gear_indices = {
            gear.span()[0]: set() for gear in gear_regex.finditer(line.rstrip())
        }

        # add previous line's adjacency to current line's numbers
        for start, end in prev_line_nums_indices:
            for gear_idx in curr_line_gear_indices:
                if start - 1 <= gear_idx < end + 1:
                    curr_line_gear_indices[gear_idx].add(
                        prev_line_nums_indices[(start, end)]
                    )
        prev_line_nums_indices.clear()

        nums = nums_regex.finditer(line.rstrip())
        for num in nums:
            start, end = num.span()
            n = int(num[0])
            # add it for next line
            prev_line_nums_indices[(start, end)] = n

            # check adjacency with previous line's gears
            for gear_idx in prev_line_gear_indices:
                if start - 1 <= gear_idx < end + 1:
                    prev_line_gear_indices[gear_idx].add(n)

            # check adjaceny with current line's gears
            for gear_idx in curr_line_gear_indices:
                if start - 1 <= gear_idx < end + 1:
                    curr_line_gear_indices[gear_idx].add(n)

        tot += sum(
            prod(vals) for vals in prev_line_gear_indices.values() if len(vals) == 2
        )

        prev_line_gear_indices = curr_line_gear_indices.copy()

    return tot + sum(
        prod(vals) for vals in prev_line_gear_indices.values() if len(vals) == 2
    )


if __name__ == "__main__":
    ex_data = Path("example_data.txt").read_text()
    data = Path("data.txt").read_text()

    print(f"Part a (example): {solvea(ex_data)}")
    print(f"Part a: {solvea(data)}")

    print(f"Part b (example): {solveb(ex_data)}")
    print(f"Part b: {solveb(data)}")
