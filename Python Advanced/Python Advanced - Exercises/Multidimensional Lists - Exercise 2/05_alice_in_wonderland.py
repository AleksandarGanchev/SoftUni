def check_valid_index(f_index, s_index):
    if 0 <= f_index < n and 0 <= s_index < n:
        return True


n = int(input())

collected_tea = 0
matrix = []
alice_pos = ()
for row in range(n):
    matrix.append(input().split())
    if "A" in matrix[row]:
        alice_pos = row, matrix[row].index("A")
        matrix[row][alice_pos[1]] = "*"

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

command = input()
while collected_tea < 10:
    r, c = directions[command][0] + alice_pos[0], directions[command][1] + alice_pos[1]

    if not check_valid_index(r, c):
        print("Alice didn't make it to the tea party.")
        break

    alice_pos = r, c
    if matrix[alice_pos[0]][alice_pos[1]] == "R":
        matrix[alice_pos[0]][alice_pos[1]] = "*"
        print("Alice didn't make it to the tea party.")
        break


    if matrix[alice_pos[0]][alice_pos[1]].isdigit():
        collected_tea += int(matrix[alice_pos[0]][alice_pos[1]])

    matrix[r][c] = "*"

    if collected_tea >= 10:
        break

    command = input()

if collected_tea >= 10:
    print("She did it! She went to the party.")

[print(*i) for i in matrix]
