n = int(input())
racing_number = input()
matrix = [input().split() for _ in range(n)]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

distance_covered = 0
car_row, car_col = [0, 0]

command = input()
while command != "End":
    car_row += directions[command][0]
    car_col += directions[command][1]

    if matrix[car_row][car_col] == 'T':
        matrix[car_row][car_col] = '.'
        for row in range(n):
            if 'T' in matrix[row]:
                car_row = row
                car_col = matrix[row].index('T')
                matrix[car_row][car_col] = '.'
                distance_covered += 30

    else:
        distance_covered += 10
        if matrix[car_row][car_col] == 'F':
            matrix[car_row][car_col] = 'C'
            print(f"Racing car {racing_number} finished the stage!")
            break

    command = input()

else:
    matrix[car_row][car_col] = 'C'
    print(f"Racing car {racing_number} DNF.")

print(f"Distance covered {distance_covered} km.")
[(print(''.join(i))) for i in matrix]
