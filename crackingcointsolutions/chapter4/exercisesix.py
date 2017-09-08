'''
Created on 6 Sep 2017

Find successor

@author: igoroya
'''
from chapter4 import utils

def find_successor(node):
    if node.right is None:
        return node.parent

    next_node = node.right

    while next_node.left is not None:
        next_node = next_node.left

    return next_node

class LinkedBinaryTree(utils.BinaryTreeNode):
    def __init__(self, name=None, parent=None):
        '''
        A simple node of a binary tree with a link of child with parent
        '''
        self.name = name
        self._left = None
        self._right = None
        self.parent = None

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    def add_left(self, name=None):
        self._left = LinkedBinaryTree(name, self)

    def add_right(self, name=None):
        self._right = LinkedBinaryTree(name, self)

if __name__ == '__main__':

    my_root_node = LinkedBinaryTree(17)
    my_root_node.add_left(12)
    my_root_node.add_right(23)
    my_root_node.left.add_left(6)
    my_root_node.left.add_right(15)
    my_root_node.right.add_left(19)
    my_root_node.right.add_right(34)

    print("Node: {}, successor: {}".format(my_root_node.name, find_successor(my_root_node).name))
    print("Node: {}, successor: {}".format(my_root_node.left.name, find_successor(my_root_node.left).name))

