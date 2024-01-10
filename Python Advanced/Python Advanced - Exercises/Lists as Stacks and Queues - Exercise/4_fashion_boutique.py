from collections import deque

integers = deque([int(x) for x in input().split()])
rack_capacity = int(input())

current_rack_capacity = 0
racks_quantity = 0
while integers:
    if len(integers) == 1 and current_rack_capacity + integers[0] <= rack_capacity:
        integers.popleft()
        racks_quantity += 1
    elif current_rack_capacity + integers[0] < rack_capacity:
        current_rack_capacity += integers.popleft()
    elif current_rack_capacity + integers[0] == rack_capacity:
        current_rack_capacity += integers.popleft()
        racks_quantity += 1
        current_rack_capacity = 0
    else:
        racks_quantity += 1
        current_rack_capacity = 0


print(racks_quantity)
