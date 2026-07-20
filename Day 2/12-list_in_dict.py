students = {
    "MRU": [],
    "MRI": []
}
def add_student(students):
    university = input("Enter University (MRU/MRI): ").upper()
    student_id = int(input("Enter Student ID: "))
    for key, value in students.items():
        for student in value:
            if student[0] == student_id:
                print(f"\n{student_id} ID is already allotted in {key}.")
                return
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    branch = input("Enter Branch: ")

    students[university].append([student_id, name, age, branch])
    print("Student added successfully!")

def view_students(students):
    for university, value in students.items():
        print(f"\n{university}")

        if len(value) == 0:
            print("No records found.")
        else:
            for student in value:
                print(student)

def search_student(students):
    student_id = int(input("Enter Student ID to search: "))
    for univ, value in students.items():
        for student in value:
            if student[0] == student_id:
                print(f"\nStudent found in {univ}")
                print(student)
                return
    print("Student not found.")

while True:
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_student(students)
    elif choice == 2:
        view_students(students)
    elif choice == 3:
        search_student(students)
    elif choice == 4:
        print("Program completed.")
        break
    else:
        print("Invalid Choice")