#!/usr/bin/python3
from student_class import *

class GradeBook:
    def __init__(self, student_list=[], course_list=[]):
        self.student_list = student_list
        self.course_list = course_list
    def add_student(self):
        name = input("Names = ")
        email = input("Student Email = ")
        courses_registered = input("Courses Registered = ")
        self.student_list.append(Student(email, name, courses_registered))