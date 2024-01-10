n = int(input())

even_set = set()
odd_set = set()
for index in range(1, n+1):
    name = input()
    name_sum = 0
    for letter in name:
        name_sum += ord(letter)

    name_sum //= index

    if name_sum % 2 == 0:
        even_set.add(name_sum)
    else:
        odd_set.add(name_sum)

if sum(odd_set) > sum(even_set):
    print(*odd_set.difference(even_set), sep=", ")
elif sum(odd_set) == sum(even_set):
    print(*odd_set.union(even_set), sep=", ")
else:
    print(*odd_set.symmetric_difference(even_set), sep=", ")
