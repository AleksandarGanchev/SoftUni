parking_lot = {}

n = int(input())
for _ in range(n):
    action, *data = input().split()
    if action == "register":
        username, license_plate_number = data
        if username in parking_lot:
            print(f"ERROR: already registered with plate number {license_plate_number}")
        else:
            parking_lot[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")

    elif action == "unregister":
        username = data[0]
        if username not in parking_lot:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del parking_lot[username]


for username, license_plate_number in parking_lot.items():
    print(f"{username} => {license_plate_number}")
