"""
Author: pham cong hoang
Date: 25/09/2021
Problem:Write the encrypted text of each of the following words using a Caesar cipher with
a distance value of 3:
a. python
b. hacker
c. wow

Solution:

"""

distance = 3
ki_tu = ["python", "hacker", "wow"]
for plainText in ki_tu:
    code = ""
    for ch in plainText:
        ordvalue = ord(ch)
        cipherValue = ordvalue + distance
        if cipherValue > ord('z'):
            cipherValue = ord('a') + distance - \
            (ord('z') - ordvalue + 1)
        code += chr(cipherValue)
    print(code)