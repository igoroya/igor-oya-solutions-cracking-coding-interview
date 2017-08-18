'''
Created on 14 Aug 2017

Return Kth to Last: Implement an algorithm to find
the Kth to last element of a singly linked list

For the sake of the exercise, I will assume that we do not know the size of the list
(My custom Python list knows this information)

@author: igoroya
'''
from chapter2 import utils # TODO: try relative imports

def find_kth_to_last(my_list, position):

    slow_node = my_list.head_node
    runner_node = jump_n_nodes(my_list.head_node, position)

    if runner_node is None:
        return None

    while runner_node.next_node is not None:
        slow_node, runner_node = advance_two_pointers(slow_node, runner_node)

    return slow_node

def jump_n_nodes(node, jumps):

    for _ in range(jumps-1):
        if node.next_node is None:
            return None
        else:
            node = node.next_node

    return node

def advance_two_pointers(node1, node2):
    node1_next = node1.next_node
    node2_next = node2.next_node
    #print(node1_next)
    #print(node2_next)
    #print('')

    return node1_next, node2_next



if __name__ == '__main__':
    my_list = utils.make_sample_list()
    print(my_list)
    print(find_kth_to_last(my_list, 5))

