#! /usr/bin/python3
"""
Project: py-data-structs
File: test_binarySearchTree.py
Author: Ryan Rushton
Email: ryan.rushton79@gmail.com
Github: github.com/rushton3179
Date Created: 25/4/17
Licence: 
"""

from copy import deepcopy
from random import randrange
from unittest import TestCase

from simple.trees.binary_search_tree import BinarySearchTree, \
    check_binary_search_tree
from .test_helpers import create_bsts, create_bts


class TestBinarySearchTree(TestCase):

    bst_empty, bst_1, bst_2, bst_3, bst_4 = create_bsts()

    def test_check_binary_search_tree(self):
        bt_empty, bt_1, bt_2, bt_3, bt_4 = create_bts()
        assert check_binary_search_tree(self.bst_empty)
        assert check_binary_search_tree(self.bst_1)
        assert check_binary_search_tree(self.bst_2)
        assert check_binary_search_tree(self.bst_3)
        assert check_binary_search_tree(self.bst_4)

        assert not check_binary_search_tree(bt_2)
        assert not check_binary_search_tree(bt_3)
        assert not check_binary_search_tree(bt_4)

    def test_insert(self):
        assert check_binary_search_tree(self.bst_empty)
        self.bst_empty.insert(1)
        assert check_binary_search_tree(self.bst_empty)
        assert self.bst_empty == self.bst_1
        self.bst_empty.insert(BinarySearchTree(2, None, None))
        assert check_binary_search_tree(self.bst_empty)
        assert self.bst_empty == self.bst_2
        self.bst_empty = BinarySearchTree(None, None, None)
        self.bst_empty.insert(2)
        self.bst_empty.insert(3)
        self.bst_empty.insert(1)
        assert check_binary_search_tree(self.bst_empty)
        assert self.bst_empty == self.bst_3

        # Test 100 randomly generates trees of size 50
        # Printing the tree if failing
        for y in range(100):
            self.bst_empty = BinarySearchTree(50, None, None)
            for x in range(50):
                last_tree = deepcopy(self.bst_empty)
                z = randrange(100)
                self.bst_empty.insert(z)
                assert check_binary_search_tree(self.bst_empty)
                assert self.bst_empty.size() == (last_tree.size() + 1)
        self.bst_empty = BinarySearchTree(None, None, None)

    def test_delete(self):
        bst_1_copy = BinarySearchTree(1, None, None)
        assert check_binary_search_tree(bst_1_copy)
        bst_1_copy.delete(1)
        assert bst_1_copy == self.bst_empty
        for y in range(100):
            elems_added = []
            self.bst_empty = BinarySearchTree(50, None, None)
            for x in range(50):
                z = randrange(100)
                self.bst_empty.insert(z)
                elems_added.append(z)
            for elem in elems_added:
                last_tree = deepcopy(self.bst_empty)
                self.bst_empty.delete(elem)
                assert check_binary_search_tree(self.bst_empty)
                assert self.bst_empty.size() == last_tree.size() - 1
        self.bst_empty = BinarySearchTree(None, None, None)
