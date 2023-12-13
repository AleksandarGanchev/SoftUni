numbers = [int(x) for x in input().split(',')]

numbers_without_zeroes = []
numbers_with_zeroes = []


for index in range(len(numbers)):
    num = numbers[index]
    if num == 0:
        numbers_with_zeroes.append(num)
    else:
        numbers_without_zeroes.append(num)


print(f'{numbers_without_zeroes+numbers_with_zeroes}')