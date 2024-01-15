n = int(input())

matrix = []
for _ in range(n):
    matrix.append([int(x) for x in input().split(", ")])

flatten = [el for list_el in matrix for el in list_el]

print(flatten)


# n = int(input())
#
# matrix = []
# flatten = []
# for _ in range(n):
#     matrix.append([int(x) for x in input().split(", ")])
#
# for list_el in matrix:
#     flatten.extend(list_el)
#
# print(flatten)
