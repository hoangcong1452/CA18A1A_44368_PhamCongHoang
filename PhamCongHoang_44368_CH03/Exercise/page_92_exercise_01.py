"""
Author: Pham Cong Hoang
Date: 19/09/2021
Problem:Translate the following for loops to equivalent while loops:
a. for count in range(100):
 print(count)
b. for count in range(1, 101):
 print(count)
c. for count in range(100, 0, –1):
 print(count)

Solution:
a.count = 0
n = 0
while (count < 100):
      print ('Số thứ', n,' là:', count)
      n = n + 1
      count = count + 1
b.count = 0
n = 1
while (count < 101):
      print ('Số thứ', n,' là:', count)
      n = n + 1
      count = count + 1
c.count = 100
n = 0
while (count > 0):
      print ('Số thứ', n,' là:', count)
      n = n + 1
      count = count - 1

    ....
"""

