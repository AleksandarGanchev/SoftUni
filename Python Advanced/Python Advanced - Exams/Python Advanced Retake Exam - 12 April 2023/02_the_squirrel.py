def valid_index(r, c):
    if 0 <= r < size and 0 <= c < size:
        return True


size = int(input())
commands = input().split(", ")

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
s_pos = []
field = []
for row in range(size):
    field.append(list(input()))
    if "s" in field[row]:
        s_pos = [row, field[row].index('s')]


collected_hazelnuts = 0
for command in commands:
    s_pos[0] = s_pos[0] + directions[command][0]
    s_pos[1] = s_pos[1] + directions[command][1]

    if valid_index(s_pos[0], s_pos[1]):
        if field[s_pos[0]][s_pos[1]] == 't':
            print("Unfortunately, the squirrel stepped on a trap...")
            print(f"Hazelnuts collected: {collected_hazelnuts}")
            break

        elif field[s_pos[0]][s_pos[1]] == 'h':
            collected_hazelnuts += 1
            field[s_pos[0]][s_pos[1]] = "*"
            if collected_hazelnuts == 3:
                print("Good job! You have collected all hazelnuts!")
                print(f"Hazelnuts collected: {collected_hazelnuts}")
                break

    else:
        print("The squirrel is out of the field.")
        print(f"Hazelnuts collected: {collected_hazelnuts}")
        break

else:
    if collected_hazelnuts < 3:
        print("There are more hazelnuts to collect.")
        print(f"Hazelnuts collected: {collected_hazelnuts}")
