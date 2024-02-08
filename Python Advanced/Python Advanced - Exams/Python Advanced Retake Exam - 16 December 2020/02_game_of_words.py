def inside_field(r, c):
    if 0 <= r < SIZE and 0 <= c < SIZE:
        return True


string = input()
SIZE = int(input())

p_row, p_col = [0, 0]
field = []
for row in range(SIZE):
    field.append(list(input()))
    if 'P' in field[row]:
        p_row, p_col = row, field[row].index('P')
        field[p_row][p_col] = '-'

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

move_row, move_col = p_row, p_col
n = int(input())
for _ in range(n):
    command = input()
    move_row, move_col = move_row + directions[command][0], move_col + directions[command][1]
    if inside_field(move_row, move_col):
        p_row, p_col = move_row, move_col
        if field[move_row][move_col].isalpha():
            string += field[move_row][move_col]
            field[move_row][move_col] = "-"
    else:
        move_row, move_col = p_row, p_col
        if len(string):
            string = string[:-1]

field[p_row][p_col] = 'P'

print(string)
[print(''.join(i)) for i in field]
