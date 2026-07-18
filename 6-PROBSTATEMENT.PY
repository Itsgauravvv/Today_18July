name  = input("Enter applicant's name: ")
age = int(input("Enter age: "))
mon_salary = int(input("Enter your monthly salary: "))
work_exp = int(input("Enter your work experience in years: "))
cred_score = int(input("Enter your credit score: "))
existing_EMI = int(input("Enter your existing monthly EMI: "))


if(age >= 21 and age <=58):
    if(work_exp >= 2):
        if((existing_EMI<=0.4*mon_salary)):
            if(cred_score >=650):
                if(mon_salary>= 25000 and mon_salary <= 39999):
                    mle = 200000
                    print("Loan Application Status: Eligible")
                    print("Maximum Loan Amount: ", mle)
                elif(mon_salary>= 40000 and mon_salary <= 59999):
                    mle = 500000
                    print("Loan Application Status: Eligible")
                    print("Maximum Loan Amount: ", mle)
                elif(mon_salary>= 60000 and mon_salary <= 99999):
                    mle = 1000000
                    print("Loan Application Status: Eligible")
                    print("Maximum Loan Amount: ", mle)
                elif(mon_salary>= 100000):
                    mle = 1500000
                    print("Loan Application Status: Eligible")
                    print("Maximum Loan Amount: ", mle)
                else:
                    print("Loan Application Status: Rejected")
                    print("Reason: Monthly salary is below the minimum threshold.")
            else:
                print("Loan Application Status: Rejected")
                print("Reason: Credit score is below 650.")
        else:
            print("Loan Application Status: Rejected")
            print("Reason: Existing EMI is greater than 40% of monthly salary")
    else:
            print("Loan Application Status: Rejected")
            print("Reason: Work experience is less than 2 years.")
else:
    print("Loan Application Status: Rejected")
    print("Reason: Age is not within the eligible range of 21 to 58 years.")        

        