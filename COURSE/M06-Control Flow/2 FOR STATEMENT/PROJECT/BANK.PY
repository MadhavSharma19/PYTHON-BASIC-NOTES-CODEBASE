# ============================================
# Project: Student Management System
# Concepts Used:
# - for loop
# - if-else
# - list
# - input
# ============================================

print("====================================")
print("    STUDENT MANAGEMENT SYSTEM")
print("====================================")

# Total number of students
total_students = int(input("Enter Number of Students: "))

# Empty list to store student names
student_names = []

# Empty list to store marks
student_marks = []

# ---------------- ENTER STUDENT DATA ----------------
for i in range(total_students):

    print("\nEnter Details of Student", i + 1)

    name = input("Enter Student Name: ")
    marks = int(input("Enter Marks: "))

    # Store data in lists
    student_names.append(name)
    student_marks.append(marks)

print("\n====================================")
print("          STUDENT REPORT")
print("====================================")

# Variable for class total
class_total = 0

# ---------------- DISPLAY REPORT ----------------
for i in range(total_students):

    marks = student_marks[i]

    # Add marks to class total
    class_total = class_total + marks

    # Grade system
    if marks >= 90:
        grade = "A"

    elif marks >= 75:
        grade = "B"

    elif marks >= 50:
        grade = "C"

    else:
        grade = "Fail"

    # Pass or Fail
    if marks >= 40:
        result = "PASS"

    else:
        result = "FAIL"

    # Print student report
    print("\nStudent:", student_names[i])
    print("Marks:", marks)
    print("Grade:", grade)
    print("Result:", result)

# ---------------- CLASS AVERAGE ----------------
average = class_total / total_students

print("\n====================================")
print("Class Total Marks:", class_total)
print("Class Average:", average)
print("====================================")

# ---------------- TOPPER FINDER ----------------
highest_marks = max(student_marks)
topper_index = student_marks.index(highest_marks)

print("\n🏆 Class Topper")
print("Name:", student_names[topper_index])
print("Marks:", highest_marks)

print("\n====================================")
print("   THANK YOU FOR USING SYSTEM")
print("====================================")