matrix = []
for row in range(6):
    matrix.append(input().split())

data = input()
row_pos = int(data[1])
col_pos = int(data[4])

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

command = input()
while command != "Stop":
    command_args = command.split(', ')
    if len(command_args) == 3:
        operation, direction, value = command_args
        row_pos += directions[direction][0]
        col_pos += directions[direction][1]
        if operation == "Create":
            if matrix[row_pos][col_pos] == '.':
                matrix[row_pos][col_pos] = value
        elif operation == "Update":
            if matrix[row_pos][col_pos] != '.':
                matrix[row_pos][col_pos] = value

    elif len(command_args) == 2:
        operation, direction = command_args
        row_pos += directions[direction][0]
        col_pos += directions[direction][1]
        if operation == "Delete":
            if matrix[row_pos][col_pos] != '.':
                matrix[row_pos][col_pos] = '.'
        elif operation == "Read":
            if matrix[row_pos][col_pos] != '.':
                print(matrix[row_pos][col_pos])

    command = input()

[print(' '.join(i)) for i in matrix]
