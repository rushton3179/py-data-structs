#! /usr/bin/python3
"""
Project: py-data-structs
File: avl_tree.py
Author: Ryan Rushton
Email: ryan.rushton79@gmail.com
Github: github.com/rushton3179
Date Created: 25/4/17
Licence: 
"""

from .binary_tree import BinaryTree

class AvlTree(BinaryTree):

    def balance_factor(self):
        return self.left.height() - self.right.height()
