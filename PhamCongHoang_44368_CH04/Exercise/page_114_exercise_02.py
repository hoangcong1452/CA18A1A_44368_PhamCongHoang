"""
Author: pham cong hoang
Date: 25/09/2021
Problem:Translate each of the following numbers to binary numbers:
a. 4710
b. 12710
c. 6410

Solution:

"""
decimal = int(input("Enter a decimal integer: "))
if decimal == 0:
    print(0)
else:
    print("Quotient Remainder Binary")
    bitString = ""
    while decimal > 0:
            remainder = decimal % 2
            decimal = decimal // 2
            bitString = str(remainder) + bitString
            print("%5d%8d%12s" % (decimal, remainder,
                                    bitString))
 print("The binary representation is", bitString)