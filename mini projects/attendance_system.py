
students = {}

def add_student():
    roll_no = input("Enter roll number: ")
    name = input("Enter student name: ")

    if roll_no in students:
        print("Student already exists!")
        return

    students[roll_no] = {
        "name": name,
        "present": 0,
        "absent": 0
    }

    print("Student added successfully!")


def mark_attendance():
    roll_no = input("Enter roll number: ")

    if roll_no not in students:
        print("Student not found!")
        return

    status = input("Enter P for Present or A for Absent: ").upper()

    if status == "P":
        students[roll_no]["present"] += 1
        print("Marked Present!")
    elif status == "A":
        students[roll_no]["absent"] += 1
        print("Marked Absent!")
    else:
        print("Invalid attendance status!")


def display_attendance():
    if not students:
        print("No students registered.")
        return

    print("\n--- ATTENDANCE RECORDS ---")

    for roll_no, details in students.items():
        total = details["present"] + details["absent"]

        print("\nRoll Number:", roll_no)
        print("Name:", details["name"])
        print("Present:", details["present"])
        print("Absent:", details["absent"])

        if total > 0:
            percentage = (details["present"] / total) * 100
            print("Attendance:", round(percentage, 2), "%")
        else:
            print("Attendance: No records yet")


def low_attendance():
    print("\n--- STUDENTS BELOW 75% ---")

    found = False

    for roll_no, details in students.items():
        total = details["present"] + details["absent"]

        if total > 0:
            percentage = (details["present"] / total) * 100

            if percentage < 75:
                print(details["name"], "-", round(percentage, 2), "%")
                found = True

    if not found:
        print("No students below 75%.")


def main():
    while True:
        print("\n===== STUDENT ATTENDANCE SYSTEM =====")
        print("1. Add Student")
        print("2. Mark Attendance")
        print("3. Display Attendance")
        print("4. Check Low Attendance")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            mark_attendance()
        elif choice == "3":
            display_attendance()
        elif choice == "4":
            low_attendance()
        elif choice == "5":
            print("Thank you!")
            break
        else:
            print("Invalid choice!")


main()
