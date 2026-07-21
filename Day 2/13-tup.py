employees = []

while True:
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Assign Project")
    print("4. Remove Project")
    print("5. Search Employee")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        emp_id = int(input("Enter Employee ID: "))
        name = input("Enter Employee Name: ")
        department = input("Enter Department: ")
        projects = []

        employee = (emp_id, name, department, projects)

        employees.append(employee)

        print("Employee added successfully!")

    elif choice == 2:

        if len(employees) == 0:
            print("No employee records found.")
        else:
            print("\nEmployee Details")
            print("-" * 50)

            for emp in employees:
                print(f"ID         : {emp[0]}")
                print(f"Name       : {emp[1]}")
                print(f"Department : {emp[2]}")
                print(f"Projects   : {emp[3]}")
                print("-" * 50)

    elif choice == 3:

        emp_id = int(input("Enter Employee ID: "))

        found = False

        for emp in employees:
            if emp[0] == emp_id:
                project = input("Enter Project Name: ")
                emp[3].append(project)
                print("Project assigned successfully!")
                found = True
                break

        if not found:
            print("Employee not found.")

    elif choice == 4:

        emp_id = int(input("Enter Employee ID: "))

        found = False

        for emp in employees:

            if emp[0] == emp_id:

                if len(emp[3]) == 0:
                    print("No projects assigned.")
                else:
                    print("Projects:", emp[3])
                    project = input("Enter project to remove: ")

                    if project in emp[3]:
                        emp[3].remove(project)
                        print("Project removed successfully!")
                    else:
                        print("Project not found.")

                found = True
                break

        if not found:
            print("Employee not found.")

    elif choice == 5:

        emp_id = int(input("Enter Employee ID: "))

        found = False

        for emp in employees:

            if emp[0] == emp_id:

                print("\nEmployee Found")
                print(f"ID         : {emp[0]}")
                print(f"Name       : {emp[1]}")
                print(f"Department : {emp[2]}")
                print(f"Projects   : {emp[3]}")

                found = True
                break

        if not found:
            print("Employee not found.")

    elif choice == 6:
        print("Thank you!")
        break

    else:
        print("Invalid choice.")