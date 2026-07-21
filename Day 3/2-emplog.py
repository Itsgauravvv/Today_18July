import logging

logging.basicConfig(
    filename="C:\\Users\\Gaurav Joshi\\OneDrive\\Desktop\\MRPythonTraining\\logs\\emp.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Employee Training Tracker Started")

emp_details = []


def add_emp(emp_details):
    try:
        emp_id = int(input("Enter Employee ID: "))
        for emp in emp_details:
            if emp[0] == emp_id:
                logging.error(f"Duplicate Employee ID Entered - ID:{emp_id}")
                print("Error: Employee ID already exists!")
                return

        emp_name = input("Enter Employee Name: ")
        designation = input("Enter Employee Designation: ")
        salary = float(input("Enter Employee Salary: "))

        emp = [emp_id, emp_name, designation, salary]
        emp_details.append(emp)

        logging.info(f"Employee Added - ID:{emp_id}, Name:{emp_name}")
        print("Employee added successfully!")

    except ValueError:
        logging.error("Invalid input while adding employee.")
        print("Invalid input! Please enter correct values.")


def view_emp(emp_details):
    logging.info("Viewed Employee List")

    print("\nEmployee Details:")

    if len(emp_details) == 0:
        print("No employees found.")
        logging.warning("View attempted but employee list is empty.")
    else:
        for emp in emp_details:
            print(f"Employee ID : {emp[0]}")
            print(f"Employee Name : {emp[1]}")
            print(f"Designation : {emp[2]}")
            print(f"Salary : {emp[3]}")
            print("-" * 30)


def search_emp(emp_details):
    try:
        search_id = int(input("Enter Employee ID to search: "))

        for emp in emp_details:
            if emp[0] == search_id:
                logging.info(f"Employee Found - ID:{search_id}")

                print("\nEmployee Found")
                print(f"Employee ID : {emp[0]}")
                print(f"Employee Name : {emp[1]}")
                print(f"Designation : {emp[2]}")
                print(f"Salary : {emp[3]}")
                return

        logging.warning(f"Employee Not Found - ID:{search_id}")
        print("Employee not found.")

    except ValueError:
        logging.error("Invalid Employee ID entered for search.")
        print("Please enter a valid Employee ID.")


while True:

    print("\n========== Employee Training Tracker ==========")
    print("1. View Employees")
    print("2. Add Employee")
    print("3. Search Employee")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            view_emp(emp_details)

        elif choice == 2:
            add_emp(emp_details)

        elif choice == 3:
            search_emp(emp_details)

        elif choice == 4:
            logging.info("Program Closed")
            print("Thank You!")
            break

        else:
            logging.warning("Invalid Menu Choice Entered")
            print("Invalid Choice!")

    except ValueError:
        logging.error("Non-numeric menu choice entered.")
        print("Please enter a valid number.")