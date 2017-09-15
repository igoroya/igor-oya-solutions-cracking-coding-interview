'''
Created on 9 Sep 2017

First Common Ancestor

@author: igoroya
'''
from chapter4 import utils



def find_first_common_ancestor(root, p, q):
    node, is_ancestor = common_ancestor_helper(root, p, q)
    return node if is_ancestor else None


def common_ancestor_helper(root, p, q):

    if root is None:
        return (None, False)

    if (root is p) and (root is q):
        # here we find that the node is at same time p and q
        return (root, True)

    left_node, is_left = common_ancestor_helper(root.left, p, q)
    if is_left:
        # Here we have that node at left is both p and q
        return (left_node, is_left)

    right_node, is_right = common_ancestor_helper(root.right, p, q)
    if is_right:
        # Here we have that node at right is both p and q
        return (right_node, is_right)

    if (left_node is not None) and (right_node is not None):
        # Here we have found one ancerstor at left and other at right
        return (root, True)
    elif (root is p) or (root is q):
        # here we find one of the ancestors
        is_ancestor =  (left_node is not None) or (right_node is not None)
        return (root, is_ancestor)
    else:
        # Here we arrive at one leaf of the tree and ancestor was not found
        return (left_node, False) if left_node is not None else (right_node, False)



if __name__ == '__main__':
    my_root_node = utils.BinaryTreeNode(17)
    my_root_node.left = utils.BinaryTreeNode(12)
    my_root_node.right = utils.BinaryTreeNode(23)
    my_root_node.left.left = utils.BinaryTreeNode(19)
    my_root_node.left.right = utils.BinaryTreeNode(28)
    my_root_node.right.left = utils.BinaryTreeNode(190)
    my_root_node.right.right = utils.BinaryTreeNode(280)
    my_root_node.left.left.left = utils.BinaryTreeNode(119)
    my_root_node.left.right.left = utils.BinaryTreeNode(128)
    my_root_node.left.right.left.right = utils.BinaryTreeNode(444)

    """
                            17
                12                 23
            19       28       190     280
        119       128
                      444
    """

    node_k = utils.BinaryTreeNode(64)

    print(find_first_common_ancestor(my_root_node,  my_root_node.left,  my_root_node.right))

