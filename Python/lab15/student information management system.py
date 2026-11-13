students = {
    "101": {
        "Name": "Amy",
        "Branch": "BTech",
        "Semester": 1,
        "Marks": [99, 95, 98]
    },
    "102": {
        "Name": "Aadya",
        "Branch": "BTech",
        "Semester": 1,
        "Marks": [82, 88, 85]
    },
    "103": {
        "Name": "Nishi",
        "Branch": "BTech",
        "Semester": 1,
        "Marks": [95, 97, 92]
    }
}

while True:
    print("===== STUDENT INFORMATION MANAGEMENT SYSTEM =====")
    print("1. View All Students")
    print("2. Search Student by Roll Number")
    print("3. Register New Student")
    print("4. Update Student Details")
    print("5. View Academic Performance")
    print("6. Delete Student Record")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    
    if choice == "1":
        print("====Enrolled Student Records====")

        for roll, student in students.items():
            print(f"Roll No: {roll}")
            print(f"Name: {student['Name']}")
            print(f"Branch: {student['Branch']}")
            print(f"Semester: {student['Semester']}")
            print(f"Marks: {student['Marks']}")

        print("Total Enrolled Students:", len(students))

    
    elif choice == "2":
        roll = input("Enter Roll Number to search: ")
        student = students.get(roll)

        if student is not None:
            print("Student Record")
            for key, value in student.items():
                print(f"{key}: {value}")
        else:
            print("Student not found.")

    
    elif choice == "3":
        print("====Register New Student====")

        roll = input("Enter Roll Number: ")

        if roll in students:
            print("Roll Number already exists.")
            continue

        name = input("Enter Student Name: ")
        branch = input("Enter Branch (e.g., BTech, BCA AI): ")

        semester_input = input("Enter Semester: ")

        if not semester_input.isdigit():
            print("Enter a valid numeric semester.")
            continue

        semester = int(semester_input)

        if semester < 1:
            print("Semester must be at least 1.")
            continue

        marks = []
        valid_marks = True

        for i in range(3):
            mark_input = input(f"Enter marks for Subject {i + 1}: ")

            if not mark_input.isdigit():
                print(" Marks must be numeric.")
                valid_marks = False
                break

            mark = int(mark_input)

            if mark < 0 or mark > 100:
                print(" Marks must be between 0 and 100.")
                valid_marks = False
                break

            marks.append(mark)

        if valid_marks and len(marks) == 3:
            students[roll] = {
                "Name": name,
                "Branch": branch,
                "Semester": semester,
                "Marks": marks
            }

            print(
                f"Student '{name}' "
                f"(Roll No: {roll}) registered successfully."
            )
        else:
            print("Student registration cancelled.")

    
    elif choice == "4":
        roll = input("Enter Roll Number to update: ")

        if roll in students:
            student = students[roll]

            print(f"Current details for {student['Name']}:")
            print("1. Branch:", student["Branch"])
            print("2. Semester:", student["Semester"])

            field = input(
                "Choose field to update "
                "(1 for Branch, 2 for Semester): "
            )

            if field == "1":
                new_branch = input("Enter new Branch: ")

                if new_branch.strip():
                    student["Branch"] = new_branch
                    print(" Branch updated successfully.")
                else:
                    print(" Branch cannot be empty.")

            elif field == "2":
                semester_input = input("Enter new Semester: ")

                if semester_input.isdigit():
                    semester = int(semester_input)

                    if semester >= 1:
                        student["Semester"] = semester
                        print(
                            "Semester updated successfully."
                        )
                    else:
                        print(" Semester must be at least 1.")
                else:
                    print(" Enter a valid numeric semester.")

            else:
                print(" Invalid field choice.")

        else:
            print(" Student not found.")

    
    elif choice == "5":
        roll = input("Enter Roll Number for Academic Performance: ")

        if roll in students:
            student = students[roll]
            marks = student["Marks"]

            total = sum(marks)
            average = total / len(marks)

            print("========== ACADEMIC REPORT ==========")
            print(f"Student Name : {student['Name']} (Roll: {roll})")
            print(f"Subject Marks: {marks}")
            print(f"Total Marks  : {total} / {len(marks) * 100}")
            print(f"Average Marks: {average:.2f}%")

            if average >= 40:
                print("Final Result : PASS")
            else:
                print("Final Result : FAIL")

            print("=====================================")

        else:
            print(" Student not found.")

    
    elif choice == "6":
        roll = input("Enter Roll Number to delete: ")

        student = students.pop(roll, None)

        if student is not None:
            print(
                f"Record for '{student['Name']}' "
                f"(Roll No: {roll}) deleted successfully."
            )
        else:
            print("Student not found.")

    
    elif choice == "7":
        print("Thank you for using Student Information System,Goodbye!")
        break

    
    else:
        print("Invalid choice.Enter a number from 1 to 7.")