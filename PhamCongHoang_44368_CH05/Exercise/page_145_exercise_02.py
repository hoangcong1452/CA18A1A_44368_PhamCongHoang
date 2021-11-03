"""
Author: pham cong hoang
Date:09/10/2021
Problem:
g. tuple(data)
2. Assume that the variable data refers to the list [5, 3, 7]. Write the expressions
that perform the following tasks:
a. Replace the value at position 0 in data with that value’s negation.
b. Add the value 10 to the end of data.
c. Insert the value 22 at position 2 in data.
d. Remove the value at position 1 in data.
e. Add the values in the list newData to the end of data.
f. Locate the index of the value 7 in data, safely.
g. Sort the values in data.

Solution:
a.[-5, 3, 7]
b.[-5, 3, 7, 10]
c.[-5, 3, 22, 7, 10]
d.[-5, 22, 7, 10]
e.[-5, 22, 7, 10, 2, 8, 9]
f.
g.[-5, 2, 7, 8, 9, 10, 22]
"""
list= [5,3,7]
list[0]=-5
print(list)
list.extend([10])
print(list)
list.insert(2,22)
print(list)
list.pop(1)
print(list)
new_list = [2,8,9]
list = list + new_list
print(list)
list_moi=sorted(list)
print(list_moi)
