#!/usr/bin/python3
import time
from classes import *

gradebook = GradeBook()

def menu():
    while True:
        print("\n")
        print("ALU GRADE BOOK APP by Nick-Lemy K.\n\n")
        print("What do you want to do ?\n")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Register Student for Course")
        print("4. Upload Grades")
        print("5. Save data")
        print("6. Load your Data")
        print("7. Calculate Ranking")
        print("8. Search Student by Grade")
        print("9. Generate Students' Transcripts")
        print("10. Students List")
        print("11. Exit\n\n")

        choice = int(input("Enter your choice: "))
        print("\n")

        if choice == 1:
            gradebook.add_student()
            time.sleep(3)

        elif choice == 2:
            gradebook.add_course()
            time.sleep(3)

        elif choice == 3:
            gradebook.show_students()
            gradebook.register_student_for_course()
            time.sleep(3)

        elif choice == 4:
            gradebook.show_students()
            gradebook.upload_grades()
            time.sleep(3)

        elif choice == 5:
            gradebook.save_to_file()
            print("Data saved !")
            time.sleep(3)

        elif choice == 6:
            try:
                gradebook.load_from_file()
                print("Data loaded !")
            except:
                print("No data available...")
            finally:
                time.sleep(3)

        elif choice == 7:
            gradebook.calculate_GPA()
            gradebook.calculate_ranking()
            time.sleep(3)

        elif choice == 8:
            gradebook.search_by_grade()
            time.sleep(3)

        elif choice == 9:
            gradebook.generate_transcript()
            time.sleep(3)
        elif choice == 10:
            gradebook.show_students()
            time.sleep(3)
        elif choice == 11:
            break
        else:
            print("Invalid choice, try again.")

menu()
