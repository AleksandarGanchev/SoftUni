first_number = int(input())
second_number = int(input())
largest = 0

for num in range(first_number,second_number+1):
    if num % first_number == 0 and num <= second_number:
        largest = num

print(largest)