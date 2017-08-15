'''
Created on 14 Aug 2017

@author: igoroya
'''
from chapter2 import utils # TODO: try relative imports

if __name__ == '__main__':
    cargo = 'Hello'
    my_list = utils.SinglyLinkedList()
    my_list.append(cargo)
    print(cargo)
    my_list.append("wawaway")
    print(my_list)
    my_string = "perico"
    my_list.append(my_string)
    print(my_list)
    my_list.pop(my_string)
    print(my_list)
    my_list.add_in_front(my_string)
    print(my_list)
    my_list.pop(my_string)
    print(my_list)