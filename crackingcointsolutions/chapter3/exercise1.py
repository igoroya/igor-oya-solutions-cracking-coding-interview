'''
Created on 23 Aug 2017

Three in one: Describe how you could use a single array to implement three stacks

Idea: get an array and alternate entries (1, 2, 3) for each stack.
Predefine the array with some reasonable size. Re-scale if needed be when it is about to get filled.
I'll use a numpy array for the exercise and assume we work with floats

This stack is not thread safe etc...

@author: igoroya
'''
import numpy

def make_empty_array_stack(stack_size):
    '''
    Makes a numoy array filled with zeros three times the size of teh argument
    '''
    return numpy.zeros(3*stack_size)

def resize_array_stack(array, resize_factor = 2):
    '''
    Multiplies the size of the array according to the resize_factor
    Data are basically repeated in the extended part
    '''
    shape = (1,  array.size * resize_factor)
    return numpy.resize(array, shape)

class ThreeStacskOnArray():
    def __init__(self, stack_size):
        self._array = make_empty_array_stack(stack_size)
        self._stack_size = [0, 0, 0]

    def __get_index(self, stack_id):
        return stack_id - 1 + (self._stack_size[stack_id - 1]- 1 )*3

    def push(self, item, stack_id):
        '''
        add an item at the end of the queue
        Stack IDs are 1, 2 & 3
        '''
        if (3 * self._stack_size[stack_id - 1]) == self._array.size:
            self._array = resize_array_stack(self._array)

        self._stack_size[stack_id -1] = self._stack_size[stack_id - 1] + 1
        index = self.__get_index(stack_id)
        self._array[index] = item


        #need to add the resizing thing


    def remove(self, stack_id):
        '''
        removes 1st item of the queue
        '''
        index = self.__get_index(stack_id)
        self._array[index] = numpy.NaN
        self._stack_size[stack_id -1] = self._stack_size[stack_id -1 ] - 1


    def peek(self, stack_id):
        '''
       `returns to the top of the queue (without removing)
        '''
        index = self.__get_index(stack_id)
        return self._array[index]

    def isEmpty(self, stack_id):
        '''
        Returns True if the queu is empty
        '''
        return not bool(self._stack_size[stack_id -1])

if __name__ == '__main__':
    my_stacks = ThreeStacskOnArray(50)
    print("Is empty: {}".format(my_stacks.isEmpty(2)))
    my_stacks.push(34.0, 2)
    print("Is empty: {}".format(my_stacks.isEmpty(2)))
    print("Peek: {}".format( my_stacks.peek(2)))

    my_stacks.push(11.0, 2)
    print("Peek: {}".format( my_stacks.peek(2)))
    my_stacks.remove(2)
    print("Peek: {}".format( my_stacks.peek(2)))
    my_stacks.remove(2)
    print("Is empty: {}".format(my_stacks.isEmpty(2)))
