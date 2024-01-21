n = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(n)]
bomb_indices = ([int(x) for x in c.split(",")] for c in input().split())

directions = (
    (-1, 0),   # up
    (1, 0),    # down
    (0, -1),   # left
    (0, 1),    # right
    (-1, 1),   # up right diagonal
    (-1, -1),  # up left diagonal
    (1, 1),    # bottom right diagonal
    (1, -1),   # bottom left diagonal
    (0, 0)     # current
)

for i, j in bomb_indices:
    if matrix[i][j] < 0:
        continue

    for x, y in directions:
        r, c = i + x, j + y

        if 0 <= r < n and 0 <= c < n:
            matrix[r][c] -= matrix[i][j] if matrix[r][c] > 0 else 0

alive_cells = [num for i in range(n) for num in matrix[i] if num > 0]


print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")
[print(*i) for i in matrix]

