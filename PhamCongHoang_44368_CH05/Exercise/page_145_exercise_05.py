"""
Author: pham cong hoang
Date:09/10/2021
Problem:Assume that data refers to a list of numbers, and result refers to an empty list.
Write a loop that adds the nonzero values in data to the result list, keeping them in their relative positions and excluding the zeros

Solution:
list = [7, 105, 0, 0, 9, 62]
ket_qua = []
for number in list:
   if number != 0:
       ket_qua += str(number)
print(ket_qua)


"""
list = [7, 105, 0, 0, 9, 62]
ket_qua = []
for number in list:
   if number != 0:
       ket_qua += str(number)
print(ket_qua)
