bad_grades_count = int(input())
failures_count = 0
total_grades = 0
task_count = 0
grades_count = 0

while bad_grades_count > failures_count:
    task_name = input()
    if task_name == 'Enough':
        print(f"Average score: {average_grades:.2f}")
        print(f"Number of problems: {task_count}")
        print(f"Last problem: {last_task}")
        break
    grade = int(input())
    if grade <= 4:
        failures_count += 1
    total_grades += grade
    task_count += 1
    grades_count += 1
    average_grades = total_grades / grades_count
    last_task = task_name

else:
    print(f"You need a break, {failures_count} poor grades.")