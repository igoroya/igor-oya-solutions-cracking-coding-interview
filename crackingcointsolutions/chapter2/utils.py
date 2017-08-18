'''
Created on 13 Aug 2017

Utilities module to provide a linked list for the exersises. IThere is no out of the box
collection in the python collections modules. In real life, one would usually use python lists
(they are not linked lists), or deques.

Disclaimer: The implementation here won't be very efficient, is not pythonic etc.
if one would be serious with making a linked list, one would have a look to a c impl.
Also, gpes without saying, this is not thread safe

@author: igoroya
'''
import string

class SinglyLinkedList(object):
    class Node(object):
        def __init__(self, cargo, next_node = None):
            self.cargo = cargo
            self.next_node = next_node

        def __eq__(self, other):
            return self.cargo == other.cargo and self.next_node and other.next_node

        def __repr__(self):
            return self.cargo.__repr__()

    def __init__(self):
        '''
        create an empty linked list
        '''
        self.head_node = None
        self.__current = self.head_node
        self._length = 0

    def __len__(self):
        return self._length

    def __contains__(self, value):
        current = self.head_node
        while current:
            if current.cargo == value:
                return True
            current = current.next_node
        return False

    def __iter__(self):
        while self.__current:
            current = self.__current
            self.__current = self.__current.next_node
            yield current

        self.__current = self.head_node

    def __repr__(self):
        node = self.head_node
        reps = []
        while node is not None:
            reps.append(node.__repr__())
            node = node.next_node

        return reps.__repr__()

    def insert(self, value, position = 0):
        if value is None:
            raise ValueError('cannot add None values')
        if position < 0:
            raise ValueError('cannot add values at negative position')
        if position > self._length:
            raise ValueError('cannot add value at position {} when list size is {}'.format(position, self._length))
        if position == 0:
            self.node = self.Node(value, self.head_node)
            self.head_node = self.node
            self.__current = self.head_node
            self._length += 1
        else:
            current = self.head_node
            count = 0
            while current and ((count + 1) <= position):
                if count + 1 == position:
                    self.node = self.Node(value, current.next_node)
                    current.next_node = self.node
                    self._length += 1
                    return
                else:
                    current = current.next_node
                    count += 1

    def pop(self, value):
        '''
        Remove a node based on the cargo data and pop the node object.
        None is returned if value does not exist.
        Update head if needed
        '''
        node = self.head_node

        if node.cargo == value:
            self.head_node = node.next_node
            self._length -= 1
            return node

        while node is not None:
            if node.next_node.cargo is value:
                node.next_node = node.next_node.next_node
                self._length -= 1
                return node
            node = node.next_node

        return None

    def search(self, value):
        '''
        Look for the 1st node that carries value and return it,
        or None if it does not exist
        '''
        current = self.head_node
        while current:
            if current.cargo == value:
                return current
            current = current.next_node
        return None

    def add_in_front(self, value):
        self.insert(value, 0)

    def append(self, value):
        self.insert(value, self._length)



def make_sample_list():
    '''
    Helper function to create a sampel list for the exercises
    '''

    my_list = SinglyLinkedList()

    value = 'Head'
    my_list.append(value)

    my_string = string.ascii_lowercase[:5]

    for c in my_string:
        my_list.append(c)

    #do twice to have dups
    for c in my_string:
        my_list.append(c)


    value = 'Tail'
    my_list.append(value)

    return my_list



def make_sample_list_nums():
    '''
    Helper function to create a sampel list for the exercises
    '''

    my_list = SinglyLinkedList()

     #do twice to have dups
    for n in range(6):
        my_list.append(2*n)

    for n in range(6):
        my_list.append(n)




    return my_list

