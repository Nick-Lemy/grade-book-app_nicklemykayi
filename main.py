#!/usr/bin/python3
import time
from classes import *

gradebook = GradeBook()

def menu():
    while True:

        print("\n")
        print("Welcome to the Grade Book App of ALU\n\n")
        print("What do you want to do ?\n")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Register Student for Course")
        print("4. Calculate Ranking")
        print("5. Search by Grade")
        print("6. Generate Transcript")
        print("7. Show all students")
        print("8. Exit\n\n")

        choice = int(input("Enter your choice: "))
        print("\n")

        if choice == 1:
            gradebook.add_student()

        elif choice == 2:
            gradebook.add_course()
        
        elif choice == 3:
            gradebook.register_student_for_course()
        elif choice == 7:
            gradebook.show_students()

        else:
            pass

menu()