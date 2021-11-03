"""
Author: pham cong hoang
Date: 22/10/2021
Problem: The factorial of a positive integer n, fact(n), is defined recursively as follows:
fact( ) n 1 5 , when n 1 5
fact( ) n n 5 2 * fact n ( ) 1 , otherwise
Define a recursive function fact that returns the factorial of a given positive
integer.
Solution:

"""
def fact(n):
    if n < 2:
        return 1
    else:
        return n * fact(n-1)