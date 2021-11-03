"""
Author: pham cong hoang
Date: 25/09/2021
Problem:Assume that the variable myString refers to a string, and the variable
reversedString refers to an empty string. Write a loop that adds the characters
from myString to reversedString in reverse order

Solution:
khai báo 2 biến data
cho chạy vòng lặp data có kí tự xong thì gán data chạy đó lên data rỗng

"""
data = "myString"
data_rong = ""
for i in range(len(data)):
    data_rong = data[i] + data_rong
print(data_rong)