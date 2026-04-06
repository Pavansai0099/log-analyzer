# Step 1: Read file
with open("logs.txt", "r") as file:
    logs = file.readlines()

# Step 2: Initialize counters
error_count = 0
warning_count = 0
info_count = 0

# Step 3: Analyze logs
for log in logs:
    if "ERROR" in log:
        error_count += 1
    elif "WARNING" in log:
        warning_count += 1
    elif "INFO" in log:
        info_count += 1

# Step 4: Print results
print("Log Analysis Result:")
print("Errors:", error_count)
print("Warnings:", warning_count)
print("Info:", info_count)

# ✅ Step 5: Paste HERE (at the end)

import matplotlib.pyplot as plt

labels = ['Errors', 'Warnings', 'Info']
values = [error_count, warning_count, info_count]

plt.bar(labels, values)
plt.title("Log Analysis")
plt.xlabel("Log Type")
plt.ylabel("Count")
plt.show()