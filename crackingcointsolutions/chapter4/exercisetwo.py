'''
Created on 29 Aug 2017

@author: igoroya
'''
from chapter4 import utils
import collections

def make_binary_search_tree(data):
    root_node = utils.BinaryTreeNode()
    process_array(data, root_node)
    return root_node

def process_array(array, node=None):
    if (len(array) == 0):
        return None
    middle = int(len(array) / 2)
    lower_array = array[0: middle]
    higher_array = array[middle + 1:]
    #print("Array: {}, Middle: {}, low: {}, high: {}".format(array, array[middle], lower_array, higher_array))
    if node is None:
        node = utils.BinaryTreeNode()
    node.name = array[middle]
    node.left = process_array(lower_array)
    node.right = process_array(higher_array)
    return node

def print_tree(node):
    my_stack = collections.deque()
    my_stack.append(node)
    while len(my_stack) > 0:
        node = my_stack.pop()
        print(node)
        #print(node.name)
        #for child in node.children:
        #    print(child.name)

        if node.right is not None:
            my_stack.append(node.right)
        if node.left is not None:
            my_stack.append(node.left)


if __name__ == '__main__':
    my_data = [1, 2, 4, 7, 10, 14, 16, 30, 35, 40, 54, 76]
    my_tree = make_binary_search_tree(my_data)
    print_tree(my_tree)