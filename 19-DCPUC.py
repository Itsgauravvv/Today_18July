power_consumption = float(input("Enter total power consumption (kW): "))
cooling_efficiency = float(input("Enter cooling efficiency (%): "))
rack_load = float(input("Enter rack load percentage (%): "))

if power_consumption > 1000 and cooling_efficiency < 70:
    print("Data Center Status: Critical")
elif rack_load > 85:
    print("Data Center Status: Warning")
elif cooling_efficiency >= 85 and rack_load <= 70:
    print("Data Center Status: Normal")
else:
    print("Data Center Status: Moderate Risk")