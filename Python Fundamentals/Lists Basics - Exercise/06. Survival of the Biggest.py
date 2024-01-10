numbers = [int(x) for x in input().split()]
numbers_to_remove = int(input())

for _ in range(numbers_to_remove):
    min_number = min(numbers)
    numbers.remove(min_number)


for idx in range(len(numbers)):
    num = numbers[idx]
    if idx == len(numbers) - 1:
        print(num)
    else:
        print(num,end =', ')