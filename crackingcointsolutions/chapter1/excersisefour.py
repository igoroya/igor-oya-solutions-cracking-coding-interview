'''
Created on 9 Aug 2017
Palindrome permutation: Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters.
The palindrome does not need to be limited to just dictionary words.
EXAMPLE:
Input: Tact Coa
Output: True (permutation: "taco cat", "atco cta", etc.)

What to learn:
- integer division is done by operator //
- string.lower() make a string lower case
- my_set.remove(' ') removes a ' ' from a set
- remember to use parenthesis in expressions like "is (0 or 1)"

@author: igoroya
'''

'''
Deduction:

Put some example and deduce common patterns

# letters   # same letter pairs   Example
0           0
1           0                      a
2           1                      aa
3           1                      iaa -->aia
4           2                      aaee
5           2                      iaeae --> aeiea
6           3
7           3
8           4


Pattern:
1) Remove blank espaces
2) find if n_letters//2 pairs exist --> This means to have a set of size n_letters//2
'''


def is_palindrome_permutation(string):
    low_string = string.lower()
    length = len(low_string)

    if length is (0 or 1):
        return True

    needed_pairs = length//2

    print(string)

    char_set = {c for c in low_string}

    try:
        char_set.remove(' ')
    except KeyError:
        pass

    print('needs a set of ' + str(needed_pairs) + ' letter(s)')
    print(char_set)

    if len(char_set) == needed_pairs:
        return True
    else:
        return False

if __name__ == '__main__':
    str1 = 'a'
    str2 = 'aa'
    str3 = 'aeeeaa'
    str4 = 'Tact Coa'
    str5 = 'Ma'
    str6 = 'Tact Coai'
    str7 = 'Tact    '
    print(is_palindrome_permutation(str1))
    print(is_palindrome_permutation(str2))
    print(is_palindrome_permutation(str3))
    print(is_palindrome_permutation(str4))
    print(is_palindrome_permutation(str5))
    print(is_palindrome_permutation(str6))
    print(is_palindrome_permutation(str7))