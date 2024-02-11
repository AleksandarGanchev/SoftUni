def check_valid_index(row, col):
    if 0 <= row < SIZE and 0 <= col < SIZE:
        return True


def find_bombs(r, c):
    position_value = 0
    for moving_row, moving_col in directions:
        check_row, check_col = moving_row + r, moving_col + c
        if check_valid_index(check_row, check_col) and field[check_row][check_col] == '*':
            position_value += 1
    field[r][c] = position_value


SIZE = int(input())
num_bombs = int(input())
field = [['0'] * SIZE for x in range(SIZE)]

bomb_row, bomb_col = [0, 0]
for bomb in range(num_bombs):
    bomb_row, bomb_col = [int(x) for x in input()[1:-1].split(', ')]
    field[bomb_row][bomb_col] = '*'

directions = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
    (-1, -1),
    (1, -1),
    (-1, 1),
    (1, 1)
]

for row in range(SIZE):
    for col in range(SIZE):
        if field[row][col] != '*':
            find_bombs(row, col)

[print(" ".join(str(cell) for cell in row)) for row in field]
