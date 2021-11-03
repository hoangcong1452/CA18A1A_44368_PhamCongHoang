"""
Author: Pham Cong Hoang
Date: 04/09/2021
Problem:
Five Star Retro Video rents VHS tapes and DVDs to the same connoisseurs who
like to buy LP record albums. The store rents new videos for $3.00 a night, and
oldies for $2.00 a night. Write a program that the clerks at Five Star Retro Video
can use to calculate the total charge for a customer’s video rentals. The program
should prompt the user for the number of each type of video and output the total
cost.

Solution:
moi = 3
cu = 2
sluong_moi = int(input ("so luong dia moi:"))
sluong_cu= int(input("so luong dia cu:"))
so_ngay= int(input("so ngay:"))
thanh_tien_moi=sluong_moi*so_ngay
thanh_tien_cu=sluong_cu*so_ngay
print("so tien la:",thanh_tien_cu+thanh_tien_moi)

    ....
"""
moi = 3
cu = 2
sluong_moi = int(input ("so luong dia moi:"))
sluong_cu= int(input("so luong dia cu:"))
so_ngay= int(input("so ngay:"))
thanh_tien_moi=sluong_moi*so_ngay
thanh_tien_cu=sluong_cu*so_ngay
print("so tien la:",thanh_tien_cu+thanh_tien_moi)