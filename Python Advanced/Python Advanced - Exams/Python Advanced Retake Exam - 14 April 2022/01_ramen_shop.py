from collections import deque

ramen_bows = list(map(int, input().split(", ")))
customers = deque(int(x) for x in input().split(", "))

while ramen_bows and customers:
    bow = ramen_bows.pop()
    customer = customers.popleft()

    if bow == customer:
        continue

    if bow > customer:
        bow -= customer
        ramen_bows.append(bow)

    elif customer > bow:
        customer -= bow
        customers.appendleft(customer)


if customers:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join([str(x) for x in customers])}")
else:
    print("Great job! You served all the customers.")
    if ramen_bows:
        print(f"Bowls of ramen left: {', '.join([str(x) for x in ramen_bows])}")
