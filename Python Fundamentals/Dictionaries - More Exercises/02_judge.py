command = input()
judge = {}
individual_standings = {}
while command != 'no more time':
    username, contest, points = command.split(' -> ')
    points = int(points)

    if contest not in judge:
        judge[contest] = {username: points}
    else:
        if username not in judge[contest]:
            judge[contest][username] = points
        else:
            if points > judge[contest][username]:
                judge[contest][username] = points

    if username not in individual_standings:
        individual_standings[username] = {contest: points}
    else:
        if contest in individual_standings[username]:
            if points > individual_standings[username][contest]:
                individual_standings[username][contest] = points
        else:
            individual_standings[username][contest] = points
    command = input()

for contest_name, participants in judge.items():
    print(f"{contest_name}: {len(participants)} participants")
    if len(participants) > 0:
        sorted_participants = sorted(participants.items(), key=lambda x: (-x[1], x[0]))
        counter = 1
        for name, points in sorted_participants:
            print(f"{counter}. {name} <::> {points}")
            counter += 1

new_dict = {}
for test_name, course in individual_standings.items():
    for key, value in course.items():
        if test_name not in new_dict:
            new_dict[test_name] = value
        else:
            new_dict[test_name] += value

output = dict(sorted(new_dict.items(), key=lambda x: (-x[1], x[0])))

print("Individual standings:")
for index, (name, points) in enumerate(output.items()):
    print(f"{index+1}. {name} -> {points}")
