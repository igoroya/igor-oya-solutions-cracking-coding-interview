'''
Created on 15 Sep 2017

BST sequences

@author: igoroya
'''

from chapter4 import utils

def get_bst_sequences(root_node):
    """
    Build any array with the content and find all the permutations
    """
    array = []
    build_one_array_from_bst(root_node, array)

    permute(array, 0, len(array) - 1)

def build_one_array_from_bst(root_node, array):
    """
    Build an arraylist from a depth first search
    """
    if root_node is None:
        return

    if array is None:
        raise AttributeError("array is empty")

    build_one_array_from_bst(root_node.left, array)
    array.append(root_node.name)
    build_one_array_from_bst(root_node.right, array)


def permute(array, l, r):
    if l == r:
        print(array)
    else:
        for i in range(l, r+1):
            array[l], array[i] = array[i], array[l]
            permute(array, l+1, r)
            array[l], array[i] = array[i], array[l]

if __name__ == '__main__':
    my_root_node = utils.BinaryTreeNode(17)
    my_root_node.left = utils.BinaryTreeNode(12)
    my_root_node.right = utils.BinaryTreeNode(23)
    my_root_node.left.left = utils.BinaryTreeNode(6)
    my_root_node.left.right = utils.BinaryTreeNode(15)
    my_root_node.right.left = utils.BinaryTreeNode(19)
    my_root_node.right.right = utils.BinaryTreeNode(34)

    """
                        17
                12                23
            6        15        19    34

    """

    get_bst_sequences(my_root_node)


