lst1 = ["Computer_Science", "Information_Technology", "Machine_Learning", "TOC", "Maths"]
m1= int(input("Enter the marks of Computer Science: "))
m2 = int(input("Enter the marks of IT: "))
m3 = int(input("Enter the marks of Machine Learning: "))
m4 = int(input("Enter the marks of TOC: "))
m5 = int(input("Enter the marks of Maths: "))

total_marks = m1+ m2+ m3+ m4 + m5
cnt = len(lst1)
print("The total subjects are: ", cnt)
print(f"The total marks obt in all subjects is: {total_marks}")
print(f"The average marks obt in all subjects is: {total_marks/cnt}")
