"""
Author: Pham Cong Hoang
Date: 29/10/2021
Problem:
Rrsources to manage a student's name and test scores.
"""
from functools import reduce

class student(object):

    def __init__(self, name, number):
        """tat cả diem = 0."""
        self._name = name
        self._scores = []
        for count in range(number):
            self._scores.append(0)
    def getName(self):
        """tra ve ten cua hoc sinh."""
        return self._name

    def getScores(self):
        """tra ve diem cua hsinh"""
        return  self._scores

    def setScore(self, i, score):
        """dat lại diem thu i dem tu 1"""
        self._scores[i - 1] = score

    def getScore(self, i):
        """ tra ve diem thu i dem tu 1."""
        return self._scores[i-1]

    def getAverage(self):
        """ giu lai diem tb."""
        sum = reduce(lambda x, y: x + y, self._scores)
        return sum / len(self._scores)

    def getHighScore(self):
        """tra ve diem cao nhat."""
        return max(self.scores)

    def __str__(self):
        """tra ve dai dien chuoi hsinh """
        return "Name: " + self._name + "\nScores: " + \
            " ".join(map(str, self._scores))

if __name__ == '__main__':

    student_a = student("Pham Thanh Nam", 5)
    print("Name: ", student_a.getName())
    print("Score: ", student_a.getScores())
    print("Score in i: ", student_a.getScore(2))

    student_a.setScore(1, 9.0)
    print("Score in i: ", student_a.getScore(1))

    print("====="*10)
    print(student_a)