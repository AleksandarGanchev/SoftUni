from collections import deque

males = [int(x) for x in input().split()]
females = deque(int(x) for x in input().split())

matches = 0
while males and females:
    last_male = males.pop()
    if last_male <= 0:
        continue

    last_female = females.popleft()
    if last_female <= 0:
        males.append(last_male)
        continue

    if last_male % 25 == 0 or last_female % 25 == 0:
        if last_male % 25 == 0:
            females.appendleft(last_female)
            males.pop()
        if last_female % 25 == 0:
            males.append(last_male)
            females.popleft()

    elif last_male == last_female:
        matches += 1

    else:
        males.append(last_male-2)

print(f"Matches: {matches}")
if males:
    print(f"Males left: {', '.join([str(x) for x in males[::-1]])}")
else:
    print("Males left: none")

if females:
    print(f"Females left: {', '.join([str(x) for x in females])}")
else:
    print("Females left: none")
