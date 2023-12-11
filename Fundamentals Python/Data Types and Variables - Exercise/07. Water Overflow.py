tank_capacity = 255
avaiable_place = 0
n = int(input())

for i in range(n):
    added_water = int(input())
    if added_water <= tank_capacity:
        tank_capacity -= added_water
        avaiable_place += added_water
    else:
        print('Insufficient capacity!')

print(avaiable_place)
