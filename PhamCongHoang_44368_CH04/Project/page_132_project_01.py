"""
Author: pham cong hoang
Date: 25/09/2021
Problem:Write a script that inputs a line of plaintext and a distance value and outputs an
encrypted text using a Caesar cipher. The script should work for any printable
characters

Solution:
plainText = input("Enter a one-word, lowercase message: ")
distance = int(input("Enter the distance value: "))
code = ""
for ch in plainText:
 ordvalue = ord(ch)
 cipherValue = ordvalue + distance
 if cipherValue > ord('z'):
 cipherValue = ord('a') + distance - \
 (ord('z') - ordvalue + 1)
 code += chr(cipherValue)
print(code)

"""
plainText = input("Enter a one-word, lowercase message: ")
distance = int(input("Enter the distance value: "))
code = ""
for ch in plainText:
    ordvalue = ord(ch)
    cipherValue = ordvalue + distance
    if cipherValue > ord('z'):
        cipherValue = ord('a') + distance - \
                        (ord('z') - ordvalue + 1)
    code += chr(cipherValue)
print(code)