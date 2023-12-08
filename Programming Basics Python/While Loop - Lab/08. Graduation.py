student_name = input()
failures = 0
total_grades = 0
years_count = 0
average_grades = 0
grades_count = 0

while failures < 2:
    grade = float(input())
    if grade < 4:
        failures += 1
        if failures == 1:
            years_count += 1
    if grade >= 4:
        grades_count += 1
        total_grades += grade
        average_grades = total_grades / grades_count
        years_count += 1
    if years_count == 12:
        print(f"{student_name} graduated. Average grade: {average_grades:.2f}")
        break

if failures == 2:
    print(f"{student_name} has been excluded at {years_count} grade")