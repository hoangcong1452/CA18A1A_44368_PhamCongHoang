"""
Author: pham cong hoang
Date:09/10/2021
Problem:
Assume that the variable data refers to the dictionary {'b':20, 'a':35}. Write the
expressions that perform the following tasks:
a. Replace the value at the key 'b' in data with that value’s negation.
b. Add the key/value pair 'c':40 to data.
c. Remove the value at key 'b' in data, safely.
d. Print the keys in data in alphabetical order

Solution:
a.
b.data={'b':20, 'a':35}
data['c']=40
print(data)
c.data.pop('b')
d.sorted(data)



"""
data={'b':20, 'a':35}
data['c']=40
print(data)
data.pop('b')
print(data)
sorted(data)
print(data)



