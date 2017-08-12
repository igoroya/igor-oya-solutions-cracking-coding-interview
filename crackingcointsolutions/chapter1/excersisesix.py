'''
Created on 10 Aug 2017

String compression: Implement a method to perform basic string compression
using the counts of repeated characters. For example, the string aabcccccaaa would
become a2b1c5a3. if the 'compressed' string would not become smaller than the original string,
your method should return the original string. You can assume the string has only uppercase
and lowercase letters (a - z)

Things to learn:
- make sure to cast numbers to string (if this is what you wanted)
- join strings from a list by " ''.join(i for i in my_strings)  "
- add at the end of list something via .append()

@author: igoroya
'''
def compress(string):
    previous = ' '
    times = 1
    my_strings = []
    for c in string:
        if c is previous:
            times += 1
            position = len(my_strings) - 1
            my_strings[position] = str(times)
        else:
            my_strings.append(c)
            my_strings.append('1')
            times = 1
        previous = c


    compressed =''.join(i for i in my_strings)

    if len(compressed) > len(string):
        return string
    else:
        return compressed

if __name__ == '__main__':
    str1 = 'aabcccccaaa'
    print(compress(str1))
    str1 = 'aeiou'
    print(compress(str1))
    str1 = 'aeiouuuuuuuuuuuuuuuuuuuuuuuuuuuuuu'
    print(compress(str1))
    str1 = 'wwwwwwww'
    print(compress(str1))
    str1 = 'w'
    print(compress(str1))