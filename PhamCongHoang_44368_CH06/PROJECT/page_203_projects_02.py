"""
Author: pham cong hoang
Date: 22/10/2021
Problem: Convert Newton’s method for approximating square roots in Project 1 to a recursive function named newton.
(Hint: The estimate of the square root should be
passed as a second argument to the function.)
Solution:

"""
import math
TOLERANCE = 0.000001
def newton(x, estimate):
    difference = abs(x - estimate ** 2)
    if difference <= TOLERANCE:
        return estimate
    else:
        return newton(x, (estimate + x / estimate) / 2)
def main():
    while True:
        x = input("Nhập một số dương hoặc nhập / quay lại để thoát: ")
        if x == "":
            break
        x = float(x)
        # Output the result
        print("Chương trình ước tính là", newton(x, 1))
        print("Python là ước tính là   ", math.sqrt(x))
main()

