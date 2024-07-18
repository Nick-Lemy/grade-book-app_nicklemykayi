from classes.student_class import Student
grade_book = open('students_names.txt', 'w')

def add_student():
    names = input("Enter Student Full name: ")
    email = input("Enter Student Email: ")
    student = Student(names=names, email=email, gpa=0, )
    grade_book.write(f"{student.names}, {student.email}, {student.courses_registered}, {student.gpa}")


def menu():
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
    else:
        pass


menu()
