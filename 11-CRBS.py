compute_hours = float(input("Enter compute hours: "))
storage_used = float(input("Enter storage used (GB): "))
plan = input("Enter support plan (Basic/Premium/Enterprise): ").lower()

compute_rate = 10     
storage_rate = 5    
support_fee = 0

if plan == "basic":
    support_fee = 500

elif plan == "premium":
    support_fee = 1000
    compute_rate = 8      

elif plan == "enterprise":
    support_fee = 2000
    compute_rate = 7      
    storage_rate = 1.5    

else:
    print("Invalid plan selected!")
    exit()

if compute_hours <= 100:
    compute_cost = compute_hours * compute_rate
elif compute_hours <= 200:
    compute_cost = (100 * compute_rate) + ((compute_hours - 100) * (compute_rate + 2))
else:
    compute_cost = (100 * compute_rate) + (100 * (compute_rate + 2)) + ((compute_hours - 200) * (compute_rate + 5))

storage_cost = storage_used * storage_rate

total_bill = compute_cost + storage_cost + support_fee

print("Support Plan :", plan.title())
print("Compute Cost : ", compute_cost)
print("Storage Cost : ", storage_cost)
print("Support Fee  : ", support_fee)
print("Total Bill   : ", total_bill)