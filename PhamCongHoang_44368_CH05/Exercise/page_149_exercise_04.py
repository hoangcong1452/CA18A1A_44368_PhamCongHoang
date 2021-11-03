"""
Author: pham cong hoang
Date:09/10/2021
Problem:
Define a function named summation. This function expects two numbers, named
low and high, as arguments. The function computes and returns the sum of the
numbers between low and high, inclusive.

Solution:
def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total


"""
def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total