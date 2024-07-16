#!/usr/bin/python3
class Student:
    def __init__(self, email, names, courses_registered, gpa=0):
        self.email = email
        self.names = names
        self.courses_registered = courses_registered
        self.gpa = gpa
    def calculate_gpa(self):
        grades = []
        for i in self.courses_registered:
            a = int(input(f"{i}= "))
            grades.append(a)
        for i in grades:
            self.gpa += i
        return self.gpa

nick = Student("n.kayiranga@gmail.com", "Nick-Lemy Kayiranga", courses_registered=["Learning Process", "Self Directed Learning", "Python Programming"])
print(nick.calculate_gpa())