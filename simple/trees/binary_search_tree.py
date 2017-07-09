#! /usr/bin/python3
"""
Project: py-data-structs
File: binary_search_tree.py
Author: Ryan Rushton
Email: ryan.rushton79@gmail.com
Github: github.com/rushton3179
Date Created: 25/4/17
Licence: 
"""

from copy import deepcopy

from .binary_tree import BinaryTree


class BinarySearchTree(BinaryTree):

    def __init__(self, node, left, right):
        super(BinarySearchTree, self).__init__(node, left, right)

    def ensure_tree(self, val):
        if type(val) is not BinarySearchTree:
            return BinarySearchTree(val, None, None)
        return val

    def insert(self, bst, equal_above=True, make_set=False):
        bst = self.ensure_tree(bst)
        if self.node == bst.node and not make_set:
            if equal_above:
                if not self.insert_right(bst):
                    self.right.insert(bst)
            else:
                if not self.insert_left(bst):
                    self.left.insert(bst)
        elif self.insert_empty(bst):
            return True

        elif bst.node < self.node:
            if not self.insert_left(bst):
                self.left.insert(bst)

        elif bst.node > self.node:
            if not self.insert_right(bst):
                self.right.insert(bst)

    def delete(self, node, search='dfs'):
        if search != 'dfs' and search != 'bfs':
            raise AttributeError
        if search == 'dfs':
            target = self.depth_first_search(node)
        else:
            target = self.breadth_first_search(node)

        if target:
            if target.has_no_children():
                target.node = None
                return target

            elif target.left_empty() and not target.right_empty():
                target_right = deepcopy(target.right)
                target.node = target_right.node
                target.right = target_right.right
                target.left = target_right.left
                return target

            elif not target.left_empty() and target.right_empty():
                target_left = deepcopy(target.left)
                target.node = target_left.node
                target.right = target_left.right
                target.left = target_left.left
                return target

            elif target.left.height() > target.right.height():
                target_right = deepcopy(target.right)
                target_left = deepcopy(target.left)
                target.node = target_left.node
                target.right = target_left.right
                target.left = target_left.left
                target.insert(target_right)
                return target
            elif target.left.height() <= target.right.height():
                target_right = deepcopy(target.right)
                target_left = deepcopy(target.left)
                target.node = target_right.node
                target.right = target_right.right
                target.left = target_right.left
                target.insert(target_left)
                return target


def check_binary_search_tree(bst):
    if bst.is_empty():
        return True
    elif bst.has_no_children():
        return True
    elif not bst.left_empty() and bst.right_empty() and bst.left.node <= \
                                                            bst.node:
        return check_binary_search_tree(bst.left)
    elif not bst.right_empty() and bst.left_empty() and bst.right.node >= \
            bst.node:
        return check_binary_search_tree(bst.right)
    elif not bst.right_empty() and not bst.left_empty() and bst.left.node <= \
            bst.node <= bst.right.node:
        left_rtn = check_binary_search_tree(bst.left)
        right_rtn = check_binary_search_tree(bst.right)
        if left_rtn and right_rtn:
            return True
