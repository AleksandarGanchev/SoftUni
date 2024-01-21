size = int(input())
commands = input().split()
matrix = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

collected_coal = 0
total_coal = 0
miner_pos = ()
for row in range(size):
    matrix.append(input().split())

    if "s" in matrix[row]:
        miner_pos = row, matrix[row].index("s")
        matrix[row][miner_pos[1]] = "*"

    if "c" in matrix[row]:
        total_coal += matrix[row].count("c")

for command in commands:
    i, j = directions[command][0] + miner_pos[0], directions[command][1] + miner_pos[1]

    if not (0 <= i < size and 0 <= j < size):
        continue

    miner_pos = i, j

    if matrix[i][j] == "c":
        collected_coal += 1
        if collected_coal == total_coal:
            print(f"You collected all coal! ({i}, {j})")
            break

    elif matrix[i][j] == "e":
        print(f"Game over! ({i}, {j})")
        break

    matrix[i][j] = "*"

else:
    print(F"{total_coal - collected_coal} pieces of coal left. ({miner_pos[0]}, {miner_pos[1]})")
