"""
Author: pham cong hoang
Date: 18/10/2021

Problem: Modify this chapter’s case study program (the c-curve) so that it draws the line segments
using random colors.
Solution:

"""

import random
from time import sleep
from turtle import Turtle

def cCurve(t, x1, y1, x2, y2, cap_do):
    def drawLine(x1, y1, x2, y2):
        t.up()
        t.goto(x1, y1)
        t.down()
        t.goto(x2, y2)
    if cap_do == 0:
        drawLine(x1, y1, x2, y2)
    else:
        xm = (x1 + x2 + y1 - y2) // 2
        ym = (x2 + y1 + y2 - x1) // 2
        cCurve(t, x1, y1, xm, ym, cap_do - 1)
        cCurve(t, xm, ym, x2, y2, cap_do - 1)
def main():
    cap_do = int(input("Nhập cấp độ (khác 0): "))
    t = Turtle()
    r, g, b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    t.pencolor(r, g, b)
    t.hideturtle()
    cCurve(t, 50, -5, 50, 50, cap_do)
    sleep(5)

if __name__ == '__main__':
    main()




