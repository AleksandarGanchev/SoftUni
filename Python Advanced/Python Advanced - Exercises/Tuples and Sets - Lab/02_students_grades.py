students_number = int(input())

students_grades = {}
for _ in range(students_number):
    student_name, grade = input().split()
    if student_name not in students_grades:
        students_grades[student_name] = []
    students_grades[student_name].append(float(grade))

for student, grades in students_grades.items():
    average = sum(grades) / len(grades)
    print(f"{student} -> {' '.join([str(f'{grade:.2f}')for grade in grades])}"
          f" (avg: {average:.2f})")
