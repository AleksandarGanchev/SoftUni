from collections import deque

truck_tour = deque()
n_petrol_pumps = int(input())

pump_stops = 0
starting_index = 0
for _ in range(n_petrol_pumps):
    petrol_amount, distance = input().split()
    truck_tour.append([int(petrol_amount), int(distance)])

while pump_stops < n_petrol_pumps:
    petrol_in_tank = 0

    for i in range(n_petrol_pumps):
        added_petrol = truck_tour[i][0]
        travel_distance = truck_tour[i][1]
        petrol_in_tank += added_petrol

        if petrol_in_tank < added_petrol:
            starting_index += 1
            pump_stops = 0
            truck_tour.rotate(-1)
            break

        petrol_in_tank -= travel_distance
        pump_stops += 1


print(starting_index)
