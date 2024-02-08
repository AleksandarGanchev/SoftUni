def snake_inside_territory(r, c):
    if 0 <= r < SIZE and 0 <= c < SIZE:
        return True


def find_other_burrow(matrix):
    for b_row in range(SIZE):
        for b_col in range(SIZE):
            if matrix[b_row][b_col] == 'B':
                return b_row, b_col


SIZE = int(input())

territory = []
eaten_food = 0
s_row, s_col = [0, 0]
for row in range(SIZE):
    territory.append(list(input()))
    if 'S' in territory[row]:
        s_row, s_col = row, territory[row].index('S')
        territory[s_row][s_col] = '.'

move_row, move_col = s_row, s_col
while True:
    command = input()
    if command == "up":
        move_row -= 1
    elif command == "down":
        move_row += 1
    elif command == "left":
        move_col -= 1
    elif command == "right":
        move_col += 1

    if not snake_inside_territory(move_row, move_col):
        print("Game over!")
        break

    if territory[move_row][move_col] == '*':
        eaten_food += 1
        if eaten_food == 10:
            territory[move_row][move_col] = 'S'
            print("You won! You fed the snake.")
            break

        territory[move_row][move_col] = '.'

    elif territory[move_row][move_col] == 'B':
        territory[move_row][move_col] = '.'
        move_row, move_col = find_other_burrow(territory)
        territory[move_row][move_col] = '.'

    else:
        territory[move_row][move_col] = "."

    s_row, s_col = move_row, move_col

print(f"Food eaten: {eaten_food}")
[print(''.join(i)) for i in territory]
