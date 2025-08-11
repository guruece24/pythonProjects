import sys

class Student:
    def __init__(self, myName, myGrade):
       self.name = myName
       self.grade = myGrade

    def display(self, myAge):
        print(f"student {self.name} is in grade {self.grade} and age is {myAge}")

s1 = Student("guru", 10)
s2 = Student("prasad", 43)
s3 = Student("king", 63)

print(s1.name)
print(s1.grade)

s1.display(43)
s2.display(54)
s3.display(34)

