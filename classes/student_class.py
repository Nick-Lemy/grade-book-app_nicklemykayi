#!/usr/bin/python3
class Student:
    def __init__(self, email, names, courses_registered=[], gpa=0):
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
    def register_for_course(self):
        new_course = input("New Course name = ")
        self.courses_registered.append(new_course)

# nick = Student("n.kayiranga@gmail.com", "Nick-Lemy Kayiranga", courses_registered=["Learning Process", "Self Directed Learning", "Python Programming"])
# print(nick.calculate_gpa())
# nick.register_for_course()
# print(nick.courses_registered)