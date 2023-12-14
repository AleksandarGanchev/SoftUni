nfs = {}

n = int(input())
for _ in range(n):
    command = input().split("|")
    car, mileage, starting_fuel = command
    mileage = int(mileage)
    starting_fuel  = int(starting_fuel)
    nfs[car] = [mileage, starting_fuel]

data = input()
while data != 'Stop':
    data = data.split(" : ")
    if data[0] == 'Drive':
        drive, car, distance, fuel = data
        distance = int(distance)
        fuel = int(fuel)
        if nfs[car][1] < fuel:
            print("Not enough fuel to make that ride")

        if nfs[car][1] >= fuel:
            nfs[car][1] -= fuel
            nfs[car][0] += distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

        if nfs[car][0]  >= 100000:
            del nfs[car]
            print(f"Time to sell the {car}!")

    elif data[0] == 'Refuel':
        refuel, car, fuel = data
        fuel = int(fuel)
        if nfs[car][1] + fuel >= 75:
            print(f"{car} refueled with {75-nfs[car][1]} liters")
            nfs[car][1] = 75
        else:
            nfs[car][1] += fuel
            print(f"{car} refueled with {fuel} liters")

    elif data[0] == 'Revert':
        revert, car, kilometers = data
        kilometers = int(kilometers)
        nfs[car][0] -= kilometers

        if nfs[car][0] < 10000:
            nfs[car][0] = 10000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")

    data = input()

for k, v in nfs.items():
    print(f"{k} -> Mileage: {v[0]} kms, Fuel in the tank: {v[1]} lt.")