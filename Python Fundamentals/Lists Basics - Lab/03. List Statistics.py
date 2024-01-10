n = int(input())

positive_numbers = []
sum_negatives = []


for _ in range(n):
    number = int(input())
    if number >= 0:
        positive_numbers.append(number)
    else:
        sum_negatives.append((number))

print(positive_numbers)
print(sum_negatives)
print(f'Count of positives: {len(positive_numbers)}')
print(f'Sum of negatives: {sum(sum_negatives)}')