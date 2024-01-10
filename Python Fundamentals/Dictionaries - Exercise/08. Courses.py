courses = {}

command = input()
while command != "end":
    course_name, student_name = command.split(" : ")
    if course_name not in courses:
        courses[course_name] = [student_name]
    else:
        courses[course_name].append(student_name)

    command = input()

for course_name, students in courses.items():
    print(f"{course_name}: {len(students)}")
    for student in students:
        print(f"-- {student}")
