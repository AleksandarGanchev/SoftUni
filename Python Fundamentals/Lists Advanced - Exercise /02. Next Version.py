numbers = [int(x) for x in input().split('.')]
first, second, third = numbers

if third < 10:
    third += 1
if third == 10:
    third = 0

if third == 0:
    if second < 10:
        second += 1
    if second == 10:
        second = 0

if second == 0:
    first += 1

print(f'{first}.{second}.{third}')