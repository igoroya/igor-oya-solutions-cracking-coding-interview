'''
Created on 17 Aug 2017

Partition: Write code to partition a linked list around a value x, such that
all nodes less than x come before all nodes greater than or equal to x. If x is contained
within the list, the values of x only need to be after the elements less than x (see below).
The partition element x can appear anywhere in the right partition; it does not need to appear between
the left and the right partitions.

EXAMPLE:
Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition = 5]
Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8

@author: igoroya
'''
from chapter2 import utils # TODO: try relative imports

def partition(linked_list, partition):
    # Idea: run over list and put to head any element that is below value
    # One could check proper types here

    node = linked_list.head_node

    while node.next_node is not None:
        #print("Evaluate node: {}".format(node.next_node))
        if node.next_node.cargo < partition:
            #print("{} is smaller than {}".format(node.next_node.cargo, partition))
            put_next_node_to_head(linked_list, node)
        else:
            node = node.next_node

def put_next_node_to_head(linked_list, prev_node):
    head = linked_list.head_node
    my_node = prev_node.next_node
    next_node = prev_node.next_node.next_node

    prev_node.next_node = next_node
    my_node.next_node = head
    linked_list.head_node = my_node



if __name__ == '__main__':
    my_list = utils.make_sample_list_nums()
    print( my_list)

    pivot = 4
    partition(my_list, pivot)
    print("{} (pivot {})".format(my_list, pivot))