age = int(input("Enter patient age: "))
oxygen_level = float(input("Enter oxygen level (%): "))
heart_rate = int(input("Enter heart rate (bpm): "))
symptom_severity = input("Enter symptom severity (mild/moderate/severe): ").lower()
if oxygen_level < 90:
    print("Patient Status: Emergency")
elif age >= 60 and symptom_severity == "severe":
    print("Patient Status: High Priority")
elif symptom_severity == "mild":
    print("Patient Status: General Queue")
else:
    print("Patient Status: Medium Priority")