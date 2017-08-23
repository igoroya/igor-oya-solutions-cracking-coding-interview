'''
Created on 17 Aug 2017

Sum lists: You have two numbers represented by a linked list, where each node contains a single digit.
The digits are stored in reverse order, such that the 1s digit is at the head of the list. Write a function
that adds the two numbers and returns the sum as a linked list.

EXAMPLE:
Input: (7 -> 1 -> 6) + (5 -> 9 -> 2). That is 617 + 295
Output: 2 -> 1 ->9. That is, 912

FOLLOW UP:
Suppose that the digits are stored in forward order. Repeat the above problem
EXAMPLE:
Input: (6 -> 1 -> 7) + (2 -> 9 -> 5) . That is, 617 + 295
Output: 9 -> 1 -> 2. That is, 912

@author: igoroya
'''
from chapter2 import utils

def sum_lists(list1, list2):
    # for the sake of the exercise, I'll assume that I do not know the length of the
    # list beforehand (my implementation of a singly linked list knows it)
    # Basically, I assume I just have 2 head nodes

    node1 = list1.head_node
    node2 = list2.head_node

    new_list = utils.SinglyLinkedList()

    carry_over = 0

    while (node1 is not None) and (node2 is not None):
        if (node1 is not None):
            value1 = node1.cargo
            node1 = node1.next_node
        else:
            value1 = 0

        if (node2 is not None):
            value2 = node2.cargo
            node2 = node2.next_node
        else:
            value2 = 0

        added_value, carry_over = add_terms(value1, value2, carry_over)
        #print("value:{}, carry_over:{}".format(added_value, carry_over))
        new_list.append(added_value)

    if carry_over != 0:
        new_list.append(carry_over)

    return new_list

def invert_list(original_list):
    '''
    reorded the list in such a way that the head is the tail, so we can use the existing code
    sum_lists
    '''
    new_list = utils.SinglyLinkedList()
    my_node = original_list.head_node
    while (my_node is not None):
        new_list.add_in_front(my_node.cargo)
        my_node = my_node.next_node

    return new_list

def sum_lists_inv(list1, list2):
    inv_list1 = invert_list(list1)
    inv_list2 = invert_list(list2)

    sum_list_inv = sum_lists(inv_list1, inv_list2)

    return invert_list(sum_list_inv)

def add_terms(dt1, dt2, carry_over = 0):
    '''
    Adds two digits by giving back the added value for the digi and the
    carry over value
    '''
    added = dt1 + dt2 + carry_over
    #print(added)
    #print(added%10)

    return added%10, int((added - (added%10))/10)


if __name__ == '__main__':
    # Original exercise
    list1 = utils.SinglyLinkedList()
    list1.append(7)
    list1.append(1)
    list1.append(6)
    print(list1)

    list2 = utils.SinglyLinkedList()
    list2.append(5)
    list2.append(9)
    list2.append(2)
    print(list2)

    sum_list = sum_lists(list1, list2)
    print(sum_list)

    print("----")

    list1 = utils.SinglyLinkedList()
    list1.append(7)
    list1.append(1)
    list1.append(6)
    print(list1)

    list2 = utils.SinglyLinkedList()
    list2.append(5)
    list2.append(9)
    list2.append(8)
    print(list2)

    sum_list = sum_lists(list1, list2)
    print(sum_list)
    print("----")

    # 2nd part of exercise


    list1 = utils.SinglyLinkedList()
    list1.append(6)
    list1.append(1)
    list1.append(7)
    print(list1)

    list2 = utils.SinglyLinkedList()
    list2.append(2)
    list2.append(9)
    list2.append(5)
    print(list2)

    sum_list = sum_lists_inv(list1, list2)
    print(sum_list)

    print("----")

    list1 = utils.SinglyLinkedList()
    list1.append(6)
    list1.append(1)
    list1.append(7)
    print(list1)

    list2 = utils.SinglyLinkedList()
    list2.append(8)
    list2.append(9)
    list2.append(5)
    print(list2)

    sum_list = sum_lists_inv(list1, list2)
    print(sum_list)
    print("----")
