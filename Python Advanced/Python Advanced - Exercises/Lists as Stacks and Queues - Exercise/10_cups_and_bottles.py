from collections import deque


cups_capacity = deque(int(x) for x in input().split())
bottles_capacity = [int(x) for x in input().split()]

wasted_water = 0
while cups_capacity:
    if not bottles_capacity:
        break
    if bottles_capacity[-1] >= cups_capacity[0]:
        wasted_water += (bottles_capacity[-1] - cups_capacity[0])
        cups_capacity.popleft()
        bottles_capacity.pop()
    else:
        cups_capacity[0] -= bottles_capacity[-1]
        bottles_capacity.pop()

if cups_capacity:
    print("Cups: ", end="")
    for cup in cups_capacity:
        print(f"{cup} ", end="")

elif bottles_capacity:
    print("Bottles: ", end="")
    for bottle in bottles_capacity:
        print(f"{bottle} ", end="")

print("\n"f"Wasted litters of water: {wasted_water}")
