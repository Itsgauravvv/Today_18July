test_coverage = float(input("Enter test coverage percentage: "))
security_scan = input("Did the security scan pass? (yes/no): ").lower()
code_review = input("Is the code review completed? (yes/pending): ").lower()
environment = input("Enter environment (development/staging/production): ").lower()
if security_scan == "no":
    print("Deployment Status: Rejected (Security Scan Failed)")

elif (environment == "production" and test_coverage >= 80 and security_scan == "yes" and code_review == "yes"):
    print("Deployment Status: Approved for Production")

elif environment == "staging" and security_scan == "yes":
    print("Deployment Status: Approved for Staging (Warnings Allowed)")

elif environment == "development" and code_review == "pending":
    print("Deployment Status: Conditional Approval")

else:
    print("Deployment Status: Rejected")