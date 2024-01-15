def found_position(matrix, element):
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == element:
                return (i, j)


n = int(input())
matrix = []

for _ in range(n):
    inner_list = input()
    matrix.append(inner_list)

symbol = input()
position = found_position(matrix, symbol)

if position:
    print(position)
else:
    print(f"{symbol} does not occur in the matrix")
