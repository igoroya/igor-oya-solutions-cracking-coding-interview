'''
Created on 23 Aug 2017

Utilities to provide simple queues and stacks structures
It is mainly based on the standard deques. It is not fully efficient for the
'peek' operation, but keep as it is for simplicity

@author: igoroya
'''

import collections
import random
import copy

class Queue(object):
    '''
    Represents a very simple queue by wrapping a deque
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self._deque = collections.deque()

    def __repr__(self):
        '''
        Provide the content of the queue. The repr have the 'deque' incorporated
        in the string, a production solution should take it out
        '''
        return self._deque.__repr__()

    def add_item(self, item):
        '''
        add an item at the end of the queue
        '''
        self._deque.appendleft(item)

    def remove(self):
        '''
        removes 1st item of the queue
        '''
        self._deque.pop()

    def peek(self):
        '''
       `returns to the top of the queue (without removing)
        '''
        value = self._deque.pop()
        self._deque.append(value)
        return value

    def is_empty(self):
        '''
        Returns True if the queu is empty
        '''
        return not bool(self._deque)


class Stack(object):
    '''
    Represents a very simple stack by wrapping a deque
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self._deque = collections.deque()

    def __repr__(self):
        '''
        Provide the content of the stack. The repr have the 'deque' incorporated
        in the string, a production solution should take it out
        '''
        return self._deque.__repr__()

    def __len__(self):
        return self._deque.__len__()

    def __copy__(self):
        newone = type(self)()
        newone._deque = copy.copy(self._deque)
        return newone

    def push(self, item):
        '''
        add an item at the top of the stack
        '''
        self._deque.appendleft(item)

    def remove(self):
        '''
        removes item of the top of the stack
        '''
        self._deque.popleft()

    def peek(self):
        '''
       `returns to the top of the stack (without removing)
        '''
        value = self._deque.popleft()
        self._deque.appendleft(value)
        return value

    def is_empty(self):
        '''
        Returns True if the stack is empty
        '''
        return not bool(self._deque)


def add_some_values(stack, n_values):
    '''
    Adds some float values to the stack
    '''
    values = [random.randint(0,100) for _ in range(n_values)]

    for i in values:
        stack.push(i)

def add_some_values_queue(queue, n_values):
    '''
    Adds some float values to the stack
    '''
    values = [random.randint(0,100) for _ in range(n_values)]

    for i in values:
        queue.add_item(i)
