from pathlib import Path


class Element:
    def __init__(self, parent, name, subelements, size):
        self.parent = parent
        self.name = name
        self.subelements = subelements
        self.size = size

    def add_subelements(self, element):
        if self.subelements is None:
            raise Exception("Element of type file cannot contain subelements")
        self.subelements[element.name] = element

    def compute_size(self):
        if self.size:
            # Assuming directories can't change
            return

        if any([elem.size == 0 for elem in self.subelements.values()]):
            print("errr")
            print(self.name)
        self.size = sum([elem.size for elem in self.subelements.values()])

    def __repr__(self, level=0):
        res = " "*level + f"- {self.name} (dir)"
        for elem in self.subelements.values():
            if elem.subelements is None:
                res += "\n" + " "*(level+1) + f"- {elem.name} (size: {elem.size})"
            else:
                res += "\n" + elem.__repr__(level=level+1)
        return res


def get_root(path):
    with open(path, mode='r') as f:
        f.readline().rstrip()
        root = Element(None, "/", {}, 0)
        cur_dir = root
        for line in f:
            items = line.rstrip().split()
            if items[0] == "$" and items[1] == "cd":
                if items[2] == "..":
                    cur_dir.compute_size()
                    cur_dir = cur_dir.parent
                else:
                    cur_dir = cur_dir.subelements[items[2]]
            elif items[0] != "$":
                if items[0] == "dir":
                    cur_dir.add_subelements(Element(cur_dir, items[1], {}, 0))
                else:
                    cur_dir.add_subelements(Element(cur_dir, items[1], None, int(items[0])))

    # compute dirs for the last branch of opened directories (which are not cd-ed out of)
    while cur_dir is not None:
        cur_dir.compute_size()
        cur_dir = cur_dir.parent

    return root

def sum_dirs_below_size(root, size=100000):
    tot = 0
    subelements = list()
    for elem in root.subelements.values():
        if elem.subelements is None:
            continue
        if elem.size <= size:
            tot += elem.size
        tot += sum_dirs_below_size(elem)

    return tot


def solvea(path):
    root = get_root(path)
    return sum_dirs_below_size(root)


def get_smallest_dir_above_threshold(root, threshold):
    res = root.size

    for elem in root.subelements.values():
        if elem.subelements is None:
            continue
        if elem.size > threshold:
            res = min(res, get_smallest_dir_above_threshold(elem, threshold))

    return res

def solveb(path):
    root = get_root(path)
    tot_disk = 70000000
    needed = 30000000
    assert needed < tot_disk
    used = root.size
    to_free = needed-(tot_disk-used)
    if to_free < 0:
        return 0

    return get_smallest_dir_above_threshold(root, to_free)


if __name__ == "__main__":
    example_path = Path("example_data.txt")
    puzzle_path = Path("data.txt")

    print(f"Part a (example): {solvea(example_path)}")
    print(f"Part a: {solvea(puzzle_path)}")

    print(f"Part b (example): {solveb(example_path)}")
    print(f"Part b: {solveb(puzzle_path)}")
