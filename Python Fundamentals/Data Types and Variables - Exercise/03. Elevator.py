people_count = int(input())
elevator_capacity = int(input())

full_courses = people_count // elevator_capacity

if people_count > full_courses * elevator_capacity:
    full_courses += 1
    print(full_courses)
else:
    print(full_courses)

