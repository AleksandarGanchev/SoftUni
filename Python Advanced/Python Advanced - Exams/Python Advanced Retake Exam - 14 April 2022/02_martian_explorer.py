def swap_index(r, c):
    if r < 0:
        r = 5
    elif r > 5:
        r = 0

    if c < 0:
        c = 5
    elif c > 5:
        c = 0

    return [r, c]


field = []
e_row, e_col = [0, 0]
for row in range(6):
    field.append(input().split())
    if 'E' in field[row]:
        e_row = row
        e_col = field[row].index('E')

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

deposits = []
commands = input().split(', ')
for command in commands:
    e_row += directions[command][0]
    e_col += directions[command][1]

    e_row, e_col = swap_index(e_row, e_col)

    if field[e_row][e_col] == 'R':
        print(f"Rover got broken at ({e_row}, {e_col})")
        break

    elif field[e_row][e_col] == 'W':
        print(f"Water deposit found at {(e_row, e_col)}")
        if "water" not in deposits:
            deposits.append("water")
    elif field[e_row][e_col] == 'M':
        print(f"Metal deposit found at {(e_row, e_col)}")
        if "metal" not in deposits:
            deposits.append("metal")
    elif field[e_row][e_col] == 'C':
        print(f"Concrete deposit found at {(e_row, e_col)}")
        if "concrete" not in deposits:
            deposits.append("concrete")

if len(deposits) == 3:
    print("Area suitable to start the colony.")
else:
    print(f"Area not suitable to start the colony.")
