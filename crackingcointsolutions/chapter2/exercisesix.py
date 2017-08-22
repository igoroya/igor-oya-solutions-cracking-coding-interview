'''
Created on 22 Aug 2017

Palindrome: implement a function to check if a linked list is a palindrome

Assumptions: each node of the list contains a single letter.

1) Invert-copy list, gives also back list size
2) compare until middle: size/2

@author: igoroya
'''
from chapter2 import utils # TODO: try relative imports


def invert_list(my_list):
    "returns inverted list and size of it"
    inv_list = utils.SinglyLinkedList()
    node = my_list.head_node
    entries = 0

    while node is not None:
        inv_list.add_in_front(node.cargo)
        entries += 1
        node = node.next_node
    return inv_list, entries

def are_same_until_middle(list1, list2, size):
    node1 = list1.head_node
    node2 = list2.head_node

    for _ in range(int(1 + size/2)):
        if node1.cargo != node2.cargo:
            return False
        node1 = node1.next_node
        node2 = node2.next_node

    return True

def is_palindrome(orig_list):
    inv_list, size = invert_list(orig_list)

    return are_same_until_middle(orig_list, inv_list, size)


if __name__ == '__main__':
    list1 = utils.SinglyLinkedList()
    list1.append('a')
    list1.append('b')
    list1.append('a')
    print("List {} is palindrome? {}".format(list1, is_palindrome(list1)))
    print("----")

    list1 = utils.SinglyLinkedList()
    list1.append('a')
    list1.append('b')
    list1.append('b')
    print("List {} is palindrome? {}".format(list1, is_palindrome(list1)))
    print("----")

    list1 = utils.SinglyLinkedList()
    list1.append('a')
    list1.append('b')
    list1.append('b')
    list1.append('a')
    print("List {} is palindrome? {}".format(list1, is_palindrome(list1)))
    print("----")


    list1 = utils.SinglyLinkedList()
    list1.append('a')
    list1.append('a')
    list1.append('b')
    list1.append('a')
    list1.append('a')
    print("List {} is palindrome? {}".format(list1, is_palindrome(list1)))
    print("----")

    list1 = utils.SinglyLinkedList()
    list1.append('a')
    list1.append('b')
    list1.append('c')
    list1.append('d')
    list1.append('e')
    print("List {} is palindrome? {}".format(list1, is_palindrome(list1)))
    print("----")

    list1 = utils.SinglyLinkedList()
    list1.append('a')
    list1.append('b')
    list1.append('c')
    list1.append('b')
    list1.append('a')
    print("List {} is palindrome? {}".format(list1, is_palindrome(list1)))
    print("----")


