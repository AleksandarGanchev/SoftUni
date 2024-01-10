n = int(input())

parking_lot = set()

for _ in range(n):
    action, car_number = input().split(", ")
    if action == "IN":
        parking_lot.add(car_number)

    elif action == "OUT":
        parking_lot.remove(car_number)

if parking_lot:
    print(*parking_lot, sep="\n")
else:
    print("Parking Lot is Empty")
