def find_queens(matrix):
    positions = []
    for r in range(SIZE):
        for c in range(SIZE):
            if matrix[r][c] == 'Q':
                positions.append([r, c])

    return positions


def valid_index(r, c):
    if 0 <= r < SIZE and 0 <= c < SIZE:
        return True


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

SIZE = 8

can_capture = []
chessboard = []
k_row, k_col = [0, 0]
for row in range(SIZE):
    chessboard.append(input().split())
    if 'K' in chessboard[row]:
        k_row, k_col = row, chessboard[row].index('K')


queens_positions = find_queens(chessboard)

curr_row = 0
curr_col = 0
for queen_row, queen_col in queens_positions:
    curr_row, curr_col = queen_row, queen_col
    for x, y in directions:
        while valid_index(curr_row+x, curr_col+y):
            curr_row += x
            curr_col += y
            if chessboard[curr_row][curr_col] == 'K':
                can_capture.append([queen_row, queen_col])
                break
            elif chessboard[curr_row][curr_col] == 'Q':
                break
        curr_row, curr_col = queen_row, queen_col


if can_capture:
    for capture in can_capture:
        print(capture)
else:
    print(f"The king is safe!")
