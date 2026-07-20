def func_payroll():
    emp_id = int(input("Enter Employee ID: "))
    emp_name =input("Enter Employee Name: ")
    basic_salary= float(input("Enter Basic Salary: "))
    overtime_hours= int(input("Enter Overtime Hours: "))
    leave_days =int(input("Enter Number of Leave Days: "))
    return emp_id, emp_name, basic_salary, overtime_hours, leave_days
    
def calculate_hra(basic_salary):
    hra = basic_salary * 0.20
    return hra

def calculate_da(basic_salary):
    da = basic_salary * 0.10
    return da

def calculate_overtime_payment(overtime_hours):
    overtime_payment = overtime_hours * 500
    return overtime_payment

def calculate_leave_deduction(basic_salary, leave_days):
    if leave_days > 2:
        leave_deduction = (basic_salary - 1000)
        return leave_deduction
    else:
        return 0
def calculate_pf(basic_salary):
    pf = basic_salary * 0.12
    return pf

def calculate_gross_salary(basic_salary, hra, da, overtime_payment):
    gross_salary = basic_salary + hra + da + overtime_payment
    return gross_salary

def calculate_professional_tax(gross_salary):
    if gross_salary <= 30000:
        professional_tax = 200

    elif gross_salary <= 60000:
        professional_tax = 500

    else:
        professional_tax = 1000

    return professional_tax

def calculate_total_deductions(pf, professional_tax, leave_deduction):
    total_deductions = pf + professional_tax + leave_deduction
    return total_deductions

def calculate_net_salary(gross_salary, total_deductions):
    net_salary = gross_salary - total_deductions
    return net_salary
def display_payroll(emp_id, emp_name, basic_salary, hra, da, overtime_payment, leave_deduction, pf, professional_tax, gross_salary, total_deductions, net_salary):
    print("\n------------------------------------------------")
    print("\n Employee Salary Slip")
    print("\n------------------------------------------------")
    print(f"Employee ID: {emp_id}")
    print(f"Employee Name: {emp_name}")
    print(f"Basic Salary: {basic_salary}")
    print(f"HRA: {hra}")
    print(f"DA: {da}")
    print(f"Overtime Payment: {overtime_payment}")
    print(f"Leave Deduction: {leave_deduction}")
    print(f"PF: {pf}")
    print(f"Professional Tax: {professional_tax}")
    print(f"Gross Salary: {gross_salary}")
    print(f"Total Deductions: {total_deductions}")
    print(f"Net Salary: {net_salary}")
    print("\n------------------------------------------------")
    
emp_id, emp_name, basic_salary, overtime_hours, leave_days = func_payroll()

hra = calculate_hra(basic_salary)
da = calculate_da(basic_salary)
overtime_payment = calculate_overtime_payment(overtime_hours)
leave_deduction = calculate_leave_deduction(basic_salary, leave_days)
pf = calculate_pf(basic_salary)

gross_salary = calculate_gross_salary(basic_salary, hra, da, overtime_payment)

professional_tax = calculate_professional_tax(gross_salary)

total_deductions = calculate_total_deductions(pf, professional_tax, leave_deduction)

net_salary = calculate_net_salary(gross_salary, total_deductions)
    
display_payroll(emp_id, emp_name, basic_salary, hra, da,overtime_payment,leave_deduction,pf,professional_tax,gross_salary,total_deductions,
    net_salary
)