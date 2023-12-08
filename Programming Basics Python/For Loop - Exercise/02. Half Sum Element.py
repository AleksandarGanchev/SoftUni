from sys import maxsize

n = int(input())
max_number = - maxsize
total_sum = 0

for i in range(n):
    current_number = int(input())
    if current_number > max_number:
        max_number = current_number
    total_sum += current_number

diff = abs(total_sum - max_number)
total_numbers = abs(max_number-diff)

if diff == max_number:
    print('Yes')
    print(f'Sum = {diff}')

else:
    print('No')
    print(f'Diff = {total_numbers}')