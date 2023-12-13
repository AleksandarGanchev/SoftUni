numbers = [int(number) for number in input().split()]
k = int(input())
executed_people = []

counter = 0
numbers_index = 0

while len(numbers) > 0:
    counter += 1
    if counter % k == 0:
        executed_people.append((numbers[numbers_index]))
        numbers.pop(numbers_index)
    else:
        numbers_index += 1

    if numbers_index >= len(numbers):
        numbers_index = 0


print(str(executed_people).replace(' ', ''))
