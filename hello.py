
# Display School Header
print("\n" + "="*80)
print("\t\t\t CENTRAL BOARD OF SECONDARY EDUCATION (CBSE)")
print("\t\t\t   NATIONAL PUBLIC SCHOOL, NARELA")
print("\t\t\t         ACADEMIC YEAR 2021-2022")
print("="*80 + "\n")


# Input Student Details
nikstudentname = input("Enter your name: ")
nikclass = int(input("Enter your class: "))
nikrollno = int(input("Enter your roll no: "))
nikmothername = input("Enter your mother's name: ")
nikfathername = input("Enter your father's name: ")
nikdob = input("Enter your date of birth (DD/MM/YYYY): ")

# Input Subjects & Marks
subjects = []
marks = []
for i in range(1, 6):
    sub = input(f"Enter subject {i}: ")
    mark = int(input(f"Enter marks for {sub}: "))
    subjects.append(sub)
    marks.append(mark)

# Checking for Failures & Applying Grace Marks
grace_count = 0
result = "PASS"
for i in range(5):
    if marks[i] < 31:
        print(f" Failed in {subjects[i]} (Marks: {marks[i]})")
        result = "FAIL"
    elif marks[i] in [31, 32] and grace_count < 2:
        grace_points = 33 - marks[i]
        marks[i] = 33
        grace_count += 1
        print(f"✅ Grace Marks Applied in {subjects[i]}: +{grace_points} (New Marks: {marks[i]})")

if grace_count > 2:
    print(" More than 2 subjects required grace marks. Result: FAIL")
    result = "FAIL"

# Calculate Total, Average & Grade
if result == "PASS":
    total_marks = sum(marks)
    average_marks = total_marks / 5
    
    if average_marks >= 90:
        grade = "A+"
    elif average_marks >= 80:
        grade = "A"
    elif average_marks >= 70:
        grade = "B"
    elif average_marks >= 60:
        grade = "C"
    else:
        grade = "D"
else:
    total_marks = "N/A"
    average_marks = "N/A"
    grade = "N/A"

# Display Final Report Card
print("\n" + "*"*40)
print("\t\t STUDENT REPORT CARD")
print("*"*40)
print(f"Student Name   : {nikstudentname}")
print(f"Class          : {nikclass}")
print(f"Roll No        : {nikrollno}")
print(f"Mother's Name  : {nikmothername}")
print(f"Father's Name  : {nikfathername}")
print(f"Date of Birth  : {nikdob}\n")
print("-"*40)
print("Subjects", "\tMarks")
print("-"*40)
for i in range(5):
    print(f"{subjects[i]:<15} {marks[i]:>3}")
print("-"*40)
print(f"Total Marks    : {total_marks}")
print(f"Average Marks  : {average_marks}")
print(f"Grade          : {grade}")
print(f"Result         : {result}")
print("*"*40)