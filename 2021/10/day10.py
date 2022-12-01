import statistics

from pathlib import Path


def solve10a(nav_subsystem_log):

    total_syntax_error = 0

    matching_parens = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }
    error_to_score = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137
    }

    for line in nav_subsystem_log:
        open_braces = list()
        for char in line.rstrip():
            if char in matching_parens.keys():
                open_braces.append(char)
            elif matching_parens[open_braces.pop()] != char:
                total_syntax_error += error_to_score[char]
                break

    return total_syntax_error


def solve10b(nav_subsystem_log):

    errors = list()

    matching_parens = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }
    error_to_score = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }

    for line in nav_subsystem_log:
        open_braces = list()
        corrupted = False
        for char in line.rstrip():
            if char in matching_parens.keys():
                open_braces.append(char)
            elif matching_parens[open_braces.pop()] != char:
                corrupted = True
                break
        if not corrupted:
            incomplete_score = 0
            for char in open_braces[::-1]:
                incomplete_score *= 5
                incomplete_score += error_to_score[matching_parens[char]]
            errors.append(incomplete_score)

    return statistics.median(errors)


if __name__ == "__main__":
    data_path = Path('10_data.txt')

    with open(data_path, mode='r') as f:
        nav_subsystem_log = f.readlines()

    print(f"Total syntax error: {solve10a(nav_subsystem_log)}")
    print(f"Autocomplete score: {solve10b(nav_subsystem_log)}")
