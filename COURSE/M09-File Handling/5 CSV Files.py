# =========================================
# Topic : CSV Files
# =========================================

# CSV = Comma Separated Values

import csv

# Writing CSV file

with open("students.csv", "w", newline="") as file:

    writer = csv.writer(file)

    # Writing headings
    writer.writerow(["Name", "Marks", "Course"])

    # Writing rows
    writer.writerow(["Madhav", 95, "Python"])

    writer.writerow(["Arjun", 88, "Java"])

    writer.writerow(["Simran", 97, "AI"])

print("CSV File Created")

# =========================================
# Reading CSV file
# =========================================

with open("students.csv", "r") as file:

    reader = csv.reader(file)

    for row in reader:

        print(row)