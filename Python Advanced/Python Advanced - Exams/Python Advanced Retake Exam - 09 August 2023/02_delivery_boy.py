def valid_index(rol, col):
    if 0 <= rol < rows and 0 <= col < cols:
        return True

    return False


rows, cols = [int(x) for x in input().split()]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
    }

field = []
b_pos = []
starting_pos = []
for row in range(rows):
    field.append(list(input()))
    if 'B' in field[row]:
        b_pos = [row, field[row].index('B')]
        starting_pos = [row, field[row].index('B')]

while True:
    command = input()
    r, c = b_pos[0] + directions[command][0], b_pos[1] + directions[command][1]
    if valid_index(r, c):

        if field[r][c] == '*':
            r, c = b_pos[0], b_pos[1]
            continue

        if field[r][c] == 'P':
            print("Pizza is collected. 10 minutes for delivery.")
            field[r][c] = 'R'
        elif field[r][c] == 'A':
            print("Pizza is delivered on time! Next order...")
            field[r][c] = 'P'
            [print(''.join(x)) for x in field]
            break
        elif field[r][c] == "-":
            field[r][c] = '.'

        b_pos[0], b_pos[1] = [r, c]

    else:
        field[starting_pos[0]][starting_pos[1]] = " "
        print("The delivery is late. Order is canceled.")
        [print(''.join(x)) for x in field]
        break
