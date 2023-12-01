import re
from pathlib import Path


def solvea(data):
    find_digit = re.compile(r"\d")
    return sum(
        int(find_digit.search(line)[0] + find_digit.search(line[::-1])[0])
        for line in data.splitlines()
    )


def solveb(data):
    return solvea(
        data.replace("one", "one1one")
        .replace("two", "two2two")
        .replace("three", "three3three")
        .replace("four", "four4four")
        .replace("five", "five5five")
        .replace("six", "six6six")
        .replace("seven", "seven7seven")
        .replace("eight", "eight8eight")
        .replace("nine", "nine9nine")
    )


if __name__ == "__main__":
    ex_data_a = Path("example_data_a.txt").read_text()
    ex_data_b = Path("example_data_b.txt").read_text()
    data = Path("data.txt").read_text()

    print(f"Part a (example): {solvea(ex_data_a)}")
    print(f"Part a: {solvea(data)}")

    print(f"Part b (example): {solveb(ex_data_b)}")
    print(f"Part b: {solveb(data)}")
