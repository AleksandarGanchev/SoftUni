from collections import deque

times = deque(int(x) for x in input().split())
tasks = deque(int(x) for x in input().split())

rubber_ducks = {
    "Darth Vader Ducky": 0,
    "Thor Ducky": 0,
    "Big Blue Rubber Ducky": 0,
    "Small Yellow Rubber Ducky": 0
}

while times and len(tasks) > 0:
    programmer_time = times.popleft()
    task = tasks.pop()

    result = programmer_time * task

    if 0 <= result <= 60:
        rubber_ducks["Darth Vader Ducky"] += 1
    elif 61 <= result <= 120:
        rubber_ducks["Thor Ducky"] += 1
    elif 121 <= result <= 181:
        rubber_ducks["Big Blue Rubber Ducky"] += 1
    elif 181 <= result <= 240:
        rubber_ducks["Small Yellow Rubber Ducky"] += 1
    else:
        tasks.append(task-2)
        times.append(programmer_time)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded: ")
for duck, count in rubber_ducks.items():
    print(f"{duck}: {count}")
