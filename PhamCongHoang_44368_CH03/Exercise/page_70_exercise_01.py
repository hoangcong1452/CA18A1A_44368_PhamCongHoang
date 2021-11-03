"""
Author: Pham Cong Hoang
Date: 19/09/2021
Problem:Write the outputs of the following loops:
a. for count in range(5):
 print(count + 1, end = " ")
b. for count in range(1, 4):
 print(count, end = " ")
c. for count in range(1, 6, 2):
 print(count, end = " ")
d. for count in range(6, 1, –1):
 print(count, end = " ")

Solution:
a. 1 2 3 4 5
b. 1 2 3
c. 1 3 5
d. 6 5 4 3 2 1

    ....
"""

for count in range(5):
    print(count + 1, end = " ")
for count in range(1, 4):
    print(count, end = " ")
for count in range(1, 6, 2):
    print(count, end = " ")
for count in range(6, 1, -1):
    print(count, end = " ")