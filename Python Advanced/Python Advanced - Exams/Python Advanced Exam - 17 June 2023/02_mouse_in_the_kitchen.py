def valid_index(row, col):
    if 0 <= row < rows and 0 <= col < cols:
        return True


rows, cols = [int(x) for x in input().split(",")]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
    }

eaten_cheese = 0
total_cheese = 0
m_pos = []
cupboard = []
for row in range(rows):
    cupboard.append(list(input()))
    if 'M' in cupboard[row]:
        m_pos = [row, cupboard[row].index('M')]
        cupboard[m_pos[0]][m_pos[1]] = "*"
    if 'C' in cupboard[row]:
        total_cheese += cupboard[row].count('C')


command = input()
while command != "danger":
    r, c = directions[command][0] + m_pos[0], directions[command][1] + m_pos[1]
    if valid_index(r, c):
        if cupboard[r][c] == '@':
            r, c = m_pos[0], m_pos[1]
            command = input()
            continue

        elif cupboard[r][c] == 'T':
            cupboard[r][c] = "M"
            print("Mouse is trapped!")
            break

        elif cupboard[r][c] == 'C':
            eaten_cheese += 1
            if eaten_cheese == total_cheese:
                cupboard[r][c] = "M"
                print("Happy mouse! All the cheese is eaten, good night!")
                break
            else:
                cupboard[r][c] = "*"

    else:
        cupboard[m_pos[0]][m_pos[1]] = "M"
        print("No more cheese for tonight!")
        break
    m_pos[0], m_pos[1] = r, c
    command = input()


else:
    if total_cheese > eaten_cheese:
        cupboard[m_pos[0]][m_pos[1]] = "M"
        print("Mouse will come back later!")
[print(''.join(i)) for i in cupboard]
