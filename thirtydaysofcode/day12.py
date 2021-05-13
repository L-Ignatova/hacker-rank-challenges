# link to problem: https://www.hackerrank.com/challenges/30-inheritance/problem

class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, firstName, lastName, idNumber, score):
        super().__init__(firstName, lastName, idNumber)
        self.score = score

    def calculate(self):
        grade = sum(self.score) / len(self.score)
        scores = {
            'T': grade < 40,
            'D': 40 <= grade < 55,
            'P': 55 <= grade < 70,
            'A': 70 <= grade < 80,
            'E': 80 <= grade < 90,
            'O': 90 <= grade <= 100,
        }
        for key, val in scores.items():
            if val == True:
                return key


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())