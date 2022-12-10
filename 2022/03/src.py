import string
from pathlib import Path


def solvea(path):
    with open(path, mode='r') as f:
        alphabet = string.ascii_lowercase
        item_to_priority = dict()
        for idx, letter in enumerate(alphabet):
            item_to_priority[letter] = idx + 1
            item_to_priority[letter.upper()] = idx + 27

        priorities_sum = 0
        for rucksack in f:
            rucksack = rucksack.rstrip()
            first_cmpt = set(rucksack[:len(rucksack)//2])
            second_cmpt = set(rucksack[len(rucksack)//2:])

            for item in first_cmpt:
                if item in second_cmpt:
                    priorities_sum += item_to_priority[item]
                    break

    return priorities_sum


def solveb(path):
    with open(path, mode='r') as f:
        alphabet = string.ascii_lowercase
        item_to_priority = dict()
        for idx, letter in enumerate(alphabet):
            item_to_priority[letter] = idx + 1
            item_to_priority[letter.upper()] = idx + 27

        priorities_sum = 0
        rucksacks = f.readlines()
        for i in range(len(rucksacks))[::3]:
            ruck1 = set(rucksacks[i].rstrip())
            ruck2 = set(rucksacks[i+1].rstrip())
            ruck3 = set(rucksacks[i+2].rstrip())
            badge = ruck1.intersection(ruck2).intersection(ruck3).pop()
            priorities_sum += item_to_priority[badge]

        return priorities_sum




#             for item in first_cmpt:
#                 if item in second_cmpt:
#                     priorities_sum += item_to_priority[item]
#                     break

    return priorities_sum


if __name__ == "__main__":
    example_path = Path("example_data.txt")
    puzzle_path = Path("data.txt")

    print(f"Part a (example): {solvea(example_path)}")
    print(f"Part a: {solvea(puzzle_path)}")

    print(f"Part b (example): {solveb(example_path)}")
    print(f"Part b: {solveb(puzzle_path)}")
