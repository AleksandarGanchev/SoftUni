rows = int(input())

matrix = []

for _ in range(rows):
    inner_list = [int(x) for x in input().split()]
    matrix.append(inner_list)

diagonal_sum = 0
for index in range(rows):
    diagonal_sum += matrix[index][index]

print(diagonal_sum)
