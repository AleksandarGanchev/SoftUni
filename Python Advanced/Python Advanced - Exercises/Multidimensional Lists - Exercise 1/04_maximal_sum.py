rows, cols = [int(x) for x in input().split()]

matrix = [[int(x) for x in input().split()] for row in range(rows)]
sub_matrix = []
max_sum = float("-Inf")
for row_idx in range(rows-2):
    for col_idx in range(cols-2):
        first_row = matrix[row_idx][col_idx:col_idx+3]
        second_row = matrix[row_idx+1][col_idx:col_idx+3]
        third_row = matrix[row_idx+2][col_idx:col_idx+3]

        current_sum = sum(first_row) + sum(second_row) + sum(third_row)
        if current_sum > max_sum:
            max_sum = current_sum
            sub_matrix = [first_row, second_row, third_row]

print(f"Sum = {max_sum}")
for i in sub_matrix:
    print(' '.join([str(x) for x in i]))





















# rows, cols = [int(x) for x in input().split()]
#
# matrix = [[int(x) for x in input().split()] for row in range(rows)]
# sub_matrix = []
# max_sum = float("-Inf")
# for row_idx in range(rows-2):
#     for col_idx in range(cols-2):
#         current = matrix[row_idx][col_idx]
#         second = matrix[row_idx][col_idx+1]
#         third = matrix[row_idx][col_idx+2]
#
#         below = matrix[row_idx+1][col_idx]
#         below_second = matrix[row_idx+1][col_idx+1]
#         below_third = matrix[row_idx+1][col_idx+2]
#
#         third_col_first = matrix[row_idx+2][col_idx]
#         third_col_second = matrix[row_idx+2][col_idx+1]
#         third_col_third = matrix[row_idx+2][col_idx+2]
#
#         current_sum = (
#                 current + second + third
#                 + below + below_second + below_third
#                 + third_col_first + third_col_second + third_col_third)
#
#         if current_sum > max_sum:
#             max_sum = current_sum
#             sub_matrix = [[current, second, third],
#                           [below, below_second, below_third],
#                           [third_col_first, third_col_second, third_col_third]]
#
# print(f"Sum = {max_sum}")
# print(' '.join([str(x) for x in sub_matrix[0]]))
# print(' '.join([str(x) for x in sub_matrix[1]]))
# print(' '.join([str(x) for x in sub_matrix[2]]))
