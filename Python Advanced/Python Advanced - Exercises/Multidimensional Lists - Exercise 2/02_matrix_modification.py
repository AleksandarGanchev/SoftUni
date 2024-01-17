n = int(input())
matrix = [[int(x) for x in input().split()]for _ in range(n)]

data = input()
while data != "END":
    command = data.split()
    operation, row, col, value = command[0], int(command[1]), int(command[2]), int(command[3])

    if operation == "Add" and 0 <= row <= n-1 and 0 <= col <= n-1:
        matrix[row][col] += value
    elif operation == "Subtract" and 0 <= row <= n and 0 <= col <= n:
        matrix[row][col] -= value
    else:
        print("Invalid coordinates")

    data = input()

for row in matrix:
    print(*row)
