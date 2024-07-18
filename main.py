#!/usr/bin/python3
import time
from classes.student_class import Student
from classes.course_class import Course

grade_book = {}
course_list = []
# grade_book = open('students_names.txt', 'a')
def print_grade_book():
    for k, v in grade_book.items():
        print(f"{k} | {v[0]} | {v[1][0:].name} | {v[2]}")

def add_student():
    names = input("Enter Student Full name: ")
    email = input("Enter Student Email: ")
    student = Student(names=names, email=email, gpa=0, )
    grade_book[student.email]=[student.names, student.courses_registered, student.gpa]
    print_grade_book()
    # grade_book.write(f"\n{student.names}, {student.email}, {student.courses_registered}, {student.gpa}")
    time.sleep(2)


def add_course():
    name = input("Enter Course name: ")
    trimester = input("Enter trimster: ")
    credits = int(input("Enter course credits: "))
    course = Course(name=name, trimester=trimester, credits=credits)
    course_list.append(course)
    time.sleep(2)

def register_for_course():
    student_email = input("Student email: ")
    course_number = 0
    for i in course_list:
        course_number += 1
        print(f"\n{course_number}. {i.name}")
    course_chose = int(input(f"\nChoice your course from 1 to {course_number}: "))
    grade_book[student_email][1].append(course_list[course_chose - 1])
    print_grade_book()

def menu():
    while True:
        print("\n")
        print("Welcome to the Grade Book App of ALU\n\n")
        print("What do you want to do ?\n\n")
        print("1. Add Student\n")
        print("2. Add Course\n")
        print("3. Register Student for Course\n")
        print("4. Calculate Ranking\n")
        print("5. Search by Grade\n")
        print("6. Generate Transcript\n")
        print("7. Exit\n\n")
        choice = int(input("Enter your choice: "))
        print("\n")

        if choice == 1:
            add_student()

        elif choice == 2:
            add_course()
        
        elif choice == 3:
            register_for_course()

        elif choice == 7:
            break

        else:
            pass


menu()
