"""
Author: Pham Cong Hoang
Date: 04/09/2021
Problem:
An employee’s total weekly pay equals the hourly wage multiplied by the total number of regular hours plus any overtime pay. Overtime pay equals the total
overtime hours multiplied by 1.5 times the hourly wage. Write a program that takes as inputs the hourly wage, total regular hours, and total overtime hours and
displays an employee’s total weekly pay

Solution:


    ....
"""
so_gio_lv=float(input("số giờ làm trong tuần là:"))
so_gio_lam_them=float(input("số giờ làm thêm:"))
so_tien_gio_lam_chinh=float(input("tien lam gio chinh:"))
so_tien_gio_lam_them= so_tien_gio_lam_chinh*1.5
luong_chinh=so_gio_lv*so_tien_gio_lam_chinh
luong_them=so_gio_lam_them*so_tien_gio_lam_them
print("tong luong tuan nay la:",luong_chinh+luong_them)