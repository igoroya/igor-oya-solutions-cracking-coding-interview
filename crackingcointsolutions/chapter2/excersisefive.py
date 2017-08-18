'''
Created on 17 Aug 2017

Sum lists: You have two numbers represented by a linked list, where each node contains a single digit.
The digits are stored in reverse order, such that the 1s digit is at the head of the list. Write a function
that adds the two numbers and returns the sum as a linked list.

EXAMPLE:
Input: (7 -> 1 -> 6) + (5 -> 9 -> 2). That is 617 + 295
Output: 9 -> 1 ->2. That is, 912

FOLLOW UP:
Suppose that the digits are stored in forward order. Repeat the above problem
EXAMPLE:
Input: (6 -> 1 -> 7) + (2 -> 9 -> 5) . That is, 617 + 295
Output: 9 -> 1 ->. That is, 912

@author: igoroya
'''
from chapter2 import utils # TODO: try relative imports

def sum_lists(list1, list2):
    sum_list = utils.SinglyLinkedList()
    # for the sake of the exercise, I'll assume that I do not know the length of the
    # list beforehand (my implementtion of a singly linked list knows it)
    # Basically, I assume I just have 2 head nodes

if __name__ == '__main__':
    pass