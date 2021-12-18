import copy

from math import ceil, floor
from pathlib import Path
from functools import reduce
from itertools import combinations


class BinaryTreeNode:

    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


    def __repr__(self):
        if self.value is not None:
            return str(self.value)
        return (self.left is not None) * ('[' + repr(self.left) + ',') + \
               (self.right is not None) * (repr(self.right) + ']')


    def reduce(self):
        while (height := self.get_height()) > 4 or self.max_num() >= 10:
            if height == 5:
                self.explode()
            else:
                self.split()


    def get_height(self):
        if self.value is not None:
            return 0
        height_subtrees = 0
        if self.left is not None:
            height_subtrees = self.left.get_height()
        if self.right is not None:
            height_subtrees = max(self.right.get_height(), height_subtrees)
        return height_subtrees + 1


    def explode(self):
        left_value_node = None
        stack = [(self, 0)]

        while True:
            node, level = stack.pop()

            if level == 4 and node.left is not None and node.right is not None:
                # add left value to leftmost number
                left_val = node.left.value
                if left_value_node is not None:
                    left_value_node.value += left_val
                right_val = node.right.value

                # replace pair with 0 value node
                node.left = None
                node.right = None
                node.value = 0

                # add right value to rightmost number
                while stack:
                    node, _ = stack.pop()
                    if node.value is not None:
                        node.value += right_val
                        break
                    if node.right is not None:
                        stack.append((node.right, 0))
                    if node.left is not None:
                        stack.append((node.left, 0))
                break
            if node.value is not None:
                left_value_node = node
                continue
            if node.right is not None:
                stack.append((node.right, level+1))
            if node.left is not None:
                stack.append((node.left, level+1))

    def max_num(self):
        if self.value is not None:
            return self.value
        num = 0
        if self.left is not None:
            num = self.left.max_num()
        if self.right is not None:
            num = max(self.right.max_num(), num)
        return num


    def split(self):
        stack = [self]

        while stack:
            node = stack.pop()
            if node.value is not None and node.value >= 10:
                node.left = BinaryTreeNode(value=floor(node.value / 2))
                node.right = BinaryTreeNode(value=ceil(node.value / 2))
                node.value = None
                break
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)


    def get_magnitude(self):
        if self.value is not None:
            return self.value
        res = 0
        if self.left is not None:
            res += 3*self.left.get_magnitude()
        if self.right is not None:
            res += 2*self.right.get_magnitude()
        return res


def str2bintree(data_str):
    if data_str.isdigit():
        return BinaryTreeNode(value=int(data_str))

    count_open_parens = 0
    central_comma_idx = float('inf')
    for i, char in enumerate(data_str):
        if char == '[':
            count_open_parens += 1
        elif char == ']':
            count_open_parens -= 1
        elif char == ',' and count_open_parens == 1:
            central_comma_idx = i

    left_branch = str2bintree(data_str[1:central_comma_idx])
    right_branch = str2bintree(data_str[central_comma_idx+1:-1])

    return BinaryTreeNode(left=left_branch, right=right_branch)


def add_snailfish(num1, num2):
    sum = BinaryTreeNode(left=num1, right=num2)
    sum.reduce()
    return sum


if __name__ == "__main__":
    data_path = Path('18_data.txt')
    snailfish_numbers = list()

    with open(data_path, mode='r') as f:
        for line in f:
            snailfish_numbers.append(str2bintree(line.rstrip()))

    # part a
    lan_num = reduce(lambda x,y: add_snailfish(x, y), copy.deepcopy(snailfish_numbers))
    print(f"Magnitude of final sum: {lan_num.get_magnitude()}")

    # part b
    max_magnitude = 0
    for num_a, num_b in combinations(snailfish_numbers, 2):
        sum_1 = add_snailfish(copy.deepcopy(num_a), copy.deepcopy(num_b))
        sum_2 = add_snailfish(copy.deepcopy(num_b), copy.deepcopy(num_a))

        max_magnitude = max(sum_1.get_magnitude(), sum_2.get_magnitude(), max_magnitude)

    print(f"Maximum magnitude of the sum of any two provided snailfish numbers: {max_magnitude}")
