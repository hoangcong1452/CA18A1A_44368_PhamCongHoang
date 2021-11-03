"""
De thi 02
date:29/10/2021
Pham Cong Hoang
Câu 1: Viết hàm in các số nguyên tố trong khoảng từ 30 đến 200

"""

def Cau1():
    def snt(n):
        f=True
        for j in range (2,n):
            if n%j==0:
                f=False
                break
        return  f
    def in_snt(a=30,b=200):
        for i in range(a,b+1):
            if snt(i):
                print(i,end="  ")
        print()
    in_snt(30,200)

if __name__=='__main__':
    Cau1()
