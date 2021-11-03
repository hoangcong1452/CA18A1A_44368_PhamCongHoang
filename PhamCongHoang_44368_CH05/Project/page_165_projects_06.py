"""
Author: pham cong hoang
Date:09/10/2021
Problem:Define a function decimalToRep that returns the representation of an integer in a
given base. The two arguments should be the integer and the base. The function
should return a string. It should use a lookup table that associates integers with
digits. Include a main function that tests the conversion function with numbers
in several bases.

Solution:


"""
def mean(list):
    l = len(list)
    i = 0
    sum = 0
    while i<l:
        sum += list[i]
    i+=1
    return sum/l
def median(list):
    l = len(list)
    list = sorted(list)
    mid = l//2
    if l%2 == 0:
        return (list[mid]+list[mid-1])/2
    else:
        return list[mid]
def mode(lst):
    d = dict()
    mode = False
    modeValue = 0
    result = 0
    for x in lst:
        if(not d.get(x)):
            d[x] = 1
        else:
            d[x]+=1
        mode = True
        if(d[x] > modeValue):
            modeValue = d[x]
            result = x
        if(mode):
           return result
        else:
            return "No mode"
def main():
    lst = [3, 1, 7, 1, 4, 10]
    print("List:",lst)
    print("Mode:",mode(lst))
    print("Median:",median(lst))
    print("Mean:",mean(lst))
main()
