"""
Author: pham cong hoang
Date: 18/10/2021

Problem: How would a column-major traversal of a grid work? Write a code segment that prints the positions
visited by a column-major traversal of a 2-by-3 grid.
Solution:
A nested loop structure to traverse a grid consists of two loops, an outer one and an inner one.
Each loop has a different loop control variable. The outer loop iterates over one coordinate,
while the inner loop iterates over the other coordinate.

"""
rong = 2
cao = 3
for y in range(cao):
    for x in range(rong):
        print((x, y), end = " ")
    print()
