"""
Author: pham cong hoang
Date:09/10/2021
Problem:
Assume that the variable data refers to the list [5, 3, 7]. Write the values of the
following expressions:
a. data[2]
b. data[-1]
c. len(data)
d. data[0:2]
e. 0 in data
f. data + [2, 10, 5]
g. tuple(data)


Solution:
a.7
b.7
c.3
d.[5, 3]
e.5
f.[5, 3, 7, 2, 10, 5]
g.(5, 3, 7)



"""
list_a= [5,3,7]
print(list_a[2])
print(list_a[-1])
print(len(list_a))
print(list_a[0:2])
print(list_a[0])
print(list_a + [2,10,5])
print(tuple(list_a))


