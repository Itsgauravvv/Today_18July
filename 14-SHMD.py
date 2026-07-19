cpu_usage = float(input("Enter CPU usage (%): "))
memory_usage = float(input("Enter Memory usage (%): "))
disk_usage = float(input("Enter Disk usage (%): "))
latency = float(input("Enter Network latency (ms): "))
latency_threshold = 100

if cpu_usage > 90 and memory_usage > 85:
    print("System Status: Critical (High CPU and Memory Usage)")
elif disk_usage > 95:
    print("System Status: Storage Critical")
elif latency > latency_threshold:
    print("System Status: Network Issue (High Latency)")
elif cpu_usage > 75 or memory_usage > 70 or disk_usage > 80:
    print("System Status: Warning")
else:
    print("System Status: Healthy")