name = input("Enter student name: ")
roll_no = input("Enter roll number: ")
marks = []
result = "Pass"

for i in range(1, 6):
    m = int(input("Enter marks for Subject " + str(i) + " (0-100): "))
    if m < 0 or m > 100:
        print("Invalid marks! Please enter marks between 0 and 100.")
        exit()
    marks.append(m)
    if m < 40:
        result = "Fail"
        
total = sum(marks)
percentage = (total / 500) * 100

if result == "Fail":
    grade = "F"
    remark = "Failed in one or more subjects"
elif percentage >= 90:
    grade = "A+"
    remark = "Outstanding"
elif percentage >= 80:
    grade = "A"
    remark = "Excellent"
elif percentage >= 70:
    grade = "B"
    remark = "Very Good"
elif percentage >= 60:
    grade = "C"
    remark = "Good"
elif percentage >= 50:
    grade = "D"
    remark = "Satisfactory"
elif percentage >= 40:
    grade = "E"
    remark = "Pass"
else:
    grade = "F"
    remark = "Fail"

print("========== REPORT CARD ==========")
print("Student Name:",name)
print("Roll Number:",roll_no)
print("Subject Marks:",marks)
print("Total Marks:",total, "/ 500")
print("Percentage:",percentage, "%")
print("Result:",result)
print("Grade:",grade)
print("Remark:",remark)
print("================================")
