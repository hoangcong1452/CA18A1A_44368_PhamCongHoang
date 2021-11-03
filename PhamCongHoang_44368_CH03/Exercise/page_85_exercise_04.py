"""
Author: Pham Cong Hoang
Date: 19/09/2021
Problem:Assume that the variables x and y refer to strings. Write a code segment that prints
these strings in alphabetical order. You should assume that they are not equal.

Solution:
cau = input("nhập: ")
tu = [word.lower() for word in cau.split()]
tu.sort()
print("The sorted words are:")
for word in tu:
   print(word)
    ....
"""
cau = input("nhập: ")
tu = [word.lower() for word in cau.split()]
tu.sort()
print("The sorted words are:")
for word in tu:
   print(word)