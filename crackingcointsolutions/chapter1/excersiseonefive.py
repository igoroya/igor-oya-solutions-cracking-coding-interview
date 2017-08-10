'''
Created on 9 Aug 2017
One away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one  edit (or zero edits) away
EXAMPLE:
pale, ple --> True
pales, pale --> True
pale, bale --> True
pale, bake --> False

-----
I will assume these are ASCII characters.


There are 128 characters,
I build a list with a value from 0 to 127 for each string.
If the string size is same, I check for 1 or 0 index are different

If string size difference is one, I move along smaller until I find one false, increase index
checking that remaining are true.

If string size difference is two or more, I quit


Bads idea? I will build a hash functions using the characters numbering
Then I can check is hash functions match when looping over and removing one character


To learn:
- one can unpack tuples with * as argument in a function
- to loop over the size of a collection, one can use 'for i in range(len(str1))'

@author: igoroya
'''

def is_one_away(str1, str2):
    diff_sizes = len(str1) - len(str2)

    if abs(diff_sizes) > 1:
        return False

    str1_vals = [ord(i) for i in str1]
    str2_vals = [ord(i) for i in str2]

    if diff_sizes == 0:
        hits = 0
        for i in range(len(str1)):
            if str1_vals[i] != str2_vals[i]:
                hits += 1
            if hits > 1:
                return False
        return True

    if diff_sizes == 1:
        return check_one_more_char(str1_vals, str2_vals)
    elif diff_sizes == -1:
        return check_one_more_char(str2_vals, str1_vals)
    else:
        return False

def check_one_more_char(str_a_list, str_b_list):
    'str_a_list is one unit larger than str_b_list '
    for i in range(len(str_b_list)):
        jump = 0
        if str_a_list[i + jump] != str_b_list[i]:
            jump += 1
        if jump > 1:
            return False
    return True

if __name__ == '__main__':
    ex1 = ("ale", "ple")
    print(is_one_away(*ex1))
    ex1 = ("pales", "pale")
    print(is_one_away(*ex1))
    ex1 = ("pale", "bale")
    print(is_one_away(*ex1))
    ex1 = ("pale", "bake")
    print(is_one_away(*ex1))
    ex1 = ("palepapepepe", "bake")
    print(is_one_away(*ex1))
    ex1 = ("a", "a")
    print(is_one_away(*ex1))
    ex1 = ("", "")
    print(is_one_away(*ex1))
    ex1 = ("a", "")
    print(is_one_away(*ex1))
    ex1 = ("a ver", "aver")
    print(is_one_away(*ex1))
    ex1 = ("a ver", "haber")
    print(is_one_away(*ex1))
