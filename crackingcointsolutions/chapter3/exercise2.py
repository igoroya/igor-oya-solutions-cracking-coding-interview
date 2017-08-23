'''
Created on 23 Aug 2017

Minimum: How would design a stack that which, in addition to push and pop, has
a function that returns the minimum element. Push, pop and peek should operate at O(1) time

Idea: cache the minimum value, then return when asked

@author: igoroya
'''
from chapter3 import utils

class StackV2(utils.Stack):
    def __init__(self):
        super().__init__()

if __name__ == '__main__':
    pass