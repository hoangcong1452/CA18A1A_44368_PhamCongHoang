"""
Author: Pham Cong Hoang
Date: 19/09/2021
Problem:The German mathematician Gottfried Leibniz developed the following method
to approximate the value of π:
π/4 5 1 ] 1/3 1 1/5 ] 1/7 1 . . .
Write a program that allows the user to specify the number of iterations used in
this approximation and that displays the resulting value.

Solution:

    ....
"""
pi = 0
for x in range(1, 100, 2):
    if x % 4 == 1:
        pi += (1/x)
    else:
        pi -= (1/x)
pi = pi * 4
print(pi)
