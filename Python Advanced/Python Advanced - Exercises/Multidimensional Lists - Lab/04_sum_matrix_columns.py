i, j = [int(x) for x in input().split(", ")]
inner_list = []
matrix = []

for _ in range(i):
    inner_list = [int(x) for x in input().split()]
    matrix.append(inner_list)

for j_index in range(j):
    column_sum = 0
    for i_index in range(i):
        column_sum += matrix[i_index][j_index]
    print(column_sum)
