empid = []
for i in range(1, 6):
    empid.append(int(input("Enter Employee ID: ")))

for emp in empid:
    if emp%5==0:
        continue
    if emp==37:
        break
    if emp>20:
        print(f"employee ID greater than 20 are: {emp}")
