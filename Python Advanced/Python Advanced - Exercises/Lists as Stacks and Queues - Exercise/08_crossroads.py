from collections import deque

green_duration = int(input())
free_window = int(input())
cars = deque()
cars_passed = 0
no_crash = True

command = input()
while command != "END":
    if command != "green":
        cars.append(command)
    elif command == "green":
        current_green = green_duration

        while current_green > 0 and len(cars):
            car = cars.popleft()
            if current_green >= len(car):
                current_green -= len(car)
                cars_passed += 1

            else:
                time = current_green + free_window
                if time >= len(car):
                    cars_passed += 1
                    current_green = 0
                else:
                    print("A crash happened!")
                    print(f"{car} was hit at {car[time]}.")
                    no_crash = False
                    break

    command = input()

if no_crash:
    print("Everyone is safe.")
    print(f"{cars_passed} total cars passed the crossroads.")
