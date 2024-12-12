import operator
import re
from pathlib import Path


def solve(path, extended=False):
    instr_pattern = r"(mul\(\d{1,3},\d{1,3}\))"
    if extended:
        instr_pattern += r"|(do\(\))|(don't\(\))"
    instr_regex = re.compile(instr_pattern)
    factors_regex = re.compile(r"\d{1,3}")
    enabled = True
    tot = 0
    for line in path.open():
        for m in instr_regex.finditer(line):
            group = m.group()
            match group:
                case "do()":
                    enabled = True
                case "don't()":
                    enabled = False
                case _:
                    if enabled:
                        tot += operator.mul(*(int(x) for x in group.replace("mul(", "").replace(")", "").split(",")))
    return tot


if __name__ == "__main__":
    ex_path = Path("example_data.txt")
    path = Path("data.txt")

    print(f"Part a (example): {solve(ex_path)}")
    print(f"Part a: {solve(path)}")

    print(f"Part b (example): {solve(ex_path, extended=True)}")
    print(f"Part b: {solve(path, extended=True)}")
