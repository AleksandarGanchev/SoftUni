numbers = input().split()
result = []

for number in numbers:
    number = int(number) * -1
    result.append(number)

print(result)
