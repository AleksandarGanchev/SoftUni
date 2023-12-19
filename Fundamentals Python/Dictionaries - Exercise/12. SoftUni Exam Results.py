exam_results = {}
submissions = {}

command = input()
while command != "exam finished":
    command = command.split("-")
    if len(command) == 3:
        username, language, points = command
        points = int(points)
        if username not in exam_results:
            exam_results[username] = {language: points}
        elif language not in exam_results[username]:
            exam_results[username][language] = points
        else:
            if points > exam_results[username][language]:
                exam_results[username][language] = points

        if language not in submissions:
            submissions[language] = [username]
        else:
            submissions[language].append(username)

    elif len(command) == 2:
        username, banned = command
        if username in exam_results:
            del exam_results[username]

    command = input()

print("Results:")
for key,values in exam_results.items():
    for course_name, points in values.items():
        print(f"{key} | {points}")

print("Submissions:")
for course_name, users_count in submissions.items():
    print(f"{course_name} - {len(users_count)}")
