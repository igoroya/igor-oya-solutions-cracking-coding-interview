'''
Created on 31 Aug 2017

@author: igoroya
'''
import collections
from chapter4 import utils

def is_balanced(root_node):
    """
    Calculates if a node is balanced, assuming that a tree is not balanced if
    the depth of the two sub-trees of any node differs more than one
    """

    calculate_node_height(root_node) #this associates to each node a height

    stack = collections.deque()

    node = root_node
    stack.append(node)

    while len(stack) > 0:
        node = stack.pop()

        left_height = 0
        right_height = 0

        if node.right is not None:
            stack.append(node.right)
            right_height = node.right.height
        if node.left is not None:
            stack.append(node.left)
            left_height = node.left.height

        if abs(right_height - left_height) > 1:
            return False

        return True


def calculate_node_height(root_node):
    """
    Calculates the height of a node by finding
    how many levels exist down to the node which is
    located deepest.
    """
    if root_node is None:
        return 0

    height =  1 + max(calculate_node_height(root_node.left),
               calculate_node_height(root_node.right)
               )
    setattr(root_node, 'height', height)
    return height

if __name__ == '__main__':
    my_root_node = utils.BinaryTreeNode("A")
    my_root_node.left = utils.BinaryTreeNode("B")
    my_root_node.right = utils.BinaryTreeNode("C")
    my_root_node.left.left = utils.BinaryTreeNode("D")
    my_root_node.left.left.left = utils.BinaryTreeNode("E")
    my_root_node.left.left.right = utils.BinaryTreeNode("F")

    print("Is balanced? {}".format(is_balanced(my_root_node)))

    my_root_node = utils.BinaryTreeNode("A")
    my_root_node.left = utils.BinaryTreeNode("B")
    my_root_node.right = utils.BinaryTreeNode("C")
    my_root_node.left.left = utils.BinaryTreeNode("D")
    my_root_node.left.right = utils.BinaryTreeNode("E")

    print("Is balanced? {}".format(is_balanced(my_root_node)))
