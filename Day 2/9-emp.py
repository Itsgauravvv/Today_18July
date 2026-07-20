emp_details = []

def add_emp(emp_details):
    emp_id = int(input("Enter Employee ID: "))
    emp_name = input("Enter Employee Name: ")
    designation = input("Enter Employee Designation: ")
    salary = float(input("Enter Employee Salary: "))

    emp = [emp_id, emp_name, designation, salary]
    emp_details.append(emp)

    print("Employee added successfully!")

def view_emp(emp_details):
    print("\nEmployee Details:")

    if len(emp_details) == 0:
        print("No employees found.")
    else:
        for emp in emp_details:
            print(emp)

def search_emp(emp_details):
    search_id = int(input("Enter Employee ID to search: "))

    for emp in emp_details:
        if emp[0] == search_id:
            print("\nEmployee Found")
            print(f"Employee ID : {emp[0]}")
            print(f"Employee Name : {emp[1]}")
            print(f"Designation : {emp[2]}")
            print(f"Salary : {emp[3]}")
            return

    print("Employee not found.")
while True:

    print("\n========== Employee Training Tracker ==========")
    print("1. View Employees")
    print("2. Add Employee")
    print("3. Search Employee")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        view_emp(emp_details)
    elif choice == 2:
        add_emp(emp_details)
    elif choice == 3:
        search_emp(emp_details)
    elif choice == 4:
        break

    else:
        print("Invalid Choice!")