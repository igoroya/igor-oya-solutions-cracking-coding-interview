'''
Created on Aug 8, 2017
Check permutation: Given two strings, write a method to decide if one is a permutation of the other

Things to learn:
- a python set orders set content
- in a set, one uses == to compare same content  
@author: igoroya
'''


def check_string_permuntation(str1, str2):
    if len(str1) is not len(str2):
        return False
    strset1 = {i for i in str1}
    strset2 = {i for i in str2}
    
    if strset1 == strset2:
        return True
    else:
        return False

if __name__ == '__main__':
    str1 = 'aeiou'
    str2 = 'aeiuo'
    str3 = 'pepe'
    str4 = 'aeiouaeiou'
    print(check_string_permuntation(str1, str2))
    print(check_string_permuntation(str1, str3))
    print(check_string_permuntation(str1, str4))
