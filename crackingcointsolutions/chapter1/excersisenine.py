'''
Created on 11 Aug 2017
String rotation: Assume you have a method isSubstring which checks if one word is a substring
of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one
call to isSubstring (e.g. "waterbottle" is rotation of "erbottlewat)

@author: igoroya
'''

def is_substring(string, substring):
    return substring in string

def is_rotation(s1, s2):
    if len(s1) is not len(s2):
        return False

    #pick 1st word of s1, loop over str2 until found
    chars_start = ''

    ref_char = s1[0]
    for i in range(len(s2)):
        if s2[i] is ref_char:
            chars_end = s2[i+1:len(s2)]
            break
        else:
            chars_start += s2[i]
    compare = chars_end + chars_start

    return is_substring(s1, compare)


if __name__ == '__main__':
    s1 = "aeiou"
    s2 = "ouaei"
    print(is_rotation(s1, s2))
    s1 = "william"
    s2 = "wallace"
    print(is_rotation(s1, s2))
    s1 = "waterbottle"
    s2 = "erbottlewat"
    print(is_rotation(s1, s2))
    s1 = "a"
    s2 = "22"
    print(is_rotation(s1, s2))
