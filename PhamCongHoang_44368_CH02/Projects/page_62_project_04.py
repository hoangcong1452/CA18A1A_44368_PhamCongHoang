"""
Author: Pham Cong Hoang
Date: 04/09/2021
Problem:Write a program that takes the radius of a sphere (a floating-point number) as
input and then outputs the sphere’s diameter, circumference, surface area, and
volume.


Solution:
r = float(input("bán kính là:"))
d = r*2
cv=d*3.14
S=3.14*d**2
V=1/6*3.14*d**3
print("duong kinh la:",d)
print("chu vi:", cv)
print("dien tich:",S)
print("the tich:",V)

    ....
"""
r = float(input("bán kính là:"))
d = r*2
cv=d*3.14
S=3.14*d**2
V=1/6*3.14*d**3
print("duong kinh la:",d)
print("chu vi:", cv)
print("dien tich:",S)
print("the tich:",V)

