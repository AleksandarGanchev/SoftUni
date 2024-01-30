n = int(input())
battlefield = []
blown_mines = 0
cruisers = 3
s_row, s_col = [0, 0]
for row in range(n):
    battlefield.append(list(input()))
    if 'S' in battlefield[row]:
        s_row, s_col = [row, battlefield[row].index('S')]
        battlefield[s_row][s_col] = '-'

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

command = input()
while True:
    s_row, s_col = s_row + directions[command][0], s_col + directions[command][1]
    if battlefield[s_row][s_col] == 'C':
        cruisers -= 1
        battlefield[s_row][s_col] = '-'
        if cruisers == 0:
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            break

    elif battlefield[s_row][s_col] == '*':
        blown_mines += 1
        battlefield[s_row][s_col] = '-'
        if blown_mines == 3:
            print(f"Mission failed, U-9 disappeared! Last known coordinates [{s_row}, {s_col}]!")
            break

    command = input()

battlefield[s_row][s_col] = 'S'
[print(''.join(i)) for i in battlefield]
