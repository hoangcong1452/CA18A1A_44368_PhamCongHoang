"""
Author: pham cong hoang
Date: 22/10/2021
Problem:Explain what happens when the following recursive function is called with the value 4
as an argument:
def example(n):
if n > 0:
print(n)
example(n)
else:
example(n - 1)
Solution:
"""
def example(n):
    if n > 0:
        print(n)
        example(n)
    else:
        example(n - 1)