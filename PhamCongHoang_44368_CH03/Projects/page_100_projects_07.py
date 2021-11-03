"""
Author: Pham Cong Hoang
Date: 19/09/2021
Problem:Teachers in most school districts are paid on a schedule that provides a salary
based on their number of years of teaching experience. For example, a beginning
teacher in the Lexington School District might be paid $30,000 the first year. For
each year of experience after this first year, up to 10 years, the teacher receives a
2% increase over the preceding value. Write a program that displays a salary schedule, in tabular format, for teachers in a school district. The inputs are the starting
salary, the percentage increase, and the number of years in the schedule. Each row
in the schedule should contain the year number and the salary for that year.

Solution:

    ....
"""
luong = 30000
y = int(input("nhập số năm: "))
for x in range(1,y+1):
    if x <= 10:
        luong =luong + (luong *0.02)
    else:
        luong = luong
    print("%5.0f %10.0f" % (x, luong))