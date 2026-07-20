emp_skills = {}

def add_employee_skill(emp_skills):
    emp_id = int(input("Enter Employee ID: "))
    emp_name = input("Enter Employee Name: ")
    skill = input("Enter Employee Skill: ")

    emp_skills[emp_id] = {
        "Name": emp_name,
        "Skill": skill
    }
    print("Employee skill added successfully!")

def view_all_employees(emp_skills):
    if len(emp_skills) == 0:
        print("No employee records found.")
    else:
        print("\nEmployee Details:")
        for emp_id, details in emp_skills.items():
            print(f"\nEmployee ID: {emp_id}")
            print(f"Employee Name: {details['Name']}")
            print(f"Skill: {details['Skill']}")

def search_employee_skill(emp_skills):
    emp_id = int(input("Enter Employee ID to search: "))

    if emp_id in emp_skills:
        print("\nEmployee Found!")
        print(f"Employee Name: {emp_skills[emp_id]['Name']}")
        print(f"Skill: {emp_skills[emp_id]['Skill']}")
    else:
        print("Employee not found.")

while True:
    print("\n========== Employee Skill Management System ==========")
    print("1. Add Employee Skill")
    print("2. View All Employees")
    print("3. Search Employee Skill")
    print("4. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_employee_skill(emp_skills)
    elif choice == 2:
        view_all_employees(emp_skills)
    elif choice == 3:
        search_employee_skill(emp_skills)
    elif choice == 4:
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice!")
        
        
