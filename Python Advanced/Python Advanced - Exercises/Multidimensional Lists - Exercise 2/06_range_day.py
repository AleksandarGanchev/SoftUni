def check_move(move_direction, curr_step):
    r = directions[move_direction][0] * curr_step + shooter_pos[0]
    c = directions[move_direction][1] * curr_step + shooter_pos[1]

    if 0 <= r < len(matrix) and 0 <= c < len(matrix) and matrix[r][c] != "x":
        return [r, c]

    return shooter_pos


def shoot(shoot_direction):
    r = shooter_pos[0] + directions[shoot_direction][0]
    c = shooter_pos[1] + directions[shoot_direction][1]

    while 0 <= r < len(matrix) and 0 <= c < len(matrix):
        if matrix[r][c] == "x":
            matrix[r][c] = "."
            return [r, c]

        r += directions[shoot_direction][0]
        c += directions[shoot_direction][1]


directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

matrix = []
shot_targets = 0
total_targets = 0
shooter_pos = ()
down_targets = []
for row in range(5):
    matrix.append(input().split())
    if "A" in matrix[row]:
        shooter_pos = row, matrix[row].index("A")
    total_targets += matrix[row].count("x")

n = int(input())
for _ in range(n):
    command = input().split()
    if command[0] == "move":
        move, direction, steps = command[0], command[1], int(command[2])
        shooter_pos = check_move(direction, steps)
    elif command[0] == "shoot":
        target_down = shoot(command[1])
        if target_down:
            shot_targets += 1
            down_targets.append(target_down)

        if shot_targets == total_targets:
            print(f"Training completed! All {total_targets} targets hit.")
            break

else:
    print(f"Training not completed! {total_targets - shot_targets} targets left.")

[print(i) for i in down_targets]


