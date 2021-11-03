"""
Author: pham cong hoang
Date: 22/10/2021
Problem: Write the code for a filtering that generates a list of the positive numbers in a list
named numbers. You should use a lambda to create the auxiliary function.
Solution:

"""
nums = [34, 1, 0, -23, 12, -88]
print("Số ban đầu trong danh sách: ",nums)
new_nums = list(filter(lambda x: x >0, nums))
print("Các số dương trong danh sách đã nói: ",new_nums)