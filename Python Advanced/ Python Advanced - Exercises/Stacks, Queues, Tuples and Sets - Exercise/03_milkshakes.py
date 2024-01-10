from collections import deque

chocolate = deque([int(x) for x in input().split(", ")])
cups_of_milk = deque([int(x) for x in input().split(", ")])

milkshakes = 0
while chocolate and cups_of_milk:
    if cups_of_milk[0] <= 0 or chocolate[-1] <= 0:
        if chocolate[-1] <= 0:
            chocolate.pop()
        if cups_of_milk[0] <= 0:
            cups_of_milk.popleft()
        continue

    else:
        if chocolate[-1] == cups_of_milk[0]:
            chocolate.pop()
            cups_of_milk.popleft()
            milkshakes += 1
        else:
            chocolate[-1] -= 5
            cups_of_milk.rotate(-1)

    if milkshakes == 5:
        break

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolate:
    print(f"Chocolate: {', '.join(str(x) for x in chocolate)}")
else:
    print("Chocolate: empty")
if cups_of_milk:
    print(f"Milk: {', '.join(str(x) for x in cups_of_milk)}")
else:
    print("Milk: empty")
