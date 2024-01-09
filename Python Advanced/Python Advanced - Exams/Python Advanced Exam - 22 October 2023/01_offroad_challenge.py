from collections import deque

initial_fuel = deque(int(x) for x in input().split())
additional_consumption = deque(int(x) for x in input().split())
fuel_needed = deque(int(x) for x in input().split())

altitude = 0
reached_all = True
while initial_fuel:
    last_quantity = initial_fuel.pop()
    first_consumption = additional_consumption.popleft()

    if last_quantity - first_consumption >= fuel_needed.popleft():
        altitude += 1
        print(f"John has reached: Altitude {altitude}")
    else:
        print(f"John did not reach: Altitude {altitude + 1}")
        reached_all = False
        break

if reached_all:
    print("John has reached all the altitudes and managed to reach the top!")
else:
    print("John failed to reach the top.")
    if altitude < 1:
        print("John didn't reach any altitude.")
    else:
        result = []
        for index in range(1, altitude + 1):
            result.append(f"Altitude {index}")
        print(f"Reached altitudes: {', '.join(result)}")
