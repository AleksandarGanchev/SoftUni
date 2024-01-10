employee1 = int(input())
employee2 = int(input())
employee3 = int(input())
students_count = int(input())
hours = 0

while students_count > 0:
    hours += 1
    if hours % 4 == 0:
        hours += 1

    students_count -= employee1
    if students_count > 0:
        students_count -= employee2
    if students_count > 0:
        students_count -= employee3


print(f"Time needed: {hours}h.")