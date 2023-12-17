student_academy = {}

n = int(input())
for _ in range(n):
    student = input()
    grade = float(input())

    if student not in student_academy:
        student_academy[student] = [grade]
    else:
        student_academy[student].append(grade)


for student, grades in student_academy.items():
    average_grade = sum(grades) / len(grades)
    if average_grade >= 4.50:
        print(f"{student} -> {average_grade:.2f}")
