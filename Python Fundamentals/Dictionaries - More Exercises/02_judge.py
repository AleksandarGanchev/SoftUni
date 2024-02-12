command = input()
judge, individual = {}, {}

while command != 'no more time':
    username, contest, points = [int(x) if x.isdigit() else x for x in command.split(' -> ')]

    if contest not in judge:
        judge[contest] = {username: points}
    elif username not in judge[contest]:
        judge[contest][username] = points
    elif points > judge[contest][username]:
        judge[contest][username] = points
    command = input()

for course, data in judge.items():
    print(f"{course}: {len(data)} participants")
    sorted_by_points = dict(sorted(data.items(), key=lambda x: (-x[1], x[0])))
    for rank, (name, total_points) in enumerate(sorted_by_points.items()):
        print(f"{rank+1}. {name} <::> {total_points}")

print("Individual standings:")
for course, info in judge.items():
    for name, points in info.items():
        if name not in individual:
            individual[name] = points
        else:
            individual[name] += points

sorted_by_points = dict(sorted(individual.items(), key=lambda x: (-x[1], x[0])))
for rank, (username, total_points) in enumerate(sorted_by_points.items()):
    print(f"{rank+1}. {username} -> {total_points}")
