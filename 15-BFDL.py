# Input from user
t_amount = float(input("Enter transaction amount: "))
location_mismatch = input("Is there a location mismatch? (yes/no): ").lower()
unusual_login = input("Is the login time unusual? (yes/no): ").lower()
account_age = int(input("Enter account age (in months): "))

if t_amount > 100000 and location_mismatch == "yes":
    print("Transaction Status: Fraud Alert")
elif account_age < 6 and unusual_login == "yes":
    print("Transaction Status: Risk Alert")
elif t_amount >= 50000 and unusual_login == "yes":
    print("Transaction Status: Under Review")
else:
    print("Transaction Status: Approved")