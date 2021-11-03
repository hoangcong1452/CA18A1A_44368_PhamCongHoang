"""
Author: pham cong hoang
Date: 25/09/2021
Problem:Modify the scripts of Projects 1 and 2 to encrypt and decrypt entire files of text.

Solution:

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
plainText = ""
for ch in code:
    ordvalue = ord(ch)
    cipherValue = ordvalue - distance
    if cipherValue < ord('a'):
        cipherValue = ord('z') - \
        (distance - (ord('a') - ordvalue - 1))
    plainText += chr(cipherValue)
print(plainText)