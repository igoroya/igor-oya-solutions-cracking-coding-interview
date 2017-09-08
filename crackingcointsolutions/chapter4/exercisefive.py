'''
Created on 4 Sep 2017

Validate BST

This is the classical solution to this problem

@author: igoroya
'''
from chapter4 import utils


def is_binary_tree(root_node):

    high = float("inf")
    low = float("-inf")

    return is_binary_tree_node(root_node, low, high)

def is_binary_tree_node(node, low, high):
    if node is None:
        return True

    return (low < node.name and
            high > node.name and
            is_binary_tree_node(node.left, low, node.name) and
            is_binary_tree_node(node.right, node.name, high))


if __name__ == '__main__':
    my_root_node = utils.BinaryTreeNode(17)
    my_root_node.left = utils.BinaryTreeNode(12)
    my_root_node.right = utils.BinaryTreeNode(23)
    my_root_node.left.left = utils.BinaryTreeNode(6)
    my_root_node.left.right = utils.BinaryTreeNode(15)
    my_root_node.right.left = utils.BinaryTreeNode(19)
    my_root_node.right.right = utils.BinaryTreeNode(34)

    print(is_binary_tree(my_root_node))