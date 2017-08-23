'''
Created on 23 Aug 2017

Utilities to provide simple queues and stacks structures
It is mainly based on the standard deques. It is not fully efficient for the
'peek' operation, but keep as it is for simplicity

@author: igoroya
'''

import collections

class Queue(object):
    '''
    Represents a very simple queue by wrapping a deque
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self._deque = collections.deque

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

    def isEmpty(self):
        '''
        Returns True if the queu is empty
        '''
        return bool(self._deque)


class Stack(object):
    '''
    Represents a very simple stack by wrapping a deque
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self._deque = collections.deque

    def add_item(self, item):
        '''
        add an item at the end of the queue
        '''
        self._deque.appendleft(item)

    def remove(self):
        '''
        removes 1st item of the queue
        '''
        self._deque.popleft()

    def peek(self):
        '''
       `returns to the top of the queue (without removing)
        '''
        value = self._deque.popleft()
        self._deque.appendleft(value)
        return value

    def isEmpty(self):
        '''
        Returns True if the queu is empty
        '''
        return bool(self._deque)

