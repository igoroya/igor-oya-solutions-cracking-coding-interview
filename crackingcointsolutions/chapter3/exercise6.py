'''
Created on 25 Aug 2017

Animal Shelter

@author: igoroya
'''

from enum import Enum
import collections

class AnimalType(Enum):
    DOG = 1
    CAT = 2


class ShelterQueue():
    '''
    Represents a queue in an animal shelter
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self._deque = collections.deque()

    def __repr__(self):
        return self._deque.__repr__()

    def add_animal(self, animal_name, animal_type):
        '''
        add an item at the end of the queue
        animal type must be AnimalType
        '''
        if isinstance(animal_type, AnimalType):
            self._deque.appendleft((animal_name, animal_type))
        else:
            print("Wrong type of animal, we do not host {}s".format(animal_type))

    def dequeue_any(self):
        '''
        removes 1st item of the queue
        '''
        return self._deque.pop()

    def __roll_back(self, buffer):
        for i in reversed(buffer):
            self._deque.append(i)

    def _dequeue_animal(self, animal_type):
        '''
        removes 1st animal of animal_type of the queue
        '''
        if self.is_empty():
            return None
        buffer = []
        while (self.peek()[1] is not animal_type):
            buffer.append(self._deque.pop())
            if self.is_empty():
                self.__roll_back(buffer)
                return None

        selected = self._deque.pop()
        self.__roll_back(buffer)
        return selected

    def dequeue_cat(self):
        '''
        removes 1st cat of the queue
        '''
        return self._dequeue_animal(AnimalType.CAT)

    def dequeue_dog(self):
        '''
        removes 1st dog of the queue
        '''
        return self._dequeue_animal(AnimalType.DOG)

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


if __name__ == '__main__':
    shelter_queue = ShelterQueue()
    shelter_queue.add_animal("Teddy", AnimalType.DOG)
    shelter_queue.add_animal("Yodi", AnimalType.DOG)
    shelter_queue.add_animal("Puffo", AnimalType.DOG)
    shelter_queue.add_animal("Milu", AnimalType.CAT)
    shelter_queue.add_animal("Mati", AnimalType.DOG)
    shelter_queue.add_animal("Princess", AnimalType.CAT)
    print(shelter_queue)

    print("Get any {}".format(shelter_queue.dequeue_any()))
    print("Get cat {}".format(shelter_queue.dequeue_cat()))
    print("Get dog {}".format(shelter_queue.dequeue_dog()))
    print(shelter_queue)



