i, j = [int(x) for x in input().split(", ")]

matrix = []

for _ in range(i):
    inner_list = [int(x) for x in input().split(", ")]
    matrix.append(inner_list)

max_sum = float("-inf")
for row_idx in range(i-1):
    for col_idx in range(j-1):
        current_element = matrix[row_idx][col_idx]
        below_element = matrix[row_idx+1][col_idx]
        next_element = matrix[row_idx][col_idx+1]
        diagonal = matrix[row_idx+1][col_idx+1]

        current_sum = current_element + below_element + next_element + diagonal

        if current_sum > max_sum:
            max_sum = current_sum
            sub_matrix = [[current_element, next_element], [below_element, diagonal]]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)
