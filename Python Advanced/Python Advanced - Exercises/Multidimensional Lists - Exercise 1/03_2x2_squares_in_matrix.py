rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for row in range(rows)]

matches = 0
for row_idx in range(rows-1):
    for col_idx in range(cols-1):
        current = matrix[row_idx][col_idx]
        below_el = matrix[row_idx][col_idx+1]
        next_el = matrix[row_idx+1][col_idx]
        diagonal_el = matrix[row_idx+1][col_idx+1]
        if current == below_el and current == next_el and current == diagonal_el:
            matches += 1

print(matches)
