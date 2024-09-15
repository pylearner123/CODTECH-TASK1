def calculate_average(grades):
    return sum(grades) / len(grades)

def calculate_letter_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    else:
        return 'F'

def calculate_gpa(average):
    if average >= 90:
        return 4.0
    elif average >= 80:
        return 3.0
    elif average >= 70:
        return 2.0
    elif average >= 60:
        return 1.0
    else:
        return 0.0

def main():
    grades = []
    
    while True:
        subject = input("Enter the subject (or 'done' to finish): ")
        if subject.lower() == 'done':
            break
        try:
            grade = float(input(f"Enter the grade for {subject}: "))
            grades.append(grade)
        except ValueError:
            print("Invalid input. Please enter a numeric value for the grade.")
    
    if not grades:
        print("No grades were entered.")
        return
    
    average = calculate_average(grades)
    letter_grade = calculate_letter_grade(average)
    gpa = calculate_gpa(average)
    
    print("\n--- Grade Report ---")
    print(f"Average Grade: {average:.2f}")
    print(f"Letter Grade: {letter_grade}")
    print(f"GPA: {gpa:.2f}")

if __name__ == "__main__":
    main()