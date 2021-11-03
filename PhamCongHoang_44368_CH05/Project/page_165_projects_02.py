"""
Author: pham cong hoang
Date:09/10/2021
Problem:

Solution:


"""
fileName = input("Enter the filename: ")
f = open(fileName, 'r')
numbers = []
for line in f:
    words = line.split()
    for word in words:
        numbers.append(float(word))
numbers.sort()
midpoint = len(numbers) // 2
print("The median is", end = " ")
if len(numbers) % 2 == 1:
    print(numbers[midpoint])
else:
    print((numbers[midpoint] + numbers[midpoint - 1]) / 2)

