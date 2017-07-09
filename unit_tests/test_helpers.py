#! /usr/bin/python3
"""
Project: py-data-structs
File: test_helpers.py
Author: Ryan Rushton
Email: ryan.rushton79@gmail.com
Github: github.com/rushton3179
Date Created: 25/4/17
Licence: 
"""

from unittest import mock

from simple.trees.binary_search_tree import BinarySearchTree
from simple.trees.binary_tree import BinaryTree


@mock.patch.multiple(BinaryTree, __abstractmethods__=set())
def create_bts():
    bt_empty = BinaryTree(None, None, None)
    bt_1 = BinaryTree(1, None, None)
    bt_2 = BinaryTree(1, BinaryTree(2, None, None), None)
    bt_3 = BinaryTree(1, BinaryTree(2, None, None), BinaryTree(3, None, None))
    bt_4 = BinaryTree(
        1, BinaryTree(
            2, None, BinaryTree(
                3, BinaryTree(
                    4, None, None), BinaryTree(
                    5, None, None))), BinaryTree(
            6, BinaryTree(7, None, BinaryTree(
                8, None, None)), None))
    return bt_empty, bt_1, bt_2, bt_3, bt_4


def create_bsts():
    bst_empty = BinarySearchTree(None, None, None)
    bst_1 = BinarySearchTree(1, None, None)
    bst_2 = BinarySearchTree(1, None, BinarySearchTree(2, None, None))
    bst_3 = BinarySearchTree(2, BinarySearchTree(1, None, None),
                             BinarySearchTree(3, None, None))
    bst_4 = BinarySearchTree(
        5, BinarySearchTree(
            2, BinarySearchTree(1, None, None), BinarySearchTree(
                4, BinarySearchTree(
                    3, None, None), None)),
        BinarySearchTree(
            8, BinarySearchTree(6, None, BinarySearchTree(
                7, None, None)), None))
    return bst_empty, bst_1, bst_2, bst_3, bst_4

