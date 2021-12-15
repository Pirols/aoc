from pathlib import Path
from collections import Counter, defaultdict


def step(current_polymer, pairs):
    # naive unoptimised version - used for part a

    letters = list()

    for i in range(len(current_polymer)-1):
        letters.append(current_polymer[i])
        letters.append(pairs.get(current_polymer[i:i+2], ''))

    # also add last letter
    letters.append(current_polymer[-1])

    return ''.join(letters)


def step_dict(polymer_dict, pairs):

    stepped_polymer_dict = defaultdict(int)

    for twogram, num in polymer_dict.items():
        if twogram in pairs:
            let = pairs[twogram]
            stepped_polymer_dict[twogram[0] + let] += num
            stepped_polymer_dict[let + twogram[1]] += num
        else:
            stepped_polymer_dict[twogram] = num

    return stepped_polymer_dict


def count_chars(polymer_dict, last_char):

    letter_counts = defaultdict(int)

    for pair, num in polymer_dict.items():
        letter_counts[pair[0]] += num

    letter_counts[last_char] += 1

    return letter_counts


if __name__ == "__main__":
    data_path = Path('14_data.txt')

    with open(data_path, mode='r') as f:
        polymer_template = f.readline().rstrip()
        f.readline()
        pairs = dict()
        for line in f:
            pair, _, out = line.rstrip().split(' ')
            pairs[pair] = out

    # last char won't change
    last_char = polymer_template[-1]

    # make dictionary of pairs occurrencies
    polymer_dict = defaultdict(int)
    for i in range(len(polymer_template)-1):
        polymer_dict[polymer_template[i:i+2]] += 1

    # part a
    for _ in range(10):
        polymer_dict = step_dict(polymer_dict, pairs)

    letter_counts = count_chars(polymer_dict, last_char)
    max_val, min_val = 0, float('inf')
    for let, num in letter_counts.items():
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num
    print(f"Part a: {max_val - min_val}")

    # part b
    for _ in range(30):
        polymer_dict = step_dict(polymer_dict, pairs)

    letter_counts = count_chars(polymer_dict, last_char)
    max_val, min_val = 0, float('inf')
    for let, num in letter_counts.items():
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num
    print(f"Part b: {max_val - min_val}")
