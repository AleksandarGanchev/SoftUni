size = int(input())
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

gambler_money = 100
gambler_position = []
matrix = []
for row in range(size):
    matrix.append(list(input()))
    if "G" in matrix[row]:
        gambler_position = [row, matrix[row].index("G")]
        matrix[row][gambler_position[1]] = '-'


command = input()
while command != "end":
    [r, c] = directions[command][0] + gambler_position[0], directions[command][1] + gambler_position[1]

    if 0 <= r < size and 0 <= c < size:
        if matrix[r][c] == 'W':
            gambler_money += 100

        elif matrix[r][c] == 'P':
            gambler_money -= 200
            if gambler_money <= 0:
                print("Game over! You lost everything!")
                break

        elif matrix[r][c] == 'J':
            gambler_money += 100000
            print("You win the Jackpot!"'\n'f"End of the game. Total amount: {gambler_money}$")
            matrix[r][c] = "G"
            for curr_row in matrix:
                print(''.join(curr_row))

            break

    matrix[r][c] = "-"

    if not (0 <= r < size and 0 <= c < size):
        print("Game over! You lost everything!")
        break
    gambler_position[0], gambler_position[1] = [r, c]

    command = input()

else:
    if gambler_money > 0:
        matrix[r][c] = "G"
        print(f"End of the game. Total amount: {gambler_money}$")
        for curr_row in matrix:
            print(''.join(curr_row))
