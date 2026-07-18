p = int(input("Enter the principal value: "))
r = int(input("Enter the rate(%): "))
t = int(input("Enter the time in years: "))

SI = (p*r*t)/100
print(f"The Simple interest is: {SI}")

CI = p*((1+(r/100))**t-1)
print(f"The Compound interest is: {CI}")