"""
De On Tap 02
Date: 30/10/2021
Pham Cong Hoang
"""
def cau01():
  a = input('Nhập số: ')
  ar = [int(i) for  i in a]
  ar  = ar[::-1]
  res = []
  for i in range(len(ar)):
    res.append(ar[i]*(2**i))
    sum_res = sum(res)
  print('Số nhị phân là: ',sum_res)
if __name__ == '__main__':
    cau01()
