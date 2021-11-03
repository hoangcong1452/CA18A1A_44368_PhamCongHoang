"""
Author: Pham Cong Hoang
Date: 19/09/2021
Problem:The variables x and y refer to numbers. Write a code segment that prompts the user for
an arithmetic operator and prints the value obtained by applying that operator to x and y.


Solution:

    ....
"""
x= int(input("nhập x:"))
y= int(input("nhập y:"))
pheptinh=input("nhập phép tính:")
kq=0
if pheptinh == '+':
    kq=x+y
elif pheptinh == '-':
    kq=x-y
elif pheptinh== '*':
    kq=x*y
elif pheptinh == '/':
    kq=x/y
else:
    print("xin nhập lại:")
print("kết quả là:",kq)