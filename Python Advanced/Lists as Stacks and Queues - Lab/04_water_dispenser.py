from collections import deque

water_dispenser = int(input())
queue = deque([])
name = input()
while name != "Start":
    queue.append(name)
    name = input()

data = input()
while data != "End":
    data = data.split()
    if len(data) == 1:
        wanted_water = int(data[0])
        if water_dispenser >= wanted_water:
            print(f"{queue.popleft()} got water")
            water_dispenser -= wanted_water
        else:
            print(f"{queue.popleft()} must wait")

    elif len(data) == 2:
        refill, top_up_water = data
        water_dispenser += int(top_up_water)

    data = input()

print(f"{water_dispenser} liters left")
