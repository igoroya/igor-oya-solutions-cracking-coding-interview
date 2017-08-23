'''
Created on 23 Aug 2017

Loop detection: Given a circular linked list, implement an algorithm
that returns the beginning of the loop

DEFINITION
Circular linked list: A (corrupt) linked list in which a node's next pointer points
to another as to make a loop in the linked list.

EXAMPLE:
Input A -> B -> C -> D -> E -> C [the same as C earlier]
Output: C

@author: igoroya
'''

from chapter2 import utils

# Idea: Store in a set a tuple of (node, next_node)
# Run list and check if new tuple is already in list

def is_circular(my_list):
    my_set = set()
    node = my_list.head_node

    count = 0

    while node.next_node is not None:
        if (node.cargo, node.next_node.cargo) in my_set:
            # indication that may be same, make that "node"
            # is referenced before by runnign again
            if is_node_in_list_num_nodes(node.next_node, my_list, count):
                return True, node
        my_set.add((node.cargo, node.next_node.cargo))
        node = node.next_node
        count += 1
    return False, None

def is_node_in_list_num_nodes(my_node, my_list, n):
    '''
    Find is a node is in a list's first N nodes
    '''
    count = 0
    node = my_list.head_node
    while node is not None:
        if my_node is node:
            return True
        if count == n:
            break
        node = node.next_node
        count += 1

    return False

if __name__ == '__main__':
    # a well behaving list
    str1 = "here"
    list1 = utils.SinglyLinkedList()
    list1.append("a")
    list1.append("e")
    list1.append("i")
    list1.append("o")
    list1.append(str1)
    print("Is circular?: {}, at {}".format(*is_circular(list1)))

    # corrupted list now:
    list1.head_node.next_node.next_node.next_node.next_node =  list1.head_node.next_node
    print("Is circular?: {}, at {}".format(*is_circular(list1)))

    # this is not corrupted
    str1 = "here"
    list1 = utils.SinglyLinkedList()
    list1.append("a")
    list1.append("e")
    list1.append("i")
    list1.append("o")
    list1.append(str1)
    list1.append("a")
    list1.append("e")
    list1.append("i")
    list1.append("o")
    list1.append(str1)
    print("Is circular?: {}, at {}".format(*is_circular(list1)))

    # this is corrupted
    str1 = "here"
    list1 = utils.SinglyLinkedList()
    list1.append("a")
    list1.append("e")
    list1.append("i")
    list1.append("o")
    list1.append(str1)
    list1.append("a")
    list1.append("e")
    list1.append("i")
    list1.append("o")
    list1.append(str1)
    list1.head_node.next_node.next_node.next_node.next_node.next_node.next_node =  list1.head_node.next_node.next_node
    print("Is circular?: {}, at {}".format(*is_circular(list1)))

