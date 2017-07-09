#! /usr/bin/python3
"""
Project: py-data-structs
File: test_binaryTree.py
Author: Ryan Rushton
Email: ryan.rushton79@gmail.com
Github: github.com/rushton3179
Date Created: 25/4/17
Licence: 
"""

from unittest import TestCase, mock

from simple.trees.binary_tree import BinaryTree
from .test_helpers import create_bts


class TestBinaryTree(TestCase):

    bt_empty, bt_1, bt_2, bt_3, bt_4 = create_bts()

    @mock.patch.multiple(BinaryTree, __abstractmethods__=set())
    def test_equals(self):
        bt_empty_copy = BinaryTree(None, None, None)
        assert bt_empty_copy == self.bt_empty
        bt_1_copy = BinaryTree(1, None, None)
        assert bt_1_copy == self.bt_1
        bt_4_copy = BinaryTree(
            1, BinaryTree(
                2, None, BinaryTree(
                    3, BinaryTree(
                        4, None, None), BinaryTree(
                        5, None, None))), BinaryTree(
                6, BinaryTree(7, None, BinaryTree(
                    8, None, None)), None))
        assert bt_4_copy == self.bt_4

    @mock.patch.multiple(BinaryTree, __abstractmethods__=set())
    def test_is_empty(self):
        assert self.bt_empty.is_empty()
        assert not self.bt_1.is_empty()

    @mock.patch.multiple(BinaryTree, __abstractmethods__=set())
    def test_has_no_children(self):
        assert self.bt_empty.has_no_children()
        assert self.bt_1.has_no_children()
        assert not self.bt_2.has_no_children()
        assert not self.bt_4.has_no_children()

    @mock.patch.multiple(BinaryTree, __abstractmethods__=set())
    def test_size(self):
        assert self.bt_empty.size() == 0
        assert self.bt_1.size() == 1
        assert self.bt_2.size() == 2
        assert self.bt_3.size() == 3
        assert self.bt_4.size() == 8

    @mock.patch.multiple(BinaryTree, __abstractmethods__=set())
    def test_height(self):
        assert self.bt_empty.height() == -1
        assert self.bt_1.height() == 0
        assert self.bt_2.height() == 1
        assert self.bt_3.height() == 1
        assert self.bt_4.height() == 3

    @mock.patch.multiple(BinaryTree, __abstractmethods__=set())
    def test_insert_empty(self):
        empty_tree = BinaryTree(None, None, None)
        assert not empty_tree.contains(1)
        empty_tree.insert_empty(1)
        assert empty_tree.contains(1)

    @mock.patch.multiple(BinaryTree, __abstractmethods__=set())
    def test_insert_left(self):
        bt = BinaryTree(None, None, None)
        assert bt.is_empty()
        bt.insert_left(1)
        assert bt == self.bt_1
        bt.insert_left(2)
        assert bt == self.bt_2

    @mock.patch.multiple(BinaryTree, __abstractmethods__=set())
    def test_insert_right(self):
        bt = BinaryTree(None, None, None)
        assert not bt.contains(1)
        bt.insert_right(1)
        assert bt == self.bt_1
        bt.insert_right(2)
        assert bt == BinaryTree(1, None, BinaryTree(2, None, None))

    @mock.patch.multiple(BinaryTree, __abstractmethods__=set())
    def test_depth_first_search(self):
        assert self.bt_empty.depth_first_search(1) is None
        assert self.bt_1.depth_first_search(1) == self.bt_1
        assert self.bt_2.depth_first_search(2) == BinaryTree(2, None, None)
        assert self.bt_3.depth_first_search(3) == BinaryTree(3, None, None)
        assert self.bt_4.depth_first_search(8) == BinaryTree(8, None, None)
        assert self.bt_4.depth_first_search(4) == BinaryTree(4, None, None)
        bt_4_sub = BinaryTree(7, None, BinaryTree(8, None, None))
        bt_4_sub_2 = BinaryTree(3, BinaryTree(4, None, None),
                                BinaryTree(5,  None, None))
        assert self.bt_4.depth_first_search(7) == bt_4_sub
        assert self.bt_4.depth_first_search(3) == bt_4_sub_2

    @mock.patch.multiple(BinaryTree, __abstractmethods__=set())
    def test_breadth_first_search(self):
        assert self.bt_empty.breadth_first_search(1) is None
        assert self.bt_1.breadth_first_search(1) == self.bt_1
        assert self.bt_2.breadth_first_search(2) == BinaryTree(2, None, None)
        assert self.bt_3.breadth_first_search(3) == BinaryTree(3, None, None)
        assert self.bt_4.breadth_first_search(8) == BinaryTree(8, None, None)
        assert self.bt_4.breadth_first_search(4) == BinaryTree(4, None, None)
        bt_4_sub = BinaryTree(7, None, BinaryTree(8, None, None))
        bt_4_sub_2 = BinaryTree(3, BinaryTree(4, None, None),
                                BinaryTree(5, None, None))
        assert self.bt_4.breadth_first_search(7) == bt_4_sub
        assert self.bt_4.breadth_first_search(3) == bt_4_sub_2

    @mock.patch.multiple(BinaryTree, __abstractmethods__=set())
    def test_contains_dfs(self):
        assert self.bt_1.contains(1)
        assert self.bt_2.contains(2)
        assert self.bt_3.contains(3)
        assert self.bt_3.contains(BinaryTree(3, None, None))
        assert not self.bt_3.contains(4)
        assert not self.bt_3.contains(BinaryTree(4, None, None))
        assert self.bt_4.contains(6)

    @mock.patch.multiple(BinaryTree, __abstractmethods__=set())
    def test_contains_bfs(self):
        assert self.bt_1.contains(1, search='bfs')
        assert self.bt_2.contains(2, search='bfs')
        assert self.bt_3.contains(3, search='bfs')
        assert self.bt_3.contains(BinaryTree(3, None, None), search='bfs')
        assert not self.bt_3.contains(4, search='bfs')
        assert not self.bt_3.contains(BinaryTree(4, None, None), search='bfs')
        assert self.bt_4.contains(6, search='bfs')




