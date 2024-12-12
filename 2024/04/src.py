from pathlib import Path


def count_word(path, word):
    def word_in_dir(point, dir, length):
        if not 0 <= point[0] + dir[0] * (length - 1) <= height - 1 or not 0 <= point[1] + dir[1] * (length - 1) <= width - 1:
            return ""
        return "".join(text[point[0] + dir[0] * i][point[1] + dir[1] * i] for i in range(length))

    text = [list(line.rstrip()) for line in path.open()]
    if not text:
        return 0
    DIRS = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]
    height = len(text)
    width = len(text[0])
    tot = 0
    for idx in range(height):
        for jdx in range(width):
            if text[idx][jdx] == word[0]:
                tot += sum(word_in_dir((idx, jdx), dir, len(word)) == word for dir in DIRS)
    return tot


def count_mas(path):
    text = [list(line.rstrip()) for line in path.open()]
    if not text:
        return 0
    height = len(text)
    width = len(text[0])
    tot = 0
    other_letters = {"M", "S"}
    for idx in range(height):
        for jdx in range(width):
            if text[idx][jdx] == "A":
                if idx in (0, height - 1) or jdx in (0, width - 1):
                    continue
                tot += (
                    {text[idx + 1][jdx + 1], text[idx - 1][jdx - 1]} == other_letters
                    and
                    {text[idx - 1][jdx + 1], text[idx + 1][jdx - 1]} == other_letters
                )
    return tot


if __name__ == "__main__":
    ex_path = Path("example_data.txt")
    path = Path("data.txt")

    print(f"Part a (example): {count_word(ex_path, 'XMAS')}")
    print(f"Part a: {count_word(path, 'XMAS')}")

    print(f"Part b (example): {count_mas(ex_path)}")
    print(f"Part b: {count_mas(path)}")
