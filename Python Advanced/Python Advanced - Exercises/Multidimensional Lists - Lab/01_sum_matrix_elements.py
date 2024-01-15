i, j = [int(x) for x in input().split(", ")]

matrix = []

total_sum = 0
for _ in range(i):
    inner_list = [int(x) for x in input().split(", ")]
    total_sum += sum(inner_list)
    matrix.append(inner_list)

print(total_sum)
print(matrix)
