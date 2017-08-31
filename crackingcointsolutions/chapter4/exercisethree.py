'''
Created on 30 Aug 2017

@author: igoroya
'''
import collections
from chapter4 import utils

def make_lists(root_node):
    stack = collections.deque()

    node_i = 1
    lists = []

    node = root_node
    stack.append(node)

    while len(stack) > 0:
        node = stack.pop()
        add_list(lists, node_i, node.name)
        node_i += 1
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)
    return lists

def add_list(lists, node_i, name):
    get_level = calc_level(node_i)
    level = get_level()
    if len(lists) < level:
        lists.append([name])
    else:
        lists[level - 1].append(name)

def calc_level(node_i): # this is a closure, reduces the overhead of having to derive level all the time
    level = 1
    def work():
        nonlocal level
        while True:
            div =(pow(2, level) - 1 ) // node_i
            if div == 1:
                return level
            elif div < 1:
                level += 1
            else:
                print("Something went wrong")
                return None # Should be an exception
    return work

if __name__ == '__main__':
    root_node = utils.BinaryTreeNode("A") # this is the root node
    root_node.left = utils.BinaryTreeNode("B")
    root_node.right = utils.BinaryTreeNode("C")
    node = root_node.left
    node.left = utils.BinaryTreeNode("D")
    node.right = utils.BinaryTreeNode("E")
    node = root_node.right
    node.left = utils.BinaryTreeNode("F")
    node.right = utils.BinaryTreeNode("G")
    node = node.left
    node.left = utils.BinaryTreeNode("H")
    node.right = utils.BinaryTreeNode("I")


    lists = make_lists(root_node)
    print(lists)