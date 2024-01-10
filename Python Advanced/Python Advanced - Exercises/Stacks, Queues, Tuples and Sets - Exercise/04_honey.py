from collections import deque

working_bees = deque(int(x) for x in input().split())
nectar = deque(int(x) for x in input().split())
symbols = deque(input().split())

total_honey = 0
while working_bees and nectar:
    first_bee = working_bees.popleft()
    last_nectar = nectar.pop()

    if first_bee > last_nectar:
        working_bees.appendleft(first_bee)
        continue

    symbol = symbols.popleft()

    if symbol == "+":
        total_honey += abs(first_bee + last_nectar)
    elif symbol == "-":
        total_honey += abs(first_bee - last_nectar)
    elif symbol == "*":
        total_honey += abs(first_bee * last_nectar)
    elif symbol == "/":
        if last_nectar == 0:
            continue
        total_honey += abs(first_bee / last_nectar)

print(f"Total honey made: {total_honey}")

if working_bees:
    print("Bees left:", end=" ")
    print(*working_bees, sep=", ")

elif nectar:
    print("Nectar left:", end=" ")
    print(*nectar, sep=", ")
