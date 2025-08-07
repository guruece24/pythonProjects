import sys


class Student:
    def __init__(self, name, grade):
       self.name = name
       self.grade = grade

    def display(self):
        print(f"student {self.name} is in grade {self.grade}")

s1 = Student("guru", 10)
s2 = Student("prasad", 43)
s3 = Student("king", 63)

s1.display()
s2.display()
s3.display()

