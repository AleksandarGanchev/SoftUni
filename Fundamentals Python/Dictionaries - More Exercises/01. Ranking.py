ranking = {}
results = {}

command = input()
while command != "end of contests":
    command = command.split(':')
    contest, contest_password = command
    ranking[contest] = contest_password
    command = input()

data = input()
while data != "end of submissions":
    s_contest, password, username, points = data.split('=>')
    points = int(points)

    if s_contest in ranking:
        if ranking[s_contest] == password:
            if username not in results:
                results[username] = {s_contest: points}
            else:
                if s_contest in results[username]:
                    if points > results[username][s_contest]:
                        results[username][s_contest] = points
                else:
                    results[username][s_contest] = points

    data = input()

best_points = 0

for username, info in results.items():
    current_points = 0

    for course, points in info.items():
        current_points += points
        if current_points > best_points:
            best_points = current_points
            best = f"Best candidate is {username} with total {best_points} points."


results = dict(sorted(results.items()))
print(best)
for username, contests in results.items():
    results[username] = dict(sorted(contests.items(), key=lambda item: item[1], reverse=True))
print("Ranking:")
for username, contests in results.items():
    print(f"{username}")
    for contest, points in contests.items():
        print(f"#  {contest} -> {points}")
