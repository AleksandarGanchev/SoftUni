chessboard = []
w_row, w_col = [0, 0]
b_row, b_col = [0, 0]

for row in range(8):
    chessboard.append(input().split())
    if 'w' in chessboard[row]:
        w_row, w_col = [row, chessboard[row].index('w')]
    if 'b' in chessboard[row]:
        b_row, b_col = [row, chessboard[row].index('b')]

while True:
    if w_row - 1 == b_row:
        if w_col - 1 == b_col or w_col + 1 == b_col:
            print(f"Game over! White win, capture on {chr(97 + b_col)}{abs(b_row-8)}.")
            break

    w_row -= 1
    if w_row == 0:
        print(f"Game over! White pawn is promoted to a queen at {chr(97+w_col)}8.")
        break

    if b_row + 1 == w_row:
        if b_col + 1 == w_col or b_col - 1 == w_col:
            print(f"Game over! Black win, capture on {chr(97 + w_col)}{abs(w_row-8)}.")
            break

    b_row += 1
    if b_row == 7:
        print(f"Game over! Black pawn is promoted to a queen at {chr(97 + b_col)}1.")
        break
