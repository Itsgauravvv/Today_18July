rating = int(input("Enter the rating of the employee: "))
y_of_exp = int(input("Enter the years of experience of the employee: "))
p_d_s = input("Enter the project delivery status of the employee (On-time or Delayed): ")

if rating == 5 and y_of_exp > 10 and p_d_s == "On-time":
    print("The employee is eligible for 30% bonus.")
elif rating == 4 and y_of_exp > 7:
    print("The employee is eligible for 20% bonus.")
elif rating == 3 and p_d_s == "Delayed":
    print("The employee is eligible for 5% bonus.")
else:
    print("The employee is not eligible for bonus.")