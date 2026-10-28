
def calculate_total(marks):
    return sum(marks)


def calculate_percentage(marks):
    total = calculate_total(marks)
    return total / len(marks)


def calculate_grade(percentage):
    if percentage >= 90:
        return "A Grade"
    elif percentage >= 75:
        return "B Grade"
    elif percentage >= 60:
        return "C Grade"
    elif percentage >= 35:
        return "Pass"
    else:
        return "Fail"


def display_result(name, marks):
    total = calculate_total(marks)
    percentage = calculate_percentage(marks)
    grade = calculate_grade(percentage)

    print("\n--- Student Result ---")
    print("Name:", name)
    print("Marks:", marks)
    print("Total:", total, "/ 500")
    print("Percentage:", percentage, "%")
    print("Grade:", grade)


name = input("Enter student name: ")

marks = []
for i in range(1, 6):
    mark = int(input(f"Enter marks for subject {i} (0-100): "))
    if mark < 0 or mark > 100:
        print("Invalid marks! Enter a value from 0 to 100.")
        exit()
    marks.append(mark)

display_result(name, marks)
