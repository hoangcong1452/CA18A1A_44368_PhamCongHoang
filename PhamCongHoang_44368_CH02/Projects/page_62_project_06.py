"""
Author: Pham Cong Hoang
Date: 04/09/2021
Problem:The kinetic energy of a moving object is given by the formula KE 1 2/ mv 5 2 ( )
where m is the object’s mass and v is its velocity. Modify the program you created
in Project 5 so that it prints the object’s kinetic energy as well as its momentum

Solution:
m = float(input("khoi luong la:"))
vt = float(input("van toc la:"))
KE = 1/2*m*vt**2
print("dong nang la:",KE)

    ....
"""
m = float(input("khoi luong la:"))
vt = float(input("van toc la:"))
KE = 1/2*m*vt**2
print("dong nang la:",KE)
