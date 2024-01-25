def valid_index(c_row, c_col):
    if 0 <= c_row < i and 0 <= c_col < j:
        return True


def is_obstacle(matrix, row_idx, col_idx):
    if not matrix[row_idx][col_idx] == "O":
        return True


i, j = [int(x) for x in input().split()]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

moves_made = 0
touched_opponents = 0
b_pos = []
playground = []
for row in range(i):
    playground.append(input().split())
    if 'B' in playground[row]:
        b_pos = [row, playground[row].index('B')]
        playground[row][b_pos[1]] = '-'


command = input()
while command != "Finish":
    r, c = b_pos[0] + directions[command][0], b_pos[1] + directions[command][1]
    if valid_index(r, c) and is_obstacle(playground, r, c):
        b_pos[0], b_pos[1] = r, c
        if playground[r][c] == "-":
            moves_made += 1

        elif playground[r][c] == "P":
            playground[r][c] = "-"
            touched_opponents += 1
            moves_made += 1
            if touched_opponents == 3:
                break

    else:
        r, c = b_pos[0], b_pos[1]

    command = input()

print("Game over!")
print(f"Touched opponents: {touched_opponents} Moves made: {moves_made}")

