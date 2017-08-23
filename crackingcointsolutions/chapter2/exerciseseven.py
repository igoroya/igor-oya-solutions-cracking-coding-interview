'''
Created on 23 Aug 2017

Give two singly linked lists, determine if the two lists intersect.
Return the intersecting node. Note that the intersection is defined based on reference, not value.
That is, if the kth node of the first linked list is the exact same node (by reference) as the jth
node of the second linked list, then they are intersecting.

@author: igoroya
'''

from chapter2 import utils


def do_intersect(list1, list2):
    # run one list and build a set (hash) with the refernces
    # run second list and check if it is in set

    references = set()

    # run 1st list and fill the set
    node = list1.head_node
    while node is not None:
        references.add(node.cargo)
        node = node.next_node

    # run 2nd list and check if ref. in set
    node = list2.head_node
    while node is not None:
        if node.cargo in references:
            return node
        node = node.next_node

    return None

if __name__ == '__main__':
    str1 = "here"
    list1 = utils.SinglyLinkedList()
    list1.append("a")
    list1.append("e")
    list1.append("i")
    list1.append("o")
    list1.append(str1)

    list2 = utils.SinglyLinkedList()
    list2.append(1)
    list2.append(2)
    list2.append(3)
    list2.append(4)
    list2.append(str1)

    list3 = utils.SinglyLinkedList()
    list3.append("X")
    list3.append("W")
    list3.append("Y")

    list4 = utils.SinglyLinkedList()
    list4.append("X")
    list4.append(3)
    list4.append("Y")

    print("Intersection: {}".format(do_intersect(list1, list2)))
    print("Intersection: {}".format(do_intersect(list1, list3)))
    print("Intersection: {}".format(do_intersect(list2, list4)))




