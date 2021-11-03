"""
Author: pham cong hoang
Date: 25/09/2021
Problem:Assume that the variable myString refers to a string. Write a code segment that
uses a loop to print the characters of the string in reverse order.

Solution:
dùng data là conghoang
chạy vòng lặp để in ra từng kí tự data đó
để đếm ngược thì in data kiểu -i

"""
data = "conghoang"
for i in range(1,len(data)+1):
    print(data[-i])