#! /usr/bin/python3
"""
Project: py-data-structs
File: binary_tree.py
Author: Ryan Rushton
Email: ryan.rushton79@gmail.com
Github: github.com/rushton3179
Date Created: 25/4/17
Licence: 
"""

from abc import ABC, abstractmethod


class BinaryTree(ABC):

    def __init__(self, node, left, right):
        self.node = node
        self.left = left
        self.right = right

    def __eq__(self, other):
        if other:
            if self.node != other.node:
                return False
            else:
                return self.left == other.left and self.right == other.right
        return False

    @abstractmethod
    def insert(self, node):
        pass

    @abstractmethod
    def delete(self, node, search='dfs'):
        pass

    @abstractmethod
    def ensure_tree(self, val):
        if type(val) is not BinaryTree:
            return BinaryTree(val, None, None)
        return val

    def is_empty(self):
        if self.has_no_children() and self.node is None:
            return True
        return False

    def left_empty(self):
        if self.left is not None and self.left.node is not None:
            return False
        return True

    def right_empty(self):
        if self.right is not None and self.right.node is not None:
            return False
        return True

    def has_no_children(self):
        if self.left_empty() and self.right_empty():
            return True
        return False

    def size(self) -> int:
        if self.is_empty():
            return 0
        if self.has_no_children():
            return 1
        elif self.left_empty():
            return 1 + self.right.size()
        elif self.right_empty():
            return 1 + self.left.size()
        else:
            return 1 + self.left.size() + self.right.size()

    def height(self) -> int:
        if self.is_empty():
            return -1
        if self.has_no_children():
            return 0
        elif self.left_empty():
            return 1 + self.right.height()
        elif self.right_empty():
            return 1 + self.left.height()
        else:
            return 1 + max(self.left.height(), self.right.height())

    def insert_empty(self, binary_tree) -> bool:
        binary_tree = self.ensure_tree(binary_tree)
        if self.is_empty():
            self.node = binary_tree.node
            self.left = binary_tree.left
            self.right = binary_tree.right
            return True
        return False

    def insert_left(self, binary_tree) -> bool:
        binary_tree = self.ensure_tree(binary_tree)
        if self.insert_empty(binary_tree):
            return True
        if not self.left_empty():
            return False
        else:
            self.left = binary_tree
            return True

    def insert_right(self, binary_tree) -> bool:
        binary_tree = self.ensure_tree(binary_tree)
        if self.insert_empty(binary_tree):
            return True
        if not self.right_empty():
            return False
        else:
            self.right = binary_tree
            return True

    def depth_first_search(self, target):
        if self.node == target:
            return self
        else:
            if not self.right_empty():
                rtn = self.right.depth_first_search(target)
                if rtn:
                    return rtn
            if not self.left_empty():
                rtn = self.left.depth_first_search(target)
                if rtn:
                    return rtn

    def breadth_first_search(self, target):
        queue = list()
        queue.append(self)
        while len(queue) > 0:
            elem = queue.pop(0)
            if elem and elem.node == target:
                return elem
            else:
                if not elem.left_empty():
                    queue.append(elem.left)
                if not elem.right_empty():
                    queue.append(elem.right)

    def contains(self, val, search='dfs'):
        if type(val) is BinaryTree:
            val = val.node
        if search != 'dfs' and search != 'bfs':
            raise AttributeError
        if search == 'dfs' and self.depth_first_search(val):
            return True
        if search == 'bfs' and self.breadth_first_search(val):
            return True
        return False

    def print(self, prefix="", is_tail=True):
        if is_tail:
            if self.node is not None:
                print(prefix + "└── " + str(self.node))
                if self.right is None:
                    print(prefix + "    ├── ")
                else:
                    self.right.print(prefix + "    ", False)
                if self.left is None:
                    print(prefix + "    └── ")
                else:
                    self.left.print(prefix + "    ", True)
            else:
                print(prefix + "└── ")
        else:
            print(prefix + "├── " + str(self.node))
            if self.right is None:
                print(prefix + "│   ├── ")
            else:
                self.right.print(prefix + "│   ", False)
            if self.left is None:
                print(prefix + "│   └── ")
            else:
                self.left.print(prefix + "│   ", True)

    def pretty_print(self):
        BinaryTreePrinter().print_tree(self)


class BinaryTreePrinter:

    def print_tree(self, bt):
        max_level = bt.height()+1
        tree_list = [bt]
        self.print_node_internal(tree_list, 1, max_level)

    def print_node_internal(self, tree_list, level: int, max_level: int):

        def print_whitespaces(count: int):
            for i in range(count):
                print(' ', end='')

        def all_nodes_none(tree_list):
            for tree in tree_list:
                if tree:
                    return False
            return True

        if len(tree_list) == 0 or all_nodes_none(tree_list):
            return

        floor = max_level - level
        edge_lines = int(2 ** max(floor - 1, 0))
        first_spaces = int((2 ** floor) - 1)
        between_spaces = int((2 ** (floor + 1)) - 1)

        print_whitespaces(first_spaces)

        new_tress_list = list()
        for tree in tree_list:
            if tree:
                print(tree.node, end='')
                new_tress_list.append(tree.left)
                new_tress_list.append(tree.right)
                print_whitespaces(between_spaces - len(str(tree.node)) + 1)
            else:
                new_tress_list.append(None)
                new_tress_list.append(None)
                print(' ', end='')
                print_whitespaces(between_spaces)
        print('')

        for i in range(1, edge_lines+1):
            for j in range(len(tree_list)):
                print_whitespaces(first_spaces - i)
                if tree_list[j] is None:
                    print_whitespaces(2 * edge_lines + i + 1)
                    continue
                if tree_list[j].left:
                    print('/', end='')
                else:
                    print_whitespaces(1)

                print_whitespaces(2 * i - 1)

                if tree_list[j].right:
                    print('\\', end='')
                else:
                    print_whitespaces(1)

                print_whitespaces(2 * edge_lines - i)

            print('')

        self.print_node_internal(new_tress_list, level + 1, max_level)
