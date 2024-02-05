from math import floor


def traverse(r, c, matrix):
    matrix_size = len(matrix) - 1

    if r < 0:
        r = matrix_size
    elif r > matrix_size:
        r = 0

    if c < 0:
        c = matrix_size
    elif c > matrix_size:
        c = 0

    return r, c


SIZE = int(input())

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

result = []
collected_coins = 0
p_row, p_col = [0, 0]
field = []
for row in range(SIZE):
    field.append([int(x) if x.isdigit() else x for x in input().split()])
    if 'P' in field[row]:

        p_row, p_col = row, field[row].index('P')
        result.append([p_row, p_col])
        field[p_row][p_col] = 0


while True:
    direction = input()
    p_row, p_col = p_row + directions[direction][0], p_col + directions[direction][1]
    p_row, p_col = traverse(p_row, p_col, field)
    if field[p_row][p_col] == 'X':
        if collected_coins > 0:
            collected_coins = floor((collected_coins / 2))

        result.append([p_row, p_col])
        break

    else:
        collected_coins += field[p_row][p_col]
        field[p_row][p_col] = 0

    result.append([p_row, p_col])
    if collected_coins >= 100:
        break

if collected_coins < 100:
    print(f"Game over! You've collected {collected_coins} coins.")
else:
    print(f"You won! You've collected {collected_coins} coins.")

print("Your path:")
for output in result:
    print(output)
