command = input()
coffee_count = 0

while command != 'END':
    if command == 'DOG' or command == 'CAT' or command == 'MOVIE' or command == 'CODING':
        coffee_count += 2
    if command == 'dog' or command == 'cat' or command == 'movie' or command == 'coding':
        coffee_count += 1

    command = input()

if coffee_count > 5:
    print("You need extra sleep")
else:
    print(coffee_count)