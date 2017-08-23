'''
Created on 14 Aug 2017

Remove Dups: Write code to remove duplicates from an unsorted linked list.

FOLLOW UP:

How would you solve this problem if a temporary buffer is not allowed

@author: igoroya
'''
from chapter2 import utils


def remove_dups(my_list):
    '''
    Removes dups in list. One would make it part of the list class itself
    This solution uses hashing via the usage of set to achieve O(N) time
    '''
    if len(my_list) == 0:
        return

    node = my_list.head_node

    my_set = {node.cargo}

    while node.next_node is not None:
        if node.next_node.cargo in my_set:
            node.next_node = node.next_node.next_node
            my_list._length -= 1
        else:
            my_set.add(node.next_node.cargo)
            node = node.next_node

def remove_dups_2(my_list):
    '''
    Removes dups in list, without using data structures.
    This works at O(N^2)
    '''
    if len(my_list) == 0:
        return

    node = my_list.head_node

    while node.next_node is not None:
        other_node = node
        while other_node.next_node is not None:
            if node.cargo == other_node.next_node.cargo:
                other_node.next_node = other_node.next_node.next_node
                my_list._length -= 1
            else:
                other_node = other_node.next_node
        node = node.next_node

if __name__ == '__main__':
    my_list = utils.make_sample_list()
    print(my_list)
    remove_dups(my_list)
    print(my_list)

    my_list = utils.make_sample_list()
    print(my_list)
    remove_dups_2(my_list)
    print(my_list)
