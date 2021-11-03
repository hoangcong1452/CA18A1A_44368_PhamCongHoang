"""
Author: Pham Cong Hoang
Date: 19/09/2021
Problem:Write a program that accepts the lengths of three sides of a triangle as inputs.
The program output should indicate whether or not the triangle is a right triangle. Recall from the Pythagorean theorem that in a right triangle, the square of
one side equals the sum of the squares of the other two sides.

Solution:
canh_huyen=int(input("nhập cạnh huyền:"))
canh_gocvuong1=int(input("nhập canh góc vuông 1:"))
canh_gocvuong2=int(input("nhập canh góc vuông 2:"))
if canh_huyen*canh_huyen == canh_gocvuong1*canh_gocvuong1+canh_gocvuong2*canh_gocvuong2
    print("là tam giac vuong")
else: print("không phải tam giác vuông")

    ....
"""
canh_huyen=int(input("nhập cạnh huyền:"))
canh_gocvuong1=int(input("nhập canh góc vuông 1:"))
canh_gocvuong2=int(input("nhập canh góc vuông 2:"))
if canh_huyen*canh_huyen == canh_gocvuong1*canh_gocvuong1+canh_gocvuong2*canh_gocvuong2:
    print("là tam giac vuong")
else: print("không phải tam giác vuông")