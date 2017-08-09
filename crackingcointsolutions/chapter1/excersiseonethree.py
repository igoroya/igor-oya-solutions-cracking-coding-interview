'''
Created on Aug 9, 2017

URLify: Write a method to replace all spaces in a string with '%20'.
You may assume that the string has sufficient space at the end to hold
additional characters, and that you are given the true length of the string.

EXAMPLE:
input:  "Mr John Smith    ", 13
output: "Mr%20John%20Smith"

I am assuming that the string is using ascii

Things to tearn:
- For in-place character modification use bytearray
- bytearray from string needs to get encoding, example encoding="ASCII"
- bytearray can replace in-place bytes from bytes
- bytearray can be truncated by slicing (as :N)
- bytearry can be turn into a string by ".decode()"

@author: igoroya
'''


def urlify_string_1(string):
    # encode to bytearray so we can do in-place modification
    original_length = len(string)
    as_bytes = bytearray(string, encoding="ASCII")
    blank_space_bytes = bytearray(" ", encoding="ASCII")
    url_str_bytes = bytearray("%20", encoding="ASCII")
    urlfied_bytes = as_bytes.replace(
        blank_space_bytes, url_str_bytes)[:original_length]
    return urlfied_bytes.decode()

if __name__ == '__main__':
    str1 = "Mr John Smith    "
    str2 = "Amparo"
    str3 = "a e i o u        "
    print(urlify_string_1(str1))
    print(urlify_string_1(str2))
    print(urlify_string_1(str3))
