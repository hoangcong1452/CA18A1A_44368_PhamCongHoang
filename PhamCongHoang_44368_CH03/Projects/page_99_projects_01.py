"""
Author: Pham Cong Hoang
Date: 19/09/2021
Problem:Write a program that accepts the lengths of three sides of a triangle as inputs.
The program output should indicate whether or not the triangle is an equilateral triangle.

Solution:

    ....
"""
a= int(input("nhập cạnh a:"))
b= int(input("nhập cạnh b:"))
c= int(input("nhập cạnh c:"))
if a==b==c:
    print("là tam giac cân")
else:print("không phải tam giác cân")