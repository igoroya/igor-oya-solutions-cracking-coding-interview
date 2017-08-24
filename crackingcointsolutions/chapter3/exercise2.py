'''
Created on 23 Aug 2017

Minimum: How would design a stack that which, in addition to push and pop, has
a function that returns the minimum element. Push, pop and peek should operate at O(1) time

Idea: when asked for the minimum, empty the stack and make a new one replacing the old one,
calculating the minimum in the process. Then get_minimum_element would be O(N) N being the size
of the stack.

@author: igoroya
'''
from chapter3 import utils

class StackV2(utils.Stack):

    def get_minimum_element(self):
        entries = []
        minimum = float('inf')
        while not self.is_empty():
            entry = self.peek()
            #print(entry)
            if entry < minimum:
                minimum = entry
            #print(entry)
            entries.append(entry)
            self.remove()

        for i in reversed(entries):
            self.push(i)

        return minimum

if __name__ == '__main__':
    my_stack = StackV2()
    utils.add_some_values(my_stack, 20)
    print(my_stack)
    print("is empty {}".format(my_stack.is_empty()))
    print("-----")
    print("Minimum value: {}".format(my_stack.get_minimum_element()))
    print("-----")
    print(my_stack)
