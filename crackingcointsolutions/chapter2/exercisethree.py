'''
Created on 17 Aug 2017

Delete middle node: Implement an algorithm to delete a node in the middle,
(i.e. any node by the first and the last node, not exactly at the middle) of a singly linked list,
given only access to the node.


@author: igoroya
'''
from chapter2 import utils


def delete_node(node):
    #idea is to add the data from next node to this node
    #link this node to the one node after next node

    if node.next_node is None:
        raise Exception("Last node provide, not valid")

    node.cargo = node.next_node.cargo
    node.next_node = node.next_node.next_node

if __name__ == '__main__':
    my_list = utils.make_sample_list()
    print(my_list)
    #get one node that is in the middle
    my_node = my_list.search('c')
    delete_node(my_node)
    print(my_list)
