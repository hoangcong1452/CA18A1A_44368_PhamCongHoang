"""
Author: pham cong hoang
Date: 22/10/2021


Problem:Explain what happens when the following recursive function is called with the
values "hello" and 0 as arguments:
def example(aString, index):
   if index == len(aString):
       return ""
    else:
       return aString[index] + example(aString, index + 1)
Solution:

"""
def example(aString, index):
   if index != len(aString):
       return aString[index] + example(aString, index + 1)
   else:
       return ""