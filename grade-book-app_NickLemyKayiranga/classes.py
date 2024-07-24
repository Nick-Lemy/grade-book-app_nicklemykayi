#!/usr/bin/python3
import json

class Student:
    def __init__(self, names, email, courses_registered=None, GPA=0):
        if courses_registered is None:
            courses_registered = {}
        self.email = email
        self.names = names
        self.courses_registered = courses_registered
        self.GPA = GPA

    def calculate_GPA(self):
        sum_grades = 0
        sum_credits = 0
        for course, grade in self.courses_registered.items():
            sum_grades += (4 * grade) / course.credits
            sum_credits += 1
        self.GPA = sum_grades / sum_credits if sum_credits != 0 else 0.0

    def register_for_course(self, course):
        self.courses_registered[course] = 0

    def to_dict(self):
        return {
            'names': self.names,
            'email': self.email,
            'courses_registered': {course.name: grade for course, grade in self.courses_registered.items()},
            'GPA': self.GPA
        }

    @classmethod
    def from_dict(cls, data, course_list):
        courses_registered = {next(course for course in course_list if course.name == name): grade for name, grade in data['courses_registered'].items()}
        return cls(data['names'], data['email'], courses_registered, data['GPA'])

class Course:
    def __init__(self, name, trimester, credits):
        self.name = name
        self.trimester = trimester
        self.credits = credits

    def to_dict(self):
        return {
            'name': self.name,
            'trimester': self.trimester,
            'credits': self.credits
        }
    
    @classmethod
    def from_dict(cls, data):
        return cls(data['name'], data['trimester'], data['credits'])

class GradeBook:
    def __init__(self):
        self.student_list = []
        self.course_list = []

    def add_student(self):
        names = input("Enter student name: ")
        email = input("Enter student email: ")
        new_student = Student(names, email)
        self.student_list.append(new_student)
        print(f"The student {new_student.names} has been added !")

    def add_course(self):
        course_name = input("Enter new course name: ")
        course_trimester = input("Enter course trimester: ")
        course_credit = float(input("New course credit: "))
        new_course = Course(course_name, course_trimester, course_credit)
        self.course_list.append(new_course)
        print(f"The course {new_course.name} has been added successfully")

    def register_student_for_course(self):
        student_email = input("Student email: ")
        for student in self.student_list:
            if student.email == student_email:
                print("\nCourses available: \n")
                for index, course in enumerate(self.course_list):
                    print(f"{index + 1}. {course.name}")
                choice = int(input("Choose your course: "))
                student.register_for_course(self.course_list[choice - 1])
                print(f"{student.names} has been registered for {self.course_list[choice - 1].name}")

    def upload_grades(self):
        student_email = input("Student email: ")
        for student in self.student_list:
            if student.email == student_email:
                print(f"The student {student.names} found!")
                for course in student.courses_registered.keys():
                    print(course.name)
                course_to_upload = input("Select a course: ")
                for course in student.courses_registered.keys():
                    if course_to_upload == course.name:
                        grade = float(input(f"Enter grade for {course.name}: "))
                        student.courses_registered[course] = grade
                        print(f"{student.names} got {grade} in {course.name}.")

    def calculate_GPA(self):
        for student in self.student_list:
            student.calculate_GPA()

    def show_students(self):
        for student in self.student_list:
            print(f"{student.names} <=> {student.email}")

    def save_to_file(self, filename='data.txt'):
        data = {
            'students': [student.to_dict() for student in self.student_list],
            'courses': [course.to_dict() for course in self.course_list]
        }
        with open(filename, 'w') as file:
            json.dump(data, file)

    def load_from_file(self, filename='data.txt'):
        with open(filename, 'r') as file:
            data = json.load(file)
        self.course_list = [Course.from_dict(course_data) for course_data in data['courses']]
        self.student_list = [Student.from_dict(student_data, self.course_list) for student_data in data['students']]
    
    def calculate_ranking(self):
        self.student_list.sort(key= lambda student: student.GPA, reverse=True)
        for i, student in enumerate(self.student_list, 1):
            print(f"{i}. {student.names} | {student.email} | {student.GPA}")

    def search_by_grade(self):
        min_grade = float(input("Enter minimum GPA: "))
        max_grade = float(input("Enter maximum GPA: "))
        filtered_students = [student for student in self.student_list if min_grade <= student.GPA <= max_grade]
        for student in filtered_students:
            print(f"{student.names} | {student.email} | {student.GPA}")

    def generate_transcript(self):
        for student in self.student_list:
            print(f"Transcript for {student.names} ({student.email}):")
            for course, grade in student.courses_registered.items():
                print(f"{course.name} = {grade} ({course.credits} credits)")
