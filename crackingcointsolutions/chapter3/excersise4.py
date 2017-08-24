'''
Created on 24 Aug 2017

Queue via stacks

@author: igoroya
'''
from chapter3 import utils

class QueueV2(object):
    def __init__(self):
        self._input_stack = utils.Stack()
        self._output_stack = utils.Stack()
        # Add this to avoid making twice the 2 stack movement when peek & remove
        self.__cached_peek = None

    def add_item(self, item):
        '''
        add an item at the end of the queue
        '''
        if(self.__cached_peek is None):
            self.__cached_peek = item
        self._input_stack.push(item)

    def remove(self):
        '''
        removes 1st item of the queue
        '''
        while (self._input_stack):
            self._output_stack.push(self._input_stack.peek())
            self._input_stack.remove()

        # Pop the one of top: this is the oldest one
        self._output_stack.remove()
        self.__cached_peek = self._output_stack.peek()

        #move again all to the 1st stack
        while (self._output_stack):
            self._input_stack.push(self._output_stack.peek())
            self._output_stack.remove()

    def peek(self):
        '''
       `returns to the top of the queue (without removing)
        '''
        return self.__cached_peek

    def is_empty(self):
        '''
        Returns True if the queu is empty
        '''
        return self._input_stack.is_empty()

    def __repr__(self):
        return self._input_stack.__repr__()


if __name__ == '__main__':
    my_queue = QueueV2()
    utils.add_some_values_queue(my_queue, 15)
    print(my_queue)
    print("-------------")
    print("peek next: {}".format(my_queue.peek()))
    my_queue.remove()
    print("peek after removing one: {}".format(my_queue.peek()))
    print("-------------")
    print(my_queue)
    new_val = "perico"
    print("Adding entry: {}".format(new_val))
    my_queue.add_item(new_val)
    print(my_queue)
    print("peek next: {}".format(my_queue.peek()))
    my_queue.remove()
    print("peek after removing one: {}".format(my_queue.peek()))
    print("-------------")
    print(my_queue)


