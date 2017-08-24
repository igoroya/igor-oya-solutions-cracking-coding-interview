'''
Created on 24 Aug 2017

Stack of plates

@author: igoroya
'''
from chapter3 import utils


class StackOfPlates(object):
    '''
    Represents a set of literal stacks plates
    '''

    def __init__(self, max_stack_size):
        '''
        Constructor
        '''
        self._stacks = [] # lazy init of 1st stack at 1st push
        self._max_stack_size = max_stack_size

    def __repr__(self):
        return self._stacks.__repr__()

    def __len__(self):
        sizes = 0
        for stack in self._stacks:
            sizes += len(stack)
        return sizes

    def n_of_stacks(self):
        return len(self._stacks)

    def push(self):
        '''
        add a plate at the top of the active stack. if the active stack is full, start new one
        '''
        if (not bool(self._stacks)) or (len(self._stacks[-1]) == self._max_stack_size):
            stack = utils.Stack()
            self._stacks.append(stack)
        else:
            stack = self._stacks[-1]

        stack.push("Plate")

    def remove(self):
        '''
        removes top plate of the last stack
        '''
        if(not bool(self._stacks)):
            print("Sorry, not stacks exist") # better would be an execption
            return

        self._stacks[-1].remove()
        if self._stacks[-1].is_empty():
            self._stacks.pop()

    def peek(self):
        '''
       `returns to the top of the queue (without removing)
        '''
        if(not bool(self._stacks)):
            print("All stacks are empty")
            return None

        return self._stacks[-1].peek()

    def is_empty(self):
        '''
        Returns True if the queu is empty
        '''
        return not bool(self._stacks)

    def pop_at(self, stack_index):
        if stack_index + 1>=  len(self._stacks):
            print("Stack does not exist")
            return None #should be a exception instead
        value = self._stacks[stack_index].peek()
        self._stacks[stack_index].remove()
        return value

if __name__ == '__main__':
    my_plates = StackOfPlates(10)
    for _ in range(35):
        my_plates.push()
    print(my_plates)
    print("Number of plates: {} using: {} stacks".format(len(my_plates), my_plates.n_of_stacks()))
    for _ in range(35):
        my_plates.remove()
    print("is empty? {}".format(my_plates.is_empty()))

    for _ in range(35):
        my_plates.push()

    my_plates.pop_at(0)
    my_plates.pop_at(1)
    my_plates.pop_at(2)
    my_plates.pop_at(3)
    my_plates.pop_at(4)
    print(my_plates)


