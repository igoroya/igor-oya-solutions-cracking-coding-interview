'''
Created on Aug 8, 2017
Is Unique: Implement an algorithm to determine if a string has all unique
characters. What if you cannot use additional data structures?

Assumptions: this searches for all unique ASCII characters, that are 128

Things to learn:
ord("c") give the ascii number of an ascii character
chr(i) gives the ascii char from an int value
there are 128 arcii chars

@author: igoroya
'''


def has_all_char_unique(string):
    if len(string) > 128:
        return False
    chars = [False]*128
    for s in string:
        i = ord(s)
        if chars[i]:
            return False
        else:
            chars[i] = True

    return True 


def has_all_no_struct(string):
    # generate ascii strings on the fly and compare tp string
    for s in string:
        hit = 0
        for k in string:
            if s is k:
                hit += 1
                if hit > 1:
                    return False
    return True


if __name__ == '__main__':
    print ("test 1")

    my_str = "pepe"
    print(has_all_char_unique(my_str))
    my_str = "aeiou"
    print(has_all_char_unique(my_str))
    my_str = "1"
    print(has_all_char_unique(my_str))
    my_str = "11"
    print(has_all_char_unique(my_str))
    all_ascii = ''.join(chr(i) for i in range(128))
    print(has_all_char_unique(all_ascii))

    print("\ntest 2")
    print(has_all_no_struct(my_str))
    my_str = "1"
    print(has_all_no_struct(my_str))
    print(has_all_no_struct(all_ascii))
