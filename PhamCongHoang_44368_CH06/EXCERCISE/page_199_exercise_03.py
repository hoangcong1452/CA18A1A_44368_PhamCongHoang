"""
Author: pham cong hoang
Date: 22/10/2021
Problem:Write the code for a reducing that creates a single string from a list of strings named
words.
Solution:

"""

def convert(s):
    new = ""
    for x in s:
        new += x
    return new
s = ['g', 'e', 'e', 'k', 's', 'f', 'o', 'r', 'g', 'e', 'e', 'k', 's']
print(convert(s))
