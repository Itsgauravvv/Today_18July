ann_inc = float(input("Enter annual income: "))
age = int(input("Enter age: "))
investment = float(input("Enter investment amount: "))

if ann_inc < 500000:
    tax = 0
elif ann_inc <= 1000000:
    tax = ann_inc * 0.10
elif ann_inc <= 2000000:
    tax = ann_inc * 0.20
else:
    tax = ann_inc * 0.30

if age >= 60:
    tax = tax - 50000
    print("Senior Citizen Exemption Applied: ₹50,000")

tax = tax - investment

if tax < 0:
    tax = 0

print("Annual Income:", ann_inc)
print("Age:", age)
print("Investment Amount:", investment)
print("Final Tax Payable: ", tax)