size = int(input())

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
    }

ship = []
caught_fish = 0
s_pos = []
for row in range(size):
    ship.append(list(input()))
    if 'S' in ship[row]:
        s_pos = [row, ship[row].index('S')]
        ship[s_pos[0]][s_pos[1]] = "-"

no_whirlpool = True
command = input()
while command != "collect the nets":
    s_pos[0], s_pos[1] = directions[command][0] + s_pos[0], directions[command][1] + s_pos[1]

    if 0 <= s_pos[0] < size and 0 <= s_pos[1] < size:

        if ship[s_pos[0]][s_pos[1]] == 'W':
            caught_fish = 0
            print(f"You fell into a whirlpool! The ship sank and you lost the fish you caught. Last coordinates of the ship: [{s_pos[0]},{s_pos[1]}]")
            no_whirlpool = False
            break

        if ship[s_pos[0]][s_pos[1]].isdigit():
            caught_fish += int(ship[s_pos[0]][s_pos[1]])
            ship[s_pos[0]][s_pos[1]] = "-"

    else:
        if command == "right":
            s_pos[1] = 0

        elif command == "left":
            s_pos[1] = size - 1

        elif command == "up":
            s_pos[0] = size - 1

        elif command == "down":
            s_pos[0] = 0

        if ship[s_pos[0]][s_pos[1]] == 'W':
            caught_fish = 0
            print(f"You fell into a whirlpool! The ship sank"
                  f" and you lost the fish you caught. "
                  f"Last coordinates of the ship: {s_pos[0], s_pos[1]}")
            break

        if ship[s_pos[0]][s_pos[1]].isdigit():
            caught_fish += int(ship[s_pos[0]][s_pos[1]])
            ship[s_pos[0]][s_pos[1]] = "-"

    command = input()

else:
    if caught_fish >= 20:
        print("Success! You managed to reach the quota!")
    else:
        print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - caught_fish} tons of fish more.")
if caught_fish > 0:
    print(f"Amount of fish caught: {caught_fish} tons.")
    ship[s_pos[0]][s_pos[1]] = "S"

if no_whirlpool:
    ship[s_pos[0]][s_pos[1]] = "S"
    for i in ship:
        print(''.join(i))
