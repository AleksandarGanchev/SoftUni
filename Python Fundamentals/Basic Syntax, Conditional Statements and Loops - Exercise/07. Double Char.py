command = ''
counter = 0
while command != 'End':
    command = input()
    if command == 'SoftUni':
        command = input()
    if command == 'End':
        break
    counter += 1
    if counter != 0:
        print()
    for letter in command:
        print(letter+letter, end='')

        if command == 'End':
            break