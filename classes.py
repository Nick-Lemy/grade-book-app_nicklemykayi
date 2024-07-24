#!/usr/bin/python3

class Student:
    def __init__(self, names, email, courses_registered={}, GPA=0):
        self.email = email
        self.names = names
        self.courses_registered = courses_registered
        self.GPA = GPA
        
    def calculate_GPA(self):
        sum_grades = 0
        for k, v in self.courses_registered:
            sum += 1
            
        self.GPA = sum(self.register_for_course.values())
    def register_for_course(self):
        pass

class Course:
    def __init__(self, name, trimester, credits):
        self.name = name
        self.trimester = trimester
        self.credits = credits

class GradeBook:
    student_list = []
    course_list = []
    
    def add_student(self):
        names = input("Enter student name: ")
        email = input("Enter student email: ")
        new_student = Student(names, email, courses_registered={}, GPA=0)
        self.student_list.append(new_student)
    
    def add_course(self):
        course_name = input("Enter new course name: ")
        course_trimester = input("Enter course trimester: ")
        course_credit = input("New course credit: ")
        new_course = Course(course_name, course_trimester, course_credit)
        self.course_list.append(new_course)
    
    def register_student_for_course(self):
        student_email = input("Student email: ")
        for i in self.student_list:
            if i.email == student_email:
                print("\ncourses available: \n")
                for index, value  in enumerate(self.course_list):
                    print(f"{index + 1}. {value.name}")
                choice = int(input("Choice your course: "))
                i.courses_registered[self.course_list[choice - 1]] = 0

            else:
                print("Student Not found")
    def upload_grades(self):
        student_email = input("student email: ")
        for i in self.student_list:
            if i.email == student_email:
                print(f"The Student {i.names} has been found!")
                for course in i.courses_registered.keys():
                    print(course.name)
                course_to_upload = input("Select a course: ")
                for course in i.courses_registered.keys():
                    if course_to_upload == course.name:
                        grade = input(f"Enter grade for {course.name}: ")
                        i.courses_registered[course] = grade

    def calculate_GPA(self):
        sum_grades = 0
        sum_credits = 0
        for student in self.student_list:
            for course, grade in student.courses_registered.items():
                sum_grades += course.credits * grade
                sum_credits += course.credits
            student.GPA += sum_grades / sum_credits
    
    def show_students(self):
        for i in self.student_list:
            print(f"{i.names} : {i.email} : {i.GPA}")
