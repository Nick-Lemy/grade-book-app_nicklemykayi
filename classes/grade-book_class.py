#!/usr/bin/python3
from student_class import *

class GradeBook:
    def __init__(self, student_list=[], course_list=[]):
        self.student_list = student_list
        self.course_list = course_list
    def add_student(self):
        name = input("Names = ")
        email = input("Student Email = ")
        courses_number = input("How many courses are you in ? = ")
        courses_registered =[]
        for i in courses_number:
            courses_registered.append(input(f"course{1} = "))
        self.student_list.append(Student(email, name, courses_registered))