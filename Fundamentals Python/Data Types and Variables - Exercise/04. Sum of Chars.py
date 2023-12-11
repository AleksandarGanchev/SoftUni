number = int(input())
total_sum = 0

for i in range(number):
    characters = input()
    total_sum += ord(characters)

print(f"The sum equals: {total_sum}")