"""
Author: pham cong hoang
Date: 22/10/2021

Problem: A list is sorted in ascending order if it is empty or each item except the last one is
less than or equal to its successor. Define a predicate isSorted that expects a list
as an argument and returns True if the list is sorted, or returns False otherwise.
Copyright 2019 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part.
Due to electronic rights, some third party content may be suppressed from the eBook and/or eChapter(s).
Editorial review has deemed that any suppressed content does not materially affect the overall learning experience.
Cengage Learning reserves the right to remove additional content at any time if subsequent rights restrictions require it.
Copyright 2019 Cengage Learning. All Rights Reserved. May not be copied, scanned, or duplicated, in whole or in part.
 WCN 02-200-203204
C h a p t e r 6 Design with Functions
(Hint: For a list of length 2 or greater, loop through the list and compare pairs of
items, from left to right, and return False if the first item in a pair is greater.)
Solution:

"""

def isSorted(lyst):
    if len(lyst) == 0 or len(lyst) == 1:
        return True
    else:
        for index in range(len(lyst) - 1):
            if lyst[index] > lyst[index + 1]:
                return False
        return True
def main():
    lyst = []
    print(isSorted(lyst))
    lyst = [1]
    print(isSorted(lyst))
    lyst = list(range(10))
    print(isSorted(lyst))
    lyst[9] = 3
    print(isSorted(lyst))
main()