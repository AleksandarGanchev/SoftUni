numbers = [float(x) for x in input().split()]
occurrences = {}

for number in numbers:
    if number not in occurrences:
        occurrences[number] = 1
    else:
        occurrences[number] += 1

for number, count in occurrences.items():
    print(f"{number} - {count} times")
