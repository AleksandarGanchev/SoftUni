from sys import maxsize
from math import ceil

students_count = int(input())
lectures_count = int(input())
additional_bonus = int(input())

max_bonus = 0
best_attendance = 0
for index in range(1, students_count+1):
    attendance = int(input())
    total_bonus = attendance / lectures_count * (5 + additional_bonus)
    if total_bonus > max_bonus:
        max_bonus = total_bonus
        best_attendance = attendance

print(f"Max Bonus: {ceil(max_bonus)}.")
print(f"The student has attended {best_attendance} lectures.")