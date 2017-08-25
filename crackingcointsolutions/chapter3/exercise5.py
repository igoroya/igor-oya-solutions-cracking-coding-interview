'''
Created on 25 Aug 2017

Sort Stack

@author: igoroya
'''
from chapter3 import utils
import copy

def sort_stack(stack):
    '''
    Assumes that content is comparable. One would check it in production
    skipping here for simplicity
    '''
    buffer = None
    ordered_stack = utils.Stack()

    #print("input stack: {}".format(stack))

    original_stack = copy.copy(stack)

    #print("copied stack before: {}".format(original_stack))

    while not original_stack.is_empty():
        if (ordered_stack.is_empty()) or (original_stack.peek() <= ordered_stack.peek()):
            ordered_stack.push(original_stack.peek())
            original_stack.remove()
        else:
            buffer = original_stack.peek()
            original_stack.remove()
            while(ordered_stack.peek() < buffer):
                original_stack.push(ordered_stack.peek())
                ordered_stack.remove()
                if ordered_stack.is_empty():
                    break
            original_stack.push(buffer)

    return ordered_stack

if __name__ == '__main__':
    my_stack = utils.Stack()
    utils.add_some_values(my_stack, 10)
    print("Original stack: {}".format(my_stack))
    sorter_stack = sort_stack(my_stack)
    print("Ordered stack: {}".format(sorter_stack))
    print("Original stack (after sort): {}".format(my_stack))
