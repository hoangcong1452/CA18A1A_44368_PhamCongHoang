"""
Author: pham cong hoang
Date: 25/09/2021
Problem:Translate each of the following numbers to decimal numbers:
a. 110012
b. 1000002
c. 111112

Solution:

"""
bitString = ("110012","1000002","111112")
decimal = 0
exponent = len(bitString) - 1
for digit in bitString:
    decimal = decimal + int(digit) * 2 ** exponent
    exponent = exponent - 1
print("giá trị số nguyên là:", decimal)